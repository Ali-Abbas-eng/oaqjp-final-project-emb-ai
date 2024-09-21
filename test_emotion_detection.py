import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        statement = "I am glad this happened"
        expected_emotion = "joy"
        dominant_emotion = emotion_detector(statement)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

    def test_anger(self):
        statement = "I am really mad about this"
        expected_emotion = "anger"
        dominant_emotion = emotion_detector(statement)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        expected_emotion = "disgust"
        dominant_emotion = emotion_detector(statement)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

    def test_sadness(self):
        statement = "I am so sad about this"
        expected_emotion = "sadness"
        dominant_emotion = emotion_detector(statement)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        expected_emotion = "fear"
        dominant_emotion = emotion_detector(statement)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

if __name__ == '__main__':
    unittest.main()
