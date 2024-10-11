import libro
import editorial

class D_libro:
    def __init__(self,n_paginas,isbn,id_editorial,cantidad_libros,fecha_inicio,cantidad_disponible):
        libro.__init__(isbn)
        editorial.__init__(id_editorial)
        self.n_paginas = n_paginas
        self.cantidad_libros= cantidad_libros
        self.fecha_inicio=fecha_inicio
        self.cantidad_disponible=cantidad_disponible

    
    def actualizar_disponibilidad(self, origen, cantidad):        
        if(self.cantidad_disponible > self.cantidad_disponible + cantidad):
            if(origen == "retirar"):
                if(self.cantidad_disponible > 0):
                    self.cantidad_disponible = self.cantidad_disponible - cantidad
                else:
                    print("No hay libros disponible en este momento.")
            else:
                self.cantidad_disponible = self.cantidad_disponible + cantidad
        else:
            print("error en la cantidad de libros")
    


