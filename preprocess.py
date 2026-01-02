import cv2
import numpy as np


def preprocess_for_ocr(img):
    """
    General-purpose preprocessing for food label OCR
    """

    # 1. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Resize to normalize text scale
    h, w = gray.shape
    scale = 150  # 150% scaling
    resized = cv2.resize(
        gray,
        (int(w * scale / 100), int(h * scale / 100)),
        interpolation=cv2.INTER_LINEAR
    )

    # 3. Local contrast enhancement (handles glare)
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )
    contrast = clahe.apply(resized)

    # 4. Adaptive thresholding (handles uneven lighting)
    thresh = cv2.adaptiveThreshold(
        contrast,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        10
    )

    return contrast
