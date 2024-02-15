"""
Escriba un programa que pida una temperatura en grados Celsius y que escriba esa temperatura en grados Fahrenheit. La relación entre
grados Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1.8 * C + 32

"""

C = float(input("Ingrese la Temperatura en Celsius "))

def func_fahrenheit(C):
    F = 1.8 * C + 32
    print(f"La Temperatura en Fahrenheit es de {F}°F")
    return F
    
temperatura = func_fahrenheit(C)