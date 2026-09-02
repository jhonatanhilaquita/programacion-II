"""
Estadistica POO

Jhonatan brayan quispe hilaquita
1.0 24/08/2026

"""
import math

class Estadistica:

  def __init__(self, datos):
    self._datos = datos

  def promedio(self):
    return sum(self._datos) / len(self._datos)

  def desviacion(self):
    prom = self.promedio()
    suma_diferencias = sum((x - prom) ** 2 for x in self._datos)
    return math.sqrt(suma_diferencias / (len(self._datos) - 1))

entrada = input("Ingrese 10 numeros: ").split()
numeros = [float(x) for x in entrada]

est = Estadistica(numeros)

print(f"El promedio es {est.promedio():.2f}")
print(f"La desviacion estandard es {est.desviacion():.5f}")