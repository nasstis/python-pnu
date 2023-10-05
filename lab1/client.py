import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345))

message = input("Введіть текст для відправлення: ")
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"Від сервера отримано: {response}")

client_socket.close()