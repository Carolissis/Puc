#  A senha deve ter mínimo 8 e máximo 15 caracteres.
#  A senha deve ter pelo menos uma letra maiúscula.
#  A senha deve ter pelo menos uma letra minúscula.
#  A senha deve ter pelo menos um símbolo. Ex: * ! # $ % & + - / : ; = ? @ \ |
#  A senha deve ter pelo menos um número.

eps = ['*', '!', '#', '$', '%', '&', '+', '-', '/', ':', ';', '=', '?', '@','|']
tentativas_maximas = 3

for tentativa in range(1, tentativas_maximas+1):
    senha = (input('Digite sua senha, ela deve conter:\nDe 8 a 15 caraceres\nPelo menos uma letra maiuscula e maiuscula\nUma caractere especial\nSenha: '))
    n = ap = ag = e = 0
    for c in senha:
        if c.isdigit():
            n+=1
        if c.islower():
            ap+=1 
        if c.isupper():
            ag+=1
        if c in eps:
            e+=1 
    if n >= 1 and e >= 1 and ag >= 1 and ap >= 1 and 8 <= len(senha) <= 15:
        print('Sua senha é valida')
        print(f'Sua senha é: {senha}')
        print(f'Sua senha contem {len(senha)} caracteres, sendo {ap} letras minusculas, {ag} letras maiusculas, {n} números e {e} caracteres especiais')
        break
    else: 
        print('Esta faltando algum requisito...')
        if n < 1:
            print('- Pelo menos um número.')
        if ag < 1:
            print('- Pelo menos uma letra maiúscula.')
        if e < 1:
            print('- Pelo menos um caractere especial.')
        if len(senha) < 8 or len(senha) > 15:
            print('- De 8 a 15 caracteres.')
        if tentativa == tentativas_maximas:
            print('Você atingiu o número máximo de tentativas.')
        else:
            print(f'Você tem mais {tentativas_maximas - tentativa} tentativa(s) restante(s).')

