import socket
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345))

server_socket.listen()
print("Сервер чекає на підключення...")

client_socket, client_address = server_socket.accept()
print(f"З'єднання з {client_address}")

data = client_socket.recv(1024).decode()
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Отримано: {data}\nЧас отримання: {current_time}")

response = "Отримано ваше повідомлення"
client_socket.send(response.encode())

client_socket.close()
server_socket.close()