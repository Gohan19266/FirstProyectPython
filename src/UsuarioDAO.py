import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Usuario:
    idusuario=0
    nomuser=""
    clave=""
    estado=""
    def readAll(self):
        try:
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('ReadAllUsers')
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    def ReadUser(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('ReadUser',[self.idusuario,])
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def AddUsuario(self):
        nombre=self.nomuser
        passs=self.clave
        data=[nombre,passs]
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("AddUsers",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    
    def Updateuser(self):
        try:
            iduser=self.idusuario
            name=self.nomuser
            passs=self.clave
            state=self.estado
            data=[name,passs,state,iduser]
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("UpdateUser",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
'''obj = Usuario()
print(obj.readAll())'''



