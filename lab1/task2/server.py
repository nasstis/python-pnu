import threading
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def remove_client(client):
    index = clients.index(client)
    nickname = nicknames[index]
    clients.remove(client)
    client.close()
    nicknames.remove(nickname)
    broadcast(f'{nickname} left the chat'.encode('utf-8'))

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                if message.decode('utf-8') == '/quit':
                    remove_client(client)
                    break
                else:
                    broadcast(message)
        except:
            remove_client(client)
            break

def receive():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connected with {client_address}')

        client_socket.send('nick'.encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        
        nicknames.append(nickname)
        clients.append(client_socket)

        print(f'Nickname of client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('utf-8'))
        client_socket.send('Connected to the server'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client_socket,))
        thread.start()

print('Server is listening...')
receive()