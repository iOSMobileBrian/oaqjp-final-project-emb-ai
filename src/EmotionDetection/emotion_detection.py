

import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    data = response.json()
    prediction = data['emotionPredictions'][0]
    emotions = prediction['emotion']
    text = prediction['emotionMentions'][0]['span']['text']
    dominant_emotion = max(emotions, key=emotions.get)
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}: {response.text}")
    
    return {
        "text": text,
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }