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



