import sqlite3
import os


class BaseDatos:

    def __init__(self, nombre_db='happy_burguer.db'):
        self.nombre_db = nombre_db

    def crearBaseDatos(self):
        try:
            conn = sqlite3.connect(self.nombre_db)
            conn.close()
            print("Base de datos creada")
        except Exception as e:
            print("Error al crear la base de datos: {}".format(e))

    def verificarBaseDatosExiste(self):
        if os.path.isfile(self.nombre_db):
            return True
        else:
            return False
        
    def abrirConexion(self):
        try:
            conexion = sqlite3.connect(self.nombre_db)
            print('Conexion exitosa a la base de datos')
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos: {}".format(e))
            return None
        
    def cerrarConexion(self, conexion):
        if conexion:
            conexion.close()
            print('Conexion cerrada')
        
    def crearTablas(self):
        conexion = self.abrirConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(""" CREATE TABLE IF NOT EXISTS clientes (
                    clave TEXT PRIMARY KEY,
                    nombre TEXT,
                    direccion TEXT,
                    correo_electronico TEXT,
                    telefono INTEGER) """)
      
                cursor.execute(""" CREATE TABLE IF NOT EXISTS menu (
                    clave TEXT PRIMARY KEY,
                    nombre TEXT,
                    precio FLOAT) """)
        
                cursor.execute(""" CREATE TABLE IF NOT EXISTS pedidos (
                    pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente TEXT,
                    producto TEXT,
                    precio FLOAT) """)
                

                conexion.commit()
                print('Tablas creadas correctamente')
            except Exception as e:
                print('Error al crear las tablas: {}'.format(e))
            finally: 
                self.cerrarConexion(conexion)

        
        
       

    
    
