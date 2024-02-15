"""
Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal
(imc). El imc se calcula con la fórmula: imc = (peso/altura**2)

"""

def funcion_imc (a,b):
    imc = round(a/b**2, 1)
    print(f"El IMC es {imc} Kg/m**2")
    return imc

peso = float(input("Ingrese el peso en Kilogramos: "))
altura = float(input("Ingrese la altura en metros cuadrados: "))

resultado_imc = funcion_imc (peso, altura)