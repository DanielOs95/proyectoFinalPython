#import sqlite3
from setup_database import BaseDatos


class Pedidos:

    def __init__(self):
        self.db = BaseDatos()


    def crear_pedido(self, cliente_select, producto_select):
        conexion = self.db.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT nombre FROM clientes WHERE clave = ?", (cliente_select,))
                cliente = cursor.fetchone()
                if not cliente:
                    print(f"El cliente {cliente_select} no existe")
                    return
                

                cursor.execute("SELECT nombre, precio FROM menu WHERE clave = ?", (producto_select,))
                producto = cursor.fetchone()
                if not producto:
                    print(f"El producto {producto_select} no existe")
                    return
                
                producto_nombre, precio = producto

                cursor.execute(
                    "INSERT INTO pedidos (cliente, producto, precio) VALUES (?, ?, ?)", 
                    (cliente_select, producto_nombre, precio)
                )

                conexion.commit()
        
                print('Pedido creado correctamente. Imprimiendo Ticket...')
                self.imprimir_ticket(cliente[0], producto_nombre, precio)
            except Exception as e:
                print(f"Error al crear el pedido: {e}")
            finally:
                self.db.cerrarConexion(conexion)


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