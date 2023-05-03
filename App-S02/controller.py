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
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(map_type,factorCharge):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_catalog(map_type,factorCharge)
    return control


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    data = csv.DictReader(open(filename, encoding='utf-8'))
    model.load_data(control['model'], data)

#Imprimir el resumen de cada año

def printYearsResume(control):
    return model.printYearsResume(control['model'])
# Funciones de ordenamiento

def req_1(control, year, sector):
    """
    Retorna el resultado del requerimiento 1
    """
    #? Tiempos de ejecución
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    # TODO: Modificar el requerimiento 1
    response = model.req_1(control["model"], year, sector)
    #? Tiempos de ejecución
    stop_time = get_time()
    delta_times = delta_time(start_time,stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
    delta_memories = delta_memory(stop_memory, start_memory)
    return response, delta_times, delta_memories


def req_2(control, year, sector):
    """
    Retorna el resultado del requerimiento 2
    """
    #? Tiempos de ejecución
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    # TODO: Modificar el requerimiento 2
    response = model.req_2(control["model"], year, sector)
    #? Tiempos de ejecución
    stop_time = get_time()
    delta_times = delta_time(start_time,stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
    delta_memories = delta_memory(stop_memory, start_memory)
    return response, delta_times, delta_memories


def req_3(control, year):
    """
    Retorna el resultado del requerimiento 3
    """
    #? Tiempos de ejecución
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    # TODO: Modificar el requerimiento 3
    response = model.req_3(control["model"], year)
    #? Tiempos de ejecución
    stop_time = get_time()
    delta_times = delta_time(start_time,stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
    delta_memories = delta_memory(stop_memory, start_memory)
    return response, delta_times, delta_memories


def req_4(control, year):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    #? Tiempos de ejecución
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    # TODO: Modificar el requerimiento 3
    response = model.req_4(control["model"], year)
    #? Tiempos de ejecución
    stop_time = get_time()
    delta_times = delta_time(start_time,stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
    delta_memories = delta_memory(stop_memory, start_memory)
    return response, delta_times, delta_memories


def req_5(control, year):
    """
    Retorna el resultado del requerimiento 5
    """
    
    #? Tiempos de ejecución
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    # TODO: Modificar el requerimiento 5
    response = model.req_5(control["model"], year)
     #? Tiempos de ejecución
    stop_time = get_time()
    delta_times = delta_time(start_time,stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
    delta_memories = delta_memory(stop_memory, start_memory)
    return response, delta_times, delta_memories


def req_6(control, year):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    #? Tiempos de ejecución
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    # TODO: Modificar el requerimiento 3
    response, menor = model.req_6(control["model"], year)
    #? Tiempos de ejecución
    stop_time = get_time()
    delta_times = delta_time(start_time,stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
    delta_memories = delta_memory(stop_memory, start_memory)
    return response, menor, delta_times, delta_memories


def req_7(control, top, year, subsector):
    """
    Retorna el resultado del requerimiento 7
    """
   
    #? Tiempos de ejecución
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    # TODO: Modificar el requerimiento 7
    response = model.req_7(control["model"], top, year, subsector)
    #? Tiempos de ejecución
    stop_time = get_time()
    delta_times = delta_time(start_time,stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
    delta_memories = delta_memory(stop_memory, start_memory)
    return response, delta_times, delta_memories


def req_8(control, year):
    """
    Retorna el resultado del requerimiento 8
    """
    #? Tiempos de ejecución
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()
    # TODO: Modificar el requerimiento 8
    sorted_list, response, keys_sorted = model.req_8(control["model"], year)
    #? Tiempos de ejecución
    stop_time = get_time()
    delta_times = delta_time(start_time,stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
    delta_memories = delta_memory(stop_memory, start_memory)
    return sorted_list, response, keys_sorted, delta_times, delta_memories

def sortYears(years):
    return model.sortYears(years)

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


csv.field_size_limit(2147483647)