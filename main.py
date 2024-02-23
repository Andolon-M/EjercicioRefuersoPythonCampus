import time, funciones, GestionDeJuegos as juegos, ConsultasYValidaciones, ValoracionesController

def menu():
    try:
        while True:
            funciones.limpiar_consola() 
            print(f"\n****************   Bienvenido   ********************, \nMENU PRINCIPAL")
            print("1. Gestión de  juegos")
            print("2. Consultas y valoraciones")
            print("3. Revisar puntuaciones")
            
            print("\n9. SALIR")
            opcion = input("\n---------Ingrese una opción: ")
            
            if opcion == "1":
               
                juegos.menu()
                
                
            elif opcion == "2":
                
                ConsultasYValidaciones.menu()
                
                
            elif opcion == "3":
                print("EL TOP 3 DE LOS MEJORES JUEGOS ES:\n")
                print((ValoracionesController.mejores_juegos_top3()))
                input("Precione ENTER para continuar...")
                
            elif opcion == "4":
                
                pass
                
                
            elif opcion == "5":
                auth_data = None
                break
            else:
                print("Ingrese una opción válida")
            time.sleep(2)
            
    
    except Exception as error:
       print(f"Ha habido un error, por favor comunicate con suporte.\nError: {error}")

menu()