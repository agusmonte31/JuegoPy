from principal import *
from configuracion import *
import random
import math
from extras import *

# lee el archivo y carga en la lista lista_producto todas las palabras

def lectura():
     with open("productos.txt") as productos:
        contenido = productos.readlines()
    # Procesar las líneas y formatear la salida
     lista_productos = []
     for linea in contenido:
        # Dividir la línea en sus componentes
        elementos = linea.strip().split(',')
        # Formatear la salida y agregar a la lista
        formato_linea = [elementos[0]] + elementos[1:]
        lista_productos.append(formato_linea)
     return lista_productos

#De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto , el segundo si es economico
#o premium y el tercero el precio.
def buscar_producto(lista_productos):
     producto = random.choice(lista_productos)

    # Elegir entre "economico" o "premium"
     tipo_precio = random.choice(["(economico)", "(premium)"])
     #si lo que salio es economico, entonces a la variable precio le asigno el valor de economico.
     if tipo_precio == "(economico)":
         precio = int(producto[1])
     else:
        precio= int(producto[2])

    # Crea y devolvuelve la lista de 3 elementos
     return [producto[0], tipo_precio, precio]

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):

    #obtenemos el producto desde buscar_producto,
    while True:
        producto = buscar_producto(lista_productos)
        #le asigno el valor que tiene el producto principal a precio
        precio = producto[2]
        if esUnPrecioValido(precio, lista_productos, margen):
            return producto

#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):

    contador_coincidencias = 0
    for producto in lista_productos:
        precio_economico = int(producto[1])
        precio_premium = int(producto[2])

        # Verificar si el precio dado está dentro del margen en al menos una columna
        if abs(precio - precio_economico) <= margen or abs(precio - precio_premium) <= margen:
            contador_coincidencias += 1

            # Si ya hay al menos 2 coincidencias, devolver True
            if contador_coincidencias >= 2:
                return True

    # Si no se encuentran al menos 2 coincidencias, devolver False
    return False

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen):
    precio=int(producto_principal[2])
    precio_elegido=int(producto_candidato[2])
    if abs(precio - precio_elegido) <= margen:
        return 1
    return 0

def devolverProductosRandomValidos(producto,precio, lista_productos, margen):
    listaValidos = []
     # lista de productos de forma aleatoria para que al barrer la lista sea siempre distinta
    random.shuffle(lista_productos)
    #recorro los productos de la lista de productos
    for elemento in lista_productos:
        precioEconomico=int(elemento[1])
        precioPremium=int(elemento[2])
        #si el nombre del elemento de la lista es distinto al nombre de mi producto entonces continúo
        if elemento[0]!=producto[0]:
            #PARA PRECIO ECONOMICO
            if abs(precio - precioEconomico) <= margen:
                 productoValido = [elemento[0],"(economico)",elemento[1]]
                 listaValidos.append(productoValido)
                 if len(listaValidos) == 2:
                    break
        # Verificar si el precio dado está dentro del margen en al menos una columna
            else:
                #Recorro del producto, el PREMIUM
                 if abs(precio - precioPremium) <= margen:
                     productoValido = [elemento[0],"(premium)",elemento[2]]
                     listaValidos.append(productoValido)
                     if len(listaValidos) == 2:
                        break

            # Al tener 2 productos válidos, termina y retorna los válidos en una lista


    return listaValidos

def devolverProductosRandomNOvalidos(precio, lista_productos, margen):
    #devuelve productos que no corresponden con el producto principal
    listaNOValidos = []
     # lista de productos de forma aleatoria para que al barrer la lista sea siempre distinta
    random.shuffle(lista_productos)

    for producto in lista_productos:
        # Elijo aleatoriamente entre "economico" y "premium"
        tipo_precio = random.choice(["(economico)", "(premium)"])

        # Asigno el precio según el tipo elegido

        if tipo_precio == "(economico)":
            precio_elegido = int(producto[1])
        else:
             precio_elegido= int(producto[2])

        # Verificar si el precio dado NO está dentro del margen
        if abs(precio - precio_elegido) > margen:
            # Actualizo el tipo de precio en el producto
            producto[1] = tipo_precio
            listaNOValidos.append(producto)

            # Al tener 3 productos termina y retorna los productos a la lista
            if len(listaNOValidos) == 3:
                break

    return listaNOValidos

#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    # Obtener el precio del producto principal
     precio = producto[2]
    # Obtener productos válidos
     productos_validos = devolverProductosRandomValidos(producto,precio, lista_productos, margen)
    #Obtener productos NO validos
     productos_NOValidos = devolverProductosRandomNOvalidos(precio, lista_productos, margen)
    # Hacer una copia de la lista para poder colocar el producto principal en la primera posición
     productos_seleccionados = productos_validos + productos_NOValidos
     random.shuffle(productos_seleccionados)
    # Insertar el producto principal en la primera posición de la lista
     productos_seleccionados.insert(0, producto)
     return productos_seleccionados
