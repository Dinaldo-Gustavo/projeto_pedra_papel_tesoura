import math as mt


class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        return self.numero1 + self.numero2

    def subtrair(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 == 0:
            return "Erro: Divisão por zero não é permitida"
        else:
            return self.numero1 / self.numero2

    def potencia(self):
        return pow(self.numero1, self.numero2)

    def raiz_quadrada(self):
        if self.numero1 < 0:
            return "Erro: Raiz quadrda de número negativo não é permitida"
        else:
            return mt.sqrt(self.numero1)


print("CALCULADORA BÁSICA")

while True:
    escolhas = {1: 'soma',
                2: 'subtração',
                3: 'multiplicação',
                4: 'divisão',
                5: 'potenciação',
                6: 'raiz quadrada'}

    print(f"{'-' * 40}")

    print(escolhas)

    print(f"{'-' * 40}")

    try:
        escolha = int(input("Escolha o número da operação que você deseja realizar (-1 para sair): "))
    except ValueError:
        print("Entrada Inválida! Digite um número inteiro.")
        continue

    print(f"{'-' * 40}")

    if escolha == -1:
        print("Programa Encerrado!")
        break

    elif escolha not in [1, 2, 3, 4, 5, 6]:
        print("Opção Inválida, Tente novamente!")

    else:
        try:
            num1 = float(input("Escolha o primeiro número para usar no cálculo: "))
            num2 = float(input("Escolha o segundo número para usar no cálculo: "))
        except ValueError:
            print("Entrada Inválida! Digite um número válido")
            continue

        calculo = Calculadora(num1, num2)
        if escolha == 1:
            print("A soma dos valores é: ", calculo.somar())

        elif escolha == 2:
            print("A subtração dos valores é: ", calculo.subtrair())

        elif escolha == 3:
            print("A multiplicação dos valores é: ", calculo.multiplicar())

        elif escolha == 4:
            print("A divisão dos valores é: ", calculo.dividir())

        elif escolha == 5:
            print(f"A potenciação da base {num1} elevado por {num2} é: ", calculo.potencia())

        elif escolha == 6:
            print(f"A raiz quadrada de {num1} é: ", round(calculo.raiz_quadrada(), 5))