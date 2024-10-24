*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://visitor.r20.constantcontact.com/manage/optin?v=001nFupVrVrNd4UjGfZPy62KHBuj79961VKz4QWIP-7uVcCr1I-NMtOt3RO6gWporZprHQ_BuPjcMuMYXvwSb-6Qh_PdVoVxfJWRDbpNc02StM%3DLinks to an external site.
${BROWSER}    chrome
${EMAIL}       id=inputProp0
#Variaveis com os campos do formulario
${NOME}        id=inputProp1
${CARGO}       id=inputProp2
${EMPRESA}     id=inputProp3
${BT_SALVAR}   id=update-profile-submit-btn

*** Test Cases ***
C1 - Preencher todos os campos do formulario corretamente
#Caso de teste de sucesso para preencher os campos do formulario
    Entrar no site
    Preencher todos os campos corretamente
    Clicar em enviar
    Verificar que o formulario foi enviado com sucesso

*** Keywords ***
Entrar no site
#Abre o brwoser e entra no site, confere se o site foi aberto
    Open Browser    ${URL}    ${BROWSER}   
    Maximize Browser Window
    Sleep     3s
    Page Should Contain    Se inscreva e fique atualizado!

Preencher todos os campos corretamente
#preenche todos os campos, recebe os campos como variaveis e preenche com o valor entre as apas parea reutilizar a keyword
    Preencher o campo "${EMAIL}" com o valor "caroline@gmail.com"
    Preencher o campo "${NOME}" com o valor "Caroline Assis"
    Preencher o campo "${CARGO}" com o valor "Av. Silva Jardim 1234"
    Preencher o campo "${EMPRESA}" com o valor "EzRent"
    Capture Page Screenshot

Clicar em enviar
    Click Button    ${BT_SALVAR} 

Verificar que o formulario foi enviado com sucesso
#Verifica se deu certo o envio
    Page Should Contain    Obrigado

Preencher o campo "${CAMPO}" com o valor "${VALOR}"
    Input Text    ${CAMPO}    ${VALOR}