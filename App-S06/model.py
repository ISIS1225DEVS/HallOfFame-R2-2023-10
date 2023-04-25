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


"""
FUNCIONES DE CARGA DE DATOS
"""

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    
    catalog = {"data":None}
    catalog["data"] = new_hash(10)
    
    return catalog
    

""" 
FUNCION PARA CREAR NUEVAS ESTRUCTURAS
"""

def new_hash(size):

    hash = mp.newMap(size,
                       maptype='PROBING',
                       loadfactor = 0.5,
                       cmpfunction = compareTridente)
    
    return hash


def new_info():
    return lt.newList('ARRAY_LIST')

def new_iterator():
    return lt.newList("SINGLE_LINKED")
    
    
""" 
FUNCIONES PARA SUMAR DATOS
"""

def sumar_diccionarios(actual, data):
    
    """Sumar el dato de entrada, al dato que ya existe.
    
    """
    
    contenedor = {'Total ingresos netos': None, 'Total costos y gastos': None,'Total saldo a pagar': None,
                    'Total saldo a favor': None, 'Total retenciones': None, 'Costos y gastos nómina': None,
                    'Descuentos tributarios': None, 'Costos ganancias ocasionales' : None, "Total Impuesto a cargo":None}

    new_dic = {}
    
    for llave in actual:
        if llave in contenedor:
            new_dic[llave] = limpiar_datos(actual[llave]) + limpiar_datos(data[llave])
        else:
            new_dic[llave] = actual[llave]
            
    return new_dic

""" 
FUNCIONES PARA AÑADIR ELEMENOS AL HASH
"""
def add_iterator_sector(hash, sector):
    
    lista = get_value(hash,"iterator sector")
    
    if lt.isPresent(lista,sector) == 0:
        lt.addLast(lista,sector)
        
    pass 

def add_iterator_subsector(hash, subsector):
                    
    lista = get_value(hash,"iterator subsector")
    
    if lt.isPresent(lista , subsector) == 0:
        lt.addLast(lista , subsector)
        
    pass 


def add_info(hash, data):
    
    lista = get_value(hash,"info")
    lt.addLast(lista, data)
    
    pass

def add_combined(hash, data):
    
    lista = get_value(hash,'combined')
    if lt.isEmpty(lista) == True:
        lt.addLast(lista, data)
    else:
        actual = lt.firstElement(lista)
        new_dic = sumar_diccionarios(actual, data)
        lt.changeInfo(lista, 1, new_dic)
        
    pass

def add_subsector(hash_num_sector, data):

    hash_subsector = get_value(hash_num_sector,'subsector')
    
    subsector_unico = ajustar_llave(data['Código subsector económico'])
    existsubsector = mp.contains(hash_subsector,subsector_unico)

    if existsubsector == False:
        mp.put(hash_subsector,subsector_unico,new_hash(2))
        hash_num_subsector = get_value(hash_subsector, subsector_unico)
        mp.put(hash_num_subsector,'info',new_info())
        mp.put(hash_num_subsector,'combined',new_info())
    else:
        hash_num_subsector = get_value(hash_subsector, subsector_unico)
    
    add_info(hash_num_subsector, data)
    add_combined(hash_num_subsector, data)
    
    pass


def add_sector(hash_year, data):
    
    hash_sector = get_value(hash_year,'sector')
    
    sector_unico = ajustar_llave(data['Código sector económico'])
    existsector = mp.contains(hash_sector,sector_unico)
    
    if existsector == False:
        mp.put(hash_sector,sector_unico,new_hash(4))
        hash_num_sector = get_value(hash_sector, sector_unico)
        mp.put(hash_num_sector,'info',new_info())
        mp.put(hash_num_sector,'subsector',new_hash(30))
        mp.put(hash_num_sector,"iterator subsector",new_iterator())
        mp.put(hash_num_sector,'combined',new_info()) 
    else:
        hash_num_sector = get_value(hash_sector, sector_unico)
        
    add_info(hash_num_sector, data)
    add_subsector(hash_num_sector, data)
    add_iterator_subsector(hash_num_sector, ajustar_llave(data['Código subsector económico']))
    add_combined(hash_num_sector, data)
    
    pass
    
    
def add_year(mega_hash, year, data):
    
    hash_year = get_value(mega_hash,year)
    existyear = mp.contains(hash_year,'info')
    
    if existyear == False:
        mp.put(hash_year,'info',new_info())
        mp.put(hash_year,'sector',new_hash(30))
        mp.put(hash_year,"iterator sector",new_iterator())
        mp.put(hash_year,'subsector',new_hash(30))
        mp.put(hash_year,"iterator subsector",new_iterator())
    
    
    add_info(hash_year, data)
    add_sector(hash_year, data)
    add_iterator_sector(hash_year, ajustar_llave(data['Código sector económico']))
    add_subsector(hash_year, data)
    add_iterator_subsector(hash_year, ajustar_llave(data['Código subsector económico']))
    pass


def add_todo(catalog,year,data):
    
    year = ajustar_llave(year)
    mega_hash = catalog["data"]
    exist_map = mp.contains(mega_hash,year)
    
    if exist_map == False:
        mp.put(mega_hash,year,new_hash(5))
        
    add_year(mega_hash,year,data)
    
    pass
    

"""
Funciones para limpiar datos
"""
def ajustar_llave(llave):
    return str(int(limpiar_datos(llave)))


def limpiar_datos(data_1):
    
    lista_dato = list(str(data_1))
    nueva_lista = lt.newList("ARRAY_LIST") 
    
    i = 0
    while i < len(lista_dato):

        if (lista_dato[i].isnumeric()) or (lista_dato[i] == ".") or (lista_dato[i] == ","):
            if lista_dato[i] == ",":
                lista_dato[i] = ""

            lt.addLast(nueva_lista, lista_dato[i])
            
        if (lista_dato[i].lower() == "y") or (lista_dato[i].lower() == "o") or (lista_dato[i]== "/") or (lista_dato[i] == "-"):
            i += len(lista_dato) + 1
        i += 1

    mensaje = ""
    for numeros in lt.iterator(nueva_lista):
        mensaje += numeros
    
    return float(mensaje)

"""
FUNCIONES DE OBTENER VALORES 
"""
def get_value(hash, key):
    
    pareja = mp.get(hash,key)
    value = me.getValue(pareja)
    
    return value

def get_sector_con_anio(data_structs,anio,sector):
    return get_value(get_value(get_value(data_structs["data"],anio),"sector"),sector)

def get_subsector_con_anio(data_structs,anio,subsector):
    return get_value(get_value(get_value(data_structs["data"],anio),"subsector"),subsector)
   
def get_info(hash):
    return get_value(hash,"info")

def get_combined(hash):
    return get_value(hash,"combined")

def get_subsector(hash):
    return get_value(hash,"subsector")

def get_subsector_especifico(hash,subsector):
    return get_value(get_subsector(hash), subsector)

def get_sector_iterator(hash):
    return get_value(hash,"iterator sector")

def get_subsector_iterator(hash):
    return get_value(hash,"iterator subsector")



""" 
FUNCIONES DE SORTEO
"""

def SortLista(lista,cmpfunction):
    return merg.sort(lista,cmpfunction)

def sort_all_info(data_structs):
    
    size = 0
    for year in range(2012,2022):
        sort_info(get_info(get_value(data_structs["data"],str(year))))
        size += lt.size(get_info(get_value(data_structs["data"],str(year))))
        
    return size
    
def sort_info(lista):
    return SortLista(lista,cmp_menor_Actividad_economica)

""" 
FUNCIONES DE COMPARACION
"""
def cmp_Total_saldo_pagar(data_1, data_2):
    
    if limpiar_datos(data_1["Total saldo a pagar"]) >= limpiar_datos(data_2["Total saldo a pagar"]):
        return True
    else:
        return False

def cmp_Total_saldo_a_favor(data_1, data_2):
    
    if limpiar_datos(data_1["Total saldo a favor"]) >= limpiar_datos(data_2["Total saldo a favor"]):
        return True
    else:
        return False
    
def cmp_Total_ingresos_netos(data_1, data_2):
    
    if limpiar_datos(data_1["Total ingresos netos"]) >= limpiar_datos(data_2["Total ingresos netos"]):
        return True
    else:
        return False
    
def cmp_Total_retenciones(data_1,data_2):
    
    if limpiar_datos(data_1["Total retenciones"]) >= limpiar_datos(data_2["Total retenciones"]):
        return True
    else:
        return False
    
def cmp_Total_impuestos_cargo(data_1,data_2):
    
    if limpiar_datos(data_1["Total Impuesto a cargo"]) > limpiar_datos(data_2["Total Impuesto a cargo"]):
        return True
    elif limpiar_datos(data_1["Total Impuesto a cargo"]) == limpiar_datos(data_2["Total Impuesto a cargo"]):
        return cmp_alfabetico(data_1,data_2)
    else:
        return False
    
def cmp_menor_Total_retenciones(data_1,data_2):
    
    if limpiar_datos(data_1["Total retenciones"]) <= limpiar_datos(data_2["Total retenciones"]):
        return True
    else:
        return False
    
def cmp_menor_costos_gastos_nomina(data_1,data_2):
    
    if limpiar_datos(data_1["Costos y gastos nómina"]) <= limpiar_datos(data_2["Costos y gastos nómina"]):
        return True
    else:
        return False

def cmp_menor_Total_costos_gastos(data_1,data_2):
    
    if limpiar_datos(data_1["Total costos y gastos"]) <= limpiar_datos(data_2["Total costos y gastos"]):
        return True
    elif limpiar_datos(data_1["Total costos y gastos"]) == limpiar_datos(data_2["Total costos y gastos"]):
        return cmp_menor_Actividad_economica(data_1,data_2)
    else:
        return False
    
def cmp_menor_Actividad_economica(data_1,data_2):
    
    if limpiar_datos(data_1["Código actividad económica"]) <= limpiar_datos(data_2["Código actividad económica"]):
        return True
    else:
        return False
    
def cmp_menor_sector_economico(data_1,data_2):
    
    if limpiar_datos(data_1["Código sector económico"]) <= limpiar_datos(data_2["Código sector económico"]):
        return True
    else:
        return False

    
def cmp_menor_descuentos_tributarios(data_1,data_2):
    
    if limpiar_datos(data_1["Descuentos tributarios"]) <= limpiar_datos(data_2["Descuentos tributarios"]):
        return True
    else:
        return False
        
def cmp_alfabetico(data_1,data_2):
    
    if data_1["Nombre subsector económico"] <= data_2["Nombre subsector económico"]:
        return True
    else:
        return False

def compareTridente(a,b):
    
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(b)
    if (a == authentry):
        return 0
    elif (a > authentry):
        return 1
    else:
        return -1

"""
FUNCIONES DE OBTENER MAYOR O MENOR
"""

def mayor_elemento(lista,criterio):
    
    mayor_valor = limpiar_datos(lt.firstElement(lista)[criterio])
    mayor = lt.firstElement(lista)
    
    for data in lt.iterator(lista):
        
        if limpiar_datos(data[criterio]) >= mayor_valor:
            mayor = data
            mayor_valor = limpiar_datos(data[criterio])
            
    return mayor

def menor_elemento(lista,criterio):
    
    menor_valor = limpiar_datos(lt.firstElement(lista)[criterio])
    menor = lt.firstElement(lista)
    
    for data in lt.iterator(lista):
        
        if limpiar_datos(data[criterio]) <= menor_valor:
            menor = data
            menor_valor = limpiar_datos(data[criterio])
            
    return menor

""" 
FUNCIONES DE ITERAR LISTAS CON CRITERIO 
"""

def lista_subsectores_combined(data_structs,anio,iterator):
    
    lista = lt.newList("SINGLE_LINKED")
    
    for subsector in lt.iterator(iterator):
        lt.addLast(lista, lt.firstElement(get_combined(get_subsector_con_anio(data_structs,anio,subsector))))
    
    return lista

def lista_sectores_combined(data_structs,anio,iterator):
    
    lista = lt.newList("SINGLE_LINKED")
    
    for sector in lt.iterator(iterator):
        lt.addLast(lista, lt.firstElement(get_combined(get_sector_con_anio(data_structs,anio,sector))))
    
    return lista

def lista_subsectores_del_sector_combined(iterator,hash_sector):
    
    lista = lt.newList("SINGLE_LINKED")
    
    for subsector in lt.iterator(iterator):
        lt.addLast(lista, lt.firstElement(get_combined(get_subsector_especifico(hash_sector,subsector))))
        
    return lista
    
""" 
FUNCIONES PARA EL REQUERIMIENTO 1
"""
    
def req_1(data_structs,anio,sector):
    """
    Función que soluciona el requerimiento 1
    """
    return mayor_elemento(get_info(get_sector_con_anio(data_structs,anio,sector)),"Total saldo a pagar")


""" 
FUNCIONES PARA EL REQUERIMIENTO 2
"""
def req_2(data_structs,anio,sector):
    """
    Función que soluciona el requerimiento 2
    """
    return mayor_elemento(get_info(get_sector_con_anio(data_structs,anio,sector)),"Total saldo a favor")


"""
FUNCIONES PARA EL REQUERIMIENTO 3
"""

def req_3(data_structs,anio):
    """
    Función que soluciona el requerimiento 3
    """ 
    lista_total_combined = lista_subsectores_combined(data_structs,anio,get_subsector_iterator(get_value(data_structs["data"],anio)))
    menor_retenciones = menor_elemento(lista_total_combined,"Total retenciones")
    
    return menor_retenciones, SortLista(get_info(get_subsector_con_anio(data_structs,anio, menor_retenciones["Código subsector económico"])),cmp_menor_Total_retenciones)


def req_4(data_structs, anio):
    """
    Función que soluciona el requerimiento 4
    """
    lista_total_combined = lista_subsectores_combined(data_structs,anio,get_subsector_iterator(get_value(data_structs["data"],anio)))
    mayor_costos_gastos_nomina = mayor_elemento(lista_total_combined,"Costos y gastos nómina")
    
    return mayor_costos_gastos_nomina, SortLista(get_info(get_subsector_con_anio(data_structs,anio,mayor_costos_gastos_nomina["Código subsector económico"])),cmp_menor_costos_gastos_nomina)


def req_5(data_structs,anio):
    """
    Función que soluciona el requerimiento 5
    """
    lista_total_combined = lista_subsectores_combined(data_structs,anio,get_subsector_iterator(get_value(data_structs["data"],anio)))
    mayor_descuentos = mayor_elemento(lista_total_combined,"Descuentos tributarios")
    
    return mayor_descuentos,  SortLista(get_info(get_subsector_con_anio(data_structs,anio,mayor_descuentos["Código subsector económico"])),cmp_menor_descuentos_tributarios)


    
""" 
FUNCIONES PARA EL REQUERIMIENTO 6
"""

def req_6(data_structs,anio):
    """
    Función que soluciona el requerimiento 6
    """
    
    lista_sectores = lista_sectores_combined(data_structs,anio,get_sector_iterator(get_value(data_structs["data"],anio)))    
    sector_mayor_ingresos_netos =  mayor_elemento(lista_sectores,"Total ingresos netos")
    
    lista_subsectores = lista_subsectores_del_sector_combined(get_subsector_iterator(get_sector_con_anio(data_structs,anio,sector_mayor_ingresos_netos["Código sector económico"])),get_sector_con_anio(data_structs,anio,sector_mayor_ingresos_netos["Código sector económico"]))
    subsector_mayor = mayor_elemento(lista_subsectores,"Total ingresos netos")
    subsector_menor = menor_elemento(lista_subsectores, "Total ingresos netos")
    
    actividad_mayor_mayor = mayor_elemento(get_info( get_subsector_especifico(get_sector_con_anio(data_structs,anio,sector_mayor_ingresos_netos["Código sector económico"]), subsector_mayor["Código subsector económico"])),"Total ingresos netos")
    actividad_menor_mayor = menor_elemento(get_info( get_subsector_especifico(get_sector_con_anio(data_structs,anio,sector_mayor_ingresos_netos["Código sector económico"]), subsector_mayor["Código subsector económico"])),"Total ingresos netos")
    actividad_mayor_menor = mayor_elemento(get_info( get_subsector_especifico(get_sector_con_anio(data_structs,anio,sector_mayor_ingresos_netos["Código sector económico"]), subsector_menor["Código subsector económico"])),"Total ingresos netos")
    actividad_menor_menor = menor_elemento(get_info( get_subsector_especifico(get_sector_con_anio(data_structs,anio,sector_mayor_ingresos_netos["Código sector económico"]), subsector_menor["Código subsector económico"])),"Total ingresos netos")
    
    
    subsector_mayor["Actividad económica que más aportó"] = actividad_mayor_mayor
    subsector_mayor["Actividad económica que menos aportó"] = actividad_menor_mayor
    subsector_menor["Actividad económica que más aportó"] = actividad_mayor_menor
    subsector_menor["Actividad económica que menos aportó"] = actividad_menor_menor
    
    return sector_mayor_ingresos_netos,subsector_mayor,subsector_menor

""" 
FUNCIONES PARA EL REQUERIMIENTO 7
"""

def req_7(data_structs,anio,subsector,top):
    """
    Función que soluciona el requerimiento 7
    """
    top = int(top)
    lista_info_organizada = SortLista(get_info(get_subsector_con_anio(data_structs,anio,subsector)),cmp_menor_Total_costos_gastos)
    
    if lt.size(lista_info_organizada) < top:
        return lista_info_organizada
    else:
        return lt.subList(lista_info_organizada,1,top)   
    
""" 
FUNCIONES PARA EL REQUERIMIENTO 8
"""
def req_8(data_structs,top,anio):
    """
    Función que soluciona el requerimiento 8
    """ 
    top = int(top)
    primera_lista = lt.newList("ARRAY_LIST")
    varias_tablas = lt.newList("ARRAY_LIST")
    for sector in lt.iterator(get_sector_iterator(get_value(data_structs["data"],anio))):
        subsector_mayor = mayor_elemento(lista_subsectores_del_sector_combined(get_subsector_iterator(get_sector_con_anio(data_structs,anio,sector)), get_sector_con_anio(data_structs,anio,sector)),"Total Impuesto a cargo")
        lt.addLast(primera_lista,subsector_mayor)
    
    SortLista(primera_lista,cmp_menor_sector_economico)
    
    for subsector in lt.iterator(primera_lista):
        
        lista_info_organizada = SortLista(get_info(get_subsector_con_anio(data_structs,anio,subsector["Código subsector económico"])),cmp_Total_impuestos_cargo)
        
        if lt.size(lista_info_organizada) < top:
            lt.addLast(varias_tablas,lista_info_organizada)
        else:
            lt.addLast(varias_tablas,lt.subList(lista_info_organizada,1,top))
            
    return primera_lista,varias_tablas



