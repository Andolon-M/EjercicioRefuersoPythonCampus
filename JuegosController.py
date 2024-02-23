import CrudJsones as data
from tabulate import tabulate
from funciones import confirmarDecision
import time

# Nombre del archivo JSON
archivo_json = 'ArchivosInformacion/Juegos.json'

def retronarJuegos():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    return datos  

#agregar Juegos
def agregarJuego(Juego):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    # Agregar el nuevo registro a los datos existentes
    datos = data.crear_registro(datos, Juego)
    # guardar los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#buscar un registro por ID
def buscarJuego(id_buscar):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    registro_encontrado = data.buscar_registro(datos, id_buscar, "nombre")
    if registro_encontrado:
        print("Se encontro coincidencia con el NOMBRE del sigueinte Juego\n")
        return registro_encontrado
       
    else:
        registro_encontrado = data.buscar_registro_por_id(datos, int(id_buscar))
        if registro_encontrado:
            print("Se encontro coincidencia con el ID del sigueinte Juego\n")   
            return registro_encontrado 
        else:    
            print("No se encontró ningún registro con el ID o NOMBRE", id_buscar)
            return None

#actualizar un registro por ID
def actualizarJuego(id_actualizar, nuevos_datos):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.actualizar_registro_por_id(datos, id_actualizar, nuevos_datos):
        print("CAMBIOS REALIZADOS.")
    else:
        print("NO SE HICIERON CAMBIOS.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#eliminar un registro por ID
def eliminarJuego(id_eliminar): 
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.eliminar_registro_por_id(datos, id_eliminar):
        print("Registro eliminado correctamente.")
    else:
        print("No se pudo eliminar el registro.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

def mostrarJuegos():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    
    # Convertir los datos a una lista de listas para tabulate
    tabla_datos = []
    for registro in datos:
        fila = [
        registro.get('id', ''),
        registro.get('nombre', ''),
        registro.get('tiempo', ''),
        registro.get('cantJugadores', ''),
        registro.get('existencia', '')
        
        ]
        tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "NOMBRE", "DURACION DE PARTIDA (minutos)", "CANTIDAD DE JUGADORES", "EXISTENCIA"]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def mostrarJuego(registro):   
    # Convertir los datos a una lista de listas para tabulate
    tabla_datos = []
    
    fila = [
        registro.get('id', ''),
        registro.get('nombre', ''),
        registro.get('tiempo', ''),
        registro.get('cantJugadores', ''),
        registro.get('existencia', '')
        
    ]
    tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "NOMBRE", "DURACION DE PARTIDA (minutos)", "CANTIDAD DE JUGADORES", "EXISTENCIA"]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def menuBuscarJuego(Juego):
    while True:
        opciones = input("                Opciones:             ENTER = Regresar   M = Modificar   D = Eliminar\nIngrese una opcion: ")
        if opciones.lower() == "m":
            campoModificar=input("Ingrese el nombre del campo que desea modificar: ")
            if campoModificar.lower() in Juego:
                print("El campo",campoModificar," aactualmente contiene", Juego[campoModificar.lower()])
                nuevoEstado = input("Ingrese el nuevo valor: ")                                    
                print("Esta seguro de cambiar ",campoModificar," del Juego", Juego["dni"], "de", Juego[campoModificar.lowe()],"a", nuevoEstado)
                if confirmarDecision():
                    Juego[campoModificar.lower()]=nuevoEstado.upper()
                    actualizarJuego(Juego["id"], Juego)
                else:
                    print("Regresando...")
                break
            else:
                print("El campo", campoModificar,"no se encuentra...")
    
        elif opciones.lower() == "d":
            if confirmarDecision():
                eliminarJuego(Juego["id"])
                print("Se eliminará el registro")
                time.sleep(1)
                break
        else:
            break
                 