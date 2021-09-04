import sqlite3

def main():
    cnn = sqlite3.connect("datos.db")
    cursor = cnn.cursor()
    cursor.execute("select * from trabajador")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    cnn.close()

if __name__ == "__main__":
    main()