class MaterialBiblioteca:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    @property
    def año_publicacion(self):
        return self._año_publicacion
    
    @año_publicacion.setter
    def año_publicacion(self, valor):
        from datetime import datetime
        año_actual = datetime.now().year
        if valor > año_actual:
            raise ValueError("El año de publicacion no puede ser en el futuro.")
        self._año_publicacion = valor
    
    def informacion(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Anio de Publicacion: {self.año_publicacion}"
