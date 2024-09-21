import requests, json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze: str) -> str:
    """
    This function calls the Emotion Predict function of the 
    Watson NLP Library to predict the emotions expressed in a piece of text
    Params:
    @param text_to_analyze: str, the text from which the emotions will be deciphered.

    Returns:
        str, the text version response of the server
    """
    input_json = {'raw_document': {'text': text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS)
    if response.status_code != 200:
        return {
            'joy': None,
            'anger': None,
            'fear': None,
            'sadness': None,
            'disgust': None,
        }
    response = json.loads(response.text)
    response = {
        key: value for key, value in response['emotionPredictions'][0]['emotion'].items()
    }
    response['dominant_emotion'] = max(response, key=response.get)
    return response