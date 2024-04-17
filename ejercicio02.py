class docente:
    # Constructor
    def __init__(self, codigo, nombres, apellidos, sueldo,AFP):
        self.DNI = codigo
        self.apellidos= apellidos
        self.nombres = nombres
        self.sueldo = sueldo
        self.AFP= AFP
    # función para imprimir los datos
    def imprimir(self):
        print("DNI: ", self.DNI)
        print("Nombres: ", self.nombres)
        print("Apellidos: ", self.apellidos)
        print("Sueldo: ", self.sueldo)
        print("AFP", self.AFP)
    #5ta categotias  de la clase docente
    def categoria(self):
        quita = self.sueldo*0.11
        print("descuento de 5ta categoria: ")
    #ESSALUD
    def  Essalud(self):
        esalud= self.sueldo* 0.2
        print("descuento de ESSALUD")

    #restar= self.sueldo-self.categoria-self.Essalud
   # print ("Total a pagar: $",restar)
       

# bloque principal
# creamos los nuevos objetos
docente1 = docente("754665651","Apaza","Juan",2000,20)
docente2 = docente("545545455","Flores","Smith",3000,30)

# imprimimos los datos y resultados de cada alumno
docente1.imprimir()
docente1.condicion()
docente2.imprimir()
docente2.condicion()
