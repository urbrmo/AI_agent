import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv



def main():
    load_dotenv()

    # Check if a prompt was provided
    if len(sys.argv) < 2:
        print("Error: No prompt provided.\nUsage: python3 main.py \"Your prompt here\"")
        sys.exit(1)

    # Join all arguments after the script name as the prompt
    prompt = " ".join(sys.argv[1:])

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages)
    
def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
