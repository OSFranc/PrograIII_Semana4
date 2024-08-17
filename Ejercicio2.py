class cuadernos():
    __marca=""
    hojas=0
    tipoHoja=""
    color=""
    pasta=""
    tamaño=""
    precio=0
    precioVenta=0
    __multPrecio=0
    def __init__(self,):
        self.__marca="HOJITAS"
        self.__multPrecio=1.3
    
    def marca(self):
        return self.__marca
    
    def multPrecio(self):
        return self.__multPrecio
    
class lapices():
    __marcaLp=""
    cantidad=0
    tamaño=""
    tipo=""
    material=""
    precio=0
    precioVenta=0
    __multPrecio=0
    
    def __init__(self,):
        self.__marcaLp="RAYITAS"
        self.__multPrecio=1.3
    
    def marcaLapices(self):
        return self.__marcaLp
    
    def multPrecio(self):
        return self.__multPrecio
    
def pasarDatosLapices(lapices,cantidadLp,tamañoLp,tipoLp,materialLp,precioLp):
    lapices.cantidad=cantidadLp
    lapices.tamaño=tamañoLp
    lapices.tipo=tipoLp
    lapices.material=materialLp
    lapices.precio=precioLp
    lapices.precioVenta= lapices.multPrecio()*precioLp
    
def obtenerDatosLapices(lapices):
    print(f"************ Ingresar Datos *************")

    cantidadLp=int(input("Cantidad de Lápices por paquete: "))
    tamañoLp=input("Tamaño de los lápices: ")
    while True:
        tipoLp=input("Tipo de Lapices Colores o Grafitos(C / G):").upper()
        if tipoLp=="C":
            tipoLp="Colores"
            break
        elif tipoLp=="G":
            tipoLp="Grafito"
            break
        else:
            print("Error, respuesta no válida, ingrese C o G")
    materialLp=input("Material (Ej. Madera): ")
    precioLp=float(input("Precio del producto: $"))
    pasarDatosLapices(lapices,cantidadLp,tamañoLp,tipoLp,materialLp,precioLp)
    
def mostrarDatosLapices(lapices):
    print(f"************ *************")
    print("Tipo: Lapices")
    print(f"Marca: {lapices.marcaLapices()}")
    print(f"Cantidad: {lapices.cantidad}")
    print(f"Tamaño: {lapices.tamaño}")
    print(f"Tipo: {lapices.tipo}")
    print(f"Material: {lapices.material}")
    print(f"Precio Venta: {lapices.precioVenta}")
    
    
#----------------------------- Funciones Cuadernos------------------------------------------   
def pasarDatosCuadernos(cuadernos,numHojas,tipoHojasC,colorC,pastaC,tamañoC,precioCompra):
    cuadernos.hojas=numHojas
    cuadernos.tipoHojas=tipoHojasC
    cuadernos.color=colorC
    cuadernos.pasta=pastaC
    cuadernos.tamaño=tamañoC
    cuadernos.precio=precioCompra
    cuadernos.precioVenta= precioCompra*cuadernos.multPrecio()

def obtenerDatosCuadernos(cuadernos):
    print("************ Ingresar Datos *************")

    while True:
        numHojas=int(input("Número de Hojas (50 / 100) "))
        if numHojas==50:
            break
        elif numHojas==100:
            break
        else: 
            print("Error, número de hojas no válido")
    tipoHojasC= input("Tipo de Hoja (Rayas, Cuadricula, Liso): ")
    colorC= input("Color del Cuaderno: ")
    pastaC= input("Tipo de pasta (Blanda/Dura): ")
    tamañoC= input("Tamaño del Cuaderno: ")
    precioCompra= float(input("Precio de Compra: $"))
    pasarDatosCuadernos(cuadernos,numHojas,tipoHojasC,colorC,pastaC,tamañoC,precioCompra)
    
def MostrarDatosCuadernos(cuadernos):
    print(f"************ *************")
    print("Tipo: Cuaderno")
    print(f"Marca: {cuadernos.marca()}")
    print(f"Numero de Hoja: {cuadernos.hojas}")
    print(f"Tipo de Hojas: {cuadernos.tipoHojas}")
    print(f"Color :{cuadernos.color}")
    print(f"Tipo de Pasta: {cuadernos.pasta}")
    print(f"Tamaño: {cuadernos.tamaño}")
    print(f"Precio de Venta: {cuadernos.precioVenta}")


#--------------------Iniciar Programa:
print("************************")
print("Sistema inventario")

while True:
    print("Escoja una Opción")
    opt= input("1. Ingresar Cuadernos / 2. Ingresar Lapices ")

    match opt:
        case "1":
            cuaderno1=cuadernos()
            cuaderno2=cuadernos()
            obtenerDatosCuadernos(cuaderno1)
            obtenerDatosCuadernos(cuaderno2)
            MostrarDatosCuadernos(cuaderno1)
            MostrarDatosCuadernos(cuaderno2)
    
        case "2":
                lapices1=lapices()
                lapices2=lapices()
                obtenerDatosLapices(lapices1)
                obtenerDatosLapices(lapices2)
                mostrarDatosLapices(lapices1)
                mostrarDatosLapices(lapices2)
    
    opt= input("Desea continuar el programa? (S/N)").upper()
    if opt!="S":
        break
            
    
        



