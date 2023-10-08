import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    message = input("Введіть текст для відправки (або 'закрити з'єднання' для виходу): ")
    client_socket.send(message.encode())

    if message == "закрити з'єднання":
        break

    response = client_socket.recv(1024).decode()
    print(f"Від сервера отримано: {response}")

client_socket.close()