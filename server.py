from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route for the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for emotion detection
@app.route('/emotionDetector')
def emotionDetector():
    # Get the text from query parameter
    text_to_analyse = request.args.get('textToAnalyze')

    # If no input text is provided
    if not text_to_analyse:
        return jsonify({"error": "Please provide textToAnalyze parameter"}), 400

    # Run the emotion detector function
    result = emotion_detector(text_to_analyse)

    # Handle invalid API or processing result
    if result is None:
        return jsonify({"error": "Error occurred while detecting emotion"}), 500

    # Format the response message as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # Return formatted message to frontend
    return response_text

# Run the Flask app on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
