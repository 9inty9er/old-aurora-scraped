from aurora.context_manager import ContextManager
from aurora.intent_recognition import IntentRecognition
from aurora.system_monitor import SystemMonitor

def main():
    context_manager = ContextManager()
    intent_recognition = IntentRecognition()
    system_monitor = SystemMonitor()

    while True:
        user_input = input("You: ")
        intent = intent_recognition.recognize_intent(user_input)
        
        if intent == "greeting":
            print("Aurora: Hello! How can I help you today?")
        elif intent == "farewell":
            print("Aurora: Goodbye! Have a great day!")
            break
        else:
            print("Aurora: I'm not sure how to respond to that.")

        # Example of using system monitoring
        cpu_usage = system_monitor.get_cpu_usage()
        memory_usage = system_monitor.get_memory_usage()
        disk_usage = system_monitor.get_disk_usage()

        print(f"Aurora: Current CPU usage is {cpu_usage}%")
        print(f"Aurora: Current memory usage is {memory_usage}%")
        print(f"Aurora: Current disk usage is {disk_usage}%")

if __name__ == "__main__":
    main()

