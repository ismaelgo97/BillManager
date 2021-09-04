class Obra:
    def __init__(self, nombre, cliente):
        self.nombre = nombre
        self.cliente = cliente

    def guardar(self, connection):
        cursor = connection.cursor()
        cursor.execute("insert into contacto values('"+ self.nombre +"', '"+ self.cliente.cif +"')")
        connection.commit()