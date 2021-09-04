class Trabajador:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def guardar(self, connection):
        cursor = connection.cursor()
        cursor.execute("insert into trabajador values('"+ self.nombre +"', '"+ self.dni +"')")
        connection.commit()