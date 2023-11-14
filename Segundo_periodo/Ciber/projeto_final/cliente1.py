import socket
import threading

nome = input("Digite seu nome: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 9999

try:
    cliente.connect((HOST, PORT))
except:
    print('Erro de conexão')
    exit()

def receive():
    while True:
        try:
            message = cliente.recv(1024).decode('ascii')
            if message == 'NICK':
                cliente.send(nome.encode('ascii'))
            else:
                print(message)
        except:
            print("Erro!")
            cliente.close()
            break

def write():
    while True:
        message = f'{nome}: {input("")}'
        cliente.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()