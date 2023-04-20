class Ciudadano:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Productor(Ciudadano):
    def __init__(self, nombre, edad,carrera,experiencia ):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.experiencia = experiencia

    def hola(self):
        print(f"hola soy el productor{self.nombre},tengo {self.edad} años y soy de la carrera de {self.carrera},tengo {self.experiencia} años de experiencia")

class Piloto(Ciudadano):
    def __init__(self, nombre, edad,deporte,experiencia ):
        super().__init__(nombre, edad)
        self.deporte = deporte
        self.experiencia = experiencia

    def hola(self):
        print(f"hola soy el piloto de carreras{self.nombre},tengo {self.edad} años y soy piloto de {self.deporte},tengo {self.experiencia} años de experiencia")

class ingeniero(Ciudadano):
    def __init__(self, nombre, edad ,especialidad,experiencia):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.experiencia = experiencia
    
    def hola(self):
        print(f"hola soy el Ingniero{self.nombre},tengo {self.edad} años y soy ingeniero especializado {self.especialidad}, y tengo {self.experiencia} años de experiencia")

productor1 = Productor("Juan", 30, "Ingeniería", 5)
productor1.hola()

piloto1 = Piloto("Max", 25, "automovilismo formula 1", 6)
piloto1.hola()

ingeniero1 = ingeniero("Sofia", 23, "Aeronautica", 2)
ingeniero1.hola()