from os import system
import time
import conexion as conn
db = conn.DB()
def create():
    nombre = str(input("Ingrese el Nombre: "))
    email = str(input("Ingrese el Email: "))
    if(len(nombre)>0 and len(email)>0):
        sql = "INSERT INTO sistema(nombre,email)VALUES(?,?)"
        parametros = (nombre,email)
        db.ejecutar_consulta(sql,parametros)
        print("Registros ingresados con exito")
        
while True:
    print("**************************************")
    print("\tCRUD con SQLITE")
    print("**************************************")
    print("\t[1] Insertar un registro.")
    print("\t[2] Consultar los registros.")
    print("\t[3] Actualizar un registro.")
    print("\t[4] Eliminar un registro.")
    print("\t[5] Buscar regstro.")
    print("\t[6] Salir del sistema.")
    print("**************************************")
    try:
        opcion = int(input("Seleccione una opcion: "))
        if (opcion == 1):
            create()
            time.sleep(1)
            
        elif (opcion == 2):
            time.sleep(1)
            
        elif (opcion == 3):     
            time.sleep(1)
            
        elif (opcion == 4):
            time.sleep(1)
            
        elif (opcion == 5):
            
            time.sleep(1)
        elif (opcion == 6):
            break
    except:
        print("Seleccione una opcion correcta")
        system("clear")
