import os

def execute_command(command_input):
    """
    Executes a shell command directly from user input.
    This is vulnerable to command injection.
    """
    os.system(f"echo Executing: {command_input}")
    os.system(command_input)

if __name__ == "__main__":
    user_input = input("Enter a command to execute: ")
    execute_command(user_input)


print(f"[INFO] Environment: {os.environ}")
