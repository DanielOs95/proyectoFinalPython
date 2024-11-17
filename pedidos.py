#import sqlite3
from setup_database import BaseDatos

#se crea la clase para pedidos
class Pedidos:

    def __init__(self):
        self.db = BaseDatos()


    def crear_pedido(self, cliente_select, producto_select):
        conexion = self.db.abrirConexion()
        if conexion:
#se realiza la consulta a la tabla clientes 
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT nombre FROM clientes WHERE clave = ?", (cliente_select,))
                cliente = cursor.fetchone()
                if not cliente:
                    print(f"El cliente {cliente_select} no existe")
                    return
                
#aqui se realiza la consulta a la tabla de los productos y tambien el precio
                cursor.execute("SELECT nombre, precio FROM menu WHERE clave = ?", (producto_select,))
                producto = cursor.fetchone()
                if not producto:
                    print(f"El producto {producto_select} no existe")
                    return
                
                producto_nombre, precio = producto
#despues de realizar las consultas, aqui se insertan los datos a la tabla de pedidos para crear un nuevo pedido
                cursor.execute(
                    "INSERT INTO pedidos (cliente, producto, precio) VALUES (?, ?, ?)", 
                    (cliente_select, producto_nombre, precio)
                )

                conexion.commit()
 #en esta parte y con los datos anteriores se crea un ticket        
                print('Pedido creado correctamente. Imprimiendo Ticket...')
                self.imprimir_ticket(cliente[0], producto_nombre, precio)
            except Exception as e:
                print(f"Error al crear el pedido: {e}")
            finally:
                self.db.cerrarConexion(conexion)

#esta parte es para eliminar un pedido mediante su id
    def cancelar_pedido(self, pedido_id):
        conexion = self.db.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM pedidos WHERE pedido = ?", (pedido_id,))
                conexion.commit()
                if cursor.rowcount > 0:
                    print('Pedido cancelado')
                else:
                    print('pedido no encontrado')
            except Exception as e:
                print(f"Error al cancelar el pedido: {e}")
            finally: 
                self.db.cerrarConexion(conexion)
#se crea la funcion que contendra los datos recividos y esta funcion se encargara de crear los tickets
    def imprimir_ticket(self, cliente, producto, precio):

        ticket_content= (
            "****** TIQUET DE PEDIDO *****\n"
            f"Cliente: {cliente}\n"
            f"Producto: {producto}\n"
            f"Precio Total: ${precio:.2f}\n"
            "======================================\n"
        )
        print(ticket_content)

        try:
            with open('ticket.txt', 'w') as file:
                file.write(ticket_content)
            print("Ticket guardado como 'ticket.txt'")
        except Exception as e:
            print(f"Error guardar el ticket: {e}")
        

#esta funcion se encarga de hacer la consulta a la tabla pedidos, y esta servira para mostrar los pedidos con html
    def mostrar_pedido(self, numero_pedido):
        conexion = self.db.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM pedidos WHERE pedido = ?", (numero_pedido,))
                pedido = cursor.fetchone()
                if pedido:
                    return {
                        'pedido': pedido[0],
                        'cliente': pedido[1],
                        'producto': pedido[2],
                        'precio': pedido[3]
                    }
                else:
                    return None
            except Exception as e:
                print(f"Error al consultar pedido: {e}")
                return None