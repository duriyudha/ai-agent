import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory with optional command-line arguments. Returns stdout, stderr, and exit code",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the Python script",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    if not valid_file_path:
        return f'Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    try:
        command = ["python", target_path]
        if args:
            command.extend(args)
        result = subprocess.run(command,
                                capture_output=True,
                                text=True,
                                timeout=30)
        
        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            output += "No output produced"
        else:
            output += f"STDOUT: {result.stdout}"
            output += f"STDERR: {result.stderr}"
        return output
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
            