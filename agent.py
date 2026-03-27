from google import genai
from google.genai import types
from config import API_KEY, MODEL_NAME
from tools import calculator, create_folder

def run_agent():
    client = genai.Client(api_key=API_KEY)
    
    config = types.GenerateContentConfig(tools=[calculator, create_folder])
    history = []

    print("Agent is ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=history,
                config=config
            )
        except Exception as e:
            print("API Error:", e)
            continue

        agent_text = response.text
        print("Agent:", agent_text)
        history.append(response.candidates[0].content)