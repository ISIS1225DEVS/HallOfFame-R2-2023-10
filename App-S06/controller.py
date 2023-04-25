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
    
def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def mega_load(control,memory,tamanio):
    """
    Carga los datos del reto
    """
    time_memory = start_gathering_data(memory)  
      
    data_structs = control['model']
    dianfiles = cf.data_dir + f'DIAN/Salida_agregados_renta_juridicos_AG-{tamanio}.csv'
    input_file = csv.DictReader(open(dianfiles, encoding='utf-8'))  
    
    for data in input_file:
        model.add_todo(data_structs, data['Año'], data)
        
    size = model.sort_all_info(control["model"])
    answer = (data_structs,size)
    return stop_gathering_data(answer,memory,time_memory[0],time_memory[1])
    
def req_1(control,anio,sector,memory):
    """
    Retorna el resultado del requerimiento 1
    """
    time_memory = start_gathering_data(memory)  
    return stop_gathering_data(model.req_1(control["model"],anio, sector), memory ,time_memory[0],time_memory[1])
    

def req_2(control,anio,sector,memory):
    """
    Retorna el resultado del requerimiento 2
    """
    time_memory = start_gathering_data(memory)  
    return stop_gathering_data(model.req_1(control["model"],anio, sector), memory ,time_memory[0],time_memory[1])

def req_3(control,anio,memory):
    """
    Retorna el resultado del requerimiento 3
    """
    time_memory = start_gathering_data(memory)  
    return stop_gathering_data(model.req_3(control["model"],anio), memory ,time_memory[0],time_memory[1])


def req_4(control,anio,memory):
    """
    Retorna el resultado del requerimiento 4
    """
    time_memory = start_gathering_data(memory)  
    return stop_gathering_data(model.req_4(control["model"],anio), memory ,time_memory[0],time_memory[1])


def req_5(control,anio,memory):
    """
    Retorna el resultado del requerimiento 5
    """
    time_memory = start_gathering_data(memory)  
    return stop_gathering_data(model.req_5(control["model"],anio), memory ,time_memory[0],time_memory[1])

def req_6(control,anio,memory):
    """
    Retorna el resultado del requerimiento 6
    """
    time_memory = start_gathering_data(memory)  
    return stop_gathering_data(model.req_6(control["model"],anio), memory ,time_memory[0],time_memory[1])


def req_7(control,anio,subsector,top,memory):
    """
    Retorna el resultado del requerimiento 7
    """
    time_memory = start_gathering_data(memory)  
    return stop_gathering_data(model.req_7(control["model"],anio,subsector,top), memory ,time_memory[0],time_memory[1])


def req_8(control,top,anio,memory):
    """
    Retorna el resultado del requerimiento 8
    """
    time_memory = start_gathering_data(memory)
    return stop_gathering_data(model.req_8(control["model"],top,anio), memory ,time_memory[0],time_memory[1])

def get_value(hash,key):
    return model.get_value(hash,key)

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

""" 
FUNCIONES GENERALES PARA RECOLECTAR TIEMPO Y MEMORIA
"""

def start_gathering_data(memory):
    
    start_time = get_time()
    start_memory = None
    
    if memory == True:
        tracemalloc.start()
        start_memory = get_memory()
        
    return start_time,start_memory

def stop_gathering_data(answer,memory,start_time,start_memory):
    
    stop_time = get_time()
    deltaTime = delta_time(start_time,stop_time)
    
    if memory == True:
        stop_memory = get_memory()
        tracemalloc.stop()
        deltaMemory = delta_memory(stop_memory, start_memory)
        
        return answer, deltaTime, deltaMemory
    
    return answer, deltaTime
