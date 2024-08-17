class dispositivos():
    tipo=""
    __marca=""
    modelo=""
    precio=0
    __multVenta=0
    almacenamiento=0
    ram=0
    tipoPantalla=""
    proposito=""
    año=0
    precioVenta=0
    
    def __init__(self,):
        self.__marca="PHR"
        self.__multVenta=1.7
    
    def marca(self):
        return self.__marca
    
    def multVenta(self):
        return self.__multVenta
    
def asignarDatos(dispositivos,tipoDis,modeloDis,precioDis,almacenamientoDis,ramDis,
                 pantallaDis,propositoDis,añoDis):
    dispositivos.tipo=tipoDis
    dispositivos.modelo=modeloDis
    dispositivos.precio=precioDis
    dispositivos.almacenamiento=almacenamientoDis
    dispositivos.ram=ramDis
    dispositivos.tipoPantalla=pantallaDis
    dispositivos.proposito=propositoDis
    dispositivos.año=añoDis
    dispositivos.precioVenta=precioDis*dispositivos.multVenta()

def obtenerDatos(dispositivos):
    print("********* Ingresar Datos **********")
    tipoDis=input("Tipo de Dispositivo (Laptop, Teléfono, Tablet): ")
    modeloDis=input(f"Modelo de {tipoDis}: ")
    precioDis=float(input(f"Precio: $"))
    almacenamientoDis=int(input("Capacidad de almacenamiento (gb): "))
    ramDis=int(input("Capacidad de RAM (gb): "))
    pantallaDis=input("Tipo de pantalla: ")
    propositoDis=input("Propósito (Ej. Gaming): ")
    añoDis=int(input("Año del Dispositivo: "))
    
    asignarDatos(dispositivos,tipoDis,modeloDis,precioDis,almacenamientoDis,ramDis,
                 pantallaDis,propositoDis,añoDis)
    
def MostrarDatos(dispositivo):
    print("*******************")
    print(f"Tipo: {dispositivo.tipo}")
    print(f"Marca: {dispositivo.marca()}")
    print(f"Modelo: {dispositivo.modelo}")
    print(f"Almacenamiento: {dispositivo.almacenamiento}gb")
    print(f"RAM: {dispositivo.ram}gb")
    print(f"Tipo de Pantalla: {dispositivo.tipoPantalla}")
    print(f"Propósito: {dispositivo.proposito}")
    print(f"Año: {dispositivo.año}")
    print(f"Precio de Venta: ${dispositivo.precioVenta}")

dispositivo1=dispositivos()
obtenerDatos(dispositivo1)
MostrarDatos(dispositivo1)

    
    