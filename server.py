from flask import Flask, request, render_template
import sys
sys.path.append("src")

from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text_to_analyse = request.args.get("textToAnalyze", "")
    return emotion_detector(text_to_analyse)

if __name__ == "__main__":
    app.run(debug=True)