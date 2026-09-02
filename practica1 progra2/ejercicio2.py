"""
algebra

jhonatan brayan quispe hilaquita
1.0 01/09/2026

"""
class EcuacionLineal:

  def __init__(self, a, b, c, d, e, f):
    self._a = a
    self._b = b
    self._c = c
    self._d = d
    self._e = e
    self._f = f

  def tiene_solucion(self):
    return (self._a * self._d - self._b * self._c) != 0

  def get_x(self):
    denominador = self._a * self._d - self._b * self._c
    numerador = self._e * self._d - self._b * self._f
    return numerador / denominador

  def get_y(self):
    denominador = self._a * self._d - self._b * self._c
    numerador = self._a * self._f - self._e * self._c
    return numerador / denominador

datos = input("Ingrese a, b, c, d, e, f: ").split()
a, b, c, d, e, f = map(float, datos)

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tiene_solucion():
  print(f"x = {ecuacion.get_x():.1f}, y = {ecuacion.get_y():.1f}")
else:
  print("La ecuación no tiene solución")