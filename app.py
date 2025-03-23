from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Categorized words for sentiment analysis
POSITIVE_WORDS = ["good", "happy", "joyful", "excited", "content", "grateful", "motivated", "energetic", "anticipated"]
NEGATIVE_WORDS = {
    "depressed": "Consider talking to a family member, journaling your thoughts, or seeking professional help.",
    "anxious": "Try deep breathing exercises, meditation, or a short walk to calm your mind.",
    "stressed": "Take breaks, prioritize tasks, and engage in relaxing activities like listening to music.",
    "overwhelmed": "Break tasks into smaller steps, ask for help, and practice time management.",
    "unhappy": "Engage in hobbies, talk to a close friend, or write down things you're grateful for.",
    "worried": "Challenge negative thoughts, practice mindfulness, and avoid excessive worrying.",
    "sick": "Rest well, stay hydrated, take necessary medications, and consider visiting a doctor.",
    "exhausted": "Ensure you get proper rest, take short breaks, and try relaxation techniques like stretching or meditation.",
    "nervous": "Prepare yourself, take deep breaths, and remind yourself that it's okay to feel nervous before big events.",
    "tired": "Try to get more rest, and take short breaks to refresh your mind."
}

@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json  # Get JSON data from request
    
    # Extract parameters
    text = data.get("text", "").lower()
    sleep_hours = data.get("sleep_hours", 0)
    water_intake = data.get("water_intake", 0)

    # Default responses
    emotion = "NEUTRAL"
    recommendations = []  # Store multiple recommendations

    # Check for positive emotion
    if any(word in text for word in POSITIVE_WORDS):
        emotion = "POSITIVE"
        recommendations.append("Great! Keep engaging in activities that make you happy, such as exercising, socializing, or pursuing hobbies.")

    # Check for negative emotion
    detected_negative_words = [word for word in NEGATIVE_WORDS if word in text]
    
    if detected_negative_words:
        emotion = "NEGATIVE"
        recommendations = [NEGATIVE_WORDS[word] for word in detected_negative_words]  # Only show negative recommendations

    # **New Recommendations Based on Certain Feelings**
    if any(word in text for word in ["tired", "exhausted", "stressed"]):
        recommendations.append("A refreshing bath can help you relax and feel rejuvenated.")

    if any(word in text for word in ["sick", "low-energy", "overwhelmed"]):
        recommendations.append("Eating a balanced and nutritious meal can boost your energy and well-being.")

    # Additional health recommendations
    if sleep_hours < 6:
        recommendations.append("Try to get at least 7-8 hours of sleep for better well-being.")
    if water_intake < 2:
        recommendations.append("Make sure to drink at least 2 liters of water daily to stay hydrated.")

    return jsonify({
        "emotion": emotion,
        "recommendation": " ".join(recommendations),
        "score": 0.8,  # Dummy score for now
        "sleep_hours": sleep_hours,
        "water_intake": water_intake
    })

if __name__ == "__main__":
    app.run(debug=True)
