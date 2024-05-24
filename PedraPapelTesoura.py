jogadas= ('pedra','papel','tesoura')
import random
ia= random.randint (1,3)
print("Escolha entre PEDRA, PAPEL E TESOURA (1,2,3)")
jogador=int(input("Digite o número da sua escolha: "))
#Escolhendo pedra
if ia==1:
    if jogador==1:
        print(f"Empate")
    if jogador==2:
        print("Você venceu")
    if jogador ==3:
        print("Você perdeu")
#Escolhendo papel
if ia==2:
    if jogador==1:
        print("Você perdeu")
    if jogador==2:
        print("Empate")
    if jogador ==3:
        print("Você venceu")
if ia ==3:
    if jogador ==1:
        print("Você venceu")
    if jogador ==2:
        print("Você perdeu")
    if jogador ==3:
        print("Empate")

print(f"Você escolheu: {jogador} a ia escolheu: {ia}")