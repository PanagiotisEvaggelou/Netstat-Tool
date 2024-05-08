import subprocess
import msvcrt

# Function to check if a port is open and kill the process if it is
def check_and_kill_port(port):
    # Use netstat to find the process using the port
    cmd = f'netstat -ano | findstr :{port}'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()

    # If the port is open, the output will not be empty
    if output:
        # Extract the PID from the output
        pid = output.decode('utf-8').split()[4]
        print(f"Port {port} is open. Killing process with PID {pid}.")

        # Use taskkill to kill the process
        kill_cmd = f'taskkill /F /PID {pid}'
        subprocess.run(kill_cmd, shell=True)
    else:
        print(f"Port {port} is not open.")

# Ask the user for the port number
port = input("Enter the port number you want to check and kill: ")

# Check the port
check_and_kill_port(port)

# Keep the command window open
print("Press any key to close the window...")
msvcrt.getch() # Wait for a key press
