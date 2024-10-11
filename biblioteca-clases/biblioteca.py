import libro
class biblioteca(libro): #OBJETO 
    def __init__(self,nombre,direccion,telefono):  # ENCAPSULAMIENTO 
        self.nombre =nombre
        self.direccion = direccion
        self.telefono = telefono
        
    def buscar_libro(self): #POLIMORFISMO
        pass 
    def prestar_libro(self):
        pass 
    def devolver_libro(self):
        pass 
