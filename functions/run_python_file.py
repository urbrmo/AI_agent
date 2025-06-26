import os
import subprocess

def run_python_file(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([working_directory, target_file_path]) != working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists((target_file_path)):
        return f'Error: File "{file_path}" not found.'
    
    if not target_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(['python3', target_file_path], capture_output=True, cwd=os.path.dirname(target_file_path),timeout=30, text=True,)
        if result.returncode != 0:
            return f"STDOUT:{result.stdout}\nSTDERR:{result.stderr}\nProcess exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            return "No output produced."
        else:
            return f"STDOUT:{result.stdout}\nSTDERR:{result.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"