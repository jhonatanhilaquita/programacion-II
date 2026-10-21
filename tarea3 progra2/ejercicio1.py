"""
MiPunto
jhonatan brayan quispe hilaquita
21/10/26

"""
import math

class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def get_x(self):
        return self.__x
        
    def get_y(self):
        return self.__y

    def distancia(self, *args):
        if len(args) == 1 and isinstance(args[0], MiPunto):
            otro = args[0]
            return math.sqrt((self.__x - otro.get_x()) ** 2 + (self.__y - otro.get_y()) ** 2)
        elif len(args) == 2:
            x_esp, y_esp = args[0], args[1]
            return math.sqrt((self.__x - x_esp) ** 2 + (self.__y - y_esp) ** 2)
        else:
            raise ValueError("Parámetros incorrectos para el método distancia.")


        
if __name__ == "__main__":
    p1 = MiPunto() 
    p2 = MiPunto(10, 30.5)
    
    distancia_resultado = p1.distancia(p2)
    
    print(f"Punto 1: ({p1.get_x()}, {p1.get_y()})")
    print(f"Punto 2: ({p2.get_x()}, {p2.get_y()})")
    print(f"La distancia entre los puntos es: {distancia_resultado:.4f}")