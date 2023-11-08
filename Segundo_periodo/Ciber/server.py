import socket

#criação do socket e das informações do servidor
HOST = '127.0.0.1'
PORT = 9999

#IPV4 É O PARAAMETRO AF_INET
#TCP É O PARAMETRO SOCK_STREAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AGORA FAZEMOS O "PLUG" DO IP COM A PORTA COM A FUNÇÃO BIND
sock.bind((HOST,PORT))
#127.0.0.1:9999
#O servidor precisa entrar no modo escuta (listening)
sock.listen()
print(f"o servidor {HOST}:{PORT} está ativo e aguardando conexões...")

#função que é "acesa" pelo connect do cliente, retorna 2 parametros
#conn é o socket do cliente e o ender é o endereço
#aqui é o ponto que conectamos com um cliente 
#para termos vários, precisamos de um loop infinito (#toDO)

conn, ender = sock.accept()
print("Conexão em: ", ender)

#loop para receber buffer de dados
while True:
    dados = conn.recv(1024) #1024 aceita 1024 bytes (1024 caracteres)
    print(dados)
    if not dados: 
        print("Fechando conexão...")
        conn.close()
        break
    conn.sendall(dados)

import socket
import threading

HOST = '127.0.0.1'
PORT = 9999

# Lista para manter o controle dos clientes conectados
clientes = []

def client_thread(conn, addr):
    """
    Thread para lidar com cada cliente conectado.
    """
    # Avisar todos os clientes que uma nova conexão foi estabelecida
    broadcast(f"O usuário {addr} entrou no chat!", conn)

    while True:
        try:
            # Receber dados do cliente
            dados = conn.recv(1024)
            if dados:
                print(f"Mensagem de {addr}: {dados.decode()}")
                # Broadcast a mensagem para todos os clientes
                broadcast(dados, conn)
            else:
                # Remover o cliente da lista quando a conexão for fechada
                remove_connection(conn)
                break
        except Exception as e:
            # Em caso de erro, remover a conexão e terminar a thread
            print(f"Erro: {e}")
            remove_connection(conn)
            break

def broadcast(message, connection):
    """
    Função para enviar uma mensagem para todos os clientes conectados,
    exceto o remetente da mensagem.
    """
    for client in clientes:
        if client != connection:
            try:
                client.send(message)
            except Exception as e:
                print(f"Erro ao enviar mensagem broadcast: {e}")
                remove_connection(client)

def remove_connection(conn):
    """
    Remove a conexão da lista de clientes e fecha o socket.
    """
    if conn in clientes:
        clientes.remove(conn)
        conn.close()

# Configuração do socket do servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

print(f"O servidor {HOST}:{PORT} está ativo e aguardando conexões...")

while True:
    conn, addr = sock.accept()
    print("Conexão estabelecida com: ", addr)

    # Adicionar o socket do cliente à lista de clientes
    clientes.append(conn)

    # Iniciar uma nova thread para lidar com a nova conexão
    thread = threading.Thread(target=client_thread, args=(conn, addr))
    thread.start()
