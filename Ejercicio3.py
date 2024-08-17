class vehiculo():
    origen=""
    __capacidad=0
    __ruedas=0
    marca=""
    modelo=""
    categoria=""
    transmision=""
    edicion=""
    color=""
    tipoFrenos=""
    bolsasDeAire=0
    seguro=0
    precioCompra=0
    precioVenta=0
    __multiplicadorVenta=0
    
    def __init__(self,):
        self.__capacidad=5
        self.__ruedas=4
        self.__multiplicadorVenta=1.4
    
    def capacidad(self):
        return self.__capacidad
        
    def ruedas(self):
        return self.__ruedas
    
    def multiplicadorVenta(self):
        return self.__multiplicadorVenta

def pasarDatos(vehiculo,origenPais,marcaVh,modeloVh,categoriaVh,transmisionVh,edicionVh,colorVh
               ,frenosVh,bolsasAireVh,seguroDelVh,precioDelVh):
    
    vehiculo.marca=marcaVh
    vehiculo.origen=origenPais
    vehiculo.modelo=modeloVh
    vehiculo.categoria=categoriaVh
    vehiculo.transmision=transmisionVh
    vehiculo.edicion=edicionVh
    vehiculo.color=colorVh
    vehiculo.tipoFrenos=frenosVh
    vehiculo.bolsasDeAire=bolsasAireVh
    vehiculo.seguro=seguroDelVh
    vehiculo.precioCompra=precioDelVh
    vehiculo.precioVenta=vehiculo.multiplicadorVenta()*vehiculo.precioCompra
    
def obtenerDatos(vehiculo):
    print("********* Ingresar Datos *************")
    while True:
        origenPais=  input("Origen (L: Local/ I:Importado): ").lower()
        if origenPais=="l":
            origenPais="Local"
            break
        elif origenPais=="i":
            origenPais="Importado"
            break
        else:
            print("Respuesta no válida, ingrese L o I")    
    marcaVh= input("Marca: ")
    modeloVh= input("Modelo: ")
    categoriaVh=input("Categoría del Vehículo (Ej. Sedan): ")
    transmisionVh=input("Transmisión del Vehículo: ")
    edicionVh=input(f"Edición del Modelo {modeloVh}: " )
    colorVh=input("Color: ")
    frenosVh=input("Tipo de frenos: ")
    bolsasAireVh=input("Número de Bolsas de Aire: ")
    while True:
            seguroDelVh=(input("Estado del seguro (1:Activo / 0:Inactivo): "))
            if seguroDelVh=="1":
                seguroDelVh=True
                break
            elif seguroDelVh=="0":
                seguroDelVh=False
                break
            else:
                print("Opción no válida, ingrese 1 o 0")
                
    precioDelVh=float(input("Ingrese el precio de compra: $"))
    
    pasarDatos(vehiculo,origenPais,marcaVh,modeloVh,categoriaVh,transmisionVh,edicionVh,colorVh
               ,frenosVh,bolsasAireVh,seguroDelVh,precioDelVh)

def mostrarDatos(vehiculo):
    print("*********************************************")
    print(f"- Origen: {vehiculo.origen}")
    print(f"- Marca: {vehiculo.marca}")
    print(f"- Modelo: {vehiculo.modelo}")
    print(f"- Categoría: {vehiculo.categoria}")
    print(f"- Capacidad: {vehiculo.capacidad()} pasajeros")
    print(f"- Numero de Ruedas: {vehiculo.ruedas()}")
    print(f"- Transmisión: {vehiculo.transmision}")
    print(f"- Edicion: {vehiculo.edicion}")
    print(f"- Color: {vehiculo.color}")
    print(f"- Tipo de frenos: {vehiculo.tipoFrenos}")
    print(f"- Bolsas de aire: {vehiculo.bolsasDeAire}")
    print(f"- Estado del Seguro: {vehiculo.seguro}")
    print(f"- Precio al Público: ${vehiculo.precioVenta}")
    

carro1=vehiculo()
obtenerDatos(carro1)
mostrarDatos(carro1)
    
    
    
    