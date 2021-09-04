from tkinter import *
import sqlite3

def mostrar_contactos(list, btn_add, btn_delete, root, datos):
    btn_delete.config(text="Borrar contacto")
    btn_add.config(text="Añadir contacto", state=NORMAL, command= lambda: add_data("contacto", root, datos))
    btn_view.config(state=DISABLED)
    btn_delete.config(state=DISABLED, command= lambda: borrar_data_database("contacto", datos))
    list.delete(0, END)
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()
    cursor.execute("select * from contacto")
    data = cursor.fetchall()
    for d in data:
        list.insert(END, d[0]+": "+d[1])

def mostrar_trabajadores(list, btn_add, btn_delete, root, datos):
    btn_delete.config(text="Borrar trabajador")
    btn_add.config(text="Añadir trabajador", state=NORMAL, command= lambda: add_data("trabajador", root, datos))
    btn_view.config(state=DISABLED)
    btn_delete.config(state=DISABLED, command= lambda: borrar_data_database("trabajador", datos))
    list.delete(0, END)
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()
    cursor.execute("select * from trabajador")
    data = cursor.fetchall()
    for d in data:
        list.insert(END, d[0]+": "+d[1])

def mostrar_maquinas(list, btn_add, btn_delete, root, datos):
    btn_delete.config(text="Borrar maquina")
    btn_add.config(text="Añadir maquina", state=NORMAL, command= lambda: add_data("maquina", root, datos))
    btn_view.config(state=DISABLED)
    btn_delete.config(state=DISABLED, command= lambda: borrar_data_database("maquina", datos))
    list.delete(0, END)
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()
    cursor.execute("select * from maquina")
    data = cursor.fetchall()
    for d in data:
        list.insert(END, d[0]+": "+d[1])

def mostrar_obras(list, btn_add, btn_delete, root, datos):
    btn_delete.config(text="Borrar obra")
    btn_add.config(text="Añadir obra", state=NORMAL, command= lambda: add_data("obra", root, datos))
    btn_view.config(state=DISABLED)
    btn_delete.config(state=DISABLED, command= lambda: borrar_data_database("obra", datos))
    list.delete(0, END)
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()
    cursor.execute("select * from obra")
    data = cursor.fetchall()
    for d in data:
        list.insert(END, d[0]+": "+d[1])

def borrar_data_database(tabla, datos):
    nombre, id = info.split(": ")
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()
    
    if tabla == "contacto":
        cursor.execute("delete from contacto where nombre='"+nombre+"' and cif='"+id+"'")
        conn.commit()
        cursor.execute("select * from contacto")
        data = cursor.fetchall()
        datos.delete(0, END)
        for d in data:
            datos.insert(END, d[0]+": "+d[1])
        btn_view.config(state=DISABLED)
        btn_delete.config(state=DISABLED)
    elif tabla == "maquina":
        cursor.execute("delete from maquina where nombre='"+nombre+"' and matricula='"+id+"'")
        conn.commit()
        cursor.execute("select * from maquina")
        data = cursor.fetchall()
        datos.delete(0, END)
        for d in data:
            datos.insert(END, d[0]+": "+d[1])
        btn_view.config(state=DISABLED)
        btn_delete.config(state=DISABLED)
    elif tabla == "obra":
        cursor.execute("delete from obra where nombre='"+nombre+"' and contacto='"+id+"'")
        conn.commit()
        cursor.execute("select * from obra")
        data = cursor.fetchall()
        datos.delete(0, END)
        for d in data:
            datos.insert(END, d[0]+": "+d[1])
        btn_view.config(state=DISABLED)
        btn_delete.config(state=DISABLED)
    else:
        cursor.execute("delete from trabajador where nombre='"+nombre+"' and dni='"+id+"'")
        conn.commit()
        cursor.execute("select * from trabajador")
        data = cursor.fetchall()
        datos.delete(0, END)
        for d in data:
            datos.insert(END, d[0]+": "+d[1])
        btn_view.config(state=DISABLED)
        btn_delete.config(state=DISABLED)
    
def add_data_database(tabla, window, text1, text2, error, datos):
    if text1.get() != "" and  text1.get() != "":
        try:
            conn = sqlite3.connect("datos.db")
            cursor = conn.cursor()
            cursor.execute("insert into " + tabla + " values('"+ text1.get() +"', '"+ text2.get() +"')")
            conn.commit()
            datos.delete(0, END)
            cursor.execute("select * from "+tabla)
            data = cursor.fetchall()
            for d in data:
                datos.insert(END, d[0]+": "+d[1])
            window.destroy()
        except error:
            error.config(text="Error al añadir los datos a la base de datos.")
    else:
        error.config(text="Falta algún dato.")

def add_data(tabla, master, datos):
    newWindow = Toplevel(master)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Añadir "+tabla)
    # sets the geometry of toplevel
    newWindow.geometry("300x200")
    newWindow.iconbitmap("icono.ico")
    text1 = Entry(newWindow)
    text2 = Entry(newWindow)
    error = Label(newWindow, text="")
    error.grid(column=1, row=3)
    btn_add_data = Button(newWindow, text="Aceptar")
    if tabla == "contacto":
        nombre = Label(newWindow, text="Nombre: ")
        nombre.grid(column=0, row=0)
        cif = Label(newWindow, text="CIF: ")
        cif.grid(column=0, row=1)
        text1.grid(column=1, row=0)
        text2.grid(column=1, row=1)
        btn_add_data.config(command=lambda: add_data_database(tabla, newWindow, text1, text2, error, datos))
    elif tabla == "maquina":
        nombre = Label(newWindow, text="Nombre: ")
        nombre.grid(column=0, row=0)
        matricula = Label(newWindow, text="Matricula: ")
        matricula.grid(column=0, row=1)
        text1.grid(column=1, row=0)
        text2.grid(column=1, row=1)
        btn_add_data.config(command=lambda: add_data_database(tabla, newWindow, text1, text2, error, datos))
    elif tabla == "obra":
        nombre = Label(newWindow, text="Nombre: ")
        nombre.grid(column=0, row=0)
    else:
        nombre = Label(newWindow, text="Nombre: ")
        nombre.grid(column=0, row=0)
        dni = Label(newWindow, text="DNI: ")
        dni.grid(column=0, row=1)
        text1.grid(column=1, row=0)
        text2.grid(column=1, row=1)
        btn_add_data.config(command=lambda: add_data_database(tabla, newWindow, text1, text2, error, datos))
    btn_add_data.grid(column=1, row=2)

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    global info
    info = value
    btn_view.config(state=NORMAL)
    btn_delete.config(state=NORMAL)

def main(): 
    #se crea la ventana
    root = Tk()
    root.title("Emepessur")
    root.iconbitmap("icono.ico")
    root.state('zoomed')

    btn_add = Button(root, text="Añadir", width=40, height=5, state=DISABLED)
    btn_add.place(x=610, y=20)
    global btn_view
    btn_view = Button(root, text="Ver detalles", width=40, height=5, state=DISABLED)
    btn_view.place(x=610, y=150)
    global btn_delete
    btn_delete = Button(root, text="Borrar", width=40, height=5, state=DISABLED)
    btn_delete.place(x=610, y=270)

    datos = Listbox(root, width=50, height=50)
    datos.bind('<<ListboxSelect>>', onselect)
    datos.place(x=300, y=20)

    contactos = Button(root, text="Contactos", width=40, height=5, command= lambda: mostrar_contactos(datos, btn_add, btn_delete, root, datos))
    contactos.grid(column=0, row=0, pady=20)
    trabajadores = Button(root, text="Trabajadores", width=40, height=5, command= lambda: mostrar_trabajadores(datos, btn_add, btn_delete, root, datos))
    trabajadores.grid(column=0, row=1, pady=20)
    maquinas = Button(root, text="Maquinas", width=40, height=5, command= lambda: mostrar_maquinas(datos, btn_add, btn_delete, root, datos))
    maquinas.grid(column=0, row=2, pady=20)
    obras = Button(root, text="Obras", width=40, height=5, command= lambda: mostrar_obras(datos, btn_add, btn_delete, root, datos))
    obras.grid(column=0, row=3, pady=20)

    

    root.mainloop()

if __name__ == '__main__':
    main()