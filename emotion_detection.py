import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()  # Raise an exception for bad status codes
        emotion_data = response.json()
        if 'results' in emotion_data and len(emotion_data['results']) > 0 and 'result' in emotion_data['results'][0]:
            return emotion_data['results'][0]['result']['document']['emotion']['document']
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Response text: {response.text}") # print the response
        return None

if __name__ == '__main__':
    test_text = "I love this new technology."
    emotion_result = emotion_detector(test_text)
    if emotion_result:
        print(f"Emotions detected: {emotion_result}")
    else:
        print("Emotion detection failed.")