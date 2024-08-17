class Libro():
    __Tamaño=""
    Páginas=0
    PrecioVenta=0
    Peso=0
    __PrecioxPágina=0
    __PesoxPagina=0
    Título=""
    Tapa=""
    URL=""
    ISBN=""
    Estado="No Registrado"

    def __init__(self,):
        self.__Tamaño="17x24"
        self.__PrecioxPágina=300
        self.__PesoxPagina=0.8

    def RegistrarLibro(self):
        Estado="Registrado"
        return Estado
    
    def PrecioxPágina(self):
        return self.__PrecioxPágina
    
    def PesoxPagina(self):
        return self.__PesoxPagina
    
    def TamañoLibro(self):
        return self.__Tamaño
    
def DatosLibro(Libro,Nombre,NumPag,TipoTapa,DirURL,
                   NumISBN):
        Libro.Título=Nombre
        Libro.Tapa=TipoTapa
        Libro.Páginas=NumPag
        Libro.URL=DirURL
        Libro.ISBN=NumISBN
        Libro.PrecioVenta= Libro.PrecioxPágina()*NumPag
        Libro.Peso=Libro.Páginas*Libro.PesoxPagina()


    
    
def RecibeDatosLibro(Libro):
        Nombre=input("Titulo del Libro: ")
        NumPag= int(input("Número de Páginas: "))
        TipoTapa=input("Tipo de Tapa (B/D): ")
        DirURL=input("Dirección URL (S/N): ")
        NumISBN=input("Numero ISBN: ")
        print("******************************")
        DatosLibro(Libro,Nombre,NumPag,TipoTapa,DirURL,NumISBN)

def MuestraDatosLibro(Libro):
        print("Título Libro: ", Libro.Título)
        print("Tamaño: ", Libro.TamañoLibro())
        print("Numero de Páginas: ", Libro.Páginas)
        print("Precio Venta: ", Libro.PrecioVenta)
        print("Tipo de Tapa: ", Libro.Tapa)
        print("Peso: ", Libro.Peso)
        print("Precio x Página: ", Libro.PrecioxPágina())
        print("Peso x Página: ",Libro.PesoxPagina())
        print("Dirección URL: ",Libro.URL)
        print("Numero ISBN: ", Libro.ISBN)
        print("Estado: ",Libro.Estado)


Libro1=Libro()
Libro2=Libro()

print("DATOS LIBRO 1")
RecibeDatosLibro(Libro1)

print("DATOS LIBRO 2")
RecibeDatosLibro(Libro2)

MuestraDatosLibro(Libro1)
MuestraDatosLibro(Libro2)
