import JuegosController as controller, funciones

def menu():
    
    
    print("\n1. Registrar un juego")
    print("2. Modificar un Juego")
    print("3. Eliminar un Juego")
    print("4. Mostrar un Juego")
    print("\n9. Salir")
    opcion = input("\n---------Ingrese una opción: ")
    
    
    if opcion == "1":
        Nuevojuego = pedirJuego()
        if Nuevojuego != None:
            juegosExistentes=controller.retronarJuegos()
            
            for juego in juegosExistentes:
                if Nuevojuego["nombre"] == juego["nombre"]:
                    print("                                 CANCELAR= "'"N"'"\nYa existe un juego con ese nombre\n1. Desea Actualizar el juego?",juego["nombre"],"\n2. Añadir Una la nueva cantidad de existencias")
                    opcion = funciones.ingresar_dato("Ingrese una opcion: ")
                    if opcion is False:
                        return None
                    
                    if opcion == "1":
                        
                         ActualizarJuego(juego)
                         return None
                    
                    elif opcion == "2":
                        juego["existencia"]=  int(Nuevojuego["existencia"]) + int(juego["existencia"])
                        controller.actualizarJuego(juego["id"],juego)
                    
                else:
                    controller.agregarJuego(Nuevojuego)
        else:
            print("No re sealizo ninfun registro")
    
    elif opcion == "2":
        modificarJuego = funciones.ingresar_dato("Ingrese el nombre del juego que desea modificar:                  Cancelar = '"'N"'"\n\n: ")
        if modificarJuego is False:
         return None

        JUEGOeNCONTRADO =  controller.buscarJuego(modificarJuego)
        if JUEGOeNCONTRADO!= None:
            controller.mostrarJuego(JUEGOeNCONTRADO)
            
            ActualizarJuego(JUEGOeNCONTRADO)
        else:
            print("Saliendo...")       

    elif opcion == "3":
        modificarJuego = funciones.ingresar_dato("Ingrese el nombre del juego que desea Eliminar:                  Cancelar = '"'N"'"\n\n: ")
        if modificarJuego is False:
         return None
        
        JUEGOeNCONTRADO=controller.buscarJuego(modificarJuego)
        if JUEGOeNCONTRADO!= None:
            print("Esta seguro que des eliminar el Juego: ")
            controller.mostrarJuego(JUEGOeNCONTRADO)
            if funciones.confirmarDecision():
                controller.eliminarJuego(JUEGOeNCONTRADO["id"])
            else: 
                print("Regresando...")
        
def pedirJuego():
    print("                                                  Cancelar = '"'N'"' ")
    nuevoCamper = {}
    nombres = funciones.ingresar_dato("\nIngre el nombre del juego: ")
    if nombres is False:
         return None
    Tiempo = funciones.ingresar_dato("\nIngrese el Tiempo por partida: ")
    if Tiempo is False:
         return None
    CantidadJugadores = funciones.ingresar_dato("\nIngrese la cantidad de jugadores: ")
    if CantidadJugadores is False:
         return None
    Existencia = funciones.ingresar_dato("\nIngrese la  existencia (cantidad de juegos disponibles para usar): ")
    if Existencia is False:
         return None

    nuevoCamper = {
        "nombre":nombres, 
        "tiempo":Tiempo,
        "cantJugadores":CantidadJugadores,
        "existencia":Existencia
        }
        
    return nuevoCamper

def ActualizarJuego(Juego):
 while True:
            campoModificar=input("Campos Disponibles para modificar:\n  1. 'Tiempo'\n  2 'Cantidad'\n  3. 'Existencia'\n9. Cancelar...\n\Seleccione el nombre del campo que desea modificar: ")
            
            if campoModificar.lower()  == "1":
                
                    print("El campo Tiempo actualmente contiene", Juego["tiempo"])
                    nuevoEstado = input("Ingrese el nuevo valor: ")                                    
                    print("Esta seguro de cambiar el Tiempo del Juego", Juego["nombre"], "de", Juego["tiempo"],"a", nuevoEstado)
                    if funciones.confirmarDecision():
                        Juego["tiempo"]=nuevoEstado.upper()
                        controller.actualizarJuego(Juego["id"], Juego)
                    else:
                        print("Regresando...")
                    break
            if campoModificar.lower()  == "2":
                
                    print("El campo Tiempo actualmente contiene", Juego["cantJugadores"])
                    nuevoEstado = input("Ingrese el nuevo valor: ")                                    
                    print("Esta seguro de cambiar el Tiempo del Juego", Juego["nombre"], "de", Juego["cantJugadores"],"a", nuevoEstado)
                    if funciones.confirmarDecision():
                        Juego["cantJugadores"]=nuevoEstado.upper()
                        controller.actualizarJuego(Juego["id"], Juego)
                    else:
                        print("Regresando...")
                    break
            if campoModificar.lower()  == "3":
            
                print("El campo Tiempo actualmente contiene", Juego["existencia"])
                nuevoEstado = input("Ingrese el nuevo valor: ")                                    
                print("Esta seguro de cambiar el Tiempo del Juego", Juego["nombre"], "de", Juego["existencia"],"a", nuevoEstado)
                if funciones.confirmarDecision():
                    Juego["existencia"]=nuevoEstado.upper()
                    controller.actualizarJuego(Juego["id"], Juego)
                else:
                    print("Regresando...")
                break
            if campoModificar.lower()  == "9":
            
                
                break
    
            else:
                print("El campo", campoModificar, "No se puede modificar...")
                