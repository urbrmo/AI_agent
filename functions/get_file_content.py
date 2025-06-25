import os

def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([working_directory, target_file_path]) != working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10001
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string)>10000:
                file_content_string = file_content_string[:10000] + f"[...File \"{file_path}\" truncated at 10000 characters]"
        return file_content_string


    except Exception as e:
        return f"Error: {str(e)}"