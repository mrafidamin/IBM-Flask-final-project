import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = payload, headers=header)
    response_dict = json.loads(response.text)
   
    emotions = response_dict['emotionPredictions'][0]['emotion']
    required_emotions = {key: emotions[key] for key in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
    dominant_emotion = max(required_emotions, key=required_emotions.get)

    result = {
        **required_emotions,
        "dominant_emotion": dominant_emotion
    }
    return result
