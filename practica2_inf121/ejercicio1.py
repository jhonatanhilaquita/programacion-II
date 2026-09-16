"""
INF-121 Programación II
Ejercicio 1

Jhonatan brayan quispe hilaquita
1.0 16/09/2026
"""
import math

class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = float(x)
        self.__y = float(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distancia(self, p_o_x, y=None):
        if isinstance(p_o_x, MiPunto):
            x2 = p_o_x.get_x()
            y2 = p_o_x.get_y()
        else:
            x2 = float(p_o_x)
            y2 = float(y)
        return math.sqrt((self.__x - x2)**2 + (self.__y - y2)**2)

if __name__ == "__main__":
    p1 = MiPunto()
    p2 = MiPunto(10, 30.5)

    print(f"Punto 1: ({p1.get_x()}, {p1.get_y()})")
    print(f"Punto 2: ({p2.get_x()}, {p2.get_y()})")
    
    d1 = p1.distancia(p2)
    print(f"Distancia pasando objeto MiPunto: {d1:.4f}")
    
    d2 = p1.distancia(10, 30.5)
    print(f"Distancia pasando coordenadas (x, y): {d2:.4f}")