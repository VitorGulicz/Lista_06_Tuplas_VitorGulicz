#Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista. Depois de inserir os três nomes, pergunte se deseja 
# adicionar outro. Se o fizer, permita que adicione mais nomes até responder "não". Quando ele responder "não", mostre quantas pessoas ele convidou para a festa, uma vez 
# que o usuário tenha completado sua lista de nomes, exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista. Pergunte ao
#  usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.
nomes=[]
numero=0
for numero in range(3):
    nomes.append(input("Digite o nome do convidado para a festa: "))
op=input("Deseja adicionar outro?(sim ou não)")
while op!="não":
    nomes.append(input("Digite o nome do convidado para a festa: "))
    op=input("Deseja adicionar outro?(sim ou não)")
i=len(nomes)
print("Pessoas convidadas para a festa: {}. \nNumero de pessoas convidadas: {}".format(nomes,i))
nomeop=input("Digite o nome da lista que deseja remover: ")
if nomeop in nomes:
    a=nomes.index(nomeop)
    print("Posição do nome na lista: {}".format(a))
    opRemover=input("Deseja remover o {} da lista(sim ou não)".format(nomeop))
    if "sim" in opRemover.lower():
        nomes.remove(nomeop)
    if "não" in opRemover.lower():
        print("Nome não removido")
    else:
        print("Opção invalida")
    print(nomes)
print("Vitor Gulicz")