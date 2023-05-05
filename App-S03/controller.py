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

def new_controller(decision, decision_factcarg):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    
    control = {
         'model': None}
    
    control['model'] = model.new_data_structs(decision, decision_factcarg)
    return control 

# Funciones para la carga de datos
def load_data(control, filename, memflag = True):
    """
    Carga los datos del reto, se cargan todos los impuestos
    """
    # TODO COMPLETADO: Realizar la carga de datos
    start_tiempo = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    impuestosfile = cf.data_dir + filename
    input_file = csv.DictReader(open(impuestosfile, encoding='utf-8'))
    for impuesto in input_file:
        model.add_impuesto(control['model'], impuesto)
    
    stop_tiempo = get_time()
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()

        # calcula la diferencia de memoria
        delta_memoria = delta_memory(stop_memory, start_memory)
        delta_tiempo = delta_time(start_tiempo, stop_tiempo)
        return delta_tiempo, delta_memoria
    else:
        delta_tiempo = delta_time(start_tiempo, stop_tiempo)
        return delta_tiempo

def map_size(control):
    " retorna la cantidad de años cargados en el datastructs"
    return model.data_size(control['model'])
# Funciones de ordenamiento
def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass

# Funciones de consulta sobre el catálogo
def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def data_size_lista(control):
    """
    Retorna el tamaño de una lista
    """
    size = model.data_size_lista(control)
    return size

def req_1(control, anio, cse):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
    req_1 = model.req_1(control["model"], anio, cse)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return req_1, delta_t

def req_2(control, year, codigo):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_t = get_time()
    final, headers = model.req_2(control['model'], year, codigo)
    end_t = get_time()
    delta_t = delta_time(start_t, end_t)
    return final, headers, delta_t

def req_3(control, anio):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    req_3 = model.req_3(control["model"], anio)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_3, delta_t

def req_4(control, anio):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
    req_4 = model.req_4(control["model"],int(anio))
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
    return req_4,delta_t

def req_5(control, year):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_t = get_time()
    final, headz_1, mayndmen, headz_2 = model.req_5(control['model'], year)
    end_t = get_time()
    delta_t= delta_time(start_t, end_t)
    return final, headz_1, mayndmen, headz_2, delta_t

def req_6(control,anio):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()
    req_6 = model.req_6(control["model"],anio)
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
    return req_6, delta_t

def req_7(control, top, anio, csse):
    """
    Retorna el resultado del requerimiento 7
    """
    start_time = get_time()
    req_7 = model.req_7(control["model"], top, anio, csse)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_7, delta_t

def req_8(control, top, year):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_t = get_time()
    dict_sumas, final_final = model.req_8(control['model'], top, year)
    end_t = get_time()
    delta_t = delta_time(start_t, end_t)

    return dict_sumas, final_final, delta_t
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
