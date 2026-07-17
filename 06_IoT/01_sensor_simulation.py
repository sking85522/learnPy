import time
import random

# यह कोड सिमुलेट करता है कि हम किसी हार्डवेयर सेंसर (जैसे तापमान सेंसर) से डेटा पढ़ रहे हैं।
# असली IoT प्रोजेक्ट में हम यहाँ serial library (pyserial) का उपयोग करके Arduino/Raspberry Pi से बात करेंगे।

def read_temperature_sensor():
    """सेंसर से डमी तापमान डेटा लें"""
    # 20 से 35 डिग्री के बीच कोई भी रैंडम तापमान
    return round(random.uniform(20.0, 35.0), 2)

def main():
    print("IoT स्मार्ट होम सेंसर शुरू हो रहा है...")
    print("प्रेस Ctrl+C बाहर निकलने के लिए\n")

    try:
        while True:
            temp = read_temperature_sensor()

            # डेटा के आधार पर निर्णय लें
            if temp > 30.0:
                status = "चेतावनी: बहुत गर्मी है! AC चालू करें।"
            else:
                status = "सामान्य तापमान।"

            print(f"[सेंसर रीडिंग] तापमान: {temp}°C -> {status}")

            # हर 2 सेकंड में डेटा लें
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nसेंसर सिस्टम बंद हो रहा है...")

if __name__ == "__main__":
    main()
