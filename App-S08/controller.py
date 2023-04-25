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
from time import sleep
from types import FunctionType
import model
import tracemalloc
from timeit import default_timer as timer
from datetime import datetime
import datetime as datetime
import csv
from time import sleep
import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# OPTIMIZE: Decorador Tiempos de Memoria
# ADD : Decorador Tiempos de Memoria

castBoolean=lambda x: True if x in ('True', 'true', 'TRUE', 'T', 't', '1', "Si", "SI", "Sí", "si", "Yes, YES") else False

def deltaMemory(stop_memory:tracemalloc.Snapshot, start_memory:tracemalloc.Snapshot)->float:
    """Devuelve la diferencia en memoria en KB entre dos Snapshots
    ---------------------------------------------------------------------
    Args:
        start_memory: Snapshot inicial
        stop_memory: Snapshot final
    ---------------------------------------------------------------------
    Return:
        Diferencia de uso de memoria en KB"""
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    delta_memory = delta_memory/1024.0
    return delta_memory

def printLoadDataAnswer(answer:...)->str:
    """Valida y retorna los tiempos y/o memoria
    ---------------------------------------------------------------------
    Args:
        answer: información con los tiempos y/o memoria
    ---------------------------------------------------------------------
    Return:
        String con el tiempo y/o memoria de ejecución"""
    if isinstance(answer, (list, tuple)) is True:
        return("Tiempo [ms]: "+ f"{answer[0]:.3f}"+ "||"+
            "Memoria [kB]: "+ f"{answer[1]:.3f}")
    else:
        return("Tiempo [ms]: "+ f"{answer:.3f}")


def timer_y_mem(func:FunctionType)->tuple:
    """Decorador para medir tiempos y memoria
    ---------------------------------------------------------------------
    Args:
        func: función a medir tiempo
    ---------------------------------------------------------------------
    Return:
        Tupla con el resultado de la función y los tiempos/memoria"""
    def new_func(*args:...)->tuple:
        """Función para medir tiempos y memoria
        ---------------------------------------------------------------------
        Args:
            *args: argumentos para llamar a la función
        ---------------------------------------------------------------------
        Return:
            Tupla con el resultado de la función y los tiempos/memoria"""
        print("¿Desea observar el uso de memoria? (True/False)")
        mem = input("Respuesta: ")
        mem = castBoolean(mem)
        start_time = timer()
        if mem is True:
            tracemalloc.start()
            start_memory = tracemalloc.take_snapshot()

        fun=func(*args)

        stop_time = timer()
        delta_time = (stop_time-start_time)*1000

        if mem is True:
            stop_memory = tracemalloc.take_snapshot()
            tracemalloc.stop()
            delta_memory = deltaMemory(stop_memory, start_memory)
            exec_time= delta_time, delta_memory
        else:
            exec_time= delta_time

        return fun, printLoadDataAnswer(exec_time)
    return new_func


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
@timer_y_mem
def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    rute = cf.data_dir + f"DIAN/Salida_agregados_renta_juridicos_AG{filename}"
    input_file = csv.DictReader(open(rute, encoding="utf-8"))
    for register in input_file:
        model.add_data(control["model"], register)
    return control


# Funciones de ordenamiento

@timer_y_mem
def req_1(control, code_year, code_sector):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1

    return model.req_1(control["model"], code_year, code_sector)

@timer_y_mem
def req_2(control, code_year, code_sector):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    return model.req_2(control["model"], code_year, code_sector)

@timer_y_mem
def req_3(control, code_year):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    return model.req_3(control["model"], code_year)

@timer_y_mem
def req_4(control, code_year):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4

    return model.req_4(control["model"], code_year)

@timer_y_mem
def req_5(control, code_year):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5

    return model.req_5(control["model"], code_year)

@timer_y_mem
def req_6(control, code_year):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    return model.req_6(control["model"], code_year)

@timer_y_mem
def req_7(control, code_year, code_sector):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7

    return model.req_7(control["model"], code_year, code_sector)

@timer_y_mem
def req_8(control, code_year, top):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8

    return model.req_8(control["model"], code_year, top)



