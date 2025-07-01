import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompts import system_prompt
from function_declarations import *
from functions.call_function import call_function


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

    MAX_ITERS = 20
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
    
def generate_content(client, messages, verbose):
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
        ]
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config = types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    print("Response:")
    if response.function_calls == None:
        return response.text
    
    function_responses = []
    for function in response.function_calls:
        function_call_result = call_function(function, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="tool", parts=function_responses))


if __name__ == "__main__":
    main()
