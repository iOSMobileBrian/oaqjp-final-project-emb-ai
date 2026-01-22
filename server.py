"""
Flask server for the Emotion Detection application.
"""

import sys
from flask import Flask, request, render_template

sys.path.append("src")

from EmotionDetection import emotion_detector  # pylint: disable=wrong-import-position

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Run emotion detection on user input and return result."""
    text_to_analyse = request.args.get("textToAnalyze", "").strip()
    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return result


if __name__ == "__main__":
    app.run(debug=True)
