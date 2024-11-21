import os
import cv2
import numpy as np
from tqdm import tqdm
from pathlib import Path

# Function to apply multiple augmentations to an image
def augment_image(image):
    augmented_images = []

    # **1. Rotation**: Add more angles
    for angle in [10, 15, 30, -10, -15, -30, 45, -45]:
        rows, cols = image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotated = cv2.warpAffine(image, rotation_matrix, (cols, rows))
        augmented_images.append(rotated)

    # **2. Horizontal Flip**
    flipped = cv2.flip(image, 1)
    augmented_images.append(flipped)

    # **3. Brightness Adjustment**: Add more brightness factors
    for factor in [0.5, 0.7, 1.2, 1.5]:
        bright = cv2.convertScaleAbs(image, alpha=factor, beta=0)
        augmented_images.append(bright)

    # **4. Gaussian Blur**
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    augmented_images.append(blurred)

    # **5. Gaussian Noise**
    gaussian_noise = np.random.normal(0, 25, image.shape).astype('uint8')
    noisy = cv2.add(image, gaussian_noise)
    augmented_images.append(noisy)

    # **6. Scaling (Zoom In/Out)**: Add intermediate scaling
    for scale in [0.8, 0.9, 1.1, 1.2]:
        scaled = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
        height, width = image.shape[:2]
        scaled_height, scaled_width = scaled.shape[:2]
        if scaled_height <= height and scaled_width <= width:  # Zoom out - Add padding
            top = (height - scaled_height) // 2
            bottom = height - scaled_height - top
            left = (width - scaled_width) // 2
            right = width - scaled_width - left
            padded = cv2.copyMakeBorder(scaled, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            augmented_images.append(padded)
        else:  # Zoom in - Crop to original size
            cropped = scaled[:height, :width]
            augmented_images.append(cropped)

    # **7. Shearing**
    for shear in [0.2, -0.2]:
        M = np.float32([[1, shear, 0], [shear, 1, 0]])
        sheared = cv2.warpAffine(image, M, (cols, rows))
        augmented_images.append(sheared)

    # **8. Cropping**
    h, w = image.shape[:2]
    crop = image[int(h * 0.1):int(h * 0.9), int(w * 0.1):int(w * 0.9)]  # Central crop
    resized_crop = cv2.resize(crop, (w, h))  # Resize back to original size
    augmented_images.append(resized_crop)

    # **9. Perspective Transform**
    pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])
    pts2 = np.float32([[10, 100], [cols - 100, 50], [100, rows - 100], [cols - 50, rows - 10]])
    perspective_matrix = cv2.getPerspectiveTransform(pts1, pts2)
    perspective = cv2.warpPerspective(image, perspective_matrix, (cols, rows))
    augmented_images.append(perspective)

    return augmented_images

# Process all images in a folder
def process_images(input_folder, output_folder):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    # Iterate over all images in the input folder
    for image_file in tqdm(input_folder.glob("*.*")):  # Supports all image types
        # Read the image
        image = cv2.imread(str(image_file))
        if image is None:
            print(f"Skipping invalid image: {image_file}")
            continue

        # Get the character name from the filename
        character_name = image_file.stem

        # Apply augmentations
        augmented_images = augment_image(image)

        # Save each augmented image with a unique name
        for i, aug_image in enumerate(augmented_images):
            output_path = output_folder / f"{character_name}_aug_{i}.jpg"
            cv2.imwrite(str(output_path), aug_image)

# Set input and output folder paths
input_folder = r"Persian Cuneiform for Augmentation"  # Replace with your folder
output_folder = r"Augmented Cuneiform Images"  # Replace with your desired output folder

# Run the augmentation process
process_images(input_folder, output_folder)
