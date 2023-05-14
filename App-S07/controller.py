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

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(ds, lf, n):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(ds, lf, n)
    return control


# Funciones para la carga de datos

def load_data(control, filename, orderingAlg, membool):
    """
    Carga los datos del reto
    """
    catalog = control['model']
    
    start_time = get_time()
    if membool == True:
        tracemalloc.start()
        start_memory = get_memory()
    
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for column in input_file:
        model.add_data(catalog['data'], column, orderingAlg)
      
    finish_time = get_time()
    deltatime = delta_time(start_time, finish_time)
    if membool == True:
        finish_memory = get_memory()
        tracemalloc.stop()
        deltamem = delta_memory(finish_memory, start_memory)
        return control, deltatime, deltamem 
    else:
        return control, deltatime


def selectPercentage(dataPercentage):
    """
    Retorna el sufijo del archivo al cuál se dese acceder

    Args:
        dataPercentage (str): Número seleccionado por consola para el porcentaje de datos

    Returns:
        str: Sufijo del archivo en cuestión
    """
    suffixes = {'1':'small', '2':'5pct', '3':'10pct', '4':'20pct',
                '5':'30pct', '6':'50pct', '7':'80pct', '8':'large'}
    return suffixes[dataPercentage]


# Funciones de ordenamiento

def sort(control, orderingAlg):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    model.sort(control["model"], orderingAlg)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t


# Funciones de consulta sobre el catálogo

def memoryStart():
    """
    Inicia la toma de memoria
    """
    tracemalloc.start()
    start = get_memory()
    return start


def memoryEnd():
    """
    Termina la toma de memoria
    """
    end = get_memory()
    tracemalloc.stop()
    return end


def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    return model.get_data(control, id)


def req_1(control, year, id):
    """
    Retorna el resultado del requerimiento 1
    """
    start = get_time()
    req_1 = model.req_1(control["model"], year, id)
    end = get_time()
    delta = delta_time(start, end)
    return req_1, delta


def req_2(control, year, id):
    """
    Retorna el resultado del requerimiento 2
    """
    start = get_time()
    req_2 = model.req_2(control["model"], year, id)
    end = get_time()
    delta = delta_time(start, end)
    return req_2, delta


def req_3(control, year):
    """
    Retorna el resultado del requerimiento 3
    """
    start = get_time()
    req_3 = model.req_3(control["model"], year)
    end = get_time()
    delta = delta_time(start, end)
    return req_3, delta


def req_4(control, year):
    """
    Retorna el resultado del requerimiento 4
    """
    start = get_time()
    req_4 = model.req_4(control["model"], year)
    end = get_time()
    delta = delta_time(start, end)
    return req_4, delta


def req_5(control, year):
    """
    Retorna el resultado del requerimiento 5
    """
    start = get_time()
    req_5 = model.req_5(control["model"], year)
    end = get_time()
    delta = delta_time(start, end)
    return req_5, delta


def req_6(control, year):
    """
    Retorna el resultado del requerimiento 6
    """
    start = get_time()
    req_6 = model.req_6(control["model"], year)
    end = get_time()
    delta = delta_time(start, end)
    return req_6, delta


def req_7(control, year, id):
    """
    Retorna el resultado del requerimiento 7
    """
    start = get_time()
    req_7 = model.req_7(control["model"], year, id)
    end = get_time()
    delta = delta_time(start, end)
    return req_7, delta


def req_8(control, year):
    """
    Retorna el resultado del requerimiento 8
    """
    start = get_time()
    req_8 = model.req_8(control["model"], year)
    end = get_time()
    delta = delta_time(start, end)
    return req_8, delta


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
