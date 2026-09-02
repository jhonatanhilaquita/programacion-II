"""
Cronometro

Jhonatan brayan quispe hilaquita
1.0 01/09/2026

"""
import random
import time
class Cronometro:


  def __init__(self):
    self._inicia = time.time()
    self._finaliza = self._inicia

  def get_inicia(self):
    return self._inicia

  def get_finaliza(self):
    return self._finaliza

  def inicia(self):
    self._inicia = time.time()

  def detener(self):
    self._finaliza = time.time()

  def lapso_de_tiempo(self):
    return (self._finaliza - self._inicia) * 1000

numeros = [random.randint(1, 100000) for _ in range(100000)]

cronometro = Cronometro()
cronometro.inicia()

n = len(numeros)
for i in range(n - 1):
  min = i
  for j in range(i + 1, n):
    if numeros[j] < numeros[min]:
      min = j

  numeros[i], numeros[min] = numeros[min], numeros[i]

cronometro.detener()

print(f"Tiempo de ejecucion: {cronometro.lapso_de_tiempo():.1f} ms")