import sys
sys.path.append("src")

from EmotionDetection import emotion_detector

def run_tests():
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected_emotion in test_cases.items():
        result = emotion_detector(text)
        dominant = result["dominant_emotion"]
        
        print(f"Text: {text}")
        print(f"Expected: {expected_emotion}, Detected: {dominant}")
        
        assert dominant == expected_emotion, f"FAILED for: {text}"
    
    print("\nAll emotion tests passed successfully.")

if __name__ == "__main__":
    run_tests()