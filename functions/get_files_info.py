import os

def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = working_directory

    try:
        # Normalize paths
        working_directory = os.path.abspath(working_directory)
        target_directory = os.path.abspath(os.path.join(working_directory, directory))

        # Check if target_directory is inside working_directory
        if os.path.commonpath([working_directory, target_directory]) != working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if it's actually a directory
        print("Working Directory:", working_directory)
        print("Target Directory:", target_directory)
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        # Build info string for each file/folder in directory
        output_lines = []
        for item in os.listdir(target_directory):
            item_path = os.path.join(target_directory, item)
            try:
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                output_lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
            except Exception as e:
                return f"Error: Failed to read information for {item} - {str(e)}"

        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: {str(e)}"