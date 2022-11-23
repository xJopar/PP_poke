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

class Juego_Pokemon():
    def controlCreacionPokemon(self,opcion=int,especie= None):
        self.opcion=opcion
        if self.opcion == 1:
            #print("Crearas un pokemon tipo fuego, tiene buen daño pero poca vida, como se llamara el Pokemon(su especie): ")
            self.especie=especie
            n_pokemon=Tipo_Fuego(especie)
            self.crearPokemonFuego(n_pokemon)
        elif self.opcion == 2:
            #print("Crearas un pokemon tipo agua, tiene mucha vida pero poco daño, como se llamara el Pokemon(su especie): ")
            self.especie=especie
            n_pokemon=Tipo_Agua(especie)
            self.crearPokemonAgua(n_pokemon)
        elif self.opcion==3:    
            #print("Crearas un pokemon tipo planta, tiene vida y daño equilibrados, como se llamara el Pokemon(su especie): ")
            self.especie=especie
            n_pokemon=Tipo_Planta(especie)
            self.crearPokemonPlanta(n_pokemon) 

    #Metodo Creacion de Pokemons Fuego y agregado a bd
    def crearPokemonFuego(self,pokemon_nuevo): 
        root = db.get_root() #Hace una conexion con la BD
        if isinstance(pokemon_nuevo, Tipo_Fuego):
            if pokemon_nuevo.especie in root.pokemonsTipoFuego.keys(): #Avisamos al usuario que ya hay una especie con ese nombre
                raise Exception("Esa especie de pokemon ya esta creada")
            else:
                root.pokemonsTipoFuego[pokemon_nuevo.especie] = pokemon_nuevo
                print("Pokemon creado correctamente")
                transaction.commit() #Se confirma la transacion

    #Metodo Creacion de Pokemons Agua y agregado a bd
    def crearPokemonAgua(self,pokemon_nuevo): 
        root = db.get_root() #Hace una conexion con la BD
        if isinstance(pokemon_nuevo, Tipo_Agua):
            if pokemon_nuevo.especie in root.pokemonsTipoAgua.keys(): #Avisamos al usuario que ya hay una especie con ese nombre
                raise Exception("Esa especie de pokemon ya esta creada")
            else:
                root.pokemonsTipoAgua[pokemon_nuevo.especie] = pokemon_nuevo
                print("Pokemon creado correctamente")
                transaction.commit() #Se confirma la transacion

    #Metodo Creacion de Pokemons Planta y agregado a bd
    def crearPokemonPlanta(self,pokemon_nuevo): 
        root = db.get_root() #Hace una conexion con la BD
        if isinstance(pokemon_nuevo, Tipo_Planta):
            if pokemon_nuevo.especie in root.pokemonsTipoPlanta.keys(): #Avisamos al usuario que ya hay una especie con ese nombre
                raise Exception("Esa especie de pokemon ya esta creada")
            else:
                root.pokemonsTipoPlanta[pokemon_nuevo.especie] = pokemon_nuevo
                print("Pokemon creado correctamente")
                transaction.commit() #Se confirma la transacion
    #Metodo para Mostrar los nombres para enemigos Creados
    def enlistar_nombres(self):
        root = db.get_root()
        lista_nombres = root.nombreEnemigo.values()
        return lista_nombres
    #Metodos para mostrar los distintos tipos de pokemon
    def enlistar_pokemonsFuego(self):
        root= db.get_root()
        listaPokemonFuego= root.pokemonsTipoFuego.values()
        return (listaPokemonFuego)
    def enlistar_pokemonsAgua(self):
        root= db.get_root()
        listaPokemonAgua= root.pokemonsTipoAgua.values()
        return (listaPokemonAgua)
    def enlistar_pokemonsPlanta(self):
        root= db.get_root()
        listaPokemonPlanta= root.pokemonsTipoPlanta.values()
        return (listaPokemonPlanta)
    #Metodo Mostrar Jugadores creados
    def enlistar_jugadores(self):
        root=db.get_root()
        listaJugadores= root.jugadores.values()
        return (listaJugadores)
    #Metodo para creacion de nombre y agregado a bd
    def crearNombre(self,nombre_nuevo= str): 
        root = db.get_root() #Hace una conexion con la BD
        if isinstance(nombre_nuevo, str):
            if nombre_nuevo in root.nombreEnemigo.keys(): #Avisamos al usuario que ya hay una especie con ese nombre
                raise Exception("Esa especie de pokemon ya esta creada")
            else:
                root.nombreEnemigo[nombre_nuevo] = nombre_nuevo
                print("Nombre creado correctamente")
                transaction.commit() #Se confirma la transacion
    #Metodo para actualizar los datos del jugador y guardarlo en el bd
    def actualizarJugador(self,jugador):
        root = db.get_root()
        root.jugadores[jugador.nombre] = jugador
        transaction.commit()           
    #Metodo Creacion de Jugador
    def crearJugador(self,jugador_nuevo=Jugador): 
        root = db.get_root() #Hace una conexion con la BD
        if isinstance(jugador_nuevo, Jugador):
            if jugador_nuevo.nombre in root.jugadores.keys(): #Avisamos al usuario que ya hay un jugador con ese nickname
                raise Exception("Ya hay un jugador con ese nombre")
            else:
                root.jugadores[jugador_nuevo.nombre] = jugador_nuevo
                print("Jugador creado")
                transaction.commit() #Se confirma la transacion
    #Metodo para crear pokemon inicial para un nuevo jugador
    def nuevoJugador(self,opcion,nickname,pokeApodo):
        self.nickname=nickname
        self.pokeApodo= pokeApodo
        self.opcion=int(opcion)
        if self.opcion==1:
            inicial1= Tipo_Fuego("Chamander",self.pokeApodo)
            nuevoJugador= Jugador(self.nickname,inicial1)
            self.crearJugador(nuevoJugador)
        elif opcion==2:
            inicial2= Tipo_Agua("Squirtle",pokeApodo)
            nuevoJugador= Jugador(self.nickname,inicial2)
            self.crearJugador(nuevoJugador)
        elif opcion==3:
            inicial3= Tipo_Planta("Bulbasur",pokeApodo)
            nuevoJugador= Jugador(self.nickname,inicial3)
            self.crearJugador(nuevoJugador)
        return(self.obtenerJugador(self.nickname))
    #Metodo para obtener el objeto jugador de la bd
    def obtenerJugador(self,nickname):
        self.nickname=nickname
        root= db.get_root()
        JugadorA= root.jugadores[nickname]
        transaction.commit()
        print("{}\n\n".format(nickname,JugadorA))
        return JugadorA
    #Metodo utilizado por el usuario para curar su pokemon
    def curarPoke(self,player):
        self.player=player
        player.curar_pokemon()
        self.actualizarJugador(player) #Actualizar BD, de que es curo el pokemon
    #Metodo utilizado por el usuario para cambiar su pokemon actual
    def cambiarPoke(self,player,nombreNuevoPokemon=str):
        root= db.get_root()
        self.player=player
        self.nombreNuevoPokemon= nombreNuevoPokemon
        while True:
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
                raise Exception("No se encontro el pokemon")
        self.player.cambiar_poke(nuevoPokemon)
        self.actualizarJugador(player)
    def batallar(self,player):
        root=db.get_root()
        self.player=player
        nombreEnemigo= random.choice(root.nombreEnemigo.values()) 
        #saca un pokemon aleatorio de la libreria
        pokemonAleatorio= random.randint(1,3)
        if pokemonAleatorio==1:
            pokemonEnemigo= random.choice(root.pokemonsTipoFuego.values())
        elif pokemonAleatorio==2:    
            pokemonEnemigo= random.choice(root.pokemonsTipoAgua.values())
        elif pokemonAleatorio==3:
            pokemonEnemigo= random.choice(root.pokemonsTipoPlanta.values())
        #Crear un nuevo objeto enemigo
        enemigoRandom= Enemigo(nombreEnemigo,pokemonEnemigo)
        #Guardar datos del rival
        poke_rival= enemigoRandom.pokemon
        nombrePokeRival= poke_rival.nickname
        nombreRival= enemigoRandom.nombre
        #Crear la cadena principal, con historia
        self.cadena='''\nEmpiezas a caminar por Fernando de la Mora, cuando de repente una persona te llama.\n
        - Hey tú! Soy {} y tengo {} como compañero, tengamos un duelo pokemon\n\n
        Te adelantas a {} y sacas tu pokemon, tu atacas primero!**\n
        Ha empezado un duelo, {} vas a batallar contra {}.\n\n'''.format(nombreRival,nombrePokeRival,nombreRival,self.player.nombre,nombreRival)
        while True:
            self.victoria= self.player.pokemon.atacar(poke_rival)
            if self.victoria:
                poke_rival.vida=poke_rival.vida_max
                self.cadena= self.cadena+"\n{} gano la batalla.\n{} va a llevar a su pokemon a curar.".format(self.player.nombre,nombreRival)
                break    
            self.derrota = poke_rival.atacar(self.player.pokemon)
            if self.derrota:
                self.cadena=self.cadena+"\n{} gano la batalla, tu perdiste. Te vas triste a curar a tu pokemon".format(nombreRival)
                self.player.curar_pokemon()
                #self.cadena= self.cadena + "\n{} gano la batalla, tu perdiste. Te vas triste a curar a tu pokemon".format(randomEnemigo.nombre)
                break
        return (self.cadena)                 

