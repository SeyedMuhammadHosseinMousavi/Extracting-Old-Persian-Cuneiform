# Extracting Old Persian Cuneiform Font Out of Noisy Images (Handwritten or Inscription)

This repository contains the code and resources for the paper **"Extracting Old Persian Cuneiform Font Out of Noisy Images, Handwritten or Inscription"** paper. The research focuses on developing techniques to extract and recognize Old Persian cuneiform characters from noisy datasets, including inscriptions, handwritten images, and digital scans.

---
### Update: A new image augmentor is added.

## Abstract

Old Persian cuneiform is an ancient script used for inscriptions in the Achaemenid Empire. Extracting characters from noisy datasets, such as weathered inscriptions or handwritten samples, is a challenging task. This research presents a robust methodology for:
- Preprocessing noisy cuneiform images.
- Segmenting and isolating characters.
- Recognizing characters using Optical Character Recognition (OCR) techniques.

The approach is validated on a custom dataset of 34 Old Persian cuneiform symbols, with applications in cultural preservation, digital archiving, and linguistic analysis.

- Link to the paper:
- https://ieeexplore.ieee.org/abstract/document/8342358
---

## Key Contributions

1. **Dataset Creation**:
   - A curated dataset of 34 Old Persian cuneiform characters, including noisy and clean samples.

2. **Preprocessing Pipeline**:
   - Noise reduction techniques, such as Gaussian filtering and morphological operations.
   - Binarization and thresholding to enhance symbol clarity.

3. **Segmentation**:
   - A method for isolating individual cuneiform characters from inscriptions or clustered images.

4. **Character Recognition**:
   - Using OCR techniques to classify and recognize segmented cuneiform characters.
   - Focus on improving OCR accuracy by augmenting the dataset with diverse transformations.

5. **Applications**:
   - Preservation of ancient scripts in digital form.
   - Enabling future linguistic studies and translations of ancient texts.

![image](https://github.com/user-attachments/assets/d8ebdc3f-adb3-4611-925c-a2fc628c7bae)
![image](https://github.com/user-attachments/assets/e801b898-471f-44e4-9b71-7903f6ce9b0e)
![image](https://github.com/user-attachments/assets/6c119c48-77a6-4825-b270-edaa490d323e)

---

## Methodology

### **1. Preprocessing**
The preprocessing pipeline includes:
- **Denoising**: Removes noise using Gaussian blurring and median filtering.
- **Thresholding**: Converts grayscale images into binary form for better segmentation.
- **Morphological Operations**: Cleans up artifacts and enhances character structures.

### **2. Segmentation**
A combination of contour detection and region-based segmentation is used to isolate individual cuneiform symbols.

### **3. OCR Integration**
- A custom-trained Tesseract OCR model is utilized for recognizing Old Persian cuneiform characters.
- Augmented datasets improve recognition accuracy by adding rotated, flipped, and scaled variations.
![image](https://github.com/user-attachments/assets/ff4a156f-64a2-494e-a0b3-83d535dbf0c0)

---

## Results

- The proposed pipeline achieves high accuracy in recognizing Old Persian cuneiform characters, even in noisy conditions.
- The dataset and techniques significantly reduce recognition errors compared to baseline methods.

### Example Results:
![image](https://github.com/user-attachments/assets/98d8fba2-5754-460d-aa2c-e829a73e3a96)


---

Extracting Old Persian Cuneiform Font Out of Noisy Images (Handwritten or Inscription)
Please cite below:
Mousavi, Seyed Muhammad Hossein, and Vyacheslav Lyashenko. "Extracting old persian cuneiform font out of noisy images (handwritten or inscription)." 2017 10th Iranian Conference on Machine Vision and Image Processing (MVIP). IEEE, 2017.
