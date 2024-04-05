# Caroline Assis 05/04/2024

import os
import stat
import datetime

data_hora_atual = datetime.datetime.now()
data_atual = data_hora_atual.strftime('%Y-%m-%d')
hora_atual = data_hora_atual.strftime('%H:%M:%S')

if os.path.isfile("permissao.txt"):
    print("Esse arquivo já foi criado")

os.chmod("permissao.txt", stat.S_IRWXU)

arquivo = open("permissao.txt", 'w')
arquivo.write("Data: " + data_atual + "\nHora: " + hora_atual)
arquivo.close()

os.chmod("permissao.txt", stat.S_IRUSR)



