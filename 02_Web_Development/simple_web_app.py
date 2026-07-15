# इसे चलाने के लिए पहले Flask इंस्टॉल करें: pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>नमस्ते! यह मेरा पहला फ्लास्क वेब ऐप है।</h1>"

if __name__ == "__main__":
    # ऐप को लोकल सर्वर पर चलाएं
    app.run(debug=True)
