class Producto :
    def __init__(self, id_producto, nombre, categoria_id, precio, costo, stock, descripcion):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria_id = categoria_id
        self.precio = precio
        self.costo = costo
        self.stock = stock
        self.descripcion = descripcion

    def __str__(self):
        return f"Producto(id: {self.id_producto}, nombre: {self.nombre}, precio: {self.precio}, descripcion: {self.descripcion})"
     