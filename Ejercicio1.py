class perro():
    Nombre=""
    Sexo=""
    Edad=0
    Raza=""
    Temperamento=""
    Peso=0
    Categoría=""
    __Tipo=""
    Estado="No atendido"
    
    def __init__(self,):
        self.__Tipo="Perro"
    
    def Tipo(self):
        return self.__Tipo
    
    def EstadoCliente(self):
        Estado="Atendido"
        return Estado
    
def PasarDatos(perro,NombrePerro,EdadMeses,SexoP,
                   RazaPerro,TempPerro,PesoPerro,CategoríaPerro):
        perro.Nombre=NombrePerro
        perro.Edad=EdadMeses
        perro.Sexo=SexoP
        perro.Raza=RazaPerro
        perro.Temperamento=TempPerro
        perro.Peso=PesoPerro
        perro.Categoría=CategoríaPerro
        


def ObtenerDatos(perro):
        print("************* Ingresar Datos: *******************")
        NombrePerro=input("Nombre de la Mascota: ")
        EdadMeses=int(input("Edad de la Mascota (Años): "))
        Sexop=input("Genero de la Mascota (M/F): ")
        RazaPerro=input("Raza de la Mascota: ")
        TempPerro=input("Temperamento de la Mascota: ")
        PesoPerro=float(input("Ingrese el peso del Perro (kg): "))  
        if PesoPerro>10:
            CategoríaPerro="Perro Grande"
        elif PesoPerro<10:
            CategoríaPerro="Perro Pequeño" 
        PasarDatos(perro,NombrePerro,EdadMeses,Sexop,RazaPerro,TempPerro,PesoPerro,
                   CategoríaPerro)

def MostrarDatos(perro):
    print("********************************")
    print("Animal: ",{perro.Tipo()})
    print("Nombre: ", perro.Nombre)
    print(f"Edad de {perro.Nombre}: {perro.Edad} años")
    print(f"Género de {perro.Nombre}: {perro.Sexo}")
    print(f"Raza: {perro.Raza}")
    print(f"Temperamento de {perro.Nombre}:  {perro.Temperamento}")
    print(f"Peso de {perro.Nombre}: {perro.Peso}kg")
    print(f"Categoría: {perro.Categoría}")
    print(f"Estado cliente: {perro.EstadoCliente()}")
    print("********************************")
    
perro1 = perro()
perro2 = perro()

ObtenerDatos(perro1)
ObtenerDatos(perro2)

MostrarDatos(perro1)
MostrarDatos(perro2)



        
        