""" LIBRREÍAS """
import tkinter as tk  # Tk(), Label, Canvas, Photo
import os  # Archivos en la computadora
import numpy

# Función para cargar imágenes


def CargarImg(nombre):
    ruta = os.path.join("imagenes", nombre)
    imagen = tk.PhotoImage(file=ruta)
    return imagen


# Función para cerrar la ventana principal
def Salir():
    ventana_principal.destroy()


def Validar():

    dato_recibido = entrada_binaria.get()

    if len(dato_recibido) == 12:
        Conversiones(dato_recibido)
    else:
        l_informacion.config(text="Error en el largo")


def Conversiones(dato):

    lista.delete('0', 'end')

    para_convertir = Binario_a_Decimal(int(dato))

    octal = numpy.base_repr(para_convertir, 8)
    decimal = numpy.base_repr(para_convertir, 10)
    hexadecimal = numpy.base_repr(para_convertir, 16)

    dato_octal = "El dato  " + dato + " en la base octal es:  " + str(octal)
    dato_decimal = "El dato  " + dato + \
        " en la base decimal es:  " + str(decimal)
    dato_hexadecimal = "El dato  " + dato + \
        " en la base hexadeciaml es:  " + str(hexadecimal)

    lista.insert(0, dato_octal)
    lista.insert(1, dato_decimal)
    lista.insert(2, dato_hexadecimal)


def Binario_a_Decimal(binario):
    decimal, i = 0, 0
    while (binario != 0):
        dec = binario % 10
        decimal = decimal + dec * pow(2, i)
        binario = binario // 10
        i += 1
    return decimal


"""

     CONFIGURACIÓN DE LA VENTANA PRINCIPAL

"""
ventana_principal = tk.Tk()
ventana_principal.title("DISEÑO LÓGICO")
ventana_principal.minsize(500, 450)
ventana_principal.resizable(width=tk.NO, height=tk.NO)

fondo = tk.Canvas(ventana_principal, width=600, height=600, bg='DodgerBlue4')
fondo.place(x=0, y=0)


""" Elementos de la interfaz """

# Label con el título principal
l_titulo = tk.Label(ventana_principal, text="PROYECTO DISEÑO LÓGICO ", font=("Verdana", 14), bg="DodgerBlue4", fg="maroon1")
l_titulo.place(x=130, y=10)

# Label de información
titulo = tk.Label(ventana_principal, text="Ingrese un dato binario de 12 bits", font=("Agency FB", 14), bg="DodgerBlue4", fg="black")
titulo.place(x=10, y=50)

# Entry para ingresar el dato binario
entrada_binaria = tk.StringVar()  # número que se ingresa
ingresar_dato = tk.Entry(ventana_principal, width=15, font=("Agency", 14), bg="black", fg="yellow", textvariable=entrada_binaria)
ingresar_dato.place(x=220, y=50)


def limitar_entrada(entrada_binaria):
    string_binario = entrada_binaria.get()
    if len(string_binario) > 12:
        entrada_binaria.set(string_binario[:12])
    if string_binario[-1:] not in "01":
        entrada_binaria.set(string_binario[:-1])


entrada_binaria.trace("w", lambda *args: limitar_entrada(entrada_binaria))


# Label para información
l_informacion = tk.Label(ventana_principal, text="", font=("Agency FB", 16), bg="DodgerBlue4", fg="black")
l_informacion.place(x=10, y=80)

# ListBox para desplegar la información
lista = tk.Listbox(ventana_principal, bg="yellow", width=50, height=5)
lista.place(x=10, y=120)


# ingresar_edad = Entry(ventana_principal, width=10, font=("Agency", 14), bg="white", fg="blue")
# ingresar_edad.place(x=10, y=50)


# Label con el texto ingresar edad
# l_numero = Label(ventana_principal, text="Ingrese un número: ", font=("Agency FB", 14), bg="black", fg="magenta")
# l_numero.place(x=10, y=150)


# Botón con imagen
# flecha = CargarImg("right-arrow.gif")
boton_validacion = tk.Button(ventana_principal, bg='black', text="Calcular", command=Validar, fg="lime", font=("Agency FB", 14))
# boton_ima1.config(image=flecha)
boton_validacion.place(x=400, y=40)


# Botón simple
boton_ingresar1 = tk.Button(ventana_principal, text="SALIR", command=Salir, bg="DarkRed", fg="black", font=("Verdana", 12))
boton_ingresar1.place(x=410, y=380)


# Fin del código de la ventana principal
ventana_principal.mainloop()
