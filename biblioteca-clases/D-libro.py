import libro
import editorial

class D_libro:
    def __init__(self,categoria,n_paginas,isbn,id_editorial):
        libro.__init__(isbn)
        editorial.__init__(id_editorial)
        self.categoria = categoria,
        self.n_paginas = n_paginas
         
    


