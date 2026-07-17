# इसे चलाने के लिए Kivy इंस्टॉल करें: pip install kivy
from kivy.app import App
from kivy.uix.button import Button

class MeraApp(App):
    def build(self):
        # एक बटन बनाएं जो पूरी स्क्रीन पर हो
        return Button(text="नमस्ते, यह मेरा पहला मोबाइल ऐप है!", font_size=30)

if __name__ == "__main__":
    MeraApp().run()
