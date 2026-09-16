"""
INF-121 Programación II
Ejercicio 2

Jhonatan brayan quispe hilaquita
1.0 16/09/2026
"""
import math

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def punto(self, o):
        return self.x * o.x + self.y * o.y + self.z * o.z

    def cruz(self, o):
        return Vector(
            self.y * o.z - self.z * o.y,
            self.z * o.x - self.x * o.z,
            self.x * o.y - self.y * o.x
        )

    def sumar(self, o):
        return Vector(self.x + o.x, self.y + o.y, self.z + o.z)

    def restar(self, o):
        return Vector(self.x - o.x, self.y - o.y, self.z - o.z)

    def escalar(self, r):
        return Vector(self.x * r, self.y * r, self.z * r)

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"


class AlgebraVectorial:
    def __init__(self, v1=None, v2=None):
        self.v1 = v1 if v1 else Vector()
        self.v2 = v2 if v2 else Vector()

    def es_perpendicular(self, a, b, criterio=1):
        if criterio == 1: 
            return math.isclose(a.sumar(b).modulo(), a.restar(b).modulo())
        elif criterio == 2:
            return math.isclose(a.restar(b).modulo(), b.restar(a).modulo())
        elif criterio == 3:
            return math.isclose(a.punto(b), 0.0)
        elif criterio == 4:
            return math.isclose(a.sumar(b).modulo()**2, a.modulo()**2 + b.modulo()**2)

    def es_paralela(self, a, b, criterio=1, r=1.0):
        if criterio == 1: 
            rb = b.escalar(r)
            return math.isclose(a.x, rb.x) and math.isclose(a.y, rb.y) and math.isclose(a.z, rb.z)
        elif criterio == 2:
            return math.isclose(a.cruz(b).modulo(), 0.0)

    def proyeccion(self, a, b):
        factor = a.punto(b) / (b.modulo()**2)
        return b.escalar(factor)

    def componente(self, a, b):
        return a.punto(b) / b.modulo()


if __name__ == "__main__":
    a = Vector(1, 0, 0)
    b = Vector(0, 1, 0)

    alg = AlgebraVectorial(a, b)

    print("a:", a)
    print("b:", b)
    print("Perpendicular (Criterio a):", alg.es_perpendicular(a, b, 1))
    print("Perpendicular (Criterio c):", alg.es_perpendicular(a, b, 3))
    
    a_par = Vector(2, 0, 0)
    print("Paralela (a x b = 0):", alg.es_paralela(a, a_par, criterio=2))
    print("Proyección de a sobre b:", alg.proyeccion(a, b))
    print("Componente de a en b:", alg.componente(a, b))