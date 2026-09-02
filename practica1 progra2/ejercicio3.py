"""
algebra: ecuacion cuadretica

jhonatan brayan quispe hilaquita
1.0 01/09/2026

"""
class EcuacionCuadratica:
    
  def __init__(self, a, b, c):
    self._a = a
    self._b = b
    self._c = c

  def get_discriminante(self):
    return self._b ** 2 - 4 * self._a * self._c

  def get_raiz1(self):
    discriminante = self.get_discriminante()
    return (-self._b + discriminante ** 0.5) / (2 * self._a)

  def get_raiz2(self):
    discriminante = self.get_discriminante()
    return (-self._b - discriminante ** 0.5) / (2 * self._a)

datos = input("Ingrese a, b, c: ").split()
a, b, c = map(float, datos)

ecuacion = EcuacionCuadratica(a, b, c)
discriminante = ecuacion.get_discriminante()

if discriminante > 0:
  r1 = ecuacion.get_raiz1()
  r2 = ecuacion.get_raiz2()
  print(f"La ecuación tiene dos raíces: {r1:.6f} y {r2:.6f}")
elif discriminante == 0:
  r1 = ecuacion.get_raiz1()
  print(f"La ecuación tiene una sola raíz: {r1:.6f}")
else:
  print("La ecuación no tiene raíces reales")