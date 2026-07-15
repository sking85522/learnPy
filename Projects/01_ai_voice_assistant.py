import speech_recognition as sr
import pyttsx3
import datetime

# इंजन सेटअप: कंप्यूटर को बोलने की क्षमता देना
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 for male, 1 for female (if available)

def speak(text):
    """इस फंक्शन से कंप्यूटर टेक्स्ट को आवाज़ में बोलेगा"""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """माइक्रोफोन से उपयोगकर्ता की आवाज़ सुनेगा और उसे टेक्स्ट में बदलेगा"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("सुन रहा हूँ... (Listening...)")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("समझ रहा हूँ... (Recognizing...)")
        query = r.recognize_google(audio, language='en-in')
        print(f"आपने कहा: {query}\n")
        return query.lower()
    except Exception as e:
        print("कृपया फिर से बोलें...")
        return "None"

def run_assistant():
    speak("नमस्ते! मैं आपका पर्सनल असिस्टेंट हूँ। मैं आपकी क्या मदद कर सकता हूँ?")

    while True:
        query = listen_command()

        if query == "none":
            continue

        if 'time' in query or 'समय' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(f"अभी समय है: {time}")
            speak(f"अभी समय है {time}")

        elif 'stop' in query or 'exit' in query or 'बंद करो' in query:
            speak("अलविदा! फिर मिलेंगे।")
            break

        else:
            print("मुझे यह कमांड समझ नहीं आया।")
            speak("मुझे यह कमांड समझ नहीं आया।")

if __name__ == "__main__":
    print("एआई असिस्टेंट शुरू करने के लिए 'run_assistant()' कॉल करें।")
    # run_assistant()
