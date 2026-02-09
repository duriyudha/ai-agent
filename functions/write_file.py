import os


def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    if not valid_file_path:
        return f'Error: Cannot read "{target_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    try:
        directory = os.path.dirname(target_path)
        os.makedirs(directory, exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"