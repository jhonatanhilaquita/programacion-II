"""
Algebra Vectorial
jhonatan brayan quispe hilaquita
21/10/26

"""
import math

class AlgebraVectorial:
    def __init__(self, *args):
        if len(args) == 0:
            self.__x = 0.0
            self.__y = 0.0
        elif len(args) == 2:
            self.__x = float(args[0])
            self.__y = float(args[1])
        elif len(args) == 1 and isinstance(args[0], AlgebraVectorial):
            self.__x = args[0].get_x()
            self.__y = args[0].get_y()
        else:
            raise ValueError("Parámetros de constructor inválidos.")

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def modulo(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def producto_escalar(self, b):
        return (self.__x * b.get_x()) + (self.__y * b.get_y())

    def _perp_a(self, b):
        suma = AlgebraVectorial(self.__x + b.get_x(), self.__y + b.get_y())
        resta = AlgebraVectorial(self.__x - b.get_x(), self.__y - b.get_y())
        return math.isclose(suma.modulo(), resta.modulo(), rel_tol=1e-9)

    def _perp_b(self, b):
        resta1 = AlgebraVectorial(self.__x - b.get_x(), self.__y - b.get_y())
        resta2 = AlgebraVectorial(b.get_x() - self.__x, b.get_y() - self.__y)
        return math.isclose(resta1.modulo(), resta2.modulo(), rel_tol=1e-9)

    def _perp_c(self, b):
        return math.isclose(self.producto_escalar(b), 0.0, abs_tol=1e-9)

    def _perp_d(self, b):
        suma = AlgebraVectorial(self.__x + b.get_x(), self.__y + b.get_y())
        izq = suma.modulo() ** 2
        der = (self.modulo() ** 2) + (b.modulo() ** 2)
        return math.isclose(izq, der, rel_tol=1e-9)

    def perpendicular(self, opcion, b):
        if opcion == 'a': return self._perp_a(b)
        elif opcion == 'b': return self._perp_b(b)
        elif opcion == 'c': return self._perp_c(b)
        elif opcion == 'd': return self._perp_d(b)
        else: raise ValueError("Opción de perpendicularidad inválida (use 'a', 'b', 'c' o 'd').")

    def _paralela_e(self, b):
        r = None
        if b.get_x() != 0:
            r = self.__x / b.get_x()
        elif b.get_y() != 0:
            r = self.__y / b.get_y()
        else:
            return self.__x == 0 and self.__y == 0
        
        return math.isclose(self.__x, r * b.get_x(), rel_tol=1e-9) and math.isclose(self.__y, r * b.get_y(), rel_tol=1e-9)

    def _paralela_f(self, b):
        cruz = (self.__x * b.get_y()) - (self.__y * b.get_x())
        return math.isclose(cruz, 0.0, abs_tol=1e-9)

    def paralela(self, opcion, b):
        if opcion == 'e': return self._paralela_e(b)
        elif opcion == 'f': return self._paralela_f(b)
        else: raise ValueError("Opción de paralelismo inválida (use 'e' o 'f').")

    def proyeccion_de_a_sobre_b(self, b):
        mod_b_cuadrado = b.modulo() ** 2
        if mod_b_cuadrado == 0:
            raise ValueError("No se puede proyectar sobre un vector nulo.")
        escalar = self.producto_escalar(b) / mod_b_cuadrado
        return [escalar * b.get_x(), escalar * b.get_y()]

    def componente_de_a_en_b(self, b):
        mod_b = b.modulo()
        if mod_b == 0:
            raise ValueError("El vector b no puede tener módulo cero.")
        return self.producto_escalar(b) / mod_b



if __name__ == "__main__":
    v1 = AlgebraVectorial(3, 4)
    v2 = AlgebraVectorial(-4, 3)

    print(f"Vector A: ({v1.get_x()}, {v1.get_y()})")
    print(f"Vector B: ({v2.get_x()}, {v2.get_y()})")
    print(f"¿Son perpendiculares mc? {v1.perpendicular('c', v2)}")
    print(f"¿Son perpendiculares md? {v1.perpendicular('d', v2)}")
    
    v3 = AlgebraVectorial(2, 4)
    v4 = AlgebraVectorial(4, 8)
    print(f"¿Son paralelos mf? {v3.paralela('f', v4)}")
    
    proy = v3.proyeccion_de_a_sobre_b(v4)
    print(f"Proyección de v3 sobre v4: ({proy[0]:.2f}, {proy[1]:.2f})")
    
    comp = v3.componente_de_a_en_b(v4)
    print(f"Componente de v3 en v4: {comp:.2f}")