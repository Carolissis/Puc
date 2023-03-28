#Definicoes do Input 
x= input('Digite algo: ')
print('Só tem espacos? ', x.isspace())
print('É um Número? ',x.isnumeric())
print('É alafbetico? ',x.isalpha())
print('É alphanumerico? ', x.isalnum())
print('Está em maiúscula? ', x.isupper())
print('Está em minúscula? ', x.islower())
print('Está capitalizada? ', x.istitle())