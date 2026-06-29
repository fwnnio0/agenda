import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/insertar_contacto', 'controllers.insertar_contacto.InsertarContacto',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()