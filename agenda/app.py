import web

urls = (
    "/", "Index",
    "/lista_contacto", "ListaContacto",
    "/ver_contacto", "VerContacto",
    "/editar_contacto", "EditarContacto",
    "/insertar_contacto", "InsertarContacto",
    "/borrar_contacto", "BorrarContacto"
)

app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    
class ListaContacto:
    def GET(self):
        return render.lista_contacto()
    
class VerContacto:
    def GET(self):
        return render.ver_contacto()
    
class EditarContacto:
    def GET(self):
        return render.editar_contacto()
    def POST(self):
        return render.editar_contacto()
 
    
class InsertarContacto:
    def GET(self):
        return render.insertar_contacto()
    def POST(self):
        return render.insertar_contacto()
    
class BorrarContacto:
    def GET(self):
        return render.borrar_contacto()
    def POST(self):
        return render.borrar_contacto()
 
if __name__ == "__main__":
    app.run()