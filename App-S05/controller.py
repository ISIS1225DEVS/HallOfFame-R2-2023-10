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


def new_controller(n,a,al):
    """
    Crea una instancia del modelo
    """
   
    maptype = ''
    filesize = ''
    loadFactor = al
    
    
    if n == 1:
        maptype = 'PROBING'
        
    elif n == 2:
        maptype = 'CHAINING'
    if a == 1:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-5pct.csv'
    if a == 2:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-10pct.csv'    
    if a == 3:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-20pct.csv'
    if a == 4:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-30pct.csv'
    if a == 5:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-50pct.csv'
    if a == 6:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-80pct.csv'
    if a == 7:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-large.csv'
    if a == 8:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-small.csv'
        
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(maptype, loadFactor)

    return control, filesize


# Funciones para la carga de datos

def load_data(control, filename,memflag):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    # toma el tiempo al inicio del proceso
    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    r = loadDatos(data_structs, filename)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return r, delta_time, delta_memory

    else:
        # respuesta sin medir memoria
        return r, delta_time   

def loadDatos(data_structs, filename):
    id = 0
    tagsfile = cf.data_dir + filename
    print("----ARCHIVO CARGADO------\n")
    print(tagsfile)
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for registro in input_file:
        model.add_register(data_structs, registro)
        id += 1

    return data_structs 

#Esta funcion es la que permite recortar las listas de forma linda

def recortarLista(list):
    return model.recortarLista(list)

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


def req_1(control, memflag, yearIn, codeIn):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    # toma el tiempo al inicio del proceso
    
    year = 0
    code = 0
    if yearIn == 1:
        
        year = 2012
    if yearIn == 2:
        
        year = 2013
    if yearIn == 3:
        
        year = 2014
    if yearIn == 4:
        
        year = 2015
    if yearIn == 5:
        
        year = 2016
    if yearIn == 6:
        
        year = 2017
    if yearIn == 7:
        
        year = 2018
    if yearIn == 8:
        
        year = 2019
    if yearIn == 9:
        
        year = 2020
    if yearIn == 10:
        
        year = 2021


    if codeIn == 0:
        code = 0
    if codeIn == 1:
        code = 1
    if codeIn == 2:
        code = 2
    if codeIn == 3:
        code = 3
    if codeIn == 4:
        code = 4
    if codeIn == 5:
        code = 5
    if codeIn == 6:
        code = 6
    if codeIn == 7:
        code = 7
    if codeIn == 8:
        code = 8
    if codeIn == 9:
        code = 9
    if codeIn == 10:
        code = 10
    if codeIn == 11:
        code = 11
        
    
    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    req1 = model.req_1(data_structs, year, code)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return req1, delta_time, delta_memory

    else:
        # respuesta sin medir memoria
        return req1, delta_time

def req_2(control, memflag, yearIn, codeIn):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 2
    # toma el tiempo al inicio del proceso
    
    year = 0
    code = 0
    if yearIn == 1:
        
        year = 2012
    if yearIn == 2:
        
        year = 2013
    if yearIn == 3:
        
        year = 2014
    if yearIn == 4:
        
        year = 2015
    if yearIn == 5:
        
        year = 2016
    if yearIn == 6:
        
        year = 2017
    if yearIn == 7:
        
        year = 2018
    if yearIn == 8:
        
        year = 2019
    if yearIn == 9:
        
        year = 2020
    if yearIn == 10:
        
        year = 2021


    if codeIn == 0:
        code = 0
    if codeIn == 1:
        code = 1
    if codeIn == 2:
        code = 2
    if codeIn == 3:
        code = 3
    if codeIn == 4:
        code = 4
    if codeIn == 5:
        code = 5
    if codeIn == 6:
        code = 6
    if codeIn == 7:
        code = 7
    if codeIn == 8:
        code = 8
    if codeIn == 9:
        code = 9
    if codeIn == 10:
        code = 10
    if codeIn == 11:
        code = 11
        
    
    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    req2 = model.req_2(data_structs, year, code)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return req2, delta_time, delta_memory

    else:
        # respuesta sin medir memoria
        return req2, delta_time

def req_3(control, memflag, yearIn, headers):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    


    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    req3 = model.req_3(data_structs, yearIn, headers)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return req3, delta_time, delta_memory

    else:
        # respuesta sin medir memoria
        return req3, delta_time


def req_4(control,anio,headers,memflag):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
        # toma el tiempo al inicio del proceso
    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    r = model.req_4(data_structs, anio,headers)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return r[0], delta_time, delta_memory,r[1],r[2],r[3]
    else:
        # respuesta sin medir memoria
        return r[0], delta_time,r[1],r[2],r[3]


def req_5(control,anio,headers,memflag):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
        # toma el tiempo al inicio del proceso
    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    r = model.req_5(data_structs, anio,headers)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return r[0], delta_time, delta_memory,r[1],r[2],r[3]
    else:
        # respuesta sin medir memoria
        return r[0], delta_time,r[1],r[2],r[3]

def req_6(control,anio,headers,headers2, memflag):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 6
        # toma el tiempo al inicio del proceso
    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    r = model.req_6(data_structs, anio,headers,headers2)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return r[0], delta_time, delta_memory,r[1],r[2]
    else:
        # respuesta sin medir memoria
        return r[0], delta_time,r[1],r[2]



def req_7(control,SS, anio,top, memflag):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7

    # toma el tiempo al inicio del proceso
    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    r = model.req_7(data_structs, SS, anio,top)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return r[0], delta_time, delta_memory, r[1]

    else:
        # respuesta sin medir memoria
        return r[0], delta_time, r[1]



def req_8(control,anio,headers,TOP, memflag):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
            # toma el tiempo al inicio del proceso
    start_time = getTime()
    data_structs = control['model'] 
    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    r = model.req_8(data_structs, anio,headers,TOP)
     # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return r[0], delta_time, delta_memory,r[1],r[2],r[3]
    else:
        # respuesta sin medir memoria
        return r[0], delta_time,r[1],r[2],r[3]

#ordenamientos un view
def useMerge(lista, F):
    return model.useMerge(lista,F)

# Funciones para medir tiempos de ejecucion


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
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