"""
Dado un número entero, decir cuántos dígitos tiene.
Ejm. resultado:
*Dame el número: 6667
*6667 tiene: 4 dígitos

"""
print(f"Ejm. Resultado: \n")
numero = int(input("Ingrese un número: "))
i = len(str(numero))
print(f"{numero} tiene: {i} digitos \n")
