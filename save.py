import datetime

LOG_FILE = "answers_log.txt"

def save(question, answer):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[{timestamp}]\n")
        f.write(f"Q: {question}\n")
        f.write(f"A: {answer}\n")
        f.write("-" * 50 + "\n")
    print(f"Answer saved to: {LOG_FILE}")