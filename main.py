from contacto import Contacto
import sqlite3

def main():
    conn = sqlite3.connect("datos.db")
    contact = Contacto("Rublond", "abcd1234")
    contact.guardar(conn)

if __name__ == "__main__":
    main()