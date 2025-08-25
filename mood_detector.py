import random

class MoodDetector:
    mood_keywords = {
        'happy': ['happy', 'great', 'excited', 'joyful', 'fantastic', 'good'],
        'sad': ['sad', 'tired', 'down', 'depressed', 'unhappy', 'gloomy'],
        'angry': ['angry', 'mad', 'furious', 'annoyed', 'irritated'],
        'anxious': ['anxious', 'worried', 'nervous', 'stressed']
    }

    mood_emojis = {
        'happy': ['😊', '😄', '🌞', '🎉'],
        'sad': ['😢', '😞', '💧', '😔'],
        'angry': ['😡', '🔥', '😤'],
        'anxious': ['😰', '😟', '😬'],
        'neutral': ['🤔', '😐']
    }

    mood_tips = {
        'happy': "Keep spreading the joy!",
        'sad': "Take a break, maybe call a friend or listen to music.",
        'angry': "Try deep breathing or a walk to cool off.",
        'anxious': "Close your eyes and take a few deep breaths.",
        'neutral': "It's okay to feel neutral. Stay mindful and relaxed."
    }

    def __init__(self, text):
        self.text = text.lower()
        self.detected_moods = []

    def analyze(self):
        for mood, keywords in self.mood_keywords.items():
            if any(word in self.text for word in keywords):
                self.detected_moods.append(mood)

        if not self.detected_moods:
            self.detected_moods.append('neutral')

    def detect_mood(self):
        self.analyze()
        response = ""
        for mood in self.detected_moods:
            emoji = random.choice(self.mood_emojis[mood])
            tip = self.mood_tips[mood]
            response += f"{emoji} Detected mood: **{mood.capitalize()}**\nTip: {tip}\n\n"
        return response.strip()

# Example usage
user_input = input("How are you feeling today? ")
detector = MoodDetector(user_input)
print(detector.detect_mood())
