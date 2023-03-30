class pokemon:
    def __init__(self):
        self.nombre = None
        self.tipo = None
        self.tipo_secundario  = None
        self.Generacion = None
        self.entrenador = None
        self.dialogo = None
        self.evolucion = None
        self.sum = 2
        self.numero_de_pokedex = None


    def hablar(self):
        return self.dialogo
    
    def siguiente(self):
        if n > :
            self.evolucion
        self.evolucion
      

def main():
    tipo_fuego = pokemon ()
    tipo_fuego.nombre = "Charmande"
    tipo_fuego.tipo = "Fuego"
    tipo_fuego.tipo_secundario  = "no tiene"
    tipo_fuego.Generacion = 1
    tipo_fuego.entrenador = "Santiago Blanco"
    tipo_fuego.dialogo = "Charmander"
    tipo_fuego.evolucion = "Charmeleon"
    tipo_fuego.numero_de_pokedex = "N°004"

    tipo_planta = pokemon ()
    tipo_planta.nombre = "bullbasur"
    tipo_planta.tipo = "planta"
    tipo_planta.tipo_secundario  = "veneno"
    tipo_planta.Generacion = 1
    tipo_planta.entrenador = "Santiago Blanco"
    tipo_planta.dialogo = "bullbasur"
    tipo_planta.evolucion = "Ivysaur"
    tipo_planta.numero_de_pokedex = "N°001"

    tipo_agua = pokemon ()
    tipo_agua.nombre = "squirtle"
    tipo_agua.tipo = "agua"
    tipo_agua.tipo_secundario  = "Tierra"
    tipo_agua.Generacion = 1
    tipo_agua.entrenador = "Santiago Blanco"
    tipo_agua.dialogo= "Squirrrtleeeee"
    tipo_agua.evolucion = "Wartotlte"
    tipo_agua.numero_de_pokedex = "N°007"


    print(f"El Pokemon del entrenador dice:{tipo_fuego.hablar()}")
    print(f"la informacion de la pokedex del pokemon es {tipo_fuego.nombre , tipo_fuego.tipo , tipo_fuego.tipo_secundario , tipo_fuego.Generacion , tipo_fuego.entrenador , tipo_fuego.dialogo , tipo_fuego.evolucion , tipo_fuego.numero_de_pokedex }")
    
    print(f"El Pokemon del entrenador dice:{tipo_agua.hablar()}")
    print(f"la informacion de la pokedex del pokemon es {tipo_agua.nombre , tipo_agua.tipo , tipo_agua.tipo_secundario , tipo_agua.Generacion , tipo_agua.entrenador , tipo_agua.dialogo , tipo_agua.evolucion , tipo_agua.numero_de_pokedex }")
    
    print(f"El Pokemon del entrenador dice:{tipo_planta.hablar()}")
    print(f"la informacion de la pokedex del pokemon es {tipo_planta.nombre , tipo_planta.tipo , tipo_planta.tipo_secundario , tipo_planta.Generacion , tipo_agua.entrenador , tipo_planta.dialogo , tipo_planta.evolucion , tipo_planta.numero_de_pokedex }")
    
if __name__== "__main__":
    main()    