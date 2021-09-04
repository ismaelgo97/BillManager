import sqlite3


class Contacto:
    def __init__(self, nombre, cif):
        self.nombre = nombre
        self.cif = cif

    def guardar(self, connection):
        cursor = connection.cursor()
        cursor.execute("insert into contacto values('"+ self.nombre +"', '"+ self.cif +"')")
        connection.commit()