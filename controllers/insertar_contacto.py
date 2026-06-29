import web
import sqlite3

render = web.template.render('views', base='layout')

class InsertarContacto:
    def conectar(self):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            return conexion
        except Exception as error:
            print(f"ERROR 100: {error.args}")
            return None

    def GET(self):
        return render.insertar_contacto()

    def POST(self):
        datos = web.input()
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            sql = "INSERT INTO contactos (nombre, primer_apellido, segundo_apellido) VALUES (?, ?, ?)"
            cursor.execute(sql, (datos.nombre, datos.primer_apellido, datos.segundo_apellido))
            conexion.commit()
            conexion.close()
            raise web.seeother('/lista_contactos')
        except Exception as error:
            print(f"ERROR 102: {error.args}")
            return render.insertar_contacto()