
import tipo_usuario 
import re

class usuario(tipo_usuario):
    def  __init__(self,nombre,id_usuario,id_tipo_usuario,correo,celular,habilitado):
        self.nombre=nombre
        self.id_usuario=id_usuario
        self.correo=correo
        self.celular=celular
        self.habilitado= habilitado
        self.id_tipo_usuario=id_tipo_usuario
        tipo_usuario.__init__(tipo_usuario)
    

    def validar_correo(self):
        pat_correo= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if (re.match(pat_correo,self.correo)):
            return True 
        else:
            return False
        
        
        
        