print("***********************************")
print("Bem vindo ao jogo de adivinhação!")
print("***********************************")

numero_secreto = 42
tentativas = 3
rodada = 1

while(rodada <= tentativas):
    print("Rodada {} de {}". format(rodada, tentativas))
    chute = input("Digite o seu número: ")
    numero = int(chute)

    acertou = numero == numero_secreto
    maior   = numero > numero_secreto
    menor   = numero < numero_secreto

    if(acertou):
        print("Voce acertou")
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto.")
        elif (menor):
            print("Voce errou! O seu chute foi menor que o numero secreto.")

    rodada = rodada + 1

print("Fim de jogo!")