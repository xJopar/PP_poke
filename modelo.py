import random

#################################Persona#################################
class Persona:
    def __init__(self, nombre=None,pokemon=None):
        self.nombre=nombre 
        self.pokemon=pokemon
    # Impresion del nombre
    def __str__(self):
        return self.nombre
class Enemigo(Persona):
    def __init__(self, nombre=None, pokemon=None):  
        super().__init__(nombre=nombre, pokemon=pokemon)
    def __str__(self):
        return '[*] {}'.format(self.nombre) 

class Jugador(Persona):
    def __str__(self):
        return '{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(self.nombre,self.pokemon.nickname,self.pokemon.especie,self.pokemon.tipo,self.pokemon.danho,self.pokemon.vida,self.pokemon.debilidad)     
    def verpoke(self):
        return 'Tu pokemon apodado {} es un {}\n con daño {} y vida igual a {}'.format(self.pokemon.nickname,self.pokemon.especie,self.pokemon.danho,self.pokemon.vida)                  
    def curar_pokemon(self):
        print("Curando a tu {} al 100%".format(self.pokemon.nickname))
        if not self.pokemon.vida == self.pokemon.vida_max:
            self.pokemon.vida= self.pokemon.vida_max
    def cambiar_poke(self,nuevo_pokemon):
        self.pokemon= nuevo_pokemon

#################################POKEMONS#################################

class Pokemon:
    def __init__(self,especie,nickname=None):
        #Si el nickname retorna falso poner como nickname la especie
        self.especie=especie
    def __str__(self):
        return '{}\t\t{}\t\t{}\t\t{}\t\t{} '.format(self.especie,self.tipo,self.danho,self.vida,self.debilidad)     
    def atacar(self,pokerival):
        if   self.tipo == pokerival.debilidad:
            pokerival.vida -= int(self.danho + 1)
            print("{} hizo {} de daño a {}, es un ataque efectivo. \n".format(self.nickname, int(self.danho + 1) ,str(pokerival.especie)))
        else:
            pokerival.vida -= int(self.danho)
            print("{} hizo {} de daño a {}, es un ataque normal.\n".format(self.nickname, int(self.danho) ,str(pokerival.especie)))

        if pokerival.vida <=0:
            print("{} fue derrotado".format(pokerival.especie))
            return True
        else:
            return False  

class Tipo_Fuego(Pokemon):
    def __init__(self, especie,nickname=None):
        if nickname:
            self.nickname= nickname
        else:
            self.nickname= especie         
        super().__init__(especie,nickname=None)      
    tipo= "fuego"
    danho= random.randint(5,8)
    vida=random.randint(5,10)
    debilidad= "agua"
    vida_max= vida    
    def atacar(self, pokemon):
        print("{} Usó aliento de fuego en {}!".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)

class Tipo_Agua(Pokemon):
    def __init__(self, especie,nickname=None): 
        if nickname:
            self.nickname= nickname
        else:
            self.nickname= especie   
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
        if nickname:
            self.nickname= nickname
        else:
            self.nickname= especie 
        super().__init__(especie,nickname=None) 
    tipo="planta"
    danho= random.randint(3,6)
    vida=random.randint(6,12)
    debilidad="fuego"
    vida_max= vida
    def atacar(self, pokemon):
        print("{} Usó Látigo cepa en {}!".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)