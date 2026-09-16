"""
INF-121 Programación II
Ejercicio 3

Jhonatan brayan quispe hilaquita
1.0 16/09/2026
"""
import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, o):
        return Vector3D(self.x + o.x, self.y + o.y, self.z + o.z)

    def __mul__(self, r):
        if isinstance(r, (int, float)):
            return Vector3D(self.x * r, self.y * r, self.z * r)
        return NotImplemented

    def __rmul__(self, r):
        return self.__mul__(r)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        m = abs(self)
        if m == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / m, self.y / m, self.z / m)

    def __matmul__(self, o):
        return self.x * o.x + self.y * o.y + self.z * o.z

    def cruz(self, o):
        return Vector3D(
            self.y * o.z - self.z * o.y,
            self.z * o.x - self.x * o.z,
            self.x * o.y - self.y * o.x
        )

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)

    print("a =", a)
    print("b =", b)

    print("Suma (a + b) =", a + b)
    print("Multiplicación por escalar (3 * a) =", 3 * a)
    print("Longitud |a| =", f"{abs(a):.4f}")
    print("Normal de a =", a.normal())
    print("Producto escalar (a @ b) =", a @ b)
    print("Producto vectorial (a x b) =", a.cruz(b))