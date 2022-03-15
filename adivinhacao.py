print("***********************************")
print("Bem vindo ao jogo de adivinhação!")
print("***********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")
numero = int(chute)

print("Você digitou ", chute)

if(numero_secreto == numero):
    print("Voce acertou")
else:
    print("Voce errou")