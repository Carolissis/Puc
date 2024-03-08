import pyrebase #importar o pyrebase4 no pip
import getpass #leitura da senha sem eco

firebaseConfig = {
  "apiKey": "AIzaSyCqKgv9sP8UaFi9de-3_QFVnECd9BlR7_Y",
  "authDomain": "testeaulaseginfo.firebaseapp.com",
  "projectId": "testeaulaseginfo",
  "databaseURL": "https://" + "fir-pucpr" + ".firebaseio.com",
  "storageBucket": "fir-pucpr",
  "messagingSenderId": "1078258418036",
  "appId": "1:1078258418036:web:04cd75f9bba5c548316c21",
  "measurementId": "G-K630CLR8CF"
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = getpass.getpass("Digite sua senha, com pelo menos 6 caracteres: ")

status = auth.sign_in_with_email_and_password(user,password)
idToken = status["idToken"]
info = auth.get_account_info(idToken) 

print("Resultado: ", status)
print("Token: ", idToken)
print("Info: ", info)

pausa = input('Pressione ENTER para finalizar...')
# Baseado em código de https://aicodeconvert.com/

