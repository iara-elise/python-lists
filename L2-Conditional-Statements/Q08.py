valor_01 = int(input("Valor 01: "))
valor_02 = int(input("Valor 02: "))
valor_03 = int(input("Valor_03: "))

if valor_01 + valor_02 > valor_03 and valor_01 + valor_03 > valor_02 and valor_02 + valor_03 > valor_01:
    print("É possível formar um triângulo.")

    if valor_01 == valor_02 and valor_02 == valor_03:
        print("O triângulo é equilátero!")

    elif valor_01 == valor_02 or valor_01 == valor_03 or valor_02 == valor_03:
        print("O triângulo é isosceles!")

    else:
        print("O triângulo é escaleno!")

else:
    print("Não é possível formar um triângulo.")