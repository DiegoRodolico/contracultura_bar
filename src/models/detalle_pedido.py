class Detalle_pedido:
    def __init__(self, id_detalle, id_pedido, id_producto, cantidad, precio_unitario, subtotal, estado):
        self.id_detalle = id_detalle
        self.id_pedido = id_pedido
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal
        self.estado = estado
    
    def __str__(self):
        return f"id del detalle del pedido: {self.id_detalle}, id del pedido: {self.id_pedido}, id del producto: {self.id_producto}, cantidad: {self.cantidad}, precio unitario: {self.precio_unitario}, subtotal: {self.subtotal}, estado del pedido: {self.estado}"