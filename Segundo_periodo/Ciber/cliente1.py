import socket 

#PRECISAMOS NOS CONECTAR NO SERVIDOR
HOST = '127.0.0.1' #(LOCALHOST)
PORT = 9999

sock_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#cliente solicita conexão com o servidor 
sock_cliente.connect((HOST, PORT))
#cliente envia dados para o servidor 
sock_cliente.sendall(str.encode("Ola eu sou o cliente"))

dados = sock_cliente.recv(1024)
print("Mensagem recebida do servidor para teste: ")
print(dados.decode())