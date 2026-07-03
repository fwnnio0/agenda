import web
import sqlite3

render = web.template.render('views', base='layout')

class InsertarContacto:

    def GET(self):
        return render.insertar_contacto()

    def POST(self):
        datos = web.input(
            nombre="",
            primer_apellido="",
            segundo_apellido="",
            email="",
            telefono=""
        )
        try:
            conexion = sqlite3.connect("sql/agenda.sqlite")
            cursor = conexion.cursor()
            query = """
                INSERT INTO contactos 
                (nombre, primer_apellido, segundo_apellido, email, telefono) 
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                datos.nombre,
                datos.primer_apellido,
                datos.segundo_apellido,
                datos.email,
                datos.telefono
            ))
            conexion.commit()
            conexion.close()
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return "Error al guardar el contacto"
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return "Error inesperado"

        raise web.seeother('/lista_contactos')