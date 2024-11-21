# Extracting Old Persian Cuneiform Font Out of Noisy Images (Handwritten or Inscription)

This repository contains the code and resources for the paper **"Extracting Old Persian Cuneiform Font Out of Noisy Images, Handwritten or Inscription"** paper. The research focuses on developing techniques to extract and recognize Old Persian cuneiform characters from noisy datasets, including inscriptions, handwritten images, and digital scans.

---

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


![image](https://github.com/user-attachments/assets/e801b898-471f-44e4-9b71-7903f6ce9b0e)

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

---

## Results

- The proposed pipeline achieves high accuracy in recognizing Old Persian cuneiform characters, even in noisy conditions.
- The dataset and techniques significantly reduce recognition errors compared to baseline methods.

### Example Results:


---

Extracting Old Persian Cuneiform Font Out of Noisy Images (Handwritten or Inscription)
Please cite below:
Mousavi, Seyed Muhammad Hossein, and Vyacheslav Lyashenko. "Extracting old persian cuneiform font out of noisy images (handwritten or inscription)." 2017 10th Iranian Conference on Machine Vision and Image Processing (MVIP). IEEE, 2017.
