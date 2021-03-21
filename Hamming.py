""" LIBRREÍAS """
import tkinter as tk  # Tk(), Label, Canvas, Photo
import os  # Archivos en la computadora
import matplotlib.pyplot as plt
import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Función para cargar imágenes

global dato_recibido

def CargarImg(nombre):
    ruta = os.path.join("imagenes", nombre)
    imagen = tk.PhotoImage(file=ruta)
    return imagen

#TIPO DE PARIDAD
def Paridad_P():
    bit.config(text = " PAR")

def Paridad_I():
    bit.config(text = " IMPAR")


def Paridad(dato):
    if dato == "1":
        return  "E"
    else:
        return "C"

# Función para cerrar la ventana principal
def Salir():
    ventana_principal.destroy()

def Corregir():
    dato_normal = entrada_binaria.get()
    dato_recibido = entrada_correccion.get()
    Corregir_Hamming(dato_recibido, dato_normal)

def Validar():
    dato_recibido = entrada_binaria.get()

    Calcular_Hamming_1(dato_recibido)

    if set(dato_recibido) in [{'0'}, {'1'}, {'0', '1'}]:
        if len(dato_recibido) == 12:
            Conversiones(dato_recibido)
            generar_NRZI(dato_recibido)
            l_informacion.config(text="")
        else:
            l_informacion.config(text="Error en el largo")
    else:
        l_informacion.config(text="Error en el dato")


def generar_senal_NRZI(dato):
    senal = [-1]
    for bit in dato:
        ultimo_bit = senal[-1]
        senal.append(-ultimo_bit if int(bit) else ultimo_bit)
    return senal


def generar_NRZI(dato):
    figure = plt.Figure(figsize=(6, 2.5), dpi=lista.winfo_width() / 6)
    ax = figure.add_subplot()
    chart_type = FigureCanvasTkAgg(figure, ventana_principal)
    chart_type.get_tk_widget().place(x=lista.winfo_x(), y=lista.winfo_y() + lista.winfo_height() + 10)
    ax.set_title('NRZI')
    ax.set_ylim([-1.2, 2])
    ax.set_xlim([0, 12])
    ax.set_yticks([-1, 0, 1])
    ax.step(list(range(13)), generar_senal_NRZI(dato))
    for i in range(12):
        ax.text(0.5 + i, 1.3, dato[i], fontsize=16, verticalalignment="bottom", horizontalalignment="center")
        ax.plot([i + 1, i + 1], [-1.2, 2], color="lightgrey", linestyle="--")
    ax.set_xticks([])
    return


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


# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
    return bin(num).replace("0b", "")


""" CÓDIGO HAMMING """


# Calculo de la cantidad de bits de redundancia
def calcRedundantBits(m):
    # Use the formula 2 ^ r >= m + r + 1
    # to calculate the no of redundant bits.
    # Iterate over 0 .. m and return the value
    # that satisfies the equation

    for i in range(m):
        if (2 ** i >= m + i + 1):
            return i


# Calculo de los bit de redundancia
def posRedundantBits(data, r):
    # Redundancy bits are placed at the positions
    # which correspond to the power of 2.
    j = 0
    k = 1
    m = len(data)
    res = ''

    # If position is power of 2 then insert '0'
    # Else append the data
    for i in range(1, m + r + 1):
        if (i == 2 ** j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    # The result is reversed since positions are
    # counted backwards. (m + r+1 ... 1)
    return res[::-1]


# Calculo de los bit de paridad
def calcParityBits(arr, r):
    n = len(arr)

    # For finding rth parity bit, iterate over
    # 0 to r - 1
    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            # If position has 1 in ith significant
            # position then Bitwise OR the array value
            # to find parity bit value.
            if (j & (2 ** i) == (2 ** i)):
                val = val ^ int(arr[-1 * j])
                # -1 * j is given since array is reversed

        # String Concatenation
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr


def detectError(arr, nr):
    n = len(arr)
    res = 0

    # Calculate parity bits again
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 ** i) == (2 ** i)):
                val = val ^ int(arr[-1 * j])

                # Create a binary no by appending
        # parity bits together.

        res = res + val * (10 ** i)

        # Convert binary to decimal
    #return res
    return int(str(res), 2)


"""

     CONFIGURACIÓN DE LA VENTANA PRINCIPAL

"""
ventana_principal = tk.Tk()
ventana_principal.title("DISEÑO LÓGICO")
ventana_principal.minsize(1300, 800)
ventana_principal.resizable(width=tk.NO, height=tk.NO)

fondo = tk.Canvas(ventana_principal, width=1300, height=1000, bg='DodgerBlue4')
fondo.place(x=0, y=0)




def Tabla_1(total_rows, total_columns, lst):
    # code for creating table
    for i in range(total_rows):
        for j in range(total_columns):
            e = tk.Entry(ventana_principal, width=5, fg='blue',
                      font=('Arial', 12, 'bold'))
            e.grid(row=i, column=j)
            e.insert('end', lst[i][j])
            e.place(x=471 + (j*42), y=50 + (i*22))




def Tabla_2(total_rows, total_columns, lst):
    # code for creating table
    for i in range(total_rows):
        for j in range(total_columns):
            e = tk.Entry(ventana_principal, width=5, fg='blue',
                      font=('Arial', 12, 'bold'))
            e.grid(row=i, column=j)
            e.insert('end', lst[i][j])
            e.place(x=470 + (j*42), y=330 + (i*22))



""" ESTA PARTE SE ENCARGA DE RECIBIR EL DATO BINARIO Y CODIFICARLO A HAMMING """
def Calcular_Hamming_1(datos):
    m = len(datos)
    r = calcRedundantBits(m)
    # Determine the positions of Redundant Bits
    arr = posRedundantBits(datos, r)
    # Determine the parity bits
    arr = calcParityBits(arr, r)
    arr = arr[::-1]

    # take the data
    lst = [
        [" ", "p1", "p2", "d1", "p3", "d2", "d3", "d4", "p3", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "p5", "d12"],
        [" PS", " ", " ", arr[2], " ", arr[4], arr[5], arr[6], " ", arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16]],
        ["p1", arr[0], " ", arr[2], " ", arr[4], arr[5], arr[6], " ", arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16]],
        ["p2", " ", arr[1], arr[2], " ", arr[4], arr[5], arr[6], "  ",  arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16]],
        ["p3", " ", " ", " ", arr[3], arr[4], arr[5], arr[6], "  ",  arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16]],
        ["p4", " ", " ", " ", " ", " ", " ", " ", " ", arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16]],
        ["p5", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", arr[15],arr[16]],
        ["PC", arr[0], arr[1], arr[2],arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], arr[15], arr[16]]]

    Tabla_1(len(lst), len(lst[0]), lst)


"""" ESTA PARTE SE ENCARGA DE CORREGIR EL DATO DE ENTRADA"""


def Corregir_Hamming(datos, dato1):
    m = len(dato1)
    r = calcRedundantBits(m)
    # Determine the positions of Redundant Bits
    arr2 = posRedundantBits(dato1, r)
    # Determine the parity bits
    arr2 = calcParityBits(arr2, r)

    arr = arr2[::-1]

    arr2 = datos
    correction = detectError(arr2, r)

    print(str(correction))

    print(str((DecimalToBinary(int(correction)))))

    error = str(DecimalToBinary(int(correction)))

    # take the data
    lst = [[" ", "p1", "p2", "d1", "p3", "d2", "d3", "d4", "p3", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "p5", "d12","P", "B"],
        [" PS", " ", " ", arr[2], " ", arr[4], arr[5], arr[6], " ", arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16], "1", ""],
        ["p1", arr[0], " ", arr[2], " ", arr[4], arr[5], arr[6], " ", arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16], Paridad( "0"), "0"],
        ["p2", " ", arr[1], arr[2], " ", arr[4], arr[5], arr[6], "  ",  arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16],  Paridad( error[0]) ,error[0]],
        ["p3", " ", " ", " ", arr[3], arr[4], arr[5], arr[6], "  ",  arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16], Paridad( error[1]) , error[1]],
        ["p4", " ", " ", " ", " ", " ", " ", " ", arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], " ", arr[16], Paridad( error[2]), error[2]],
        ["p5", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", arr[15],arr[16] , Paridad( error[3]) , error[3]]]

    Tabla_2(len(lst), len(lst[0]), lst)

""" Elementos de la interfaz """

# Label con el título principal
l_titulo = tk.Label(ventana_principal, text="PROYECTO DISEÑO LÓGICO ", font=("Verdana", 14), bg="DodgerBlue4",
                    fg="maroon1")
l_titulo.place(x=160, y=10)

# Label de información
titulo = tk.Label(ventana_principal, text="Ingrese un dato binario de 12 bits: ", font=("Agency FB", 14),
                  bg="DodgerBlue4", fg="black")
titulo.place(x=10, y=50)

#Label para correccion
# Label de información
correccion = tk.Label(ventana_principal, text="Modifique uno de los bit de entrada: ", font=("Agency FB", 14),
                  bg="DodgerBlue4", fg="black")
correccion.place(x=500, y=250)

ventana_principal.update()  # para poder obtener el tamaño del label luego

# Entry para ingresar el dato binario
entrada_binaria = tk.StringVar()  # número que se ingresa
ingresar_dato = tk.Entry(ventana_principal, width=15, font=("Agency", 14), bg="black", fg="yellow",
                         textvariable=entrada_binaria)
ingresar_dato.place(x=10 + titulo.winfo_width(), y=50)

#Entry para la correcion de datos
# Entry para ingresar el dato binario
entrada_correccion = tk.StringVar()  # número que se ingresa
entrada_correccion = tk.Entry(ventana_principal, width=15, font=("Agency", 14), bg="black", fg="yellow")
entrada_correccion.place(x=510 + titulo.winfo_width(), y=250)

# Label de Título Tabla 1
titulo = tk.Label(ventana_principal, text="Tabla No.1 Cálculo de los bit de paridad en el código Hamming",
                  font=("Agency FB", 14), bg="DodgerBlue4", fg="black")
titulo.place(x=500, y=10)

tabla2 = tk.Label(ventana_principal, text="Tabla No.2 Comprobación de los bit de paridad (con el primer bit de la derecha)",
                  font=("Agency FB", 14), bg="DodgerBlue4", fg="black")
tabla2.place(x=500, y=300)


bit = tk.Label(ventana_principal, text= " ", font=("Agency FB", 14),
                  bg="DodgerBlue4", fg="black")
bit.place(x=1150, y=250)




def limitar_entrada(entrada_binaria):
    string_binario = entrada_binaria.get()
    if len(string_binario) > 12:
        entrada_binaria.set(string_binario[:12])
    if string_binario[-1] not in "01":
        entrada_binaria.set(string_binario[:-1])


entrada_binaria.trace("w", lambda *args: limitar_entrada(entrada_binaria))

# ListBox para desplegar la información
lista = tk.Listbox(ventana_principal, bg="yellow", width=50, height=5)
lista.place(x=100, y=150)
ventana_principal.update()


#Botones para la música
#Ejemplo de Radiobutton, otro de las características dentro de Tkinter
radiobutton1 = tk.Radiobutton(ventana_principal, text="Paridad Par", command= Paridad_P, bg = "olive drab")
radiobutton1.place(x = 1020, y = 250)

radiobutton2 = tk.Radiobutton(ventana_principal, text="Paridad Impar", command= Paridad_I, bg = "olive drab")
radiobutton2.place(x = 1020, y = 280)


# Botón calcular
boton_calcular = tk.Button(ventana_principal, bg='black', text="Calcular", command=Validar, fg="lime",
                           font=("Agency FB", 14))
boton_calcular.place(x=250, y=100)
ventana_principal.update()  # para poder obtener el tamaño del botón

# Label para información
l_informacion = tk.Label(ventana_principal, text="", font=("Agency FB", 16), bg="DodgerBlue4", fg="red")
l_informacion.place(x=boton_calcular.winfo_x() + boton_calcular.winfo_width() + 10, y=105)

# Botón salir
boton_salir = tk.Button(ventana_principal, text="SALIR", command=Salir, bg="DarkRed", fg="black", font=("Verdana", 12))
boton_salir.place(x=200, y=450)

#Error
# Botón salir
boton_error= tk.Button(ventana_principal, text="CALCULAR", command=Corregir, bg="DarkRed", fg="black", font=("Verdana", 12))
boton_error.place(x=900, y=250)

# Fin del código de la ventana principal
ventana_principal.mainloop()
