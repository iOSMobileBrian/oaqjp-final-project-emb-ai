import requests

def emotion_detector(text_to_analyse):
    none_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {"raw_document": {"text": text_to_analyse}}

    r = requests.post(url, headers=headers, json=payload)
    print("Watson status:", r.status_code)

    
    if r.status_code == 400:
        return none_result

    data = r.json()
    emotions = data["emotionPredictions"][0]["emotion"]
    dominant = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant
    }