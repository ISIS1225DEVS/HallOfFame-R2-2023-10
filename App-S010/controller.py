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

#Creación controller

def new_controller():
    control={"model":None}
    control["model"]= model.new_data_structs()
    return control

# Funciones para la carga de datos

def load_data(control, filename, memflag=True):
    """
    Carga los datos del reto
    """
    start_time=get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
    
    file=csv.DictReader(open(filename, encoding="utf-8"))
    for negocio in file:
        model.add_data(control["model"], negocio)
    listaaimprimir=model.primerosyultimos(control["model"])   
    stop_time=get_time()
    tiempo= delta_time(start_time, stop_time)
    
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        
        return tiempo, memory, listaaimprimir
    else:
        
        
        return tiempo, listaaimprimir
    # TODO: Realizar la carga de datos
    pass

# Funciones Requerimientos (controller)

def req_1(control,año,codigose,memflag=True):
    start_time=get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
    req1=model.req_1(control["model"],año,codigose)
    end_time=get_time()
    tiempo=delta_time(start_time,end_time)
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        return req1,tiempo,memory
    else:
        return req1, tiempo

def req_2(control,año,codigose,memflag=True):
    start_time=get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
    req2=model.req_2(control["model"],año,codigose)
    end_time=get_time()
    tiempo=delta_time(start_time,end_time)
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        return req2,tiempo,memory
    else:
        return req2, tiempo

def req_3(control,año,memflag=True):
    start_time=get_time()
    
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
        
    req3=model.req_3(control["model"],año)
    end_time=get_time()
    tiempo=delta_time(start_time,end_time)
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        
        return req3, tiempo,memory
    else: 
        return req3, tiempo

def req_4(control,año,memflag=True):
    start_time=get_time()
    
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
        
    req4=model.req_4(control["model"],año)
    end_time=get_time()
    tiempo=delta_time(start_time,end_time)
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        
        return req4, tiempo,memory
    else: 
        return req4, tiempo
    # TODO: Modificar el requerimiento 4
    
def req_5(control,año, memflag=True):
    start_time=get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory=get_memory()
    req=model.req_5(control["model"],año)
    end_time=get_time()
    tiempo=delta_time(start_time,end_time)
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory=delta_memory(stop_memory, start_memory)
        return req, tiempo, memory
    else:
        return req,tiempo

def req_6(control,año,memflag=True):
    start_time=get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
    req6=model.req_6(control["model"],año)
    end_time=get_time()
    tiempo=delta_time(start_time,end_time)
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        return req6,tiempo,memory
    else:
        return req6, tiempo

def req_7(control,año,codigose,Topn,memflag=True):
    start_time=get_time()
    
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
    req7=model.req_7(control["model"],año,codigose,Topn) 
    end_time=get_time()
    tiempo=delta_time(start_time,end_time)   
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        return req7,tiempo,memory
    else:
        return req7,tiempo

def req_8(control,año,Topn,memflag=True):
    start_time=get_time()
    
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
    req8=model.req_8(control["model"],año,Topn) 
    end_time=get_time()
    tiempo=delta_time(start_time,end_time)   
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        return req8,tiempo,memory
    else:
        return req8,tiempo

# Funciones para medir tiempos de ejecucion

def get_time():
    return float(time.perf_counter()*1000)

def delta_time(start, end):
    elapsed = float(end - start)
    return elapsed

def get_memory():
    return tracemalloc.take_snapshot()

def delta_memory(stop_memory, start_memory):
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
