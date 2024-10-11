
import autor

class libro(autor):
    def __init__(self,isbn,titulo,id_autor,n_copias):
        self.isbn = isbn
        self.titulo = titulo
        autor.__init__(id_autor)
        self.n_copias= n_copias
        

    def validar_isbn(self):
        if(10 <= len(self.isbn) <= 13 and self.isbn.isdigit()):
            return True
        else:
            return False 
        