import time, funciones, JuegosController as juegos, ValoracionesController as validaciones


def menu():
    
    
    print("\n1. Consultar juego")
    print("2. Valorar un Juego")
    print("\n9. Salir")
    opcion = input("\n---------Ingrese una opción: ")
    
    if opcion == "1":
        juegoBuscar = funciones.ingresar_dato("\n                         CANCELAR = "'"N"'"\n\nIngrese el nombre del juego que desea consultar: ")
        juegoEncontrado=juegos.buscarJuego(juegoBuscar)
        juegos.mostrarJuego(juegoEncontrado)
        print("El juego encontrado tiene: ", validaciones.numero_valoraciones(juegoEncontrado))
        
        input("Precione ENTER para continuar")
    if opcion == "2":
        juegoModificar = funciones.ingresar_dato("\n                         CANCELAR = "'"N"'"\n\nIngrese el nombre del juego que desea valorar: ")
        juegoEncontrado=juegos.buscarJuego(juegoModificar)
        if juegoEncontrado != None:
            validaciones.valorar_juego(juegoEncontrado)
            print("La valoracion ha sido agregada")
        time.sleep(1)
    