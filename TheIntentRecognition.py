import requests

# Set your API key (Keep it private and secure)
API_KEY = "479c45e695dd4f7c970563b84579babf"

# DeepSeek API Endpoint
API_URL = "https://api.deepseek.com/v1/chat/completions"

def ask_ai(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    # Define the AI's behavior to focus only on agriculture
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are an AI assistant specialized in agriculture. Answer only agriculture-related questions."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response_json = response.json()
        
        if "choices" in response_json:
            return response_json["choices"][0]["message"]["content"]
        else:
            return "Sorry, I couldn't process that request."
    except Exception as e:
        return f"Error: {e}"

def chatbot():
    print("🌱 Agriculture AI Chatbot: Ask me anything related to farming, crops, soil, or market prices!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Happy farming! 🚜")
            break
        
        response = ask_ai(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
