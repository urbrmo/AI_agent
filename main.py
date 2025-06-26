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

    # Detect --verbose flag
    verbose = False
    args = sys.argv[1:]  # Exclude the script name

    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")

    # Join all arguments after the script name as the prompt
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, verbose)
    
def generate_content(client, messages, user_prompt, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config = types.GenerateContentConfig(system_instruction=system_prompt)
    )

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
