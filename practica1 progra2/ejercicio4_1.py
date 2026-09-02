""""
estadistica modular

jhonatan brayan quispe hilaquita
1.0 01/09/2026

"""
import math

def promedio(datos):
  return sum(datos) / len(datos)

def desviacion(datos):
  prom = promedio(datos)
  suma_diferencias = sum((x - prom) ** 2 for x in datos)
  return math.sqrt(suma_diferencias / (len(datos) - 1))

entrada = input("Ingrese 10 numeros: ").split()
numeros = [float(x) for x in entrada]

print(f"El promedio es {promedio(numeros):.2f}")
print(f"La desviacion estandard es {desviacion(numeros):.5f}")
