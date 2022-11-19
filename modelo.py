import random
############################################################################################################################################
class Persona:
    def __init__(self, nombre=None,pokemon=None):
        self.nombre=nombre 
        self.pokemon=pokemon
    # Impresion del nombre
    def __str__(self):
        return self.nombre
    #  Operacion para mostrar el pokemon
    def mostrar_pokemons(self):
        print("Pokemons de {} es: {} con {} de vida y {} de ataque.".format(self.nombre,self.pokemon.especie,self.pokemon.vida,self.pokemon.danho)) 
class Enemigo(Persona):
    def __init__(self, nombre=None, pokemon=None):  
        super().__init__(nombre=nombre, pokemon=pokemon)  
class Jugador(Persona):
    def verpoke(self):
        print("Tu pokemon {} es un: {} con daño {} y vida igual a {} ".format(self.pokemon.nickname,self.pokemon.especie,self.pokemon.danho,self.pokemon.vida))
    def batallar(self,randomEnemigo=Enemigo):
        print("\n\nHa empezado un duelo, {} vas a batallar contra {}.\n".format(self, randomEnemigo.nombre))
        poke_rival= randomEnemigo.pokemon
        while True:
                victoria= self.pokemon.atacar(poke_rival)
                if victoria:
                    print("{} gano la batalla.".format(self))
                    break
                derrota = poke_rival.atacar(self.pokemon)
                if derrota:
                    print("{} gano la batalla, tu perdiste".format(randomEnemigo.nombre))
                    break            
    def curar_pokemon(self):
        print("Curando a tu {} al 100%".format(self.pokemon.nickname))
        if not self.pokemon.vida == self.pokemon.vida_max:
            self.pokemon.vida= self.pokemon.vida_max
    def cambiar_poke(self,nuevo_pokemon):
        self.pokemon= nuevo_pokemon
############################################################################################################################################
class Pokemon:
    def __init__(self,especie,nickname=None):
        #Si el nickname retorna falso poner como nickname la especie
        self.especie=especie
        if nickname:
            self.nickname= nickname
        else:
            self.nickname= especie

    def atacar(self,pokerival):
        if   self.especie == pokerival.debilidad:
            pokerival.vida -= int(self.danho * 1.3)
            print("{} hizo {} de daño a {}, es un ataque efectivo.\n".format(self.nickname, int(self.danho * 1.3) ,pokerival.especie))
        else:
            pokerival.vida -= int(self.danho)
            print("{} hizo {} de daño a {}, es un ataque normal.\n".format(self.nickname, int(self.danho) ,pokerival.especie))
        if pokerival.vida <=0:
            print("{} fue derrotado".format(pokerival.especie))
            return True
        else:
            return False  

class Tipo_Fuego(Pokemon):
    def __init__(self, especie,nickname=None):  
        super().__init__(especie,nickname=None)      
    tipo="fuego"
    danho= random.randint(5,8)
    vida=random.randint(5,10)
    debilidad="agua"
    vida_max= vida    
    def atacar(self, pokemon):
        print("{} Usó aliento de fuego en {}!".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)

class Tipo_Agua(Pokemon):
    def __init__(self, especie,nickname=None):  
        super().__init__(especie,nickname=None)  
    tipo="agua"
    danho= random.randint(2,5)
    vida=random.randint(10,20)
    debilidad="planta"
    vida_max= vida
    def atacar(self, pokemon):
        print("{} Usó salpicadura en {}!".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)

class Tipo_Planta(Pokemon):
    def __init__(self, especie,nickname=None):  
        super().__init__(especie,nickname=None)      
    tipo="planta"
    danho= random.randint(3,6)
    vida=random.randint(6,12)
    debilidad="fuego"
    vida_max= vida
    def atacar(self, pokemon):
        print("{} Usó Látigo cepa en {}!".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)

