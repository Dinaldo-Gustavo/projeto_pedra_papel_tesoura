from random import choice

print(f"{'-' * 20}")
print(f"Vamos jogar Pedra, Papel ou Tesoura")
print(f"{'-' * 20}")

while True:

    computador = choice(["Pedra", "Papel", "Tesoura"])
    usuario = input("Escolha entre Pedra, Papel e Tesoura (para encerrar digite 'Parar'): ").capitalize().strip()

    if usuario == "Parar":
        print("O jogo acabou!")
        break

    elif usuario not in ["Pedra", "Papel", "Tesoura"]:
        print("Entrada Inválida!")
        print("Tente Novamente")

    elif usuario == computador:
        print(f"Eu escolhi {computador} e você {usuario}")
        print("EMPATE")

    elif (usuario == "Papel" and computador == "Pedra" or usuario == "Pedra" and computador == "Tesoura"
          or usuario == "Tesoura" and computador == "Papel"):
        print(f"Eu escolhi {computador} e você {usuario}")
        print("Você venceu!")

    else:
        print(f"Eu escolhi {computador} e você {usuario}")
        print("Eu venci!")
