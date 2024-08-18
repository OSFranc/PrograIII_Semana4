# Una venta de calzado desea implementar un sistema de inventario que permita ingresar la descripción 
# de distintos modelos de calzado como Marca, Serie, Talla, Peso, Material, Precio 
# el distribuidor siempre será "Caricia Inc." Ya que el negocio trabaja exclusivamente con esta empresa, 
# el precio de venta al público será de la siguiente manera: Si es Size 6 US o menos su precio será multiplicado por 1.3 
# y si es Size 7 US o más será multiplicado por 1.6, el precio es en dólares 

class Calzado:
    __marca = "Caricia Inc."
    serie = ""
    talla = 0
    peso = 0
    material = ""
    precioDistribuidor = 0
    precioVenta = 0

    def __init__(self):
        pass

    def obtenerMarca(self):
        return self.__marca

    def calcularPrecioVenta(self):
        if self.talla <= 6:
            self.precioVenta = self.precioDistribuidor * 1.3
        else:
            self.precioVenta = self.precioDistribuidor * 1.6

def asignarDatosCalzado(calzado, serieCalzado, tallaCalzado, pesoCalzado, materialCalzado, precioDistribuidorCalzado):
    calzado.serie = serieCalzado
    calzado.talla = tallaCalzado
    calzado.peso = pesoCalzado
    calzado.material = materialCalzado
    calzado.precioDistribuidor = precioDistribuidorCalzado
    calzado.calcularPrecioVenta()

def obtenerDatosCalzado(calzado):
    print("********* Ingresar Datos **********")
    serieCalzado = input("Serie del Calzado: ")
    tallaCalzado = int(input("Talla (US): "))
    pesoCalzado = float(input("Peso (g): "))
    materialCalzado = input("Material: ")
    precioDistribuidorCalzado = float(input("Precio del distribuidor: $"))

    asignarDatosCalzado(calzado, serieCalzado, tallaCalzado, pesoCalzado, materialCalzado, precioDistribuidorCalzado)

def mostrarDatosCalzado(calzado):
    print("*******************")
    print(f"Marca: {calzado.obtenerMarca()}")
    print(f"Serie: {calzado.serie}")
    print(f"Talla: {calzado.talla} US")
    print(f"Peso: {calzado.peso} g")
    print(f"Material: {calzado.material}")
    print(f"Precio Distribuidor: ${calzado.precioDistribuidor}")
    print(f"Precio de Venta: ${calzado.precioVenta}")


calzado1 = Calzado()
obtenerDatosCalzado(calzado1)
mostrarDatosCalzado(calzado1)