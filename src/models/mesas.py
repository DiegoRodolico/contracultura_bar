class Mesas:
    def __init__(self, id_mesa, numero, capacidad, ubicacion):
        self.id_mesa = id_mesa
        self.numero = numero
        self.capacidad = capacidad
        self.ubicacion = ubicacion
    
    def __str__(self):
        return f"id: {self.id_mesa}, numero: {self.numero}, capacidad: {self.capacidad}, ubicacion: {self.ubicacion}"