import socket

target_host = 'localhost'
target_port = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
response = client.recv(4096)

print(response)