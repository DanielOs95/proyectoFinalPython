from setup_database import BaseDatos
# se crea la clase clientes
class Clientes:

    def __init__(self):
        self.db = BaseDatos()
#se realiza la conexion a la tabla clientes para poder insertar registros 
    def agregar_cliente(self, clave, nombre, direccion, correo_electronico, telefono):
        conexion = self.db.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO clientes (clave, nombre, direccion, correo_electronico, telefono) VALUES (?, ?, ?, ?, ?)",
                    (clave, nombre, direccion, correo_electronico, telefono)
                )
                conexion.commit()
                print('Cliente agregado correctamente')
            except Exception as e:
                print(f"Error al agregar cliente: {e}")
            finally:
                self.db.cerrarConexion(conexion)
# aqui se realiza la conexion con la tabla clientes para eliminar dos de clientes
    def eliminar_cliente(self, clave):
        conexion = self.db.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM clientes WHERE clave = ?", (clave,))
                conexion.commit()
                if cursor.rowcount > 0:
                    print('Cliente eliminado correctamente')
                else:
                    print('cliente no encontrado')
            except Exception as e:
                print(f"Error al eliminar cliente: {e}")
            finally:
                self.db.cerrarConexion(conexion)
    
#aqui se hace la conexion para actualizar datos existentes en la tabla clientes
    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo_electronico=None, telefono=None):
        conexion = self.db.abrirConexion()
        if conexion:
            try:
                actualizar = []
                parametros = []

                if nombre:
                    actualizar.append("nombre = ?")
                    parametros.append(nombre)
                if direccion:
                    actualizar.append("direccion = ?")
                    parametros.append(direccion)
                if correo_electronico:
                    actualizar.append("correo_electronico = ?")
                    parametros.append(correo_electronico)
                if telefono:
                    actualizar.append("telefono = ?")
                    parametros.append(telefono)
            
                if actualizar:
                    parametros.append(clave)
                    actualizacion_query = f"UPDATE clientes SET {', '.join(actualizar)} WHERE clave = ?"
                    cursor = conexion.cursor()
                    cursor.execute(actualizacion_query, parametros)
                    conexion.commit()
                    if cursor.rowcount > 0:
                        print('Cliente actualizado correctamente')
                    else:
                        print('cliente no encontrado')
                else:
                    print("no se proporcionaron datos para actualizar")
            except Exception as e:
                print(f"Error al actualizar cliente: {e}")
            finally:
                self.db.cerrarConexion(conexion)

