import web
import _sqlite3

render = web.template.render('views', base='layout')

class VerContacto:
    def GET(self, id_contacto):
        conexion = _sqlite3.connect('sql/agenda.sqlite')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM contactos WHERE id_contacto = ?", (id_contacto,))
        contacto = cursor.fetchone()
        conexion.close()

        return render.ver_contacto(contacto)