import subprocess
import platform
import time

def run_command_in_terminal(command):
    if platform.system() == "Windows":
        subprocess.Popen(["start", "cmd", "/k", command], shell=True)
    elif platform.system() == "Linux":
        subprocess.Popen(["x-terminal-emulator", "-e", command])
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", "-a", "Terminal", command])
    else:
        print("Unsupported platform")

# List of commands you want to run in separate terminals
# until client-10.py
commands = [
    "python server.py",
    "python client.py",
    "python client2.py",
    "python client3.py",
    "python client4.py",
    "python client5.py",
    "python client6.py",
    "python client7.py",
    "python client8.py",
    "python client9.py",
    "python client10.py",
]

# Run each command in a separate terminal
for command in commands:
    run_command_in_terminal(command)
    time.sleep(1)  # Adjust delay as needed to allow terminals to open before running the next command