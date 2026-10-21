"""
algebra vectorial un vector tridimensional
jhonatan brayan quispe hilaquita
21/10/26

"""
import math

class Vector3D:
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.__a1 = float(a1)
        self.__a2 = float(a2)
        self.__a3 = float(a3)

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def __add__(self, otro):
        return Vector3D(
            self.__a1 + otro.get_a1(), 
            self.__a2 + otro.get_a2(), 
            self.__a3 + otro.get_a3()
        )

    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Vector3D(
                escalar * self.__a1, 
                escalar * self.__a2, 
                escalar * self.__a3
            )
        raise ValueError("El multiplicador debe ser un número escalar.")

    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    def longitud(self):
        return math.sqrt(self.__a1**2 + self.__a2**2 + self.__a3**2)

    def normal(self):
        lon = self.longitud()
        if lon == 0:
            raise ValueError("No se puede calcular la normal de un vector nulo.")
        return Vector3D(
            self.__a1 / lon, 
            self.__a2 / lon, 
            self.__a3 / lon
        )

    def __matmul__(self, otro):
        return (self.__a1 * otro.get_a1()) + (self.__a2 * otro.get_a2()) + (self.__a3 * otro.get_a3())

    def producto_vectorial(self, otro):
        r1 = (self.__a2 * otro.get_a3()) - (self.__a3 * otro.get_a2())
        r2 = (self.__a3 * otro.get_a1()) - (self.__a1 * otro.get_a3())
        r3 = (self.__a1 * otro.get_a2()) - (self.__a2 * otro.get_a1())
        return Vector3D(r1, r2, r3)

    def __str__(self):
        return f"({self.__a1}, {self.__a2}, {self.__a3})"



if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)

    print(f"Vector a: {a}")
    print(f"Vector b: {b}")
    
    print(f"Suma: {a + b}")

    print(f"Multiplicación por escalar: {2 * a}")
    
    print(f"Longitud de a: {a.longitud():.4f}")
    
    print(f"Vector normal de a: {a.normal()}")

    print(f"Producto escalar: {a @ b}")
    
    print(f"Producto vectorial: {a.producto_vectorial(b)}")