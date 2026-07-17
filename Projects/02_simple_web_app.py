from flask import Flask, render_template_string, request
import os

# यह एक बहुत ही सरल वेब ऐप है जो एक टेक्स्ट इनपुट लेता है और उसे उलटा (Reverse) करके वापस करता है।

app = Flask(__name__)

# HTML टेम्पलेट (इसे सीधे कोड में लिख रहे हैं ताकि एक ही फ़ाइल में सब कुछ रहे)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>टेक्स्ट रिवर्सर (Text Reverser)</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        input[type="text"] { padding: 10px; width: 300px; font-size: 16px; }
        input[type="submit"] { padding: 10px 20px; font-size: 16px; cursor: pointer; }
        .result { margin-top: 20px; font-size: 24px; color: green; font-weight: bold; }
    </style>
</head>
<body>
    <h1>कोई भी टेक्स्ट लिखें</h1>
    <form method="POST">
        <input type="text" name="user_text" placeholder="यहाँ कुछ लिखें..." required>
        <br><br>
        <input type="submit" value="टेक्स्ट को उल्टा करें (Reverse)">
    </form>

    {% if result %}
        <div class="result">
            आपका उल्टा किया हुआ टेक्स्ट:<br>
            {{ result }}
        </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    reversed_text = None
    if request.method == 'POST':
        # फॉर्म से टेक्स्ट लें
        original_text = request.form.get('user_text')
        # पायथन स्लाइसिंग [::-1] का उपयोग करके स्ट्रिंग को उल्टा करें
        reversed_text = original_text[::-1]

    return render_template_string(HTML_TEMPLATE, result=reversed_text)

if __name__ == '__main__':
    print("वेब ऐप शुरू हो रहा है... अपने ब्राउज़र में http://127.0.0.1:5000/ खोलें")
    app.run(debug=True)
