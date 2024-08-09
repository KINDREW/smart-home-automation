import os

def execute_voice_command(command):
    if command == "turn on the light":
        os.system("python3 src/relay_control.py on")
    elif command == "turn off the light":
        os.system("python3 src/relay_control.py off")
    else:
        print("Unknown command")
