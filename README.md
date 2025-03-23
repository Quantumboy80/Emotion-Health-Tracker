Emotion Health Tracker
📌 Overview
The Emotion Health Tracker is a Flask-based web application that analyzes user emotions based on text input and provides personalized recommendations for well-being. It helps users track their mental health and receive actionable advice.

🚀 Features
Sentiment analysis using predefined emotion-based keywords

Health-based recommendations (sleep, hydration, relaxation, etc.)

Simple and interactive web interface

Flask backend with REST API for emotion analysis

🛠️ Technologies Used
Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Version Control: Git & GitHub

🔧 Installation & Setup
Clone the repository

sh
Copy
Edit
--> git clone https://github.com/Quantumboy80/Emotion-Health-Tracker.git

Navigate to the project directory

sh
Copy
Edit
--> cd Emotion-Health-Tracker

Create a virtual environment (optional but recommended)

sh
Copy
Edit
--> python -m venv venv
--> source venv/bin/activate  # macOS/Linux
--> venv\Scripts\activate  # Windows


Install dependencies

sh
Copy
Edit
--> pip install -r requirements.txt

Run the Flask application

sh
Copy
Edit
--> python app.py


Access the web app
Open http://127.0.0.1:5000 in your browser.

📩 API Usage
Endpoint: /analyze
Method: POST

Payload (JSON Example):

json
Copy
Edit
{
  "text": "I feel stressed and exhausted today.",
  "sleep_hours": 5,
  "water_intake": 1.5
}
Response Example:

json
Copy
Edit
{
  "emotion": "NEGATIVE",
  "recommendation": "Take breaks, engage in relaxing activities like music. Ensure you get proper rest, take short breaks, and try relaxation techniques like stretching or meditation. Try to get at least 7-8 hours of sleep. Make sure to drink at least 2 liters of water.",
  "score": 0.8
}
🤝 Contributing
Feel free to open issues and pull requests for improvements.

📜 License
This project is open-source and available under the MIT License.
