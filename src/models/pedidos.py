class Pedidos:
    def __init__(self, id_pedido, id_mesa, id_cliente, estado, tipo, total, observaciones, fecha_creacion, fecha_cierre):
        self.id_pedido = id_pedido
        self.id_mesa = id_mesa
        self.id_cliente = id_cliente
        self.estado = estado
        self.tipo = tipo
        self.total = total
        self.observaciones = observaciones
        self.fecha_creacion = fecha_creacion
        self.fecha_cierre = fecha_cierre

    def __str__(self):
        return f"id: {self.id_pedido}, id mesa: {self.id_mesa}, id cliente: {self.id_cliente}, estado: {self.estado}, tipo: {self.tipo}, total: {self.total}, observaciones: {self.observaciones}, fecha del pedido: {self.fecha_creacion}, fecha del pago del pedido: {self.fecha_cierre}"