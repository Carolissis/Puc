import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 9999
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    SERVER.bind((HOST, PORT))
except socket.error as e:
    print(str(e))
    sys.exit()

SERVER.listen()
print(f'Servidor iniciado em {HOST}:{PORT}. Aguardando conexões...')

clientes = []
nomes = []

def broadcast(message):
    for cliente in clientes:
        cliente.send(message)

def handle(cliente):
    index = clientes.index(cliente)
    nome = nomes[index]

    while True:
        try:
            message = cliente.recv(1024)
            broadcast(message)
        except:
            clientes.remove(cliente)
            nomes.remove(nome)
            cliente.close()
            broadcast(f'{nome} saiu do chat!'.encode('ascii'))
            print(f'{nome} se desconectou')
            break

def receive():
    while True:
        cliente, addr = SERVER.accept()

        cliente.send('NICK'.encode('ascii'))
        nome = cliente.recv(1024).decode('ascii')
        nomes.append(nome)
        clientes.append(cliente)

        print(f'Conexão estabelecida com {nome}')  

        print(f'Nome do cliente é {nome}!')
        broadcast(f'{nome} entrou no chat!'.encode('ascii'))
        cliente.send('Conectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(cliente))
        thread.start()


receive()