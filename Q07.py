print("NOTAS \n")

nota_01 = float(input("Nota 01: "))
nota_02 = float(input("Nota 02: "))
nota_03 = float(input("Nota 03: "))
nota_04 = float(input("Nota 04: "))

print("\nPESOS: \n")

peso_01 = int(input("Peso 01: "))
peso_02 = int(input("Peso 02: "))
peso_03 = int(input("Peso 03: "))
peso_04 = int(input("Peso 04: "))

somaDosPesos = peso_01 + peso_02 + peso_03 + peso_04
mediaPonderada = (nota_01 * peso_01 + nota_02 + peso_02 + nota_03 * peso_03 + nota_04 * peso_04) / somaDosPesos

print(f"\nMÉDIA PONDERADA: {mediaPonderada:.1f}")
