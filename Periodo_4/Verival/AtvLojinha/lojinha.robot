***Settings***
Library    SeleniumLibrary

***Variables***
${URL}    http://165.227.93.41/lojinha-web/

***Keywords***
Acessar a pagina home do site
    Open Browser    ${URL}    chrome  
    Sleep     5s
    Element Should Be Visible    xpath=//*[@class="blue-grey darken-1"]

Digitar no campo usuário o usuário ativo “rafael”
    Click Element    name=usuario
    # Input Text       id="usuario"    rafael
***Test Cases***
CT1 - Realizar login com usuário ativo
    Acessar a pagina home do site
    Digitar no campo usuário o usuário ativo “rafael”
#     Digitar no campo senha a senha o usuário ativo “123456”
#     Acionar o botão entrar e Verificar se nome do usuário aparece na tela de boas vindas

# CT2 - Realizar login com usuário inativo
#     Acessar a pagina home do site
#     Digitar no campo usuário o usuário inativo “Paulo”
#     Digitar no campo senha a senha o usuário inativo “111111”
#     Acionar o botão entrar e verificar mensagem de falha no login