#import sqlite3
from setup_database import BaseDatos


class Pedidos:

    def __init__(self):
        self.db = BaseDatos()


    def crear_pedido(self, cliente, producto, precio):
        conexion = self.db.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO pedidos(cliente, producto, precio) VALUES (?, ?, ?)",
                    (cliente, producto, precio)
                )
                conexion.commit()
                print('Pedido creado correctamente. Imprimiendo Ticket...')
                self.imprimir_ticket(cliente, producto, precio)
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
            "****** TIQUET DE PEDIDO *****"
            f"Cliente: {cliente}"
            f"Producto: {producto}"
            f"Precio Total: ${precio:.2f}"
            "======================================"
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