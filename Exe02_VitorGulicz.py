#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos, solicite ao usuário para digitar um nome de produto e exiba a posição dele, 
# em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.
produtos=("apple", "tv","mac", "iphone x", "IPad", "apple watch", "mac book", "airpods","chromebook","android")
print(produtos)
produto=input("Digite um nome de um produto: ")
if produto in produtos:
    i=produtos.index(produto)
    print("A posição deste produto é {} - Vitor Gulicz".format(i))
else:
    print("Produto inexistente")
numero=int(input("Digite um numero entre 0 a 9: "))
if numero<10:
    print("Produto do numero escolhido: {} - Vitor Gulicz".format(produtos[numero]))
else:
    print("Numero invalido")