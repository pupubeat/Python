"""
Dadas dos notas, correspondientes a teoría y práctica, calcule su
promedio y entregue un mensaje si aprobó o no la materia.

"""
teoria = float(input("Ingrese nota Teoría "))

while teoria > 7.0:
    (f"Nota incorrecta. \n")
    teoria = float(input("Ingrese nota Teoría "))

practica = float(input("Ingrese nota Práctica "))

while practica > 7.0:
    (f"Nota incorrecta. \n")
    practica = float(input("Ingrese nota Práctica "))

def func_promedio (a,b):
    promedio = (a+b)/2
    
    if promedio > 3.9:
        print(f"Usted ha aprobado la asignatura con nota final {promedio}")

    else:
        print("Reprobado!")

promedio_final = func_promedio(teoria, practica)