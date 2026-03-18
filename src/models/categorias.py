class Categorias :
    def __init__(self,id_categoria, nombre, descripcion, icono):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.icono = icono
    
    def __str__(self):
        return f"Categorias (id: {self.id_categoria}, nombre: {self.nombre}, descripcion: {self.descripcion}, icono: {self.icono})"