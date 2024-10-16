import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

server = 'smtp.gmail.com' 
port = 587 
username = "segurancainfromacaotesteaula@gmail.com" 
password = "xzsbrsemwgycrvjt" 

mail_from = "segurancainfromacaotesteaula@gmail.com" 
mail_to = "caroolassissss@gmail.com" 
mail_subject = "Segurança da informação" 
mail_body = "Olá Mundo, Python é Legal!!" 

mensagem = MIMEMultipart() 
mensagem['From'] = mail_from 
mensagem['To'] = mail_to 
mensagem['Subject'] = mail_subject 
mensagem.attach(MIMEText(mail_body, 'plain')) 

connection = smtplib.SMTP(server, port) 
connection.starttls() 
connection.login(username,password) 
connection.send_message(mensagem) 
connection.quit() 