import time
import csv
import sys
import os
from math import asin, sin, cos, sqrt, radians
from datetime import datetime 
csv.field_size_limit(2147483647)

from DataStructures.List import single_linked_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import array_list as al
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

data_structure = None

def new_logic(user_data_structure):
    
    global data_structure
    if user_data_structure == "1":
        data_structure = al
    else:
        data_structure = lt
    
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {"neighborhood":None
               "Taxis" : None
        } 
    #poner llaves y estan llenos de none, a cada una de las llaves se le crea una nueva lista
    catalog["neighborhood"] = data_structure.new_list()
    catalog["Taxis"] = data_structure.new_list()
    return catalog


# Funciones para la carga de datos

def load_taxis_data(catalog, filename):
    """
    Carga los datos del reto
    """
    file_t = data_dir + 'taxis-large.csv'
    input_del_archivo = csv.DictReader(open(file_t, encoding="utf-8"))
    for taxi in input_del_archivo:
        al.add_last(catalog['taxis'], taxi)
        tamanio = al.size(catalog['taxis'])
    return tamanio
    
def load_neighborhoods_data(catalog, filename):
    """
    Carga los datos del reto
    """
    file_n =  data_dir + 'nyc-neighbothoods.csv'
    input_del_archivo = csv.DictReader(open(file_n, encoding="utf-8"))
    for taxi in input_del_archivo:
        al.add_last(catalog['neighborhoods'], neighborhood)
    tamanio = al.size(catalog['neighbothoods'])
    return tamanio

def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
   def req_1(catalog,cantidad_de_pasajeros):
    """
    Retorna el resultado del requerimiento 1
    p es pomedio
    
    """
    dict = {"Tiempo_requerimiento_en_ms" : None,
        "Numero_total_de_trayectos_que_cumplen_el_filtro": None,
        "Tiempo_promedio_trayecto_p_min" : None,
        "Costo_total_trayecto_p_usd": None,
        "Millas_recorridas": None,
        "Costo_pagado_peajes_p": None,
        "Medio_de_pago_mas_usado-Costo":None,
        "Tip_p" : None,
        "Fecha_inicio_mayor_frecuencia":None
    }
    
    start_time = get_time() 
    
    es_verdad = al.new_list()
    for pos in catalog["Taxis"]:
        if pos["passanger_count"] == cantidad_de_pasajeros:
            al.add_last(es_verdad,pos)
            cant += 1
        dict["Numero_total_de_trayectos_que_cumplen_el_filtro"] = cant
            
    for pos in catalog["Taxis"]["pickup_datetime"]:
        t = []
        f = "HH:MM:SS"
        pickup_dt = time.strptime(pos["pickup_datetime"][:10])
        dropoff_dt = time.strptime(pos["dropoff_datetime"][:10])
        pickup_hora = time.strptime(pos["pickup_datetime"][10:],f)
        dropoff_hora = time.strptime(pos["pickup_datetime"][10:],f)
        
        if pickup_dt == dropoff_dt:
            duracion = dropoff_hora - pickup_hora
            t.append(duracion)
        else:
            duracion = (dropoff_dt - pickup_dt) + datetime.strptime("24:00:00",f) #pasar a formato datetime
            t.append(duracion)
            
        suma = 0
        size = al.size(es_verdad)
        for pos in t:
            suma += pos/size  
            horas_a_minutos = suma/60
        dict["Tiempo_promedio_trayecto_p_min"] = horas_a_minutos + datetime.strptime("MM") 
                    
    costo = 0
    for pos in float(es_verdad["Monto_total"]):
        costo += pos
    promedio = costo/size
    dict["Costo_total_trayecto_p_usd"] = promedio
    
    millas = 0
    for pos in float(es_verdad["Distancia_millas"]):
        millas += pos
    promedio = millas/size
    dict["Millas_recorridas"] = promedio
    
    peaje = 0
    for pos in float(es_verdad["peajes_costo"]):
        peaje += pos
    promedio = peaje / size
    dict["Costo_pagado_peajes_p"] = promedio
    
    metodo_pago = {}
    for pos in (es_verdad["tipo_de_pago_y_plata_pagada"]):
        if pos in metodo_pago:
            metodo_pago["metodos_de_pago_del_servicio"] +=1
        
        else:
            metodo_pago["metodos_de_pago_del_servicio"] = 1
        
        pago_mas_alto = 0
        for pos in metodo_pago:
            if metodo_pago[pos] > pago_mas_alto:
                pago_mas_alto = metodo_pago[pos]
                m = 0
                
    dict["Medio_de_pago_mas_usado-Costo"] = metodo_pago
    
    tip = 0
    for pos in es_verdad["propina_p"]:
        tip += pos
    promedio = tip/size
    dict["Tip_p"] = promedio      
                        
    fecha_inicio = {}
    for pos in es_verdad:
        if pickup_dt in fecha_inicio:
            fecha_inicio += 1
        else:
            fecha_inicio["pickup_dt"] = 1
        m = fecha_inicio[0]
        for pos in fecha_inicio:
            if m > fecha_inicio[pos]:
                m = fecha_inicio[pos]
            dict["Fecha_inicio_mayor_frecuencia"] = m
            
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    
    dict["Tiempo_requerimiento_en_ms"] = tiempo
                                    
    return dict

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
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog,fecha_inicial, fecha_final, filtro_costo):
    """
    Retorna el resultado del requerimiento 5
    p es promedio
    """
    dict = {"Tiempo_de_ejecucion_en_ms": None,
        "Filtro_costo": filtro_costo, 
        "Numero_total_de_trayectos_que_cumplieron":None,
        "Franaja_h": None,
        "Costo_p_en_franja_h":None, 
        "Trayectos_incluidos_en_franja_h": None,
        "Tiempo_p_franja_h":None,
        "Cantidad_pasajeros_franja_h": None,
        "Costo_total_menor_franja_h":None,
        "Costo_total_mayor_franja_h":None
    }
    start_time = get_time() 
    
    es_verdad = al.new_list()
    for pos in catalog["Taxis"]:
        if pos["total_amount"] == filtro_costo:
            al.add_last(es_verdad,pos)
    
    for pos in catalog["Taxis"]["pickup_datetime"]:
        f = "AAAA:MM:DD"
        pickup_dt = time.strptime(pos["pickup_datetime"][:10],f)
        dropoff_dt= time.strptime(pos["dropoff_datetime"][:10],f)
        pickup_hora = time.strptime(pos["pickup_datetime"][10:],f)
        dropoff_hora= time.strptime(pos["dropoff_datetime"][10:],f)
        
        fecha_final_h = time.strptime(fecha_final[10:])
        fecha_final_d = time.strptime(fecha_final[:10])
        fecha_inicial_h = time.strptime(fecha_inicial[10:])
        fecha_inicial_d = time.strptime(fecha_inicial[:10])
        
        if pickup_hora == fecha_inicial_h and dropoff_hora == fecha_final_h and pickup_dt == fecha_inicial_d and dropoff_dt == fecha_final_d:
        franja = str(pickup_hora + "-" + dropoff_hora)
        dict["Franaja_h"] = franja
        
        size = al.size(es_verdad)
        costo = []
        
        for pos in float(es_verdad["Monto_total"]):
            costo += pos
            promedio = costo/size
        dict ["Costo_p_en_franja_h"] = promedio
            
        for pos in catalog["Taxis"]:
            conteo = 0
            if pos["passanger_count"] != 0:
                conteo += pos["passanger_count"]
                promedio = conteo / size
            dict["Cantidad_pasajeros_franja_h"] = promedio
            
            
        costos= []
        for pos in float(es_verdad["Monto_total"]):
            costos.append(pos)
            costos.sort
            resp = costos[0]
            dict["Costo_total_menor_franja_h"] = resp
            
            resp2 = costos[size]
            dict["Costo_total_menor_franja_h"] = resp2
            
    cant = 0        
    if pickup_hora == fecha_inicial:
        for pos in es_verdad:
            if pos["Millas_recorridas"]:
                cant += 1
            dict["Trayrctos_incluidos_en_franja_h"] = cant
            
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    
    dict["Tiempo_de_ejecucion_en_ms"] = tiempo  
            
    return dict

def haversine (Lo1,La1,Lo2,La2):
    t1 = radians(Lo1)
    t2 = radians(La1)
    t3 = radians(Lo2)
    t4 = radians(La2)
    
    lof = t3 - t1
    laf = t2 - t4
    radio = 6371
    f = 2 * radio * asin(sqrt(sin((laf/2)**2 + cos(t2) + cos(t4) * sin(lof/2)**2)))
    return f 

def req_6(catalog,neighborhood,fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    dict = {"Tiempo_de_ejecucion_en_ms": None,
        "Numero_total_de_trayectos_que_cumplieron":None,
        "Distancia_p_trayectos_cumplen":None,
        "Tiempo_p_duracion":None,
        "Barrio_mas_visitado_punto_final":None,
        "Tipo_de_pago": None,
        "Cantidad_de_trayectos_con_ese_medio_de_pago":None,
        "Es_el_medio_mas_usado":None,
        "El_que_mas_recaudó":None,
        "Tiempo_promedio_de_los_trayectos":None
    }
    start_time = get_time() 
    
    es_verdad = al.new_list()
    dura = []
    size = al.size
    for pos in catalog["Taxis"]["pickup_datetime"]:
        f = "AAAA:MM:DD"
        f2 = "HH:MM:SS"
        pickup_dt = time.strptime(pos["pickup_datetime"][:10],f)
        dropoff_dt= time.strptime(pos["dropoff_datetime"][:10],f)
        pickup_hora = time.strptime(pos["pickup_datetime"][10:],f2)
        dropoff_hora= time.strptime(pos["dropoff_datetime"][10:],f2)
        
        fecha_final_h = time.strptime(fecha_final[10:])
        fecha_final_d = time.strptime(fecha_final[:10])
        fecha_inicial_h = time.strptime(fecha_inicial[10:])
        fecha_inicial_d = time.strptime(fecha_inicial[:10])
        
        if pickup_hora == fecha_inicial_h and dropoff_hora == fecha_final_h and pickup_dt == fecha_inicial_d and dropoff_dt == fecha_final_d:
            franja = str(pickup_hora + "-" + dropoff_hora)
            dura.append(franja)
            
            tiempos = []
            p = 0            
            if pickup_dt == dropoff_dt:
                duracion = dropoff_hora - pickup_hora
                tiempos.append(duracion)
            else:
                duracion = (dropoff_hora - pickup_hora) + datetime.strptime("24:00:00",f) #pasar a formato datetime
                tiempos.append(duracion)
                
            for pos in tiempos:
                p = tiempos[pos]
                promedio = p / size     
            
        cant = 0        
    if pickup_hora == fecha_inicial:
        for pos in es_verdad:
            cant = 0
            if pos["Millas_recorridas"]:
                cant += 1
            dict["Numero_total_de_trayectos_que_cumplieron"] = cant
            al.add_last(es_verdad,pos)   
            
    list = []
    
    if fecha_final_h in dura and fecha_inicial_h in dura:
        lo1 = float(pos["pickup_longitude"])
        la1 = float(pos["pickup_latitude"])
        lo2 = float(pos["dropoff_longitude"])
        la2 = float(pos["dropoff_latitude"])
        distancia = haversine(lo1, la1, lo2, la2)
        list.append(distancia)
        p = 0
        promedio = 0
        
        for pos in list:
            p += pos
            promedio = p / size
            dict["Distancia_p_trayectos_cumplen"] = promedio
            
    barrios = catalog['neighborhoods']
    size = al.size(barrios)
    i = 0
    mejor_barrio = None
    mejor_distancia = None
    while i < size:
        elem = al.get_element(barrios, i)
        lat_b = float(elem["latitude"])
        lon_b = float(elem["longitude"])
        distancia = haversine(lat_dropoff, lon_dropoff, lat_b, lon_b)
        if mejor_distancia is None:
            mejor_distancia = distancia
            mejor_barrio = elem["neighborhood"]
        else:
            if distancia < mejor_distancia:
                mejor_distancia = distancia
                mb = elem["neighborhood"]
        i += 1
        dict ["Barrio_mas_visitado_punto_final"] = mb
    
    metodo_pago = {}
    for pos in es_verdad["tipo_de_pago_y_plata_pagada"]:
        if pos in metodo_pago:
             metodo_pago["metodos_de_pago_del_servicio"] += 1
        else:
             metodo_pago["metodos_de_pago_del_servicio"] = 1
    
    dict["Tipo_de_pago"] = metodo_pago
    
    conteo_pagos = {}
    size_taxis = al.size(catalog["Taxis"])
    
    for i in range(size_taxis):
        pos = al.get_element(catalog["Taxis"], i) 

        medio = catalog["Taxis"]["payment_type"]
        
        if medio:
            if medio not in conteo_pagos:
                conteo_pagos[medio] = 0
    
            conteo_pagos[medio] += 1
    dict["Cantidad_de_trayectos_con_ese_medio_de_pago"] = conteo_pagos
    
    conteo_pagos = {}
    size_taxis = al.size(catalog["Taxis"])
    
    for i in range(size_taxis):
        pos = al.get_element(catalog["Taxis"], i) 
        
        medio_actual = pos["payment_type"] 
        
        if medio_actual:
            if medio_actual not in conteo_pagos:
                conteo_pagos[medio_actual] = 0
            
            conteo_pagos[medio_actual] += 1
        dict["Es_el_medio_mas_usado"] = conteo_pagos
        
    for pos in es_verdad:
        payment_type = catalog["Taxis"]["payment_type"][pos]
        total_amount = catalog["Taxis"]["total_amount"][pos]
        
        if payment_type and total_amount is not None:
            try:
                amount = float(total_amount)
            except ValueError:
                continue 
            
            if payment_type in recaudacion_por_pago:
                recaudacion_por_pago[payment_type] += amount
            else:
                recaudacion_por_pago[payment_type] = amount
    
    medio_mas_recaudo = None
    max_recaudacion = -1
    
    for medio, recaudacion in recaudacion_por_pago.items():
        if recaudacion > max_recaudacion:
            max_recaudacion = recaudacion
            medio_mas_recaudo = medio
            
    dict["El_que_mas_recaudó"] = medio_mas_recaudo
    
    suma_tiempos = sum(tiempos) 
    num_trayectos = al.size(es_verdad)
    
    tiempo_promedio = None
    if num_trayectos > 0:
        tiempo_promedio = suma_tiempos / num_trayectos
        
    dict["Tiempo_promedio_de_los_trayectos"] = tiempo_promedio

    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
     
    dict["Tiempo_de_ejecucion_en_ms"] = tiempo   
    
    return dict


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
