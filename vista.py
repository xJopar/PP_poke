from tkinter import *
from tkinter import messagebox
from juego import *

class Vista(Frame):
    #Hub
    def __init__(self, juego, master=None):
        '''Metodo donde instanciamos la vista'''
        Frame.__init__(self,master)
        #configuracion del hub
        self.master = master
        master.title('Pokemon')
        master.geometry('985x770')
        master.resizable(0,0)
        self.place(relwidth=1, relheight=1)
        self.juego = juego
        #iniciamos los widgets
        self.init_widgets()

    def init_widgets(self):
        #Se crea un Frame que contiene la mitad superior del hub, contendra el titulo y el logo
        self.mitad1= Frame(master=self.master,bg="#E3CDCB",height="350")
        self.mitad1.pack(side='top',expand=False, fill='both') 

        self.logo= PhotoImage(file='imagenes/logo.png') #Se instancia el logo, creamos un label, configuramos su fondo y lo colocamos
        self.logoHub=Labels(self.mitad1,image=self.logo)
        self.logoHub.config(bg="#E3CDCB")  
        self.logoHub.place(x=235,y=50)
        #Creacion del titulo, debajo del logo
        self.titulo=Labels(self.mitad1,text='Pokemon x ZODB',font=('Arial',40,"bold"))
        self.titulo.config(background='#E3CDCB',fg='#806D79')
        self.titulo.place(x=1,y=200)

        #Se crea un Frame que contiene la mitad inferior del hub, contendra los botones
        self.mitad2= Frame(master=self.master,bg="#ECE9D2")
        self.mitad2.pack(side='bottom',expand=True,fill='both')
        #Creacion de los botones principales.
        nuevaAventuraBT=Boton(self.mitad2,text='Iniciar Nueva\n Aventura',command =self.nuevaAventuraV)
        nuevaAventuraBT.place(x=100, y=100)
        continuarAventuraBT=Boton(self.mitad2,text='Continua\ntu Aventura',command = self.continuarAventura)
        continuarAventuraBT.place(x=100,y=250)
        personalizarBT=Boton(self.mitad2,text='Personalizar\njuego',command = self.personalizacionSector)
        personalizarBT.place(x=400,y=100)
        listarBT=Boton(self.mitad2,text='Mirar \nlibrerias',command = self.enlistar)
        listarBT.place(x=400,y=250)
        salirBT=Boton_volver(self.mitad2,text='SALIR',command= self.master.destroy)
        salirBT.place(x=700, y=350 )

#Sector de crear nueva aventura.
    def nuevaAventuraV(self):
        #Creacion de nueva ventana
        self.nuevaAventuraV = VentanaSecundaria()
        self.nuevaAventuraV.title("Poner al usuario un nickname")
        #Titulo para la ventana
        self.titulo=Labels(self.nuevaAventuraV,text='Iniciar Nueva Aventura',font=('Arial',40,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=200,y=20)
        #Info para el usuario
        self.info=Labels(self.nuevaAventuraV,text='Esta apunto de iniciar su aventura pokemon pero primero ¿Como es tu apodo?',font=('Arial',15))
        self.info.config(background='#ECE9D2',fg='#806D79')
        self.info.place(x=100,y=200)
        #Texto para indicar al usuario que ingrese su nickname
        self.indicacion=Labels(self.nuevaAventuraV,text='Ingrese su nickname:',font=('Arial',30))
        self.indicacion.config(background='#ECE9D2',fg='#806D79')
        self.indicacion.place(x=1,y=400)
        #Contenedor para ingresar texto
        self.ingresarN= TextBox(self.nuevaAventuraV,font=('Arial',22))
        self.ingresarN.place(x=400,y=410)
        #Boton para aceptar
        aceptarBT= Boton(self.nuevaAventuraV,text='Siguiente',command= self.nuevaAventuraIniV)
        aceptarBT.place(x=400,y=500)
        #Boton para volver
        volverBT= Boton_volver(self.nuevaAventuraV,text='Volver',command= self.nuevaAventuraV.destroy)
        volverBT.place(x=400,y=600)    

    def nuevaAventuraIniV(self):
        #Obtener nickname del usuario
        self.nickname= self.ingresarN.get()
        #Desabilitamos el textBox
        self.ingresarN.config(state=DISABLED)
        print("Esto: {}".format(self.nickname))  
        #Creacion de nueva ventana
        self.inicial_escoger = VentanaSecundaria()
        self.inicial_escoger.title("Elegir inicial")
        #Titulo para la ventana
        self.titulo=Labels(self.inicial_escoger,text='Iniciar Nueva Aventura',font=('Arial',40,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=200,y=20)
        #Info para el usuario
        self.info=Labels(self.inicial_escoger,text='Seleccione su pokemon inicial',font=('Arial',20))
        self.info.config(background='#ECE9D2',fg='#806D79')
        self.info.place(x=100,y=200)
        #Decoracion con img
        self.imagen= PhotoImage(file='imagenes/parte_creacion.png')
        self.imgDecoracion= Labels(self.inicial_escoger,image=self.imagen)
        self.imgDecoracion.config(bg="#E3CDCB")
        self.imgDecoracion.place(x=650,y=200)
   
        #Botones para pokemones iniciales:
        self.inicialFuegoBT= Boton(self.inicial_escoger,text='Chamander',command=self.apodoF)
        self.inicialFuegoBT.place(x=400,y=400)
        self.inicialAguaBT= Boton(self.inicial_escoger,text='Squirtle',command=self.apodoA)
        self.inicialAguaBT.place(x=400,y=500)
        self.inicialPlantaBT= Boton(self.inicial_escoger,text='Bulbasur',command=self.apodoP)
        self.inicialPlantaBT.place(x=400,y=600)
        self.volverBT= Boton_volver(self.inicial_escoger,text='Volver',command= self.inicial_escoger.destroy)
        self.volverBT.place(x=680,y=710)

    def apodoF(self):
        opcion=int(1)
        apodoV= VentanaSecundaria()
        apodoV.title("Apodo para pokemo inicial")
        apodoV.geometry('560x395')
        apodoV.resizable(0,0)
        titulo=Labels(apodoV,text='¿Cual va ser su apodo?',font=('Arial',20,'bold'))
        titulo.config(background='#ECE9D2',fg='#806D79')
        titulo.place(x=200,y=20)
        #Caja de texto para introducir
        self.apodoPokemonTB= TextBox(apodoV,font=('Arial',15))
        self.apodoPokemonTB.place(x=150,y=80)           
        #Boton Aceptar
        aceptarBT= Boton(apodoV,text='Aceptar',command= lambda: [self.transferirNuevoJugador(opcion)])
        aceptarBT.place(x=150,y=200)      
                       
    def apodoA(self):
        opcion=int(2)
        apodoV= VentanaSecundaria()
        apodoV.title("Apodo para pokemo inicial")
        apodoV.geometry('560x395')
        apodoV.resizable(0,0)
        titulo=Labels(apodoV,text='¿Cual va ser su apodo?',font=('Arial',20,'bold'))
        titulo.config(background='#ECE9D2',fg='#806D79')
        titulo.place(x=120,y=20)        
        #Caja de texto para introducir
        self.apodoPokemonTB= TextBox(apodoV,font=('Arial',15))
        self.apodoPokemonTB.place(x=150,y=80)               
        #Boton Aceptar
        aceptarBT= Boton(apodoV,text='Aceptar',command= lambda: [self.transferirNuevoJugador(opcion)])
        aceptarBT.place(x=150,y=200)  

    def apodoP(self):
        opcion=int(3)
        apodoV= VentanaSecundaria()
        apodoV.title("Apodo para pokemo inicial")
        apodoV.geometry('560x395')
        apodoV.resizable(0,0)
        titulo=Labels(apodoV,text='¿Cual va ser su apodo?',font=('Arial',20,'bold'))
        titulo.config(background='#ECE9D2',fg='#806D79')
        titulo.place(x=200,y=20)
        #Caja de texto para introducir
        self.apodoPokemonTB= TextBox(apodoV,font=('Arial',15))
        self.apodoPokemonTB.place(x=150,y=80)      
        #Boton Aceptar
        aceptarBT= Boton(apodoV,text='Aceptar',command= lambda: [self.transferirNuevoJugador(opcion)])
        aceptarBT.place(x=150,y=200)  
    def transferirNuevoJugador(self,opcion):
        self.opcion=opcion
        self.apodoPokemon= self.apodoPokemonTB.get()
        self.player=self.juego.nuevoJugador(self.opcion,self.nickname,self.apodoPokemon) 
        #Prueba
        print("\n{}".format(self.player))
        self.iniciarPartida(self.player)
#Sector "iniciar sesion" para la aventura       
    def continuarAventura(self):
        #Configuracion normal de la ventana
        self.continuarAventuraV=VentanaSecundaria()
        self.continuarAventuraV.title("Iniciar sesion")
        #Titulo
        self.titulo=Labels(self.continuarAventuraV,text='Continua tu aventura',font=('Arial',40,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=200,y=5)

        #Impresion de nombres
        self.scroll = Scrollbar(self.continuarAventuraV, orient=VERTICAL)
        self.scroll.place(x=620, y=65, height=450)
        self.lista_objeto = Text(self.continuarAventuraV, yscrollcommand=self.scroll.set)
        self.lista_objeto.place(x=20, y=65, width=870, height=450)
        self.scroll.config(command=self.lista_objeto.yview)
        self.lista_objeto.config(state=DISABLED)
        #Obtener para imprimir nombres
        self.lista_objeto.config(state=NORMAL)
        self.lista_objeto.delete(1.0,'end')
        self.lista_objeto.insert(INSERT,'{0:^60}'.format('USUARIOS REGISTRADOS\n'))        
        organizador = ('''
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
        \nUSUARIO  \t\tAPODO\t\tESPECIE \t\tTIPO \t\tDAÑO \t\tVIDA \t\tDEBILIDAD\nNICKNAME
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n''')
        self.lista_objeto.insert(INSERT,organizador)          
        lista = self.juego.enlistar_jugadores()
        for pokemons in lista:
            self.lista_objeto.insert(INSERT,pokemons.__str__()+'\n')
        self.lista_objeto.config(state=DISABLED)

        #Texto de indicacion para el usuario
        self.info=Labels(self.continuarAventuraV,text='Ingrese su nickname:',font=('Arial',20))
        self.info.config(background='#ECE9D2',fg='#806D79')
        self.info.place(x=100,y=535)     
        #TextBox para el nombre
        self.ingresarNV= TextBox(self.continuarAventuraV,font=('Arial',22))
        self.ingresarNV.place(x=380,y=535)   
        #Boton volver
        volverBT= Boton_volver(self.continuarAventuraV,text='Volver',command= self.continuarAventuraV.destroy)
        volverBT.place(x=15,y=700)         
        #Boton siguiente para summit
        nombreEnemigosBT= Boton(self.continuarAventuraV,text='Siguiente',command= self.obtenerPlayer)   
        nombreEnemigosBT.place(x=400,y=610) 
    def obtenerPlayer(self):
        #Obtener nickname del usuario
        self.nickname= self.ingresarNV.get()
        self.player=self.juego.obtenerJugador(self.nickname)
        #Prueba
        print("\n{}".format(self.player))
        self.iniciarPartida(self.player)

#Sector para iniciar partida con usuario ya creado.
    def iniciarPartida(self,player):
        self.player=player
        #Prueba 2
        print("Prueba 2:{}".format(player))
        #Destruir la ventana anterior y sus stacks
        self.master.destroy()
        #Crear una nueva ventana de 0
        self.gameV= Ventana()
        self.gameV.title("Pokemon en ZODB")
        #Titulo
        self.titulo=Labels(self.gameV,text='Bienvenide  {}  a  tu\naventura  Pokemon'.format(self.player.nombre),font=('Arial',40,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=5,y=5)
        #Botones
        verPokeBT=Boton(self.gameV,text='Ver tu \nPokemon',command = self.verPoke)
        verPokeBT.place(x=100, y=350)
        batallarBT=Boton(self.gameV,text='Batallar con \nalgun entrenador',command = self.batallar)
        batallarBT.place(x=100,y=500)
        batallarBT.config(width=15,height=3)
        curarPokeBT=Boton(self.gameV,text='Curar\nPokemon',command = self.curarPoke)
        curarPokeBT.place(x=600,y=350)
        cambiarPokeBT=Boton(self.gameV,text='Cambiar\nPokemon',command = self.cambiarPoke)
        cambiarPokeBT.place(x=600,y=500)
        salirBT=Boton_volver(self.gameV,text='SALIR',command=  self.gameV.destroy)
        salirBT.place(x=700, y=700 )        
    #Funcion para mostrar en una ventana el pokemon actual
    def verPoke(self):
        #Crear ventana
        verPokeV= VentanaSecundaria()
        verPokeV.title("Ver Pokemon")
        verPokeV.geometry('560x395')
        #Poner Titulo
        titulo=Labels(verPokeV,text='Tu pokemon: ',font=('Arial',25,'bold'))
        titulo.config(background='#ECE9D2',fg='#806D79')
        titulo.place(x=60,y=40)
        #Poner texto donde se muestra el pokemon al usuario
        txt=self.player.verpoke()
        texto=Labels(verPokeV,text='{}'.format(txt),font=('Arial',15,'italic','bold'))
        texto.config(background='#dbcdc2',fg='#806D79')
        texto.place(x=40,y=180)

        volverBT= Boton_volver(verPokeV,text='Volver',command= verPokeV.destroy)
        volverBT.place(x=200,y=300)      
    #Funcion para cambiar el pokemon del usuario
    def cambiarPoke(self):
        #Configuracion normal de la ventana
        self.cambiarPokeV=VentanaSecundaria()
        self.cambiarPokeV.title("Cambiar Pokemon")
        #Titulo
        self.titulo=Labels(self.cambiarPokeV,text='Pokemons existentes:',font=('Arial',40,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=200,y=5)

        #Impresion de nombres
        self.scroll = Scrollbar(self.cambiarPokeV, orient=VERTICAL)
        self.scroll.place(x=620, y=65, height=450)
        self.lista_objeto = Text(self.cambiarPokeV, yscrollcommand=self.scroll.set)
        self.lista_objeto.place(x=20, y=65, width=870, height=450)
        self.scroll.config(command=self.lista_objeto.yview)
        self.lista_objeto.config(state=DISABLED)
        #Obtener para imprimir nombres
        self.lista_objeto.config(state=NORMAL)
        self.lista_objeto.delete(1.0,'end')
        self.lista_objeto.insert(INSERT,'{0:^60}'.format('POKEMONS'))
        organizador = ('''
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
        \nESPECIE \t\tTIPO \t\tDAÑO \t\tVIDA \t\tDEBILIDAD
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n''')
        self.lista_objeto.insert(INSERT,organizador)        
        #Sacar lista de Pokemones tipo fuego.
        lista = self.juego.enlistar_pokemonsFuego()
        lista2 = self.juego.enlistar_pokemonsAgua()
        lista3 = self.juego.enlistar_pokemonsPlanta()
        for pokemons in lista:
            self.lista_objeto.insert(INSERT,pokemons.__str__()+'\n')
        for pokemons in lista2:
            self.lista_objeto.insert(INSERT,pokemons.__str__()+'\n')
        for pokemons in lista3:
            self.lista_objeto.insert(INSERT,pokemons.__str__()+'\n')
        self.lista_objeto.config(state=DISABLED)

        #Texto de indicacion para el usuario
        self.info=Labels(self.cambiarPokeV,text='Ingrese el pokemon\nque quiere adoptar',font=('Arial',18,'bold'))
        self.info.config(background='#ECE9D2',fg='#806D79')
        self.info.place(x=100,y=535)     
        #TextBox para el nombre
        self.ingresarNPV= TextBox(self.cambiarPokeV,font=('Arial',22))
        self.ingresarNPV.place(x=380,y=535)   
        #Boton volver
        volverBT= Boton_volver(self.cambiarPokeV,text='Volver',command= self.cambiarPokeV.destroy)
        volverBT.place(x=420,y=700)         
        #Boton siguiente para summit
        nombreEnemigosBT= Boton(self.cambiarPokeV,text='Aceptar',command= self.aceptarCambio)   
        nombreEnemigosBT.place(x=400,y=610) 
    def aceptarCambio(self):
        self.nombrePokeNuevo= self.ingresarNPV.get()
        print(self.player,self.nombrePokeNuevo)
        self.juego.cambiarPoke(self.player,self.nombrePokeNuevo)
        #Crear ventana
        aceptarCambioV= VentanaSecundaria()
        aceptarCambioV.title("Haz cambiado al pokemon")
        aceptarCambioV.geometry('560x395')
        #Poner Titulo aclarando que fue un exito la curacion 
        titulo=Labels(aceptarCambioV,text='Tu pokemon nuevo\npokemon es {} '.format(self.player.pokemon.nickname),font=('Arial',25,'bold'))
        titulo.config(background='#dbcdc2',fg='#806D79')
        titulo.place(x=40,y=140)
        volverBT= Boton_volver(aceptarCambioV,text='Volver',command= lambda: [self.cambiarPokeV.destroy(),aceptarCambioV.destroy()])
        volverBT.place(x=230,y=300)         
    #Funcion para poder curar el pokemon, darle 100% de vida
    def curarPoke(self):
        self.juego.curarPoke(self.player) #Utilizamos funcion destinada a curacion.
        #Crear ventana
        curarPokeV= VentanaSecundaria()
        curarPokeV.title("Ver Pokemon")
        curarPokeV.geometry('560x395')
        #Poner Titulo aclarando que fue un exito la curacion 
        titulo=Labels(curarPokeV,text='Tu pokemon {} \n\tse curo al 100%'.format(self.player.pokemon.nickname),font=('Arial',25,'bold'))
        titulo.config(background='#dbcdc2',fg='#806D79')
        titulo.place(x=40,y=140)
        volverBT= Boton_volver(curarPokeV,text='Volver',command= curarPokeV.destroy)
        volverBT.place(x=200,y=300)        
    def batallar(self):
        #Configuracion normal de la ventana
        self.batallarV=VentanaSecundaria()
        self.batallarV.title("Batalla")
        self.batallarV.geometry("1169x978")
        #Titulo
        self.titulo=Labels(self.batallarV,text='Empiezas a caminar por Fernando de la Mora',font=('Arial',40,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=5,y=5)

        #Impresion de nombres
        self.scroll = Scrollbar(self.batallarV, orient=VERTICAL)
        self.scroll.place(x=620, y=100, height=450)
        self.lista_objeto = Text(self.batallarV, yscrollcommand=self.scroll.set)
        self.lista_objeto.place(x=20, y=100, width=740, height=546)
        self.scroll.config(command=self.lista_objeto.yview)
        self.lista_objeto.config(state=DISABLED)
        #Llamar funcion batalla de la clase juego
        self.cadena=self.juego.batallar(self.player)
        #Obtener para imprimir nombres
        self.lista_objeto.config(state=NORMAL)
        self.lista_objeto.delete(1.0,'end')
        self.lista_objeto.insert(INSERT,'{0:^60}'.format(self.cadena))
        #Boton volver
        volverBT= Boton_volver(self.batallarV,text='Volver',command= self.batallarV.destroy)
        volverBT.place(x=400,y=700)         
        #Imagen decorativa
        self.imagen= PhotoImage(file='imagenes/fdoMora.png')
        self.imgDecoracion= Labels(self.batallarV,image=self.imagen)
        self.imgDecoracion.config(bg="#E3CDCB")
        self.imgDecoracion.place(x=800,y=100)

#Sector para Personalizar el juego
    def personalizacionSector(self):
        #Configuracion normal de la ventana
        self.personalizarV=VentanaSecundaria()
        self.personalizarV.title("Perzonalizacion")
        #Titulo
        self.titulo=Labels(self.personalizarV,text='Personaliza tu juego',font=('Arial',40,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=5,y=5)
        #Imagen de decoracion 
        self.imgSeccionPersonalizar= PhotoImage(file='imagenes/personalizar.png')
        self.logoPersonalizar= Labels(self.personalizarV,image=self.imgSeccionPersonalizar)
        self.logoPersonalizar.config(bg="#ECE9D2")
        self.logoPersonalizar.place(x=200,y=200)        
        #Boton Agregar Pokemon
        agregarPokemonBT= Boton(self.personalizarV,text='Agregar un\nPokemon',command= self.agregarPokemonV)
        agregarPokemonBT.place(x=150,y=610) 
        #Boton Agregar Nombre
        agregarNombreEnemigosBT= Boton(self.personalizarV,text='Agregar nombre\npara enemigo',command= self.agregarNombreV)
        agregarNombreEnemigosBT.config(height=3,width=14)
        agregarNombreEnemigosBT.place(x=450,y=610) 
        #Boton volver
        volverBT= Boton_volver(self.personalizarV,text='Volver',command= self.personalizarV.destroy)
        volverBT.place(x=800,y=700) 
    def agregarPokemonV(self):
        self.agregarPokemonVen= VentanaSecundaria()
        self.agregarPokemonVen.title("Agregar Pokemon")
        self.agregarPokemonVen.geometry("560x395")
        #Titulo
        self.titulo=Labels(self.agregarPokemonVen,text='¿Cual es el tipo de Pokemon \nque quieres agregar?',font=('Arial',25,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=50,y=5)
        #Boton para Tipo Fuego
        agregarPokemonFuegoBT= Boton(self.agregarPokemonVen,text='FUEGO',command= self.pokeFuego)
        agregarPokemonFuegoBT.place(x=20,y=200) 
        agregarPokemonFuegoBT.config(font=("Verdana",10,"bold"),
                                    height=2,width=8)    
        #Boton para Tipo Agua
        agregarPokemonAguaBT= Boton(self.agregarPokemonVen,text='AGUA',command= self.pokeAgua)
        agregarPokemonAguaBT.place(x=220,y=200) 
        agregarPokemonAguaBT.config(font=("Verdana",10,"bold"),
                                    height=2,width=8)          
        #Boton para Tipo Planta
        agregarPokemonPlantaBT= Boton(self.agregarPokemonVen,text='PLANTA',command= self.pokePlanta)

        agregarPokemonPlantaBT.place(x=420,y=200) 
        agregarPokemonPlantaBT.config(font=("Verdana",10,"bold"),
                                    height=2,width=8)
    def pokeFuego(self):
        self.agregarPokeFuegoVen= VentanaSecundaria()
        self.agregarPokeFuegoVen.title("Agregar Pokemon")
        self.agregarPokeFuegoVen.geometry("560x395")       
        
        #Titulo para mejor cardinalidad del suario
        self.titulo=Labels(self.agregarPokeFuegoVen,text='Introduce el nombre de la especie \ndel nuevo Pokemon',font=('Arial',25,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=5,y=5)        
        #Texto para explicar al usuario
        self.textoexplicativo=Labels(self.agregarPokeFuegoVen,text='Crearas un pokemon tipo fuego, tiene buen daño pero poca vida.',font=('Arial',10,"bold"))
        self.textoexplicativo.config(background='#ECE9D2',fg='#806D79')
        self.textoexplicativo.place(x=5,y=100)        
        #Caja de Texto para input
        self.agregarpokeFuegoTB= TextBox(self.agregarPokeFuegoVen,font=('Arial',20))
        self.agregarpokeFuegoTB.place(x=150,y=200)           
        #Boton para summit
        aceptarBT= Boton(self.agregarPokeFuegoVen,text='Aceptar',command= self.transferir)
        aceptarBT.config(font=("Verdana",10,"bold"),
                                   height=2,width=8) 
        aceptarBT.place(x=220,y=320)
        self.opcion= int(1)
    def pokeAgua(self):
        self.agregarPokeAguaVen= VentanaSecundaria()
        self.agregarPokeAguaVen.title("Agregar Pokemon")
        self.agregarPokeAguaVen.geometry("560x395")       
        
        #Titulo para mejor cardinalidad del suario
        self.titulo=Labels(self.agregarPokeAguaVen,text='Introduce el nombre de la especie \ndel nuevo Pokemon',font=('Arial',25,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=5,y=5)        
        #Texto para explicar al usuario
        self.textoexplicativo=Labels(self.agregarPokeAguaVen,text='Crearas un pokemon tipo agua, tiene mucha vida pero poco daño.',font=('Arial',10,"bold"))
        self.textoexplicativo.config(background='#ECE9D2',fg='#806D79')
        self.textoexplicativo.place(x=5,y=100)        
        #Caja de Texto para input
        self.agregarpokeAguaTB= TextBox(self.agregarPokeAguaVen,font=('Arial',20))
        self.agregarpokeAguaTB.place(x=150,y=200)           
        #Boton para summit
        aceptarBT= Boton(self.agregarPokeAguaVen,text='Aceptar',command= self.transferir)
        aceptarBT.config(font=("Verdana",10,"bold"),
                                   height=2,width=8) 
        aceptarBT.place(x=220,y=320)
        self.opcion= int(2)
    def pokePlanta(self):
        self.agregarPokePlantaVen= VentanaSecundaria()
        self.agregarPokePlantaVen.title("Agregar Pokemon")
        self.agregarPokePlantaVen.geometry("560x395")       
        
        #Titulo para mejor cardinalidad del suario
        self.titulo=Labels(self.agregarPokePlantaVen,text='Introduce el nombre de la especie \ndel nuevo Pokemon',font=('Arial',25,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=5,y=5)        
        #Texto para explicar al usuario
        self.textoexplicativo=Labels(self.agregarPokePlantaVen,text='Crearas un pokemon tipo planta, tiene vida y daño equilibrados',font=('Arial',10,"bold"))
        self.textoexplicativo.config(background='#ECE9D2',fg='#806D79')
        self.textoexplicativo.place(x=5,y=100)        
        #Caja de Texto para input
        self.agregarpokePlantaTB= TextBox(self.agregarPokePlantaVen,font=('Arial',20))
        self.agregarpokePlantaTB.place(x=150,y=200)           
        #Boton para summit
        aceptarBT= Boton(self.agregarPokePlantaVen,text='Aceptar',command= self.transferir)
        aceptarBT.config(font=("Verdana",10,"bold"),
                                   height=2,width=8) 
        aceptarBT.place(x=220,y=320)
        self.opcion= int(3)
    def transferir(self):
        self.agregarPokemonVen.destroy()
        self.personalizarV.destroy()
        if self.opcion==1:
            print("Entra en fuego")
            self.pokeNuevo= str(self.agregarpokeFuegoTB.get())
            self.juego.controlCreacionPokemon(self.opcion,self.pokeNuevo)       
        elif self.opcion==2:
            print("Entra en agua")
            self.pokeNuevo= str(self.agregarpokeAguaTB.get())
            self.juego.controlCreacionPokemon(self.opcion,self.pokeNuevo)
        elif self.opcion==3:    
            print("Entra en planta")
            self.pokeNuevo= str(self.agregarpokePlantaTB.get())
            self.juego.controlCreacionPokemon(self.opcion,self.pokeNuevo)  
        self.transferirV= VentanaSecundaria()
        self.transferirV.title("Agregar Pokemon")
        self.transferirV.geometry("560x395")
        self.fin=Labels(self.transferirV,text='Pokemon {} creado con exito!'.format(self.pokeNuevo),font=('Arial',18,"bold"))
        self.fin.config(background='#ECE9D2',fg='#806D79')
        self.fin.place(x=80,y=180)           
        genialBT= Boton(self.transferirV,text='Genial',command= self.transferirV.destroy)
        genialBT.config(font=("Verdana",10,"bold"),
                                            height=2,width=8) 
        genialBT.place(x=200,y=250)
    #Agregar nombre random
    def agregarNombreV(self):
        self.agregarNombreVen= VentanaSecundaria()
        self.agregarNombreVen.title("Agregar un Nombre")
        self.agregarNombreVen.geometry("560x395")       
        
        #Titulo para mejor cardinalidad del suario
        self.titulo=Labels(self.agregarNombreVen,text='Crea un nombre nuevo para un \nenemigo',font=('Arial',25,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=5,y=5)  
        #Boton para summit
        aceptarBT= Boton(self.agregarNombreVen,text='Aceptar',command= self.enviarnombre)
        aceptarBT.config(font=("Verdana",10,"bold"),
                                   height=2,width=8) 
        aceptarBT.place(x=220,y=320)
        #Caja de Texto para input
        self.agregarNombreTB= TextBox(self.agregarNombreVen,font=('Arial',20))
        self.agregarNombreTB.place(x=150,y=200)     
    def enviarnombre(self):
        self.nombreNuevo= str(self.agregarNombreTB.get())
        self.juego.crearNombre(self.nombreNuevo)
        self.enviarnombreV= VentanaSecundaria()
        self.enviarnombreV.title("Agregar un Nombre")
        self.enviarnombreV.geometry("560x395")
        self.fin=Labels(self.enviarnombreV,text='¡Nombre creado con exito!',font=('Arial',18,"bold"))
        self.fin.config(background='#ECE9D2',fg='#806D79')
        self.fin.place(x=80,y=180)           
        genialBT= Boton(self.enviarnombreV,text='Genial',command=lambda:[self.agregarNombreVen.destroy(),self.enviarnombreV.destroy()] )
        genialBT.config(font=("Verdana",10,"bold"),
                                            height=2,width=8) 
        genialBT.place(x=200,y=250)   

#Sector las listas. De pokemons y nombres de enemigos randoms.
    def enlistar(self):
        #Configuracion normal de la ventana
        self.enlistarV=VentanaSecundaria()
        self.enlistarV.title("Listas del Juego")
        #Titulo
        self.titulo=Labels(self.enlistarV,text='Mira la libreria:',font=('Arial',40,"bold"))
        self.titulo.config(background='#ECE9D2',fg='#806D79')
        self.titulo.place(x=200,y=5)
        #Imagen para decoracion
        self.imgEnlistar= PhotoImage(file='imagenes/enlistar.png')
        self.logoEnlistar= Labels(self.enlistarV,image=self.imgEnlistar)
        self.logoEnlistar.config(bg="#ECE9D2")
        self.logoEnlistar.place(x=640,y=100)
        #Creacion de barra de dezplazamiento(scrollbar nene) y posicionamiento de la lista donde se imprimiran los datos de la BD
        self.scroll = Scrollbar(self.enlistarV, orient=VERTICAL)
        self.scroll.place(x=620, y=65, height=450)
        self.lista_objeto = Text(self.enlistarV, yscrollcommand=self.scroll.set)
        self.lista_objeto.place(x=20, y=65, width=600, height=450)
        self.scroll.config(command=self.lista_objeto.yview)
        self.lista_objeto.config(state=DISABLED)
        #Boton para imprimir pokemones
        verPokemonsBT= Boton(self.enlistarV,text='Pokemons',command= self.enlistar_nombresPokemons)
        verPokemonsBT.place(x=200,y=580)          
        #Boton para imprimir nombres
        nombreEnemigosBT= Boton(self.enlistarV,text='Nombre\nEnemigos',command= self.enlistar_nombresEnemigos)
        nombreEnemigosBT.place(x=500,y=580) 
        #Boton para volver
        salirBT= Boton_volver(self.enlistarV,text='Salir',command=lambda:[self.enlistarV.destroy()] )
        salirBT.place(x=400,y=700)      
    def enlistar_nombresPokemons(self):
        #Pokemons
        self.lista_objeto.config(state=NORMAL)
        self.lista_objeto.delete(1.0,'end')
        self.lista_objeto.insert(INSERT,'{0:^60}'.format('POKEMONS'))
        organizador = ('''
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
        \nESPECIE \t\tTIPO \t\tDAÑO \t\tVIDA \t\tDEBILIDAD
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n''')
        self.lista_objeto.insert(INSERT,organizador)        
        #Sacar lista de Pokemones tipo fuego.
        lista = self.juego.enlistar_pokemonsFuego()
        lista2 = self.juego.enlistar_pokemonsAgua()
        lista3 = self.juego.enlistar_pokemonsPlanta()
        for pokemons in lista:
            self.lista_objeto.insert(INSERT,pokemons.__str__()+'\n')
        for pokemons in lista2:
            self.lista_objeto.insert(INSERT,pokemons.__str__()+'\n')
        for pokemons in lista3:
            self.lista_objeto.insert(INSERT,pokemons.__str__()+'\n')        
        self.lista_objeto.config(state=DISABLED)
    def enlistar_nombresEnemigos(self):             
        #Nombre enemigos
        self.lista_objeto.config(state=NORMAL)
        self.lista_objeto.delete(1.0,'end')
        self.lista_objeto.insert(INSERT,'{0:^60}'.format('Nombre Enemigos\n'))
        organizador = ('''
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
        \nNombre de los enemigos randoms
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n''')
        self.lista_objeto.insert(INSERT,organizador) 
        lista = self.juego.enlistar_nombres()
        for nombreEnemigo in lista:
            self.lista_objeto.insert(INSERT,nombreEnemigo.__str__()+'\n')
        self.lista_objeto.config(state=DISABLED)


#Clases abstractas para botones, labels, ventanas y textboxes
class Boton_volver(Button):     
    #Clase para abstraer botones, heredando de Button pero estos botones son utilizados para salir/volver 
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.config(fg='black', bg='#D5A3C0', relief='sunken',
                    font=("Arial",20,"bold"),
                    activeforeground="black",
                    activebackground="#F1F1F1",
                    height=1,width=10)
        self.place(width=130)  

class Boton(Button):  
    #Clase para abstraer botones, heredando de Button pero estos botones son utilizados para selecciones
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.config(fg='black', bg='#D9D9D9', relief='raised',
                    font=("Verdana",20,"bold"),
                    activeforeground="#F1F1F1",
                    activebackground="#D5A3C0",
                    height=2,width=12)

class Labels(Label):
    #Clase para abstraer Labels
    def __init__(self, parent=None, **config):
        Label.__init__(self, parent, **config)
        super().configure(fg='black', bg='#ECE9D2')

class Ventana(Tk):
    #Clase para abstraer por medio de Tk, ventas nuevas.
    def __init__(self):
        super().__init__()
        super().geometry('985x770')
        super().config(bg='#ECE9D2')
        super().resizable(0, 0) 

class VentanaSecundaria(Toplevel):
    #Clase para abstraer por medio de herencia TopLevel, ventanas secundarias
    def __init__(self):
        super().__init__()
        super().geometry('985x770')
        super().config(bg='#ECE9D2')
        super().resizable(0, 0)
        super().grab_set() 

class TextBox(Entry):
    #Clase para abstraer las cajas de texto
    def __init__(self, parent=None, **config):
        Entry.__init__(self, parent, **config)