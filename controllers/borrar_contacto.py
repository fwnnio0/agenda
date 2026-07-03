import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:

    def buscarContacto(self, id_contacto:int):
        try:
            conexion = sqlite3.connect("sql/agenda.sqlite")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query,(id_contacto,))
            resultado = cursor.fetchone()

            contacto = {
                "id_contacto":resultado[0],
                "nombre":resultado[1],
                "primer_apellido":resultado[2],
                "segundo_apellido":resultado[3],
                "email":resultado[4],
                "telefono":resultado[5]
            }
            conexion.close()
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return []

    def borrarContacto(self, id_contacto:int):
        try:
            conexion = sqlite3.connect("sql/agenda.sqlite")
            cursor = conexion.cursor()
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query,(id_contacto,))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 104: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 105: {error.args}")
            return False

    def GET(self,id_contacto:int):
        print(f"ID_CONTACTO A BORRAR: {id_contacto}")
        contacto = self.buscarContacto(id_contacto)
        return render.borrar_contacto(contacto)

    def POST(self,id_contacto:int):
        exito = self.borrarContacto(id_contacto)
        if exito:
            print("Contacto borrado")
        else:
            print("Ocurrió un error al borrar el contacto")
        raise web.seeother('/lista_contactos')