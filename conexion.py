import ZODB

class Conexion:
    global __zodb_root
    __zodb_root = None


    def get_root(self): # Esta funcion crea una conexion con la base de datos
        global __zodb_root 
        if not __zodb_root: #Si no existe un archivo root, entonces crea
            db = ZODB.DB('pokemonBD.fs') #Crea la base de datos
            connection = db.open() #Abre la conexion y devuelve un objeto de conexión
            __zodb_root = connection.root 
        return __zodb_root 