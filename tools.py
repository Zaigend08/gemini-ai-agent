import os

def calculator(expression: str) -> str:
    """Evaluate a simple math expression safely."""
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Error evaluating expression: {e}"

def create_folder(name: str) -> str:
    """Create a folder in the current directory."""
    try:
        os.makedirs(name, exist_ok=True)
        return f"Folder '{name}' created."
    except Exception as e:
        return f"Error creating folder: {e}"