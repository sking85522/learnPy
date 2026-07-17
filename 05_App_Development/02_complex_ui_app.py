from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# यह एक कैलकुलेटर जैसा छोटा ऐप बनाएगा
class MyComplexApp(App):
    def build(self):
        # BoxLayout चीजों को एक कतार (vertical/horizontal) में लगाता है
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # निर्देश दिखाने के लिए Label
        self.label = Label(text='अपना नाम नीचे लिखें:', font_size=24)
        self.layout.add_widget(self.label)

        # टेक्स्ट इनपुट बॉक्स
        self.user_input = TextInput(font_size=24, multiline=False)
        self.layout.add_widget(self.user_input)

        # सबमिट बटन
        self.submit_btn = Button(text='मुझे ग्रीट करें!', font_size=24, background_color=(0, 1, 0, 1))
        # बटन क्लिक होने पर क्या होगा? (Event binding)
        self.submit_btn.bind(on_press=self.greet_user)
        self.layout.add_widget(self.submit_btn)

        return self.layout

    def greet_user(self, instance):
        # टेक्स्ट बॉक्स से नाम लें
        name = self.user_input.text
        if name:
            self.label.text = f'नमस्ते, {name}! आपका स्वागत है।'
        else:
            self.label.text = 'कृपया कुछ नाम लिखें!'

if __name__ == '__main__':
    MyComplexApp().run()
