from material_biblioteca import MaterialBiblioteca

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_paginas = numero_paginas
    
    def informacion(self):
        return f"{super().informacion()}, Numero de Paginas: {self.numero_paginas}"
