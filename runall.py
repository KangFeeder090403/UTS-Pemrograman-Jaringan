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

for command in commands:
    run_command_in_terminal(command)
    time.sleep(2) 
