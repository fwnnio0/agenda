import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/insertar_contacto', 'controllers.insertar_contacto.InsertarContacto',
    '/ver_contacto/(.*)', 'controllers.ver_contacto.VerContacto',
    '/borrar_contacto/(\d+)', 'controllers.borrar_contacto.BorrarContacto',
    '/editar_contacto/(.*)', 'controllers.editar_contacto.EditarContacto'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()