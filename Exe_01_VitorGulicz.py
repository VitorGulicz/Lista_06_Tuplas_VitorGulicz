#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.
paises=("Brasil","Venezuela","Argentina","Peru","Guatemala")
pais=input("Digite um dos paises a seguir:{}".format(paises))
if pais in paises:
    i=paises.index(pais)
    print("A posição deste pais na lista é {} - Vitor Gulicz".format(i))
else:
    print("pais invalido - Vitor Gulicz")