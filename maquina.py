class Maquina:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

    def guardar(self, connection):
        cursor = connection.cursor()
        cursor.execute("insert into maquina values('"+ self.nombre +"', '"+ self.matricula +"')")
        connection.commit()