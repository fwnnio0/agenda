import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/insertar_contacto', 'controllers.insertar_contacto.InsertarContacto',
    '/ver_contacto/(.*)', 'controllers.ver_contacto.VerContacto'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()