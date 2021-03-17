""" LIBRREÍAS """
from tkinter import *  # Tk(), Label, Canvas, Photo
import os  # Archivos en la computadora
import numpy

# Función para cargar imágenes

def CargarImg(nombre):
    ruta = os.path.join("imagenes", nombre)
    imagen = PhotoImage(file=ruta)
    return imagen


# Función para cerrar la ventana principal
def Salir():
    ventana_principal.destroy()


def Validaciones():

    dato_recibido = str(ingresar_dato.get())

    if verficar_dato(dato_recibido) == True:
        if len(dato_recibido) == 12:
            Conversiones(dato_recibido)
        else:
            l_informacion.config(text = "Error en el largo")
    else:
        l_informacion.config(text="Error en el dato")

def verficar_dato(dato):
    for bit in dato:
        if bit == "1" or bit == "0":
            dato  = dato[1:]
        else:
            return False
    return True


def Conversiones(dato):

    lista.delete('0', 'end')

    para_convertir = Binario_a_Decimal(int(dato))

    octal = numpy.base_repr(para_convertir, 8)
    decimal = numpy.base_repr(para_convertir, 10)
    hexadecimal = numpy.base_repr(para_convertir, 16)

    dato_octal = "El dato  " + dato + " en la base octal es:  " + str(octal)
    dato_decimal = "El dato  " + dato + " en la base decimal es:  " + str(decimal)
    dato_hexadecimal = "El dato  " + dato + " en la base hexadeciaml es:  " + str(hexadecimal)

    lista.insert(0, dato_octal)
    lista.insert(1, dato_decimal)
    lista.insert(2, dato_hexadecimal)


def Binario_a_Decimal(binario):
    decimal, i, n = 0, 0, 0
    while (binario != 0):
        dec = binario % 10
        decimal = decimal + dec * pow(2, i)
        binario = binario // 10
        i += 1
    return decimal



"""

     CONFIGURACIÓN DE LA VENTANA PRINCIPAL

"""
ventana_principal = Tk()
ventana_principal.title("DISEÑO LÓGICO")
ventana_principal.minsize(500, 450)
ventana_principal.resizable(width=NO, height=NO)

fondo = Canvas(ventana_principal, width=600, height=600, bg='DodgerBlue4')
fondo.place(x=0, y=0)


""" Elementos de la interfaz """

# Label con el título principal
l_titulo = Label(ventana_principal, text="PROYECTO DISEÑO LÓGICO ", font=("Verdana", 14), bg="DodgerBlue4", fg="maroon1")
l_titulo.place(x=130, y=10)

# Label de información
titulo = Label(ventana_principal, text="Ingrese un dato binario de 12 bits", font=("Agency FB", 14), bg="DodgerBlue4", fg="black")
titulo.place(x=10, y=50)

# Entry para ingresar el dato binario
ingresar_dato= Entry(ventana_principal, width=15, font=("Agency", 14), bg="black", fg="yellow")
ingresar_dato.place(x=220, y=50)

# Label para información
l_informacion = Label(ventana_principal, text="", font=("Agency FB", 16), bg="DodgerBlue4", fg="black")
l_informacion.place(x=10, y=80)

# ListBox para desplegar la información
lista = Listbox(ventana_principal, bg="yellow", width = 50, height= 5)
lista.place(x=10, y=120)


#ingresar_edad = Entry(ventana_principal, width=10, font=("Agency", 14), bg="white", fg="blue")
#ingresar_edad.place(x=10, y=50)



# Label con el texto ingresar edad
#l_numero = Label(ventana_principal, text="Ingrese un número: ", font=("Agency FB", 14), bg="black", fg="magenta")
#l_numero.place(x=10, y=150)




# Botón con imagen
#flecha = CargarImg("right-arrow.gif")
boton_validacion = Button(ventana_principal, bg='black', text="Calcular", command=Validaciones, fg="lime", font=("Agency FB", 14))
#boton_ima1.config(image=flecha)
boton_validacion.place(x=400, y=40)


# Botón simple
boton_ingresar1 = Button(ventana_principal, text="SALIR", command=Salir, bg="DarkRed", fg="black", font=("Verdana", 12))
boton_ingresar1.place(x=410, y=380)


# Fin del código de la ventana principal
ventana_principal.mainloop()
