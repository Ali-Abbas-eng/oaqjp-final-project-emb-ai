from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('EmotionDetectionSystem')

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    
    result = emotion_detector(text_to_analyze)
    string_result = f'For the given statement, the system response is'
    for key, value in result.items():
        if (key == 'dominant_emotion'):
            continue
        string_result += f" '{key}': {value},"
    string_result += f" and the dominant emotion is {result['dominant_emotion']}."
    return string_result

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()