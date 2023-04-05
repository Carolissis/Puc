*** Settings *** 
Documentation    Essa suite testa o site da amazon.com.busca_produtos
Test Setup       Abrir o navegador 
Test Teardown    Fechar o navegador 


*** Test Cases ***
Caso de teste número 01- Acesso ao meno "Eletronicos"
    [Documentation]    Esse teste verifica o menu eletronico do site da amazom.com.br
    ...                e verifica a categoria Computadores e Informatica 
    [Tags]             menus
    Acessar a home page pelo site Amazon.com.br
    Entrar no menu "Eletronicos e tecnologia"
    Verificar se o titulo da pagina fica "Eletronicos e Tecnologia/ Amazon.com.br"
    Verificar se aparece a frase "Eletronicos e Tecnologia"
    Verificar se aparece a categoria "Computadores e Informatica"


Caso de teste número 02- Pesquisa de um produto
    [Documentation]    Esse teste verifica a busca de um produto  
    [Tags]             busca_produtos lista_buscas
    Acessar a home page pelo site Amazon.com.br
    Digitar o nome do produto "XboxSeries S" no campo de Pesquisa
    Clicar no botão de Pesquisa
    Verificar o resultado da pesquisa se esta listando o produto pesuisado