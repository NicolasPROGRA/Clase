import re
class editorial:
    def __init__(self,id_editorial,nombre_editorial,numero_contacto,correo_editorial):
        self.id_editorial=id_editorial
        self.nombre_editorial= nombre_editorial
        self.numero_contacto= numero_contacto
        self.correo_editorial=correo_editorial


    def validar_correo(self):
        v_correo= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(v_correo,self.correo_editorial)):
            return True
        else:
            return False


