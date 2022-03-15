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
    if(numero > numero_secreto):
        print("Voce errou! O seu chute foi maior que o numero secreto.")
    elif (numero < numero_secreto):
        print("Voce errou! O seu chute foi menor que o numero secreto.")