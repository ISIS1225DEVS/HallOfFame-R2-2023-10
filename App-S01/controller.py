"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(data_type):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }

    control["model"] = model.new_data_structs(data_type)
    return control 

def load_data(control, memflag = True):
    """
    Carga los datos del reto
    """
    # toma el tiempo al inicio del proceso
    start_time = get_time()
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    # ejecutando funcion a medir
    filename = cf.data_dir + 'Salida_agregados_renta_juridicos_AG-large.csv'
    input_file = csv.DictReader(open(filename, encoding = 'utf-8'))

    for carga in input_file:
        datos = model.add_data(control["model"], carga)
 
    model.sortDataMap(datos["data"])
    # toma el tiempo al final del proceso
    stop_time = get_time()
    # calculando la diferencia en tiempo
    deltaTime = delta_time(start_time, stop_time)
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return datos["data"], deltaTime, deltaMemory
    else:
        # respuesta sin medir memoria
        return datos["data"], deltaTime

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
   
    return model.sorted_map_cod(control['model'])




# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data


def req_1(control, anio, cod):
    """
    Retorna el resultado del requerimiento 1
    """
    dato = model.req_1(control, anio, cod)

    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    
    model.req_1(control, anio, cod)
    
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    stop_memory = get_memory()
    tracemalloc.stop()       
    deltaMemory = delta_memory(stop_memory, start_memory)

    answer = (delta_t, deltaMemory)
    return dato, answer


def req_2(control, anio, cod):
    """
    Retorna el resultado del requerimiento 2
    """
    dato = model.req_2(control, anio, cod)
    
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    
    model.req_2(control, anio, cod)
    
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    stop_memory = get_memory()
    tracemalloc.stop()       
    deltaMemory = delta_memory(stop_memory, start_memory)

    answer = (delta_t, deltaMemory)
    return dato, answer


def req_3(control, anio):
    """
    Retorna el resultado del requerimiento 3
    """
    dato, table = model.req_3(control, anio)
    
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    
    model.req_3(control, anio)
    
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    stop_memory = get_memory()
    tracemalloc.stop()       
    deltaMemory = delta_memory(stop_memory, start_memory)

    answer = (delta_t, deltaMemory)
    return dato, table, answer


def req_4(control, anio):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    lista_max, table = model.req_4(control,anio)
    
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    
    model.req_4(control, anio)
    
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    stop_memory = get_memory()
    tracemalloc.stop()       
    deltaMemory = delta_memory(stop_memory, start_memory)

    answer = (delta_t, deltaMemory)
    return lista_max, table, answer


def req_5(control, anio):
    """
    Retorna el resultado del requerimiento 5
    """
    requi = model.req_5(control, anio)
    
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    
    model.req_5(control, anio)
    
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    stop_memory = get_memory()
    tracemalloc.stop()       
    deltaMemory = delta_memory(stop_memory, start_memory)

    answer = (delta_t, deltaMemory)
    return requi, answer

def req_6(control, anio):
    """
    Retorna el resultado del requerimiento 6
    """
    max_sec, sub, max_act, min_act = model.req_6(control, anio)
    
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    
    model.req_6(control, anio)
    
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    stop_memory = get_memory()
    tracemalloc.stop()       
    deltaMemory = delta_memory(stop_memory, start_memory)

    answer = (delta_t, deltaMemory)
    return max_sec, sub, max_act, min_act, answer



def req_7(control,anio,n,cod):
    """
    Retorna el resultado del requerimiento 7
    """
    table, answer = model.req_7(control,anio,n,cod)
    
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    
    model.req_7(control,anio,n,cod)
    
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    stop_memory = get_memory()
    tracemalloc.stop()       
    deltaMemory = delta_memory(stop_memory, start_memory)

    a = (delta_t, deltaMemory)
    return table, answer, a


def req_8(control,anio,n):
    """
    Retorna el resultado del requerimiento 8
    """
    lista1, lista2 = model.req_8(control,anio,n)
    
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    
    model.req_8(control,anio,n)
    
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    stop_memory = get_memory()
    tracemalloc.stop()       
    deltaMemory = delta_memory(stop_memory, start_memory)
    
    answer = (delta_t, deltaMemory)
    return lista1, lista2, answer


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

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
