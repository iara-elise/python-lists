valor_01 = int(input("Valor 01: "))
valor_02 = int(input("Valor 02: "))

if valor_01 > valor_02:
    diferenca = valor_01 - valor_02
    print(f"\nA diferença entre {valor_01} e {valor_02} é {diferenca}")

else:
    diferenca = valor_02 - valor_01
    print(f"\nA diferença entre {valor_02} e {valor_01} é {diferenca}")