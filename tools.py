import os
import subprocess


def write_file(file_path, content):
    if not isinstance(file_path, str) or not isinstance(content, str):
        raise ValueError("file_path and content must be strings")
    if not os.path.isabs(file_path):
        raise ValueError("file_path must be an absolute path")
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        raise IOError(f"Failed to write to file: {e}")


def read_file(file_path):
    if not isinstance(file_path, str) or not os.path.isabs(file_path):
        raise ValueError("file_path must be an absolute path")
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise IOError(f"Failed to read from file: {e}")


def run_python(script_path):
    if not isinstance(script_path, str) or not os.path.isabs(script_path):
        raise ValueError("script_path must be an absolute path")
    try:
        result = subprocess.run(["python", script_path], capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Error running script: {result.stderr}")
        return result.stdout
    except Exception as e:
        raise RuntimeError(f"Failed to run script: {e}")
