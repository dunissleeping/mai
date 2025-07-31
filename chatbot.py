import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# ✅ Load .env file explicitly from current script folder
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# ✅ Get API key from environment
api_key = "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"


# ✅ Raise error if key is not found
if not api_key:
    raise ValueError("❌ API key not found. Please check your .env file.")

# ✅ Initialize OpenAI client
client = OpenAI(api_key=api_key)

# 💬 Chat function
def chat(user_input):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a compassionate AI mental health assistant. "
                "Speak empathetically, like a supportive therapist. "
                "Listen, understand emotions, and help the user feel heard and safe."
            ),
        },
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or use "gpt-3.5-turbo" if needed
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# 🚀 CLI Chatbot loop
if __name__ == "__main__":
    print("🧠 Mental Health AI Assistant (type 'quit' to exit)\n")
    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() == "quit":
                print("👋 Take care. Remember, you're not alone.")
                break
            reply = chat(user_input)
            print("AI:", reply, "\n")
        except KeyboardInterrupt:
            print("\n👋 Session ended.")
            break
        except Exception as e:
            print("❌ Error:", e)
