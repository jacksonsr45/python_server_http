import socket

target_host = 'localhost'
target_port = '80'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client.send('Conecting.....')

response = client.recv(4096)
print(response)