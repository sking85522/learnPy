import cv2

def capture_video():
    # 0 का मतलब है डिफ़ॉल्ट लैपटॉप कैमरा
    cap = cv2.VideoCapture(0)

    while True:
        # कैमरे से एक फ्रेम पढ़ें
        ret, frame = cap.read()

        if not ret:
            print("कैमरा नहीं मिल रहा है।")
            break

        # फ्रेम को स्क्रीन पर दिखाएं
        cv2.imshow('Mera Camera', frame)

        # 'q' दबाने पर लूप से बाहर निकलें
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # काम खत्म होने पर कैमरा बंद करें
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("यह कोड चलाकर आप अपना वेबकैम शुरू कर सकते हैं। बंद करने के लिए 'q' दबाएं।")
    # capture_video() # इसे अनकमेंट करें यदि आप इसे अपने कंप्यूटर पर चला रहे हैं
