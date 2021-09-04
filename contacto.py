class Contacto:
    def __init__(self, nombre, cif):
        self.nombre = nombre
        self.cif = cif

    def guardar(self, connection):
        cursor = connection.cursor()