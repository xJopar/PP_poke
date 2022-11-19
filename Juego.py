from conexion import *
from modelo import *
import BTrees 
import transaction  

db=Conexion()

#Creacion de las hojas del arbol
if not hasattr(db.get_root(),'pokemonsTipoFuego'):  #Para los pokemones tipo fuego
    db.get_root().pokemonsTipoFuego = BTrees.OOBTree.BTree() 
if not hasattr(db.get_root(),'pokemonsTipoAgua'):  #Para los pokemones tipo agua
    db.get_root().pokemonsTipoAgua = BTrees.OOBTree.BTree() 
if not hasattr(db.get_root(),'pokemonsTipoPlanta'):  #Para los pokemones tipo planta
    db.get_root().pokemonsTipoPlanta = BTrees.OOBTree.BTree() 

if not hasattr(db.get_root(),'jugadores'): #Para los players
    db.get_root().jugadores= BTrees.OOBTree.BTree() 

if not hasattr(db.get_root(),'nombreEnemigo'): #Libreria con nombres que ponga el usuario para enemigos aleatorios
    db.get_root().nombreEnemigo = BTrees.OOBTree.BTree() 

#Metodo Mostrar Jugadores creados
def mostrarJugadores():
    root = db.get_root()
    for elem in root.jugadores.values():
        print("\nNickname del Jugador: {}".format(elem.nombre))
        elem.verpoke()


#Metodo Creacion de Jugador
def crearJugador(jugador_nuevo=Jugador): 
    root = db.get_root() #Hace una conexion con la BD
    if isinstance(jugador_nuevo, Jugador):
        if jugador_nuevo.nombre in root.jugadores.keys(): #Avisamos al usuario que ya hay un jugador con ese nickname
            raise Exception("Ya hay un jugador con ese nombre")
        else:
            root.jugadores[jugador_nuevo.nombre] = jugador_nuevo
            transaction.commit() #Se confirma la transacion

#Metodo Actualizar datos del jugador
def actualizarJugador(jugador):
    root = db.get_root()
    root.jugadores[jugador.nombre] = jugador
    transaction.commit()

#Metodo Creacion de Pokemons Fuego
def crearPokemonFuego(pokemon_nuevo): 
    root = db.get_root() #Hace una conexion con la BD
    if isinstance(pokemon_nuevo, Tipo_Fuego):
        if pokemon_nuevo.especie in root.pokemonsTipoFuego.keys(): #Avisamos al usuario que ya hay una especie con ese nombre
            raise Exception("Esa especie de pokemon ya esta creada")
        else:
            root.pokemonsTipoFuego[pokemon_nuevo.especie] = pokemon_nuevo
            print("Pokemon creado correctamente")
            transaction.commit() #Se confirma la transacion

#Metodo Creacion de Pokemons Agua
def crearPokemonAgua(pokemon_nuevo): 
    root = db.get_root() #Hace una conexion con la BD
    if isinstance(pokemon_nuevo, Tipo_Agua):
        if pokemon_nuevo.especie in root.pokemonsTipoAgua.keys(): #Avisamos al usuario que ya hay una especie con ese nombre
            raise Exception("Esa especie de pokemon ya esta creada")
        else:
            root.pokemonsTipoAgua[pokemon_nuevo.especie] = pokemon_nuevo
            print("Pokemon creado correctamente")
            transaction.commit() #Se confirma la transacion

#Metodo Creacion de Pokemons Planta
def crearPokemonPlanta(pokemon_nuevo): 
    root = db.get_root() #Hace una conexion con la BD
    if isinstance(pokemon_nuevo, Tipo_Planta):
        if pokemon_nuevo.especie in root.pokemonsTipoPlanta.keys(): #Avisamos al usuario que ya hay una especie con ese nombre
            raise Exception("Esa especie de pokemon ya esta creada")
        else:
            root.pokemonsTipoPlanta[pokemon_nuevo.especie] = pokemon_nuevo
            print("Pokemon creado correctamente")
            transaction.commit() #Se confirma la transacion

#Mostrar Pokemons creados
def mostrarPokemon():
    root = db.get_root()
    for elem in root.pokemonsTipoAgua.values():
        print("Pokemon {} que es de tipo {} \nEstadisticas: \n\tVida: {} \n\tDaño: {} \n\tDebilidad: {}\n".format(elem.especie,elem.tipo,str(elem.vida),str(elem.danho),elem.debilidad))
    for elem in root.pokemonsTipoFuego.values():
        print("Pokemon {} que es de tipo {} \nEstadisticas: \n\tVida: {} \n\tDaño: {} \n\tDebilidad: {}\n".format(elem.especie,elem.tipo,str(elem.vida),str(elem.danho),elem.debilidad))
    for elem in root.pokemonsTipoPlanta.values():
        print("Pokemon {} que es de tipo {} \nEstadisticas: \n\tVida: {} \n\tDaño: {} \n\tDebilidad: {}\n".format(elem.especie,elem.tipo,str(elem.vida),str(elem.danho),elem.debilidad))


#Creacion de nombres para enemigos
def crearNombre(nombre_nuevo): 
    root = db.get_root() #Hace una conexion con la BD
    if isinstance(nombre_nuevo, str):
        if nombre_nuevo in root.nombreEnemigo.keys(): #Avisamos al usuario que ya hay una especie con ese nombre
            raise Exception("Esa especie de pokemon ya esta creada")
        else:
            root.nombreEnemigo[nombre_nuevo] = nombre_nuevo
            print("Nombre creado correctamente")
            transaction.commit() #Se confirma la transacion

#Mostrar Nombres
def mostrarNombre():
    root = db.get_root()
    for elem in root.nombreEnemigo.values():
        print("Nombre: {}".format(elem))

#Juego
def iniciarJuego(player=Jugador):
    while True:
        print("Bienvenido {} a tu aventura Pokemon.\n¿Que quieres hacer?\n1-Ver tu pokemon\n2-Batallar con algun entrenador\n3-Curar a tu pokemon\n4-Cambiar tu pokemon\n5-Salir\nIntroduce tu numero: ".format(player.nombre))
        condicion=int(input())
        if condicion==1:
            player.verpoke()
        elif condicion==2:
            nombreEnemigo= random.choice(root.nombreEnemigo.values()) 
            #saca un pokemon aleatorio de la libreria
            pokemonAleatorio= random.randint(1,3)
            if pokemonAleatorio==1:
                pokemonEnemigo= random.choice(root.pokemonsTipoFuego.values())
            elif pokemonAleatorio==2:    
                pokemonEnemigo= random.choice(root.pokemonsTipoAgua.values())
            elif pokemonAleatorio==3:
                pokemonEnemigo= random.choice(root.pokemonsTipoPlanta.values())
            enemigoRandom= Enemigo(nombreEnemigo,pokemonEnemigo)
            print("Empiezas a caminar por Fernando de la Mora, cuando de repente una persona te llama.\n\n\t -Hey tú! Soy {} y tengo {} como compañero, tengamos un duelo pokemon\n".format(nombreEnemigo,pokemonEnemigo.nickname))
            print("Te adelantas a {} y sacas tu pokemon, tu atacas primero! ".format(enemigoRandom.nombre))
            player.batallar(enemigoRandom)
        elif condicion==3:
            player.curar_pokemon()
            actualizarJugador(player) #Actualizamos los datos del jugador
        elif condicion==4:
            mostrarPokemon() #Metodo para mostrar la libreria de pokemones disponibles
            while True:
                print("Escriba el nombre de la especie que quiera adoptar: ")
                nombreNuevoPokemon= input()                
                if nombreNuevoPokemon in root.pokemonsTipoAgua.keys(): 
                    nuevoPokemon=root.pokemonsTipoAgua[nombreNuevoPokemon]
                    break
                elif nombreNuevoPokemon in root.pokemonsTipoFuego.keys():
                    nuevoPokemon=root.pokemonsTipoFuego[nombreNuevoPokemon]
                    break
                elif nombreNuevoPokemon in root.pokemonsTipoPlanta.keys():
                    nuevoPokemon=root.pokemonsTipoPlanta[nombreNuevoPokemon]
                    break                
                else:
                    print("Porfavor introduzca una especie correcta.") 
            player.cambiar_poke(nuevoPokemon)
            actualizarJugador(player) #Actualizamos los datos del jugador 
        elif condicion==5:
            print("******************\n*\tLlegas a tu casa y duermes en tu cama.\t*\n******************")
            break


#Menu
while True:
    print("\n\n\n\tA@@@@@^^^_ POKEMON _^^^@@@@@@A\n\n1-Iniciar nueva aventura\n2-Continuar mi aventura\n3-Crear pokemon nuevo\n4-Crear nombre para enemigo\n5-Mostrar pokemones existentes\n6-Mostrar libreria de nombres\n7-Salir")
    condicion=int(input())    
    if condicion == 1:
        root=db.get_root()
        print("Bienvenido a tu aventura POKEMON. Crea tu Personaje: \n")
        print("Ingresa tu apodo (nickname): ") 
        nickname=input()
        print("Eligue tu pokemon inicial: \n1-Chamander\n2-Squirtle\n3-Bulbasur")
        opcion=int(input())
        print("¿Que apodo le pondras?")
        pokeApodo=None
        pokeApodo=input()
        if opcion==1:
            inicial1= Tipo_Fuego("Chamander",pokeApodo)
            nuevoJugador= Jugador(nickname,inicial1)
            crearJugador(nuevoJugador)
        elif opcion==2:
            inicial2= Tipo_Agua("Squirtle",pokeApodo)
            nuevoJugador= Jugador(nickname,inicial2)
            crearJugador(nuevoJugador)
        elif opcion==3:
            inicial3= Tipo_Planta("Bulbasur",pokeApodo)
            nuevoJugador= Jugador(nickname,inicial3)
            crearJugador(nuevoJugador)
            transaction.commit()
            nuevoJugador= root.jugadores[nickname]
        iniciarJuego(nuevoJugador)
         #Verifica si ya hay algun pj creado
    elif condicion == 2:
        root=db.get_root()
        print("\n\nBienvenido a POKEMON: \n")
        while True:
            mostrarJugadores()
            print("\nColoque su Nickname para continuar su partida: ")
            nombreSeleccionado=input()
            if nombreSeleccionado in root.jugadores.keys(): 
                loginJugador= root.jugadores[nombreSeleccionado]
                break
            else:
                print("Porfavor introduzca un nombre correcto.")     
        iniciarJuego(loginJugador)
    elif condicion == 3:
        print("Para crear un pokemon seleccione el tipo que es: 1) Fuego 2) Agua 3) Planta")
        opcion=int(input())
        if opcion == 1:
            print("Crearas un pokemon tipo fuego, tiene buen daño pero poca vida, como se llamara el Pokemon(su especie): ")
            especie=input()
            n_pokemon=Tipo_Fuego(especie)
            crearPokemonFuego(n_pokemon)
        elif opcion == 2:
            print("Crearas un pokemon tipo agua, tiene mucha vida pero poco daño, como se llamara el Pokemon(su especie): ")
            especie=str(input())
            n_pokemon=Tipo_Agua(especie)
            crearPokemonAgua(n_pokemon)
        elif opcion==3:    
            print("Crearas un pokemon tipo planta, tiene vida y daño equilibrados, como se llamara el Pokemon(su especie): ")
            especie=str(input())
            n_pokemon=Tipo_Planta(especie)
            crearPokemonPlanta(n_pokemon)       
        
    elif condicion==4:
        print("Desea agregar un nombre, introduzca el nombre que quiera agregar(no se puede repetir): ")
        nombreNuevo=input()
        crearNombre(nombreNuevo)
    elif condicion ==5:
        print("Los pokemones registrados son\n ")
        mostrarPokemon()
    elif condicion ==6:
        print("La libreria de nombres contiene\n ")
        mostrarNombre()
    elif condicion ==7:
        print("Adios,vuelva pronto")
        break