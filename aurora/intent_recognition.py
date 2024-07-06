class IntentRecognition:
    def __init__(self):
        self.intents = {
            "greeting": ["hello", "hi", "hey"],
            "farewell": ["bye", "goodbye", "see you"]
        }

    def recognize_intent(self, message):
        for intent, keywords in self.intents.items():
            if any(keyword in message.lower() for keyword in keywords):
                return intent
        return "unknown"

