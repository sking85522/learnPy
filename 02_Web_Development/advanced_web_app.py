from flask import Flask, jsonify, request

app = Flask(__name__)

# होम पेज रूट
@app.route("/")
def home():
    return """
    <h1>मेरी वेबसाइट में आपका स्वागत है!</h1>
    <p>यहाँ जाने के लिए लिंक:</p>
    <ul>
        <li><a href='/about'>हमारे बारे में (About)</a></li>
        <li><a href='/api/data'>API डेटा देखें (JSON)</a></li>
    </ul>
    """

# अबाउट पेज
@app.route("/about")
def about():
    return "<h2>हम पायथन डेवलपर्स हैं जो दुनिया बदलना चाहते हैं!</h2><a href='/'>वापस जाएं</a>"

# API रूट (JSON रिटर्न करने के लिए)
@app.route("/api/data")
def api_data():
    my_data = {
        "status": "success",
        "message": "यह एक डमी API है।",
        "users": ["Rahul", "Priya", "Amit"]
    }
    return jsonify(my_data)

# URL पैरामीटर पास करना
@app.route("/greet/<name>")
def greet_user(name):
    return f"<h2>नमस्ते {name}! वेब डेवलपमेंट की दुनिया में आपका स्वागत है।</h2>"

if __name__ == "__main__":
    print("सर्वर चालू हो रहा है... http://127.0.0.1:5000/ पर जाएं")
    app.run(debug=True)
