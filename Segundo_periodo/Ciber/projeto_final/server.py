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

def send_message(sender_socket, message):
    nome_remetente, _, content = message.partition(': ')

    if content.startswith("/privado"):
        try:
            _, nome_destinatario, mens_privada = content.split(maxsplit=2)
            if nome_destinatario in nomes:
                index = nomes.index(nome_destinatario)
                destinatario_socket = clientes[index]
                destinatario_socket.send(f'Mensagem privada de {nome_remetente}: {mens_privada}'.encode('ascii'))
            else:
                sender_socket.send(f'Usuário {nome_destinatario} não encontrado.'.encode('ascii'))
        except ValueError:
            sender_socket.send('Formato de mensagem privada inválido. Use: /private [nome] [mensagem]'.encode('ascii'))
    else:
        broadcast_message = f'{nome_remetente}: {content}'
        for client_socket in clientes:
            if client_socket != sender_socket:
                client_socket.send(broadcast_message.encode('ascii'))


def handle(cliente):
    while True:
        try:
            message = cliente.recv(1024).decode('ascii')
            if message:
                send_message(cliente, message)
            else:
                handle_disconnection(cliente)
                break
        except:
            handle_disconnection(cliente)
            break

def handle_disconnection(cliente):
    index = clientes.index(cliente)
    nome = nomes[index]
    broadcast(f'{nome} saiu do chat!'.encode('ascii'))
    print(f'{nome} se desconectou')
    clientes.remove(cliente)
    cliente.close()
    nomes.remove(nome)


def receive():
    while True:
        cliente, addr = SERVER.accept()  

        cliente.send('NICK'.encode('ascii'))
        nome = cliente.recv(1024).decode('ascii')
        nomes.append(nome)
        clientes.append(cliente)

        print(f'Conexão estabelecida com {nome} de {addr[0]}: {addr[1]}') 

        broadcast(f'{nome} entrou no chat!'.encode('ascii'))
        cliente.send('Conectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(cliente,))
        thread.start()

receive()