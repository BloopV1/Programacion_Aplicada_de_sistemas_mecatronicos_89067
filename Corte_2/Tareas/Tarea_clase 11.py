#Crear un programa basado en POO con las siguientes características:
#Crear una clase "Ciudadano" que incluya los campos privados Nombre, Cédula y Edad.
#Crear los setters y getters correspondientes a los campos, verificando que el número de cedula tenga entre 8 y 10 dígitos y que la edad ingresada sea un número positivo mayor que cero.
#Establecer un método "mostrar" que imprima la información, por ejemplo:
#Nombre: Nicolás - Edad: 28 - CC: 1289384734
#Establecer un método "esMayorDeEdad" que verifique si el ciudadano es o no mayor de edad.
class Ciudadano:
    def __init__(self, nombre, cedula, edad):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getCedula(self):
        return self.__cedula
    
    def setCedula(self, cedula):
        if len(cedula) >= 8 and len(cedula) <= 10:
            self.__cedula = cedula
    
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        if edad > 0:
            self.__edad = edad

    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return True
        else:
            return False
    
def main():
    persona = Ciudadano("Nicolas", "1289384734", 18)
    print("nombre:{} edad:{} CC:{}".format(persona.getNombre(),persona.getEdad(),persona.getCedula()))
    print("es mayor de edad:{}".format(persona.esMayorDeEdad()))
    persona = Ciudadano("Albertito","1123621574",12)
    print("nombre:{} edad:{} CC:{}".format(persona.getNombre(),persona.getEdad(),persona.getCedula()))
    print("es mayor de edad:{}".format(persona.esMayorDeEdad()))


if __name__ =="__main__":
    main()
