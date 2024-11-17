from setup_database import BaseDatos

#se crea la clase menu
class Menu:

    def __init__(self):
        self.sql = BaseDatos()
#aqui se realiza la conexion con la tabla menu para poder insertar registros
    def agregar_producto(self, clave, nombre, precio):
        conexion = self.sql.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO menu(clave, nombre, precio) VALUES (?, ?, ?)",
                    (clave, nombre, precio)
                )
                conexion.commit()
                print("Producto agregado correctamente")
            except Exception as e:
                print(f"Error al agregar producto: {e}")
            finally:
                self.sql.cerrarConexion(conexion)
#aqui se realiza la conexion con la tabla menu para poder eliminar regitros por medio de su clave unica
    def eliminar_producto(self, clave):
        conexion = self.sql.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM menu WHERE clave = ?", (clave,))
                conexion.commit()
                if cursor.rowcount > 0:
                    print('Producto eliminado correctamente')
                else:
                    print('producto no encontrado')
            except Exception as e:
                print(f"Error al eliminar el producto: {e}")
            finally:
                self.sql.cerrarConexion(conexion)
    
#aqui se hace la conexion con la tabla menu para modficar y actualizar registros exixtentes
    def actualizar_producto(self, clave, nombre=None, precio=None):
        conexion = self.sql.abrirConexion()
        if conexion:
            try:
                actualizar = []
                parametros = []

                if nombre:
                    actualizar.append("nombre = ?")
                    parametros.append(nombre)
                if precio:
                    actualizar.append("precio = ?")
                    parametros.append(precio)

                if actualizar:
                    parametros.append(clave)
                    actualizacion_query = f"UPDATE menu SET {', '.join(actualizar)} WHERE clave = ?"
                    cursor = conexion.cursor()
                    cursor.execute(actualizacion_query, parametros)
                    conexion.commit()
                    if cursor.rowcount > 0:
                        print('Producto actualizado correctamente')
                    else:
                        print('producto no encontrado')
                else:
                    print('No se proporcionaron datos para actualizar')
            except Exception as e:
                print(f"Error al actualizar el producto: {e}")
            finally:
                self.sql.cerrarConexion(conexion)
    