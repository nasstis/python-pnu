import socket
import threading 

nickname = input('Welcome to the chat! If you want to leave write "/quit". Now choose a nickname: ')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'nick':
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            if not client_socket._closed:
                print('Something went wrong')
            client_socket.close()
            break

def write():
    while True:
        message = input('')
        if message == '/quit':
            client_socket.send(message.encode('utf-8'))
            client_socket.close()
            break
        message = f'{nickname}: {message}'
        client_socket.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()