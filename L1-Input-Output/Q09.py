altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / altura ** 2
print("Seu IMC é", "{:.2f}".format(imc))
