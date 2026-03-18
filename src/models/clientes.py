class Cliente :
    def __init__(self, id_cliente, nombre, telefono, puntos):
        self.id = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.puntos = puntos

    def __str__(self):
        return f"id: {self.id_cliente}, nombre: {self.nombre}, telefono: {self.telefono}, puntos: {self.puntos}"