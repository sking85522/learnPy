import cv2
import pytesseract

# यह स्क्रिप्ट एक इमेज से टेक्स्ट पढ़ने (OCR - Optical Character Recognition) का काम करती है।
# नोट: आपको अपने कंप्यूटर पर Tesseract-OCR सॉफ्टवेयर भी इंस्टॉल करना होगा और यहाँ उसका पाथ देना होगा।
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Windows के लिए उदाहरण

def extract_text_from_image(image_path):
    try:
        # इमेज पढ़ें
        img = cv2.imread(image_path)

        # इमेज से टेक्स्ट निकालें
        text = pytesseract.image_to_string(img)

        print("--- इमेज से निकाला गया टेक्स्ट ---")
        print(text)
        print("---------------------------------")
        return text
    except Exception as e:
        print(f"एरर: क्या आपने Tesseract इंस्टॉल किया है? \nविस्तृत एरर: {e}")

if __name__ == "__main__":
    print("OCR स्क्रिप्ट तैयार है।")
    # extract_text_from_image('sample_image.jpg') # अपनी इमेज का नाम यहाँ दें
