""" Import functions """
from flask import Flask, render_template, request # Import functions
from EmotionDetection.emotion_detection import emotion_detector # Import functions

app = Flask("Emotion Detector") # Initiate application

@app.route("/emotionDetector")
def get_emotion_details():
    """ Define the function """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if dominant emotion is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."
    # Return a formatted string with the emotion values and dominant emotion
    return f"For the given statement, the system response is 'anger': {response['anger']}, \
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and \
    'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """ Render the HTML template """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
