import time
import csv
import os
csv.field_size_limit(2147483647)

from DataStructures.List import single_linked_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import array_list as arl
import math
import haversine
from datetime import datetime

#dir_data = os.path.dirname(os.path.realpath('__file__'))+ "/Data/"

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "array_list": arl.new_list(),
        "barrios": arl.new_list(), 
        }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file = open(filename, encoding =  "utf-8-sig")
    data = csv.DictReader(file)
    
    for i in data:
        arl.add_last(catalog['array_list'], i)
        
    file.close()
    return catalog
        
        

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

def calcular_duracion(catalog):
    
    tripa = catalog["array_list"]
    size = arl.size(catalog["array_list"])
    viajes_filtrados= []
    viajes_t = len(viajes_filtrados)
    
    for i in range(size):
        tripa = arl.get_element(catalog['array_list'], i)

    partes1 = tripa["pickup_datetime"].split(" ")
    fecha1 = partes1[0].split("-")
    hora1 = partes1[1].split(":")
    h1 = int(hora1[0])
    m1 = int(hora1[1])
    s1 = int(hora1[2])

    partes2 = tripa["dropoff_datetime"].split(" ")
    fecha2 = partes2[0].split("-")
    hora2 = partes2[1].split(":")
    h2 = int(hora2[0])
    m2 = int(hora2[1])
    s2 = int(hora2[2])

    
    t1 = h1 * 60 + m1 + s1 / 60.0
    t2 = h2 * 60 + m2 + s2 / 60.0

    if fecha1 != fecha2:
        t2 += 24 * 60  

    return t2 - t1


def req_2(catalog, payment_method):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    
    
    duracion_t = 0
    costo_t = 0
    distancia_t = 0 
    tolls_t = 0
    tip_total = 0
    pasajeros_f = {}
    fecha_f = {}
    
    
    start_time = get_time() 
    
    viajes_filtrados= []
    
    size = arl.size(catalog["array_list"])
    
    viajes_t= len(viajes_filtrados)
    
    for i in range(size):
        trip = arl.get_element(catalog['array_list'], i)
        if trip['payment_type'] == payment_method:
            viajes_filtrados.append(trip)
    
    viajes_t= len(viajes_filtrados)
            
    for trip in viajes_filtrados:
        
        duracion = calcular_duracion(catalog)
        costo = float(trip["total_amount"])
        dist = float(trip["trip_distance"])
        tolls = float(trip["tolls_amount"])
        tip = float(trip["tip_amount"])
        psger = int(trip["passenger_count"]) 
        fecha = trip["dropoff_datetime"].split(" ")[0]  
        
        duracion_t += duracion
        costo_t += costo
        distancia_t += dist
        tolls_t += tolls
        tip_total += tip
        
        if psger not in pasajeros_f:
            pasajeros_f[psger] = 1
        
        else:
            pasajeros_f[psger] += 1
        
        
        if  fecha not in fecha_f:
            fecha_f[fecha] = 1
        else:
            fecha_f[fecha] += 1
      
    tiempo_p = duracion_t / viajes_t
    costo_p = costo_t / viajes_t
    dist_p = distancia_t / viajes_t
    tolls_p = tolls_t / viajes_t
    tips_p = tip_total / viajes_t
    psj_mas = max(pasajeros_f, key = pasajeros_f.get)
    frecuencia = pasajeros_f[psj_mas]
    fecha_mas = max(fecha_f, key = fecha_f.get)
    frecu = fecha_f[fecha_mas]
    
    
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)

    
    
    return {
        "Tiempo de ejecución en ms": tiempo, 
        "Total trayectos": viajes_t,
        "Tiempo promedio": tiempo_p,
        "Costo total": (round(costo_p, 2)),
        "Distancia promedio": (round(dist_p, 2)),
        "Costo de peajes promedio": (round(tolls_p, 2)),
        "Propinas promedio": (round(tips_p, 2)),
        "Pasajeros frecuentes": [psj_mas, frecuencia], 
        "Fecha más frecuente": [fecha_mas, frecu]
    }
    


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog, filtro, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    
    conteo_trayectos = 0 
    duracion = 0 
    comb_f = {}
    start_time = get_time() 
    
    size = arl.size(catalog["array_list"])
    size_b = arl.size(catalog["barrios"])
    fecha_i = datetime.strptime(fecha_i, "%Y-%m-%d").date()
    fecha_f = datetime.strptime(fecha_f, "%Y-%m-%d").date()
    comb = arl.new_list()
    

    for i in range(size):
        trip = arl.get_element(catalog['array_list'], i)
        
        fecha = datetime.strptime(trip["pickup_datetime"].split(" ")[0], "%Y-%m-%d").date()
        f_drop = trip["dropoff_datetime"].split(" ")[0]
        b_orig = ""
        b_dest = ""
        d_min1 = 99999999999999999999999999999999999     #se usa un valor muy grande para asegurar que siempre el valor sea menor y asi actualizar la variable
        d_min2 = 99999999999999999999999999999999999     #se usa un valor muy grande para asegurar que siempre el valor sea menor y asi actualizar la variable

        
        if (fecha_i <= fecha) and (fecha <= fecha_f):
        
            pick_lat = float(trip["pickup_latitude"])
            pick_lon = float(trip["pickup_longitude"])
            drop_lon = float(trip["dropoff_longitude"])
            drop_lat = float(trip["dropoff_latitude"])
            
            for b in range(size_b):
                barrio = arl.get_element(catalog["barrios"], b)
                lg = barrio[2]
                lat = barrio[3]
                dist_t = haversine((pick_lat, pick_lon), (lat, lg))
                
                if dist_t < d_min1:
                    d_min1 = dist_t
                    b_orig = barrio[1]
    
            for bd in range(size_b):
                barrio = arl.get_element(catalog["barrios"], bd)
                lg = barrio[2]
                lat = barrio[3]
                dist_t = haversine((drop_lat, drop_lon), (lat, lg))
                
                if dist_t < d_min2:
                    d_min2 = dist_t
                    b_dest = barrio[1]
                    
            
            #PARA VERIFICAR QUE HAYA ALGO EN LAS VARIABLE:
            
            if (b_orig != "" ) and (b_dest != "") and (b_dest != b_orig):
                conteo_trayectos += 1
                duracion_p = float((datetime.strptime(trip["dropoff_datetime"], "%Y-%m-%d %H:%M:%S") - 
                              datetime.strptime(trip["pickup_datetime"], "%Y-%m-%d %H:%M:%S")).total_seconds() / 60)
                
                combinacion = (b_orig, b_dest)
                costo = float(trip["total_amount"])
                
                distancia = float(haversine((pick_lat, pick_lon), (drop_lat, drop_lon)))
                
                if combinacion not in comb_f:
                    comb_f[combinacion] = {"costo": costo,
                                           "duracion": duracion_p,
                                           "distancia": distancia,
                                           "conteo": 1
                        
                    }
                else:
                    comb_f[combinacion]["costo"] += costo
                    comb_f[combinacion]["duracion"] += duracion_p
                    comb_f[combinacion]["distancia"] += distancia
                    comb_f[combinacion]["conteo"] += 1
                    
                    
                
    c = None
    valor = None
    
    for i, j in comb_f.items():
        cost_p = j["costo"] / j["conteo"]
        
        if filtro == "MAYOR":
             if valor is None or cost_p > valor:
                valor = cost_p
                c = i
        elif filtro == "MENOR":
            if valor is None or cost_p < valor:
                valor = cost_p
                c = i
    
    resultado = None
    
    bar_o = None
    bar_d = None
    d_prom = 0
    tiemp_p = 0
    cost_p = 0
        
    
    if c is not None:
        rta = comb_f[c]
        bar_o = c[0]
        bar_d = c[1]
        d_prom = rta["distancia"] / rta["conteo"]
        tiemp_p = rta["duracion"] / rta["conteo"]
        cost_p = rta["costo"] / rta["conteo"]
        
    
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
        
    resultado = {"Tiempo ejecucion": tiempo,
                 "Filtro de seleccion": filtro, 
                 "Conteo trayectos": conteo_trayectos, 
                 "Barrio de origen": bar_o, 
                 "Barrio de destino": bar_d, 
                 "Distancia promedio": d_prom, 
                 "Tiempo promedio": tiemp_p, 
                 "Costo promedio": cost_p
        }
            
    return resultado

    
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



