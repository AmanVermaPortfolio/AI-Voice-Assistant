import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3:mini"

SYSTEM_PROMPT = """You are a professional female AI assistant. Follow these rules strictly:
1. Answer in exactly 2 to 3 sentences. Never more.
2. No bullet points, no dashes, no numbered lists.
3. Write in plain flowing sentences only.
4. Keep tone professional, warm and confident.
5. Always reply in English only."""

def ask(question, retries=3):
    payload = {
        "model": MODEL,
        "prompt": f"System: {SYSTEM_PROMPT}\n\nIMPORTANT: 2-3 sentences only. No bullets. Plain sentences.\n\nUser: {question}\nAssistant:",
        "stream": False
    }
    for attempt in range(1, retries + 1):
        try:
            print(f"Connecting to model (attempt {attempt}/{retries})...")
            response = requests.post(OLLAMA_URL, json=payload, timeout=30)
            response.raise_for_status()
            return response.json().get("response", "").strip()
        except requests.exceptions.ConnectionError:
            return "Cannot connect to Ollama. Please make sure ollama is running."
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == retries:
                return "The model did not respond. Please try again."