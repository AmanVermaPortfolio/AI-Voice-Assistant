from speak import speak
from listen import listen
from model import ask
from save import save

def main():
    print("=" * 50)
    print("        AI Voice Assistant - Ready")
    print("=" * 50)
    speak("Hello Aman! I am your AI assistant. How can I help you?")

    while True:
        print("\nSelect input method:")
        print("  [1]  Speak via microphone")
        print("  [2]  Type your question")
        print("  [q]  Quit")
        choice = input("Your choice (1/2): ").strip().lower()

        if choice in ['q', 'quit', 'exit']:
            speak("Goodbye! Have a great day.")
            print("Session ended.")
            break

        if choice == '1':
            question = listen()
            if not question:
                continue

        elif choice == '2':
            question = input("Your question: ").strip()
            if not question:
                continue

        else:
            print("Invalid choice. Please enter 1, 2, or q.")
            continue

        print("Processing...")
        answer = ask(question)

        print(f"\nAnswer: {answer}\n")
        speak(answer)
        save(question, answer)

if __name__ == "__main__":
    main()