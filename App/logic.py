import time
import csv
csv.field_size_limit(2147483647)

from DataStructures.List import single_linked_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {}


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pass

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    try:
        precio_min = float(input("Ingrese el valor mínimo del costo total: "))
        precio_max = float(input("Ingrese el valor máximo del costo total: "))
    except:
        print("Error: debe ingresar valores numéricos.")
        return

    inicio = time.time()

    filtrados = []
    for viaje in catalog:
        try:
            total = float(viaje["total_amount"])
            if precio_min <= total <= precio_max:
                filtrados.append(viaje)
        except:
            continue

    total_trayectos = len(filtrados)
    if total_trayectos == 0:
        print("No se encontraron trayectos en el rango dado.")
        return

    suma_duracion = 0
    suma_precio = 0
    suma_distancia = 0
    suma_peajes = 0
    suma_propinas = 0
    conteo_pasajeros = {}
    conteo_fechas = {}

    for viaje in filtrados:
        try:
            inicio_viaje = viaje["pickup_datetime"]
            fin_viaje = viaje["dropoff_datetime"]

            if inicio_viaje and fin_viaje:
                from datetime import datetime
                fmt = "%Y-%m-%d %H:%M:%S"
                t1 = datetime.strptime(inicio_viaje, fmt)
                t2 = datetime.strptime(fin_viaje, fmt)
                duracion = (t2 - t1).total_seconds() / 60
            else:
                duracion = 0

            precio = float(viaje["total_amount"])
            distancia = float(viaje["trip_distance"])
            peaje = float(viaje["tolls_amount"])
            propina = float(viaje["tip_amount"])
            pasajeros = viaje["passenger_count"]
            fecha = viaje["dropoff_datetime"].split(" ")[0]  

            suma_duracion += duracion
            suma_precio += precio
            suma_distancia += distancia
            suma_peajes += peaje
            suma_propinas += propina

            conteo_pasajeros[pasajeros] = conteo_pasajeros.get(pasajeros, 0) + 1

            conteo_fechas[fecha] = conteo_fechas.get(fecha, 0) + 1

        except:
            continue

    duracion_prom = suma_duracion / total_trayectos
    precio_prom = suma_precio / total_trayectos
    distancia_prom = suma_distancia / total_trayectos
    peaje_prom = suma_peajes / total_trayectos
    propina_prom = suma_propinas / total_trayectos

    pasajeros_mas_frec = "No disponible"
    if conteo_pasajeros:
        p_mas_frec = max(conteo_pasajeros, key=conteo_pasajeros.get)
        cantidad_pasajeros = conteo_pasajeros[p_mas_frec]
        pasajeros_mas_frec = f"{p_mas_frec} - {cantidad_pasajeros}"

    fecha_mas_frec = "No disponible"
    if conteo_fechas:
        fecha_mas_frec = max(conteo_fechas, key=conteo_fechas.get)

    fin = time.time()
    tiempo_ejecucion = (fin - inicio) * 1000  

    tabla = [
        ["Tiempo de ejecución (ms)", f"{tiempo_ejecucion:.2f}"],
        ["Número total de trayectos", total_trayectos],
        ["Tiempo promedio (min)", f"{duracion_prom:.2f}"],
        ["Precio total promedio ($)", f"{precio_prom:.2f}"],
        ["Distancia promedio (millas)", f"{distancia_prom:.2f}"],
        ["Precio promedio peajes ($)", f"{peaje_prom:.2f}"],
        ["Propina promedio ($)", f"{propina_prom:.2f}"],
        ["Pasajeros más frecuente", pasajeros_mas_frec],
        ["Fecha más frecuente de finalización", fecha_mas_frec],
    ]

    print("\nResultados del análisis:\n")
    print(tabulate(tabla, headers=["Métrica", "Valor"], tablefmt="grid"))


if __name__ == "__main__":
    catalog = cargar_datos("taxis-large.csv")  
    req_3(catalog)


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
