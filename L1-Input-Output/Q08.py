print("EQUAÇÃO DE SEGUNDO GRAU \n")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
x = float(input("Digite o valor de x: "))

y = (a * x ** 2) + (b * x) + c
print("O valor de y é:", "{:.0f}".format(y))