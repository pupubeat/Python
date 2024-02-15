"""
Introducir dos números enteros por teclado. El programa debe:
• Imprimir los números que hay entre ellos, empezando por el más pequeño, independientemente del orden introducido.
• Calcular y visualizar cuantos números hay, cuántos de ellos son pares y su suma.

"""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

x = range(a+1, b)
rango = len(x)

print(f"Primer Numero: {a}")
print(f"Segundo Numero: {b}")
conteo = 0
pares = 0

for n in x:
    print(n)

numerosPares = []

for n in x:
    if (n % 2) == 0:
        
        conteo+=1
        numerosPares.append(n)

print(numerosPares)
sumapares = sum(numerosPares)

print(f"Entre {a} y {b} hay {rango} numeros siendo {conteo} pares")
print(f"La suma de los pares es {sumapares}")