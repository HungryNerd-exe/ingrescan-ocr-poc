import cv2
import pytesseract
from preprocess import preprocess_for_ocr

IMAGE_PATH = "images/label2_cp.jpeg"


def main():
    img = cv2.imread(IMAGE_PATH)

    if img is None:
        print("Error: image not found")
        return

    processed = preprocess_for_ocr(img)

    # Visual comparison (IMPORTANT)
    cv2.imshow("Original", img)
    cv2.imshow("Preprocessed", processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    text = pytesseract.image_to_string(processed)

    print("===== OCR OUTPUT (PREPROCESSED) =====")
    print(text)


if __name__ == "__main__":
    main()
