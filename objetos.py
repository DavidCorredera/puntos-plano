import math

class Punto():
    # Representación de un punto en el plano
    def __init__(self,x=0,y=0): # VALORES 0,0 POR DEFECTO (SI AL CONSTRUCTOR SE LE LLAMA VACÍO)
        self.x=x
        self.y=y

    def mostrar(self): # DEVUELVE X:Y
        return str(self.x)+":"+str(self.y)
    
    def distancia(self, otro):
        # Devuelve la distancia entre ambos puntos
        dx = self.x - otro.x
        dy = self.y - otro.y
        
        return math.sqrt((dx*dx + dy*dy))
