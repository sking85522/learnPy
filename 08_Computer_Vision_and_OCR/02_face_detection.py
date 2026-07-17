import cv2

def detect_faces():
    # चेहरे पहचानने के लिए प्री-ट्रेंड मॉडल लोड करें (Haar Cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0) # वेबकैम शुरू करें

    print("कैमरा चालू है... चेहरे ढूंढ रहा हूँ। बंद करने के लिए 'q' दबाएं।")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # रंगीन चित्र को ग्रेस्केल (ब्लैक एंड वाइट) में बदलें क्योंकि पहचानना आसान होता है
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # चेहरे ढूंढें
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # मिले हुए चेहरों के चारों ओर एक आयत (Rectangle) बनाएं
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # टेक्स्ट लिखें
            cv2.putText(frame, 'Face Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('Face Detection (चेहरा पहचान)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # detect_faces() # इसे चलाने के लिए अनकमेंट करें
    print("चेहरा पहचानने का कोड तैयार है। चलाने के लिए कोड में कमेंट हटाएं।")
