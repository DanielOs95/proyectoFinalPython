from setup_database import BaseDatos
from clientes import Clientes
from menu import Menu
from pedidos import Pedidos

clientes = Clientes()
menu = Menu()
pedidos = Pedidos() 

#este es el menu principal el cual se muestra primero
def menu_principal():
    print('Menu de opciones')
    print('1. Clientes')
    print('2. Menu')
    print('3. Pedidos')
    print('4. Salir')

#este es el submenu clientes 
def menu_clientes():
    print('Opciones: ')
    print('1. Agregar Cliente')
    print('2. Eliminar Cliente')
    print('3. Actualizar Cliente')
    print('4. Menu Principal')
#este es el submenu de los productos
def menu_productos():
    print('Seleccionar Menú: ')
    print('1. Agregar Producto')
    print('2. Eliminar Producto')
    print('3. Actualizar Producto')
    print('4. Menu Principal')
# este es el submenu de pedidos el cual funciona con los submenus clientes y pedidos
def menu_pedidos():
    print('Pedidos: ')
    print('1. Crear Pedido')
    print('2. Cancelar Pedido')
    print('3. Menu Principal')


#esta funcion se encarga de manejar las opciones que se ingresan en el menu principal
def seleccionar_opcion():
    while True:
        menu_principal()
        opciones = int(input('Ingresa una opcion (1, 2, 3, 4): '))

        if opciones == 1:
            gestionar_clientes()
        elif opciones == 2:
            gestionar_menu()
        elif opciones == 3:
            gestionar_pedidos()
        elif opciones == 4:
            print('Saliendo...')
            break
        else:
            print('ingrese un numero valido')


#esta funcion maneja las opciones que se ingresa en el submenu clientes
def gestionar_clientes():
    while True:
        menu_clientes()
        opcion = int(input('Seleccionar Opcion: '))

        if opcion == 1:
            clave = input('Ingresar Clave del cliente: ')
            nombre = input('Ingresar Nombre del Cliente: ')
            direccion = input('Ingresar Direccion del Cliente: ')
            correo = input('Ingresar Correo del Cliente: ')
            telefono = input('Ingresar telefono del Cliente: ')
            clientes.agregar_cliente(clave, nombre, direccion, correo, telefono)
        
        elif opcion == 2:
            clave = input('Ingrese la clave del cliente a eliminar: ')
            clientes.eliminar_cliente(clave)

        elif opcion == 3:
            clave = input('Ingresar Clave del cliente para actualizar: ')
            nombre = input('Ingresar el nuevo nombre para actualizar: ')
            direccion = input('Ingresar la nueva direccion: ')
            correo = input('Ingresar el nuevo correo: ')
            telefono = input('Ingresar el nuevo telefono: ')
            clientes.actualizar_cliente(clave, nombre or None, direccion or None, correo or None, telefono or None)

        elif opcion == 4:
            break
        else:
            print('Opcion no valida, intentar otra ves')

#esta funcion se encarga de manejar las opciones que se ingresan en el submenu de productos
def gestionar_menu():
    while True:
        menu_productos()
        opcion = int(input('Selecciona una opcion: '))
        if opcion == 1:
            clave = input('Ingrese la clave del producto: ')
            nombre = input('Ingrese el nombre del producto: ')
            precio = float(input('Ingrese el precio del producto: '))
            menu.agregar_producto(clave, nombre, precio)

        elif opcion == 2:
            clave = input('Ingrese la clave del producto para eliminar: ')
            menu.eliminar_producto(clave)

        elif opcion == 3:
             clave = input('Ingrese la clave del producto para actualizar: ')
             nombre = input('Ingrese el nuevo nombre: ')
             precio = input('Ingrese el nuevo precio: ')
             menu.agregar_producto(clave, nombre, precio)
             menu.actualizar_producto(clave, nombre or None, float(precio) if precio else None)

        elif opcion == 4:
            break
        else:
            print('Ocion no valida, intentar de  nuevo')
# esta funcion se encarga de manejar las opciones que se ingresan en el submenu pedidos
def gestionar_pedidos():
    while True:
        menu_pedidos()
        opcion = int(input('Selecciona una opcion: '))

        if opcion == 1:
            cliente = input('Ingresa la clave del cliente: ')
            producto = input('Ingresa la clave del producto: ')
            #precio = float(input('Ingresa el precio del producto: '))
            pedidos.crear_pedido(cliente, producto)
        elif opcion == 2:
            pedido_id = int(input('ingresa el id del producto para cancelar: '))
            pedidos.cancelar_pedido(pedido_id)
        elif opcion == 3:
            break
        else:
            print('opcion no valida, intenta de nuevo')


seleccionar_opcion()
