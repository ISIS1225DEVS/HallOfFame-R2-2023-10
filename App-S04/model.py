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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def new_data_structs(struct_list,struct_map,load_factor):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = mp.newMap(10,
                             maptype=struct_map,
                            loadfactor=load_factor)
    
    for i in range(2012,2022):
        element_list=lt.newList(datastructure=struct_list,
                                     cmpfunction=cmp_impuestos_by_anio_CAE)
        mp.put(data_structs,str(i),element_list)
    return data_structs



# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    año=data["Año"]
    d = new_data(data["Código actividad económica"],data)
    list_to_add=me.getValue(mp.get(data_structs,año))
    lt.addLast(list_to_add, d)

    return data_structs

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO CHECK
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    data_size=0
    for i in range(2012,2022):
        list_to_study=me.getValue((mp.get(data_structs,str(i))))
        data_size+=lt.size(list_to_study)
    return data_size

def get_first_registros(catalog,anio):
    registros=me.getValue(mp.get(catalog,str(anio)))
    first_registros=lt.newList()
    for cont in range(1,4):
        registro=lt.getElement(registros,cont)
        lt.addLast(first_registros,registro)
    return first_registros
        
def get_last_registros(catalog,anio):
    registros=me.getValue(mp.get(catalog,str(anio)))
    last_registros=lt.newList()
    last=lt.lastElement(registros)
    lt.addFirst(last_registros,last)
    for cont in range(1,3):
        registro=lt.getElement(registros,-cont)
        lt.addFirst(last_registros,registro)
    return last_registros


def req_1(data_structs,anio,sector):
    """
    Función que soluciona el requerimiento 1
    """
    #Se obtiene la lista de las actividades de ese año
    list_activities_year=me.getValue(mp.get(data_structs,anio))
    #Se crea una lista con las actividades que pertenecen alsector ingresado
    list_activities_sector=lt.newList(datastructure="ARRAY_LIST")
    #Se añaden los elementos que sean de esa actividad y de ese año a la lista list_activities_sector
    for actividad in lt.iterator(list_activities_year):
        if actividad["info"]["Código sector económico"]==sector:
            lt.addLast(list_activities_sector,actividad)
    #Se ordena la lista por merge sort con el criterio de saldo a pagar
    merg.sort(list_activities_sector, cmp_saldo_pagar)
    #Se retorna el elemento con mayor saldo a pagar
    return lt.firstElement(list_activities_sector)

def req_2(data_structs,anio,sector):
    """
    Función que soluciona el requerimiento 2
    """
    #Se obtiene la lista de las actividades de ese año
    list_activities_year=me.getValue(mp.get(data_structs,anio))
    #Se crea una lista con las actividades que pertenecen alsector ingresado
    list_activities_sector=lt.newList(datastructure="ARRAY_LIST")
    #Se añaden los elementos que sean de esa actividad y de ese año a la lista list_activities_sector
    for actividad in lt.iterator(list_activities_year):
        if actividad["info"]["Código sector económico"]==sector:
            lt.addLast(list_activities_sector,actividad)
    #Se ordena la lista por merge sort con el criterio de saldo a favor
    merg.sort(list_activities_sector, cmp_saldo_favor)
    #Se retorna el elemento con mayor saldo a pagar
    return lt.firstElement(list_activities_sector)


def req_3(data_structs,anio):
    """
    Función que soluciona el requerimiento 3
    """
    #Se obtiene la lista de las actividades de ese año
    list_activities_year=me.getValue(mp.get(data_structs,anio))
    #Se crea un mapa para cada subsector económico
    map_subsector=mp.newMap(22,
                            maptype="PROBING",
                            loadfactor=0.8)
    #Se recorre la lista de registros de ese año
    for actividad in lt.iterator(list_activities_year):
        #Se crea el mapa del subsector si este no existe
        if actividad["info"]["Código subsector económico"] not in lt.iterator(mp.keySet(map_subsector)):
            #Se crea un mapa con la informacion de cada subsector que será el valor de map_subsector
            map_subsector_value=mp.newMap(9,
                                          maptype="PROBING",
                                          loadfactor=0.8)       
            mp.put(map_subsector_value,"Código sector económico",actividad["info"]["Código sector económico"])
            mp.put(map_subsector_value,"Nombre sector económico",actividad["info"]["Nombre sector económico"])
            mp.put(map_subsector_value,"Código subsector económico",actividad["info"]["Código subsector económico"])
            mp.put(map_subsector_value,"Nombre subsector económico",actividad["info"]["Nombre subsector económico"])
            mp.put(map_subsector_value,"Total de retenciones del subsector económico",int(actividad["info"]["Total retenciones"]))
            mp.put(map_subsector_value,"Total ingresos netos del subsector económico",int(actividad["info"]["Total ingresos netos"]))
            mp.put(map_subsector_value,"Total costos y gastos del subsector económico",int(actividad["info"]["Total costos y gastos"]))
            mp.put(map_subsector_value,"Total saldo a pagar del subsector económico",int(actividad["info"]["Total saldo a pagar"]))
            mp.put(map_subsector_value,"Total saldo a favor del subsector económico",int(actividad["info"]["Total saldo a favor"]))
            #Se crea una lista que servirá para guardar todas las actividades de ese subsector
            lt_activities_in_subsector=lt.newList(datastructure="ARRAY_LIST")
            #Se añade la actividad que tenemos en este momento
            lt.addLast(lt_activities_in_subsector,actividad)
            #Se añade dicha lista al mapa
            mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)
            #Se añade la tabla de información del subsector al indice del subsector
            mp.put(map_subsector,actividad["info"]["Código subsector económico"],map_subsector_value)
        
        #Si el valor del subsector ya existe
        else:
            #Encontrar valores del subsector 
            map_subsector_value=me.getValue(mp.get(map_subsector,actividad["info"]["Código subsector económico"]))
            total_retenciones=me.getValue(mp.get(map_subsector_value,"Total de retenciones del subsector económico"))
            value_ingresos=me.getValue(mp.get(map_subsector_value,"Total ingresos netos del subsector económico"))
            value_gastos=me.getValue(mp.get(map_subsector_value,"Total costos y gastos del subsector económico"))
            value_saldo_pagar=me.getValue(mp.get(map_subsector_value,"Total saldo a pagar del subsector económico"))
            value_saldo_favor=me.getValue(mp.get(map_subsector_value,"Total saldo a favor del subsector económico"))
            lt_activities_in_subsector=me.getValue(mp.get(map_subsector_value,"Actividades del subsector"))
            lt.addLast(lt_activities_in_subsector,actividad)
            
            #Añadir valores al subsector
            mp.put(map_subsector_value,"Total de retenciones del subsector económico",int(actividad["info"]["Total retenciones"])+ total_retenciones)
            mp.put(map_subsector_value,"Total ingresos netos del subsector económico",value_ingresos+int(actividad["info"]["Total ingresos netos"]))
            mp.put(map_subsector_value,"Total costos y gastos del subsector económico",value_gastos+int(actividad["info"]["Total costos y gastos"]))
            mp.put(map_subsector_value,"Total saldo a pagar del subsector económico",value_saldo_pagar+int(actividad["info"]["Total saldo a pagar"]))
            mp.put(map_subsector_value,"Total saldo a favor del subsector económico",value_saldo_favor+int(actividad["info"]["Total saldo a favor"]))
            mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)
    
    #Encontrar el sector con el minímomo de retenciones
    min_retenciones = float('inf')
    min_sectores = None

    for sector in lt.iterator(mp.keySet(map_subsector)):
        #Se obtiene la información de cada subsector
        info_subsector= me.getValue(mp.get(map_subsector,sector))
        #Se revisa si el valor del subsect
        if  me.getValue(mp.get(info_subsector,"Total de retenciones del subsector económico"))< min_retenciones:
            min_retenciones =  me.getValue(mp.get(info_subsector,"Total de retenciones del subsector económico"))
            min_sectores = info_subsector
    
    #Obtener las actividades del subsector con el mínimo de retenciones
    actividades_subsector= me.getValue(mp.get(min_sectores,"Actividades del subsector"))
    #Organizar actividades de menor a mayor con respecto a sus retenciones
    merg.sort(actividades_subsector,cmp_retenciones)

    if lt.size(actividades_subsector) > 6:
        choosen_activities= lt.subList(actividades_subsector,1,3)
        menores= lt.subList(actividades_subsector,lt.size(actividades_subsector)-2,3)
        for elemento in menores:
            lt.addLast(choosen_activities,elemento)
    else:
        choosen_activities=actividades_subsector


    return min_sectores,choosen_activities


def req_4(data_structs, anio):
    """
    Función que soluciona el requerimiento 4
    """
    #Se obtiene la lista de las actividades de ese año
    list_activities_year=me.getValue(mp.get(data_structs,anio))
    #Se crea un mapa para cada subsector económico
    map_subsector=mp.newMap(22,
                            maptype="PROBING",
                            loadfactor=0.8)
    #Se recorre la lista de registros de ese año
    for actividad in lt.iterator(list_activities_year):
        #Se crea el mapa del subsector si este no existe
        if not mp.contains(map_subsector,actividad["info"]["Código subsector económico"]):
            #Se crea un mapa con la informacion de cada subsector que será el valor de map_subsector
            map_subsector_value=mp.newMap(9,
                                          maptype="PROBING",
                                          loadfactor=0.8)       
            mp.put(map_subsector_value,"Código sector económico",actividad["info"]["Código sector económico"])
            mp.put(map_subsector_value,"Nombre sector económico",actividad["info"]["Nombre sector económico"])
            mp.put(map_subsector_value,"Código subsector económico",actividad["info"]["Código subsector económico"])
            mp.put(map_subsector_value,"Nombre subsector económico",actividad["info"]["Nombre subsector económico"])
            mp.put(map_subsector_value,"Total de costos y gastos de nomina del subsector económico",int(actividad["info"]["Costos y gastos nómina"]))
            mp.put(map_subsector_value,"Total ingresos netos del subsector económico",int(actividad["info"]["Total ingresos netos"]))
            mp.put(map_subsector_value,"Total costos y gastos del subsector económico",int(actividad["info"]["Total costos y gastos"]))
            mp.put(map_subsector_value,"Total saldo a pagar del subsector económico",int(actividad["info"]["Total saldo a pagar"]))
            mp.put(map_subsector_value,"Total saldo a favor del subsector económico",int(actividad["info"]["Total saldo a favor"]))
            #Se crea una lista que servirá para guardar todas las actividades de ese subsector
            lt_activities_in_subsector=lt.newList(datastructure="ARRAY_LIST")
            #Se añade la actividad que tenemos en este momento
            lt.addLast(lt_activities_in_subsector,actividad)
            #Se añade dicha lista al mapa
            mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)
            #Se añade la tabla de información del subsector al indice del subsector
            mp.put(map_subsector,actividad["info"]["Código subsector económico"],map_subsector_value)
        
        #Si el valor del subsector ya existe
        else:
            #Encontrar valores del subsector 
            map_subsector_value=me.getValue(mp.get(map_subsector,actividad["info"]["Código subsector económico"]))
            total_costos_y_gastos_de_nomina=me.getValue(mp.get(map_subsector_value,"Total de costos y gastos de nomina del subsector económico"))
            value_ingresos=me.getValue(mp.get(map_subsector_value,"Total ingresos netos del subsector económico"))
            value_gastos=me.getValue(mp.get(map_subsector_value,"Total costos y gastos del subsector económico"))
            value_saldo_pagar=me.getValue(mp.get(map_subsector_value,"Total saldo a pagar del subsector económico"))
            value_saldo_favor=me.getValue(mp.get(map_subsector_value,"Total saldo a favor del subsector económico"))
            lt_activities_in_subsector=me.getValue(mp.get(map_subsector_value,"Actividades del subsector"))
            lt.addLast(lt_activities_in_subsector,actividad)
            
            #Añadir valores al subsector
            mp.put(map_subsector_value,"Total de costos y gastos de nomina del subsector económico",float(actividad["info"]["Costos y gastos nómina"])+ total_costos_y_gastos_de_nomina)
            mp.put(map_subsector_value,"Total ingresos netos del subsector económico",value_ingresos+float(actividad["info"]["Total ingresos netos"]))
            mp.put(map_subsector_value,"Total costos y gastos del subsector económico",value_gastos+float(actividad["info"]["Total costos y gastos"]))
            mp.put(map_subsector_value,"Total saldo a pagar del subsector económico",value_saldo_pagar+float(actividad["info"]["Total saldo a pagar"]))
            mp.put(map_subsector_value,"Total saldo a favor del subsector económico",value_saldo_favor+float(actividad["info"]["Total saldo a favor"]))
            mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)
    
    #Encontrar el sector con el minímomo de retenciones
    costos_gastos_nomina = -1
    max_sectores = None

    for sector in lt.iterator(mp.keySet(map_subsector)):
        #Se obtiene la información de cada subsector
        info_subsector= me.getValue(mp.get(map_subsector,sector))
        #Se revisa si el valor del subsect
        if  me.getValue(mp.get(info_subsector,"Total de costos y gastos de nomina del subsector económico")) > costos_gastos_nomina:
            costos_gastos_nomina =  me.getValue(mp.get(info_subsector,"Total de costos y gastos de nomina del subsector económico"))
            max_sectores = info_subsector
    
    #Obtener las actividades del subsector con el mínimo de retenciones
    actividades_subsector= me.getValue(mp.get(max_sectores,"Actividades del subsector"))
    #Organizar actividades de menor a mayor con respecto a sus retenciones
    merg.sort(actividades_subsector,cmp_costosygastos)

    if lt.size(actividades_subsector) > 6:
        choosen_activities= lt.subList(actividades_subsector,1,3)
        i = lt.size(actividades_subsector)
        while i > lt.size(actividades_subsector)-2:
            lt.addLast(choosen_activities, lt.getElement(actividades_subsector, i))
            i-=1

    

    else:
        choosen_activities=actividades_subsector


    return max_sectores,choosen_activities
    
    # TODO: Realizar el requerimiento 4
    


def req_5(data_structs,anio):
    """
    Función que soluciona el requerimiento 5
    """
    #Se obtiene la lista de las actividades de ese año
    list_activities_year=me.getValue(mp.get(data_structs,anio))
    #Se crea un mapa para cada subsector económico
    map_subsector=mp.newMap(22,
                            maptype="PROBING",
                            loadfactor=0.8)
    #Se inicializa el mayor descuento de un periodo como 0
    max_descuento=0
    #Se inicializa el mayor subsector como ninguno
    subsector_interes=""
    #Se recorre la lista de registros de ese año
    for actividad in lt.iterator(list_activities_year):
        #Se crea el mapa del subsector si este no existe
        if actividad["info"]["Código subsector económico"] not in lt.iterator(mp.keySet(map_subsector)):
            #Se crea un mapa con la informacion de cada subsector que será el valor de map_subsector
            map_subsector_value=mp.newMap(9,
                                          maptype="PROBING",
                                          loadfactor=0.8)
            
            mp.put(map_subsector_value,"Código sector económico",actividad["info"]["Código sector económico"])
            mp.put(map_subsector_value,"Nombre sector económico",actividad["info"]["Nombre sector económico"])
            mp.put(map_subsector_value,"Código subsector económico",actividad["info"]["Código subsector económico"])
            mp.put(map_subsector_value,"Nombre subsector económico",actividad["info"]["Nombre subsector económico"])
            mp.put(map_subsector_value,"Total de descuentos tributarios del subsector económico",int(actividad["info"]["Descuentos tributarios"]))
            mp.put(map_subsector_value,"Total ingresos netos del subsector económico",int(actividad["info"]["Total ingresos netos"]))
            mp.put(map_subsector_value,"Total costos y gastos del subsector económico",int(actividad["info"]["Total costos y gastos"]))
            mp.put(map_subsector_value,"Total saldo a pagar del subsector económico",int(actividad["info"]["Total saldo a pagar"]))
            mp.put(map_subsector_value,"Total saldo a favor del subsector económico",int(actividad["info"]["Total saldo a favor"]))
            #Se crea una lista que servirá para guardar todas las actividades de ese subsector
            lt_activities_in_subsector=lt.newList(datastructure="ARRAY_LIST")
            #Se añade la actividad que tenemos en este momento
            lt.addLast(lt_activities_in_subsector,actividad)
            #Se añade dicha lista al mapa
            mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)
            #Se añade la tabla de información del subsector al indice del subsector
            mp.put(map_subsector,actividad["info"]["Código subsector económico"],map_subsector_value)
            #Se verifica si es el mayor hasta el momento
            if int(actividad["info"]["Descuentos tributarios"])>=max_descuento:
                max_descuento=int(actividad["info"]["Descuentos tributarios"])
                subsector_interes=actividad["info"]["Código subsector económico"]
            
        #Se actualizan los datos del mapa si este existe
        else:
            map_subsector_value=me.getValue(mp.get(map_subsector,actividad["info"]["Código subsector económico"]))
            #Se obtienen los valores del mapa del subsector justo antes de la activida a analizar
            value_descuentos=me.getValue(mp.get(map_subsector_value,"Total de descuentos tributarios del subsector económico"))
            value_ingresos=me.getValue(mp.get(map_subsector_value,"Total ingresos netos del subsector económico"))
            value_gastos=me.getValue(mp.get(map_subsector_value,"Total costos y gastos del subsector económico"))
            value_saldo_pagar=me.getValue(mp.get(map_subsector_value,"Total saldo a pagar del subsector económico"))
            value_saldo_favor=me.getValue(mp.get(map_subsector_value,"Total saldo a favor del subsector económico"))
            lt_activities_in_subsector=me.getValue(mp.get(map_subsector_value,"Actividades del subsector"))
            #Se actualizan los valores
            mp.put(map_subsector_value,"Total de descuentos tributarios del subsector económico",value_descuentos+int(actividad["info"]["Descuentos tributarios"]))
            mp.put(map_subsector_value,"Total ingresos netos del subsector económico",value_ingresos+int(actividad["info"]["Total ingresos netos"]))
            mp.put(map_subsector_value,"Total costos y gastos del subsector económico",value_gastos+int(actividad["info"]["Total costos y gastos"]))
            mp.put(map_subsector_value,"Total saldo a pagar del subsector económico",value_saldo_pagar+int(actividad["info"]["Total saldo a pagar"]))
            mp.put(map_subsector_value,"Total saldo a favor del subsector económico",value_saldo_favor+int(actividad["info"]["Total saldo a favor"]))
            lt.addLast(lt_activities_in_subsector,actividad)
            #Se verifica si es el mayor hasta el momento
            if (int(actividad["info"]["Descuentos tributarios"])+value_descuentos)>=max_descuento:
                max_descuento=int(actividad["info"]["Descuentos tributarios"])+value_descuentos
                subsector_interes=actividad["info"]["Código subsector económico"]
    #Se obtiene el subsector con el mayor descuento
    subsector_dict=me.getValue(mp.get(map_subsector,subsector_interes))
    #Se organizan las actividades de acuerdo a su contribución de descuentos
    list_activities_best=me.getValue(mp.get(subsector_dict,"Actividades del subsector"))
    merg.sort(list_activities_best,cmp_descuentos)
    return (subsector_dict,list_activities_best)

def req_6(data_structs,anio):
    """
    Función que soluciona el requerimiento 6
    """
    #Se obtiene la lista de las actividades de ese año
    list_activities_year=me.getValue(mp.get(data_structs,anio))
    #Se crea un mapa para cada sector económico
    map_sectors=mp.newMap(12,maptype="PROBING",loadfactor=0.8)
    #Se inicializa el mayor descuento de un periodo como 0
    max_ingresos_netos=0
    #Se inicializa el mayor subsector como ninguno
    sector_interes=None
    #Se crean listas que nos van a permitir realizar la carga de datos más rapido
    #!!!!!!!!Estas listas no son usada para la estructura principal y no se utiliza para resolver el requerimiento, solo nos permiten reducir lineas de código!!!!!!!!!!
    headers_sector_iterator=["Código sector económico","Nombre sector económico","Total ingresos netos del sector económico","Total costos y gastos del sector económico","Total saldo a pagar del sector económico","Total saldo a favor del sector económico","Subsector económico que más aporto","Subsector económico que menos aporto"]
    actividad_sector_iterator=["Código sector económico","Nombre sector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor","Código subsector económico","Código subsector económico"]
    headers_subsector_iterator=["Código subsector económico","Nombre subsector económico","Total ingresos netos del subsector económico","Total costos y gastos del subsector económico","Total saldo a pagar del subsector económico","Total saldo a favor del subsector económico"]
    actividad_subsector_iterator=["Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
     #Se recorre la lista de registros de ese año
    for actividad in lt.iterator(list_activities_year):
        #Se crea el mapa del subsector si este no existe
        if actividad["info"]["Código sector económico"] not in lt.iterator(mp.keySet(map_sectors)):
            #Se inicializa el mapa de los valores del sector
            map_sector_value=mp.newMap(9,maptype="PROBING",loadfactor=0.8)
            #Se le agregan los headers y los valores al mapa
            for i in range(0,8):
                mp.put(map_sector_value,headers_sector_iterator[i],actividad["info"][actividad_sector_iterator[i]])
            """Se repite la creacion de un subsector realizada en el requerimiento individual"""
            #Se crea un mapa de los subsectores en el sector
            map_subsectors=mp.newMap(22,maptype="PROBING",loadfactor=0.8)
            #Se le añaden los valores a dicho mapa del subsector
            map_subsector_value=mp.newMap(9,maptype="PROBING",loadfactor=0.8)
            for i in range(0,6):
                mp.put(map_subsector_value,headers_subsector_iterator[i],actividad["info"][actividad_subsector_iterator[i]])
            #Se crea una lista que servirá para guardar todas las actividades de ese subsector
            lt_activities_in_subsector=lt.newList(datastructure="ARRAY_LIST")
            #Se añade la actividad que tenemos en este momento
            lt.addLast(lt_activities_in_subsector,actividad)
            #Se añade dicha lista al mapa
            mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)
            #Se añade la tabla de información del subsector al indice del subsector
            mp.put(map_subsectors,actividad["info"]["Código subsector económico"],map_subsector_value)
            """Fin de la creacion de un subsector como en el requerimiento individual"""
            #Se verifica si es el mayor hasta el momento
            if int(actividad["info"]["Total ingresos netos"])>=max_ingresos_netos:
                max_ingresos_netos=int(actividad["info"]["Total ingresos netos"])
                sector_interes=actividad["info"]["Código sector económico"]
            #Se añade este  subsector a los subsectores del sector
            mp.put(map_sector_value,"Subsectores del sector",map_subsectors)
            #Se añade toda la info al map principal
            mp.put(map_sectors,actividad["info"]["Código sector económico"],map_sector_value)
        #Se actualizan los datos del mapa si la actividad ya está registrada
        else:
            #Se verifica el caso en el que ya este registrado el sector y el subsector y solo queda actualizar los datos de estos y actualizar la lista de actividades
            map_sector=me.getValue(mp.get(map_sectors,actividad["info"]["Código sector económico"]))
            map_subsectors=me.getValue(mp.get(map_sector,"Subsectores del sector"))
            if actividad["info"]["Código subsector económico"] in lt.iterator(mp.keySet(map_subsectors)):
                """Se actualizan los datos del subsector como en los requerimientos individuales """
                map_subsector_value=me.getValue(mp.get(map_subsectors,actividad["info"]["Código subsector económico"]))
                #Se actualizan los valores
                for i in range(2,6):
                    mp.put(map_subsector_value,headers_subsector_iterator[i],int(me.getValue(mp.get(map_subsector_value,headers_subsector_iterator[i])))+int(actividad["info"][actividad_subsector_iterator[i]]))
                lt.addLast(lt_activities_in_subsector,actividad)
                """Fin de la actualizacion del subsector"""
            #Se verifica el caso en el que ya este registrado el sector pero no el subsector  
            else: 
                """Se repite la creacion de un subsector realizada en el requerimiento individual"""
                #Se le accede al valor del subsector
                map_subsector_value=mp.newMap(9,maptype="PROBING",loadfactor=0.8)
                #Se le añaden los headers y sus respectivos valores al mapa del subsector
                for i in range(0,6):
                    mp.put(map_subsector_value,headers_subsector_iterator[i],actividad["info"][actividad_subsector_iterator[i]])
                #Se crea una lista que servirá para guardar todas las actividades de ese subsector
                lt_activities_in_subsector=lt.newList(datastructure="ARRAY_LIST")
                #Se añade la actividad que tenemos en este momento
                lt.addLast(lt_activities_in_subsector,actividad)
                #Se añade dicha lista al mapa
                mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)
                #Se añade la tabla de información del subsector al indice del subsector
                mp.put(map_subsectors,actividad["info"]["Código subsector económico"],map_subsector_value)
                """Fin de la creacion de un subsector como en el requerimiento individual"""
                #Se deja establecida la variable map_subsector_value y map_sector value para actualizar
                map_sector_value=map_sector
                map_subsector_value=me.getValue(mp.get(map_subsectors,actividad["info"]["Código subsector económico"]))
            #Se actualiza la información del sector teniendo en cuenta los nuevos datos del subsector
            for i in range(2,6):
                    mp.put(map_sector_value,headers_sector_iterator[i],int(me.getValue(mp.get(map_sector_value,headers_sector_iterator[i])))+int(actividad["info"][actividad_sector_iterator[i]]))
            #Se verifica si es el mayor hasta el momento
            if int(me.getValue(mp.get(map_sector_value,"Total ingresos netos del sector económico")))>=max_ingresos_netos:
                max_ingresos_netos=int(me.getValue(mp.get(map_sector_value,"Total ingresos netos del sector económico")))
                sector_interes=actividad["info"]["Código sector económico"]
            #Se actualiza la informacion del subsector que mas aporto si es necesario
            value_ingresos_subsector=int(me.getValue(mp.get(map_subsector_value,"Total ingresos netos del subsector económico")))
            actual_subsector_mas_aporto=str(me.getValue(mp.get(map_sector,"Subsector económico que más aporto")))
            mapa_actual_subsector_mas_aporto=me.getValue(mp.get(map_subsectors,actual_subsector_mas_aporto))
            actual_mayor_aporte_subsector=int(me.getValue(mp.get(mapa_actual_subsector_mas_aporto,'Total ingresos netos del subsector económico')))
            if actual_mayor_aporte_subsector<=value_ingresos_subsector:
                mp.put(map_sector,"Subsector económico que más aporto",actividad["info"]["Código subsector económico"])
            #Se actualiza la informacion del subsector que menos aporto si es necesario
            actual_subsector_menos_aporto=str(me.getValue(mp.get(map_sector,"Subsector económico que menos aporto")))
            mapa_actual_subsector_menos_aporto=me.getValue(mp.get(map_subsectors,actual_subsector_menos_aporto))
            actual_menor_aporte_subsector=int(me.getValue(mp.get(mapa_actual_subsector_menos_aporto,'Total ingresos netos del subsector económico')))
            if actual_menor_aporte_subsector>=value_ingresos_subsector:
                mp.put(map_sector,"Subsector económico que menos aporto",actividad["info"]["Código subsector económico"])
    #Se obtiene el sector con el mayor total ingresos netos
    sector_map_important=me.getValue(mp.get(map_sectors,sector_interes))
    subsectors_of_important_sector=me.getValue(mp.get(sector_map_important,'Subsectores del sector'))
    #Se obtiene el subsector económico que mas aporto
    code_most_subsector=me.getValue(mp.get(sector_map_important,"Subsector económico que más aporto"))
    subsector_most=me.getValue(mp.get(subsectors_of_important_sector,code_most_subsector))
    #Se obtiene el subsector económico que menos aporto
    code_less_subsector=me.getValue(mp.get(sector_map_important,"Subsector económico que menos aporto"))
    subsector_less=me.getValue(mp.get(subsectors_of_important_sector,code_less_subsector))
    #Se obtienen las actividades del subsector _most
    list_activities_subsector_most=me.getValue(mp.get(subsector_most,'Actividades del subsector'))
    merg.sort(list_activities_subsector_most,cmp_ingresos)
    #Se botiene la actividad que mas aporto del subsector_most
    actividad_mas_aporto_1=lt.firstElement(list_activities_subsector_most)
    #Se botiene la actividad que menos aporto del subsector_most
    actividad_menos_aporto_1=lt.lastElement(list_activities_subsector_most)
    #Se obtienen las actividades del subsector _less
    list_activities_subsector_less=me.getValue(mp.get(subsector_less,'Actividades del subsector'))
    merg.sort(list_activities_subsector_less,cmp_ingresos)
    #Se botiene la actividad que mas aporto del subsector_less
    actividad_mas_aporto_2=lt.firstElement(list_activities_subsector_less)
    #Se botiene la actividad que menos aporto del subsector_less
    actividad_menos_aporto_2=lt.lastElement(list_activities_subsector_less)
    #Se realiza el retorno
    return (sector_map_important,subsector_most,subsector_less,actividad_mas_aporto_1,actividad_menos_aporto_1,actividad_mas_aporto_2,actividad_menos_aporto_2)
    
def req_7(data_structs,anio,subsector,n):
    """
    Función que soluciona el requerimiento 7
    """
    #Se obtiene la lista de las actividades de ese año
    list_activities_year=me.getValue(mp.get(data_structs,anio))
    #Se obtiene la lista de las actividades del subsector que estan en el año
    list_activities_year_and_subsector=lt.newList(datastructure="ARRAY_LIST")
    for actividad in lt.iterator(list_activities_year):
        if actividad["info"]["Código subsector económico"]==subsector:
            lt.addLast(list_activities_year_and_subsector,actividad)
    #Se filtra la lista segn el criterio de menor total de costos y gastos 
    merg.sort(list_activities_year_and_subsector,cmp_costos_gastos)
    #Se toman los n primeros valores si la lista excede el n 
    if int(n)>=lt.size(list_activities_year_and_subsector):
        return list_activities_year_and_subsector
    else:
        list2return=lt.newList(datastructure="ARRAY_LIST")
        for i in range(1,int(n)+1):
            lt.addLast(list2return,lt.getElement(list_activities_year_and_subsector,i))
        return list2return
    


def req_8(data_structs,anio,top):
    """
    Función que soluciona el requerimiento 8
    """
    top=int(top)
    #Se crea una lista de los subsectores
    lista_subsectores= lt.newList(datastructure="ARRAY_LIST")
    #Se obtiene la lista de las actividades de ese año
    list_activities_year=me.getValue(mp.get(data_structs,anio))
    #Se crea un mapa para cada subsector económico
    map_subsector=mp.newMap(22,
                            maptype="PROBING",
                            loadfactor=0.8)
    #Se crea un mapa para las actividades de cada uno de los subsectores
    map_actividades=mp.newMap(6,
                            maptype="PROBING",
                            loadfactor=0.8)
    contador=0
    #Se recorre la lista de registros de ese año
    for actividad in lt.iterator(list_activities_year):
        #Se crea el mapa del subsector si este no existe
        if actividad["info"]["Código subsector económico"] not in lt.iterator(mp.keySet(map_subsector)):
            #Se crea un mapa con la informacion de cada subsector que será el valor de map_subsector
            map_subsector_value=mp.newMap(9,
                                          maptype="PROBING",
                                          loadfactor=0.8) 
            contador +=1      
            mp.put(map_subsector_value,"Código sector económico",actividad["info"]["Código sector económico"])
            mp.put(map_subsector_value,"Nombre sector económico",actividad["info"]["Nombre sector económico"])
            mp.put(map_subsector_value,"Código subsector económico",actividad["info"]["Código subsector económico"])
            mp.put(map_subsector_value,"Nombre subsector económico",actividad["info"]["Nombre subsector económico"])
            mp.put(map_subsector_value,"Total de impuestos a cargo para el subsector económico",int(actividad["info"]["Total Impuesto a cargo"]))
            mp.put(map_subsector_value,"Total ingresos netos del subsector económico",int(actividad["info"]["Total ingresos netos"]))
            mp.put(map_subsector_value,"Total costos y gastos del subsector económico",int(actividad["info"]["Total costos y gastos"]))
            mp.put(map_subsector_value,"Total saldo a pagar del subsector económico",int(actividad["info"]["Total saldo a pagar"]))
            mp.put(map_subsector_value,"Total saldo a favor del subsector económico",int(actividad["info"]["Total saldo a favor"]))
            #Se crea una lista que servirá para guardar todas las actividades de ese subsector
            lt_activities_in_subsector=lt.newList(datastructure="ARRAY_LIST")
            #Se añade la actividad que tenemos en este momento
            lt.addLast(lt_activities_in_subsector,actividad)
            #Se añade dicha lista al mapa
            mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)
            #Se añade la tabla de información del subsector al indice del subsector
            mp.put(map_subsector,actividad["info"]["Código subsector económico"],map_subsector_value)
        
        #Si el valor del subsector ya existe
        else:
            #Encontrar valores del subsector 
            map_subsector_value=me.getValue(mp.get(map_subsector,actividad["info"]["Código subsector económico"]))
            total_cargo=me.getValue(mp.get(map_subsector_value,"Total de impuestos a cargo para el subsector económico"))
            value_ingresos=me.getValue(mp.get(map_subsector_value,"Total ingresos netos del subsector económico"))
            value_gastos=me.getValue(mp.get(map_subsector_value,"Total costos y gastos del subsector económico"))
            value_saldo_pagar=me.getValue(mp.get(map_subsector_value,"Total saldo a pagar del subsector económico"))
            value_saldo_favor=me.getValue(mp.get(map_subsector_value,"Total saldo a favor del subsector económico"))
            lt_activities_in_subsector=me.getValue(mp.get(map_subsector_value,"Actividades del subsector"))
            lt.addLast(lt_activities_in_subsector,actividad)
            
            #Añadir valores al subsector
            mp.put(map_subsector_value,"Total de impuestos a cargo para el subsector económico",int(actividad["info"]["Total Impuesto a cargo"])+ total_cargo)
            mp.put(map_subsector_value,"Total ingresos netos del subsector económico",value_ingresos+int(actividad["info"]["Total ingresos netos"]))
            mp.put(map_subsector_value,"Total costos y gastos del subsector económico",value_gastos+int(actividad["info"]["Total costos y gastos"]))
            mp.put(map_subsector_value,"Total saldo a pagar del subsector económico",value_saldo_pagar+int(actividad["info"]["Total saldo a pagar"]))
            mp.put(map_subsector_value,"Total saldo a favor del subsector económico",value_saldo_favor+int(actividad["info"]["Total saldo a favor"]))
            mp.put(map_subsector_value,"Actividades del subsector",lt_activities_in_subsector)

    #Se verifica si hay menos de dos subsectores
    
    todos_subsectores=lt.newList(datastructure="ARRAY_LIST")
    for subsector in lt.iterator(mp.keySet(map_subsector)):
        #Se obtiene la información de cada subsector
        info_subsector= me.getValue(mp.get(map_subsector,subsector))
        #Se añade a la lista de subsectores
        lt.addLast(todos_subsectores,info_subsector)
    #Organizar los subsectores
    merg.sort(todos_subsectores,cmp_cargo_subsector)
    if lt.size(todos_subsectores) > 12:
        #Añadir a la lista los 3 subsectores con más total impuestos a cargo
        lista_subsectores= lt.subList(todos_subsectores,1,3)
        #Añadir a la lista los 3 subsectores con menos total impuestos a cargo
        menos_a_cargo=lt.subList(todos_subsectores,lt.size(todos_subsectores)-2,3)
        for elemento in lt.iterator(menos_a_cargo):
            lt.addLast(lista_subsectores,elemento) 
    else:
        lista_subsectores=todos_subsectores
    #Recorrer list_subsectores para hallar el top de estos
    for info_subsector in lt.iterator(lista_subsectores):
        #Se obtiene las actividades de cada subsector
        actividades= me.getValue(mp.get(info_subsector,"Actividades del subsector"))
        #Se organizan las actividades
        merg.sort(actividades,cmp_cargo_actividades)
        #Escoger actividades del top
        if lt.size(actividades) >= top:
            choosen_activities=lt.subList(actividades,1,top)
        else:
            choosen_activities=actividades
        #Se obtiene el codigo del subsector
        subsector=me.getValue(mp.get(info_subsector,"Código subsector económico"))
        #Se añade la información al mapa de actividades
        mp.put(map_actividades,subsector,choosen_activities)

    return lista_subsectores,map_actividades



            
    
      


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if float(data_1["info"]["Año"]) > float(data_2["id"]["Año"]):
        return 1
    elif float(data_1["info"]["Año"]) < float(data_2["id"]["Año"]):
        return -1
    else:
        return 0

# Funciones de ordenamiento
def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2): 
    """ Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2, 
    en caso de que sean iguales tenga en cuenta el código de la actividad económica, 
    de lo contrario devuelva falso (False). 
    Args:
          impuesto1: información del primer registro de impuestos que incluye el “Año” y 
          el “Código actividad económica” 
          impuesto2: información del segundo registro de impuestos que incluye el “Año” y 
          el “Código actividad económica” """
             
    año_comparador1=int(impuesto1["info"]["Año"])
    año_comparador2=int(impuesto2["info"]["Año"])
    if impuesto1["id"].isdigit():
        id_comparador1=int(impuesto1["id"])
    else:
        if "y" in impuesto1["id"]:
            pos=impuesto1["id"].find("y")
            id_comparador1=int(impuesto1["id"][0:pos-1])
        if "Y" in impuesto1["id"]:
            pos=impuesto1["id"].find("Y")
            id_comparador1=int(impuesto1["id"][0:pos-1])
        if "-" in impuesto1["id"]:
            pos=impuesto1["id"].find("-")
            id_comparador1=int(impuesto1["id"][0:pos-1])
        if "/" in impuesto1["id"]:
            pos=impuesto1["id"].find("/")
            prueba=impuesto1["id"][0:pos]
            if prueba.isdigit():
                id_comparador1=int(prueba)
            else:
                id_comparador1=int(prueba[:len(prueba)-1])
            
    if impuesto2["id"].isdigit():
        id_comparador2=int(impuesto2["id"])
    else:
        if "y" in impuesto2["id"]:
            pos=impuesto2["id"].find("y")
            id_comparador2=int(impuesto2["id"][0:pos-1])
        if "Y" in impuesto2["id"]:
            pos=impuesto2["id"].find("Y")
            id_comparador2=int(impuesto2["id"][0:pos-1])
        if "-" in impuesto2["id"]:
            pos=impuesto2["id"].find("-")
            id_comparador2=int(impuesto2["id"][0:pos-1])
        if "/" in impuesto2["id"]:
            pos=impuesto2["id"].find("/")
            prueba=impuesto2["id"][0:pos]
            if prueba.isdigit():
                id_comparador2=int(prueba)
            else:
                id_comparador2=int(prueba[:len(prueba)-1])
    
    if año_comparador1==año_comparador2:
            if id_comparador1<id_comparador2:
                return True
            else:
                return False
    elif año_comparador1<año_comparador2:
        return True
    else:
        return False

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    año_comparador1=int(data_1["info"]["Año"])
    año_comparador2=int(data_2["info"]["Año"])
    if data_1["id"].isdigit():
        id_comparador1=int(data_1["id"])
    else:
        if "y" in data_1["id"]:
            pos=data_1["id"].find("y")
            id_comparador1=int(data_1["id"][0:pos-1])
        if "Y" in data_1["id"]:
            pos=data_1["id"].find("Y")
            id_comparador1=int(data_1["id"][0:pos-1])
        if "-" in data_1["id"]:
            pos=data_1["id"].find("-")
            id_comparador1=int(data_1["id"][0:pos-1])
        if "/" in data_1["id"]:
            pos=data_1["id"].find("/")
            prueba=data_1["id"][0:pos]
            if prueba.isdigit():
                id_comparador1=int(prueba)
            else:
                id_comparador1=int(prueba[:len(prueba)-1])
            
    if data_2["id"].isdigit():
        id_comparador2=int(data_2["id"])
    else:
        if "y" in data_2["id"]:
            pos=data_2["id"].find("y")
            id_comparador2=int(data_2["id"][0:pos-1])
        if "Y" in data_2["id"]:
            pos=data_2["id"].find("Y")
            id_comparador2=int(data_2["id"][0:pos-1])
        if "-" in data_2["id"]:
            pos=data_2["id"].find("-")
            id_comparador2=int(data_2["id"][0:pos-1])
        if "/" in data_2["id"]:
            pos=data_2["id"].find("/")
            prueba=data_2["id"][0:pos]
            if prueba.isdigit():
                id_comparador2=int(prueba)
            else:
                id_comparador2=int(prueba[:len(prueba)-1])
    
            
    if año_comparador1==año_comparador2:
            if id_comparador1<id_comparador2:
                return 1
            else:
                return 0
    elif año_comparador1<año_comparador2:
        return 1
    else:
        return 0


def sort(data_structs,metodo):
    """
    Función encargada de ordenar la lista con los datos
    """
    for año in range(2012,2022):
        list2sort=me.getValue((mp.get(data_structs,str(año))))
        if metodo=="1":
            se.sort(list2sort, sort_criteria)
        elif metodo=="2":
            ins.sort(list2sort, sort_criteria)
        elif metodo=="3":
            sa.sort(list2sort, sort_criteria)
        elif metodo=="4":
            quk.sort(list2sort, sort_criteria)
        elif metodo=="5":
            merg.sort(list2sort, sort_criteria)
            
def cmp_saldo_pagar(dato1,dato2):
    """ Funcion cmp requerimiento 1, filtra la lista de acuerdo
    al saldo total de impuestos a pagar, donde la primera posición será la actividad
    que mayores impuestos debió pagar"""
    saldo_pagar_1= float(dato1["info"]["Total saldo a pagar"])
    saldo_pagar_2= float(dato2["info"]["Total saldo a pagar"])
    if saldo_pagar_1 < saldo_pagar_2:
        return 0
    else:
        return 1
    
def cmp_saldo_favor(dato1,dato2):
    """ Funcion cmp requerimiento 2, filtra la lista de acuerdo
    al saldo total de impuestos a favor, donde la primera posición será la actividad
    que mayores impuestos debió pagar"""
    saldo_favor_1= float(dato1["info"]["Total saldo a favor"])
    saldo_favor_2= float(dato2["info"]["Total saldo a favor"])
    if saldo_favor_1 < saldo_favor_2:
        return 0
    else:
        return 1
    
def cmp_retenciones(dato1,dato2):
    """ Funcion cmp requerimiento 3, filtra la lista de actividades de acuerdo con el total de retenciones en un
    subsector específico"""
    retencion_1= float(dato1["info"]["Total retenciones"])
    retencion_2= float(dato2["info"]["Total retenciones"])
    if retencion_1 < retencion_2:
        return 1
    else:
        return 0
    
def cmp_costosygastos(dato1,dato2):
    """ Funcion cmp requerimiento 4, filtra la lista de actividades de acuerdo con el total de retenciones en un
    subsector específico"""
    retencion_1= float(dato1["info"]["Costos y gastos nómina"])
    retencion_2= float(dato2["info"]["Costos y gastos nómina"])
    if retencion_1 < retencion_2:
        return 1
    else:
        return 0
    
def cmp_descuentos(dato1,dato2):
    """ Funcion cmp requerimiento 5, filtra la lista de actividades de acuerdo con la contribución que hicieron 
    a los descuentos de un subsector"""
    descuento_1= float(dato1['info']["Descuentos tributarios"])
    descuento_2= float(dato2['info']["Descuentos tributarios"])
    if descuento_1 < descuento_2:
        return 1
    else:
        return 0
    
def cmp_cargo_subsector(dato1,dato2):
    """ Funcion cmp requerimiento 3, filtra la lista de actividades de acuerdo con el total de retenciones en un
    subsector específico"""
    cargo_1= me.getValue(mp.get(dato1,"Total de impuestos a cargo para el subsector económico"))
    cargo_2= me.getValue(mp.get(dato2,"Total de impuestos a cargo para el subsector económico"))
    if cargo_1 < cargo_2:
        return 0
    elif cargo_1 == cargo_2:
        nombre_1= me.getValue(mp.get(dato1,"Nombre subsector económico"))
        nombre_2= me.getValue(mp.get(dato2,"Nombre subsector económico")) 
        if nombre_1 < nombre_2:
            return 0
        else:
            return 1
    else:
        return 1
    
def cmp_cargo_actividades(dato1,dato2):
    """ Funcion cmp requerimiento 8, filtra la lista de actividades de acuerdo con el total de impuestos a cargo en un
    subsector específico"""
    cargo_1= float(dato1["info"]["Total Impuesto a cargo"])
    cargo_2= float(dato2["info"]["Total Impuesto a cargo"])
    if cargo_1 < cargo_2:
        return 0
    elif cargo_1 == cargo_2:
        nombre_1=dato1["info"]["Nombre actividad económica"]
        nombre_2=dato2["info"]["Nombre actividad económica"]
        if nombre_1 < nombre_2:
            return 0
        else:
            return 1
    else:
        return 1
    

def cmp_ingresos(dato1,dato2):
    ingresos_1= float(dato1["info"]["Total ingresos netos"])
    ingresos_2= float(dato2["info"]["Total ingresos netos"])
    if ingresos_1 < ingresos_2:
        return 0
    else:
        return 1

def cmp_costos_gastos(dato1,dato2):
    ingresos_1= float(dato1["info"]["Total costos y gastos"])
    ingresos_2= float(dato2["info"]["Total costos y gastos"])
    if dato1["id"].isdigit():
        codigo_1=int(dato1["info"]["Código actividad económica"])
    else:
        if "y" in dato1["info"]["Código actividad económica"]:
            pos=dato1["info"]["Código actividad económica"].find("y")
            codigo_1=int(dato1["info"]["Código actividad económica"][0:pos-1])
        if "Y" in dato1["info"]["Código actividad económica"]:
            pos=dato1["info"]["Código actividad económica"].find("Y")
            codigo_1=int(dato1["info"]["Código actividad económica"][0:pos-1])
        if "-" in dato1["info"]["Código actividad económica"]:
            pos=dato1["info"]["Código actividad económica"].find("-")
            codigo_1=int(dato1["info"]["Código actividad económica"][0:pos-1])
        if "/" in dato1["info"]["Código actividad económica"]:
            pos=dato1["info"]["Código actividad económica"].find("/")
            prueba=dato1["info"]["Código actividad económica"][0:pos]
            if prueba.isdigit():
                codigo_1=int(prueba)
            else:
                codigo_1=int(prueba[:len(prueba)-1])
            
    if dato2["info"]["Código actividad económica"].isdigit():
        codigo_2=int(dato2["info"]["Código actividad económica"])
    else:
        if "y" in dato2["info"]["Código actividad económica"]:
            pos=dato2["info"]["Código actividad económica"].find("y")
            codigo_2=int(dato2["info"]["Código actividad económica"][0:pos-1])
        if "Y" in dato2["info"]["Código actividad económica"]:
            pos=dato2["info"]["Código actividad económica"].find("Y")
            codigo_2=int(dato2["info"]["Código actividad económica"][0:pos-1])
        if "-" in dato2["info"]["Código actividad económica"]:
            pos=dato2["info"]["Código actividad económica"].find("-")
            codigo_2=int(dato2["info"]["Código actividad económica"][0:pos-1])
        if "/" in dato2["info"]["Código actividad económica"]:
            pos=dato2["info"]["Código actividad económica"].find("/")
            prueba=dato2["info"]["Código actividad económica"][0:pos]
            if prueba.isdigit():
                codigo_2=int(prueba)
            else:
                codigo_2=int(prueba[:len(prueba)-1])
    if ingresos_1==ingresos_2:
        if codigo_1>codigo_2:
            return 1
        else:
            return 0
    elif ingresos_1 < ingresos_2:
        return 1
    else:
        return 0