#nome do usuario, mostre em seguidsa o primeiro e o ultimo nome sepradamente, ex; ana de souza primeiro= ana 
#ultimo= souza 
n= str(input('Digite seu nome: '))
x= n.split()
print('Prazer em te conhecer! ')
print('Primeiro nome; {}'.format(x[0].title()))
print('Ultimo nome: {}'.format(x[len(x)-1].title()))