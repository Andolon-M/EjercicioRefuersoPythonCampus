import csv
from collections import defaultdict

nombre_archivo = 'ArchivosInformacion/valoraciones_juegos.csv'  # Ruta al archivo CSV
def valorar_juego(juego_info):
    # Solicitar valoración al usuario
    valoracion = input("Por favor, valora el juego de 0 a 5 estrellas: ")
    
    # Verificar que la valoración sea válida
    try:
        valoracion = float(valoracion)
        if valoracion < 0 or valoracion > 5:
            raise ValueError
    except ValueError:
        print("La valoración ingresada no es válida.")
        return

    # Agregar la valoración al diccionario de información del juego
    juego_info['valoracion'] = valoracion

    # Guardar la información en un archivo CSV
    nombre_archivo = 'ArchivosInformacion/valoraciones_juegos.csv'
    campos = list(juego_info.keys())

    try:
        with open(nombre_archivo, mode='a', newline='') as archivo_csv:
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

            # Escribir encabezados si el archivo está vacío
            if archivo_csv.tell() == 0:
                escritor_csv.writeheader()

            escritor_csv.writerow(juego_info)

        print("Valoración guardada exitosamente en", nombre_archivo)
    except Exception as e:
        print("Error al guardar la valoración:", str(e))

def numero_valoraciones(juego_info):
    nombre_juego = juego_info.get('nombre')
    

    try:
        with open(nombre_archivo, mode='r') as archivo_csv:
            valoraciones = csv.DictReader(archivo_csv)
            contador = 0

            for fila in valoraciones:
                if fila['nombre'] == nombre_juego:
                    contador += 1

        return contador
    except FileNotFoundError:
        print("El archivo CSV no fue encontrado.")
        return 0
    
def mejores_juegos_top3():
    juegos_valoraciones = defaultdict(list)

    # Leer el archivo CSV y agrupar las valoraciones por juego
    with open(nombre_archivo, mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        
        for fila in lector_csv:
            nombre_juego = fila['nombre']
            valoracion = float(fila['valoracion'])
            juegos_valoraciones[nombre_juego].append(valoracion)

    # Calcular el promedio de las valoraciones para cada juego
    promedios_juegos = {}
    for nombre_juego, valoraciones in juegos_valoraciones.items():
        promedio = sum(valoraciones) / len(valoraciones)
        promedios_juegos[nombre_juego] = promedio

    # Seleccionar los 3 juegos con los promedios más altos
    top3_juegos = sorted(promedios_juegos.items(), key=lambda x: x[1], reverse=True)[:3]
    return top3_juegos