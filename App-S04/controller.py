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


def new_controller(struct_list,struct_map,load_factor):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(struct_list,struct_map,load_factor)
    return control


# Funciones para la carga de datos

def load_data(control, filename,memflag):
    """
    Carga los datos del reto
    """
    #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    #ejecucion principal
    catalog=control["model"]
    
    numero_registros=load_registers_dian(catalog,filename)
    
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return (numero_registros,delta_time_value, delta_memory_value)
    else:
        # respuesta sin medir memoria
        return (numero_registros,delta_time_value)
    
def load_registers_dian(catalog,filename):
    dian_file=cf.data_dir+filename
    input_file=csv.DictReader(open(dian_file,encoding="utf-8"),delimiter=",")
    for registro in input_file:
        model.add_data(catalog,registro)
    return model.data_size(catalog)


# Funciones de ordenamiento

def sort(control,metodo):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    model.sort(control["model"],metodo)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data

def get_primeros(control,anio):
    primeros=model.get_first_registros(control["model"],anio)
    return primeros

def get_ultimos(control,anio):
    ultimos=model.get_last_registros(control["model"],anio)
    return ultimos


def req_1(control,anio,sector,memflag):
    """
    Retorna el resultado del requerimiento 1
    """
     #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    #Ejecucion principal
    actividad=model.req_1(control["model"],anio,sector)
    
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        
        return (actividad,delta_time_value, delta_memory_value) 
    else:
        # respuesta sin medir memoria
        return (actividad,delta_time_value)

def req_2(control,anio,sector,memflag):
    """
    Retorna el resultado del requerimiento 2
    """
    #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    #Ejecucion principal
    actividad=model.req_2(control["model"],anio,sector)
    
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        
        return (actividad,delta_time_value, delta_memory_value) 
    else:
        # respuesta sin medir memoria
        return (actividad,delta_time_value)


def req_3(control,anio,memflag):
    """
    Retorna el resultado del requerimiento 3
    """
    #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    #Ejecucion principal
    tuple_dict_list=model.req_3(control["model"],anio)
    subsector=tuple_dict_list[0]
    list_activities=tuple_dict_list[1]
    
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        
        return (subsector,list_activities,delta_time_value, delta_memory_value) 
    else:
        # respuesta sin medir memoria
        return (subsector,list_activities,delta_time_value)
    


def req_4(control, anio, memflag):
    """
    Retorna el resultado del requerimiento 4
    """
    #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    #Ejecucion principal
    tuple_dict_list=model.req_4(control["model"],anio)
    subsector=tuple_dict_list[0]
    list_activities=tuple_dict_list[1]
    
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        
        return (subsector,list_activities,delta_time_value, delta_memory_value) 
    else:
        # respuesta sin medir memoria
        return (subsector,list_activities,delta_time_value)
    # TODO: Modificar el requerimiento 4
    


def req_5(control,anio,memflag):
    """
    Retorna el resultado del requerimiento 5
    """
    #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    #Ejecucion principal
    tuple_dict_list=model.req_5(control["model"],anio)
    subsector=tuple_dict_list[0]
    list_activities=tuple_dict_list[1]
    
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        
        return (subsector,list_activities,delta_time_value, delta_memory_value) 
    else:
        # respuesta sin medir memoria
        return (subsector,list_activities,delta_time_value)

def req_6(control,anio,memflag):
    """
    Retorna el resultado del requerimiento 6
    """
     #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    #Ejecucion principal
    tuple_info=model.req_6(control["model"],anio)
    sector=tuple_info[0]
    subsector_most=tuple_info[1]
    subsector_less=tuple_info[2]
    actividad_mas_aporto_1=tuple_info[3]
    actividad_menos_aporto_1=tuple_info[4]
    actividad_mas_aporto_2=tuple_info[5]
    actividad_menos_aporto_2=tuple_info[6]
    
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        
        return (sector,subsector_most,subsector_less,actividad_mas_aporto_1,actividad_menos_aporto_1,actividad_mas_aporto_2,actividad_menos_aporto_2,delta_time_value, delta_memory_value) 
    else:
        # respuesta sin medir memoria
        return (sector,subsector_most,subsector_less,actividad_mas_aporto_1,actividad_menos_aporto_1,actividad_mas_aporto_2,actividad_menos_aporto_2,delta_time_value)

def req_7(control,anio,subsector,n,memflag):
    """
    Retorna el resultado del requerimiento 7
    """
     #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    #Ejecucion principal
    list_activities=model.req_7(control["model"],anio,subsector,n)
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        return (list_activities,delta_time_value,delta_memory_value)
    else:
        return (list_activities,delta_time_value)
        


def req_8(control,anio,top,memflag):
    """
    Retorna el resultado del requerimiento 8
    """
    #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    #Ejecucion principal
    tuple_dict_list=model.req_8(control["model"],anio,top)
    list_subsector=tuple_dict_list[0]
    map_activities=tuple_dict_list[1]
    
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        
        return (list_subsector,map_activities,delta_time_value, delta_memory_value) 
    else:
        # respuesta sin medir memoria
        return (list_subsector,map_activities,delta_time_value)


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
