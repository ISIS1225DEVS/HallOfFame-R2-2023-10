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


def new_data_structs(ds, lf, n):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {"data": None}
    
    # Selecciona la estructura de datos que se quiere usar y el factor de carga para este
    if ds == '1':
        ds = 'CHAINING'
        if lf == '1': lf = 2
        elif lf == '2': lf = 4
        elif lf == '3': lf = 6
        else: lf = 8
    elif ds == '2':
        ds = 'PROBING'
        if lf == '1': lf = 0.1
        elif lf == '2': lf = 0.5
        elif lf == '3': lf = 0.7
        else: lf = 0.9

    data_structs["data"] = mp.newMap(numelements=n,
                                     maptype=ds, 
                                     loadfactor=lf,
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, column, orderingAlg):
    """
    Función para agregar nuevos elementos a la lista
    """    
    # Añade el valor para el año en caso de que no exista
    if mp.contains(data_structs, column['Año']) == False:
        mp.put(data_structs, column['Año'], lt.newList('ARRAY_LIST'))

    # Registra la información de la actividad económica en cuestión en el año correspondiente
    info = me.getValue(mp.get(data_structs, column['Año']))
    lt.addLast(info, column)
    sort(info, orderingAlg, sortCriteria=sort_criteria)
    
    


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, year, id):
    """
    Función que soluciona el requerimiento 1
    """
    actividad = ''
    saldo_ap = 0
    info_año = me.getValue(mp.get(data_structs['data'], year))
    datos = lt.iterator(info_año)
    for i in datos:
        cod = i['Código sector económico']
        if cod == id:
            s = int(i['Total saldo a pagar'])
            if s > saldo_ap:
                actividad = i
                saldo_ap = s
    return actividad


def req_2(data_structs, year, id):
    """
    Función que soluciona el requerimiento 2
    """
    actividad = ''
    saldo_af = 0
    info_año = me.getValue(mp.get(data_structs['data'], year))
    datos = lt.iterator(info_año)
    valid_id = False
    for i in datos:
        cod = i['Código sector económico']
        if cod == id:
            valid_id = True
            s = int(i['Total saldo a favor'])
            if s > saldo_af:
                actividad = i
                saldo_af = s
    if valid_id == False:
        return ''
    return actividad


def req_3(data_structs, year):
    """
    Función que soluciona el requerimiento 3
    """
    map = mp.newMap()
    map['MinNameSub'] = ''
    map['MinTR'] = 0
    i = 0
    for aEconomica in lt.iterator(me.getValue(mp.get(data_structs['data'], year))):
        subsectorName = aEconomica['Nombre subsector económico']
        if not(mp.contains(map, subsectorName)):
            mp.put(map, subsectorName, lt.newList(datastructure='ARRAY_LIST'))
            listI = me.getValue(mp.get(map, subsectorName))
            listI['Nombre sector económico'] = aEconomica['Nombre sector económico']
            listI['Código sector económico'] = aEconomica['Código sector económico']
            listI['Código subsector económico'] = aEconomica['Código subsector económico']
            listI['Nombre subsector económico'] = subsectorName
            listI['Total retenciones'] = 0
            listI['Total ingresos netos'] = 0
            listI['Total costos y gastos'] = 0
            listI['Total saldo a pagar'] = 0
            listI['Total saldo a favor'] = 0
        listI['Total retenciones'] += int(aEconomica['Total retenciones'])
        listI['Total ingresos netos'] += int(aEconomica['Total ingresos netos'])
        listI['Total costos y gastos'] += int(aEconomica['Total costos y gastos'])
        listI['Total saldo a pagar'] += int(aEconomica['Total saldo a pagar'])
        listI['Total saldo a favor'] += int(aEconomica['Total saldo a favor'])
        if i == 0:
            map['MinTR'] = listI['Total retenciones']
        if listI['Total retenciones'] < map['MinTR']:
            map['MinNameSub'] = listI['Nombre subsector económico']
            map['MinTR'] = listI['Total retenciones']
        lt.addLast(listI, aEconomica)  
        i+=1     
    sort(me.getValue(mp.get(map, map['MinNameSub'])), orderingAlg='4', sortCriteria=sort_retenciones)    
    return me.getValue(mp.get(map, map['MinNameSub'])) 


def req_4(data_structs, year):
    """
    Función que soluciona el requerimiento 4
    """
    mapa = mp.newMap()
    mapa['ns'] = ''
    mapa['t'] = 0
    info_año = me.getValue(mp.get(data_structs['data'], year))
    datos = lt.iterator(info_año)
    for i in datos:
        sub = i['Nombre subsector económico']
        if mp.contains(mapa, sub) == False:
            mp.put(mapa, sub, lt.newList(datastructure='ARRAY_LIST'))
            li = me.getValue(mp.get(mapa, sub))
            li['codsec'] = i['Código sector económico']
            li['nomsec'] = i['Nombre sector económico']
            li['codsub'] = i['Código subsector económico']
            li['nomsub'] = sub
            li['totalcyg'] = 0
            li['totaling'] = 0
            li['totalcg'] = 0
            li['totalsp'] = 0
            li['totalsf'] = 0
        lista = me.getValue(mp.get(mapa, sub))
        li['totalcyg'] += int(i['Costos y gastos nómina'])
        li['totaling'] += int(i['Total ingresos netos'])
        li['totalcg'] += int(i['Total costos y gastos'])
        li['totalsp'] += int(i['Total saldo a pagar'])
        li['totalsf'] += int(i['Total saldo a favor'])
        if li['totalcyg'] > mapa['t']:
            mapa['ns'] = li['nomsub']
            mapa['t'] = li['totalcyg']
        lt.addLast(lista, i)
    sorteo = me.getValue(mp.get(mapa, mapa['ns']))
    sort(sorteo, orderingAlg='4', sortCriteria=sort_nomina)
    
    infosubsec = me.getValue(mp.get(mapa, mapa['ns']))    
    return infosubsec


def req_5(data_structs, year):
    """
    Función que soluciona el requerimiento 5
    """
    # Organiza todos los datos del año seleccionado en un nuevo mapa
    nm = mp.newMap(numelements=17, maptype='PROBING', loadfactor=0.5)
    yearInfo = me.getValue(mp.get(data_structs['data'], year))
    for entry in lt.iterator(yearInfo):
        subs = entry['Nombre subsector económico']
        if not(mp.contains(nm, subs)):
            mp.put(nm, subs, {'list':lt.newList(datastructure='ARRAY_LIST'), 
                              'sum':0,
                              'income':0,
                              'spending':0,
                              'debt':0,
                              'profit':0})
        current = me.getValue(mp.get(nm, subs))
        lt.addLast(current['list'], entry)
        current['sum'] += int(entry['Descuentos tributarios'])
        current['income'] += int(entry['Total ingresos netos'])
        current['spending'] += int(entry['Total costos y gastos'])
        current['debt'] += int(entry['Total saldo a pagar'])
        current['profit'] += int(entry['Total saldo a favor'])
            
    # Encuentra el subsector de mayores descuentos tributarios
    most = {'subsector':None,
            'total':0}
    for subsectorName in lt.iterator(mp.keySet(nm)):
        subsector = me.getValue(mp.get(nm, subsectorName))
        if most['total'] < subsector['sum']:
            most['subsector'] = subsectorName
            most['total'] = subsector['sum']
            
    sort(me.getValue(mp.get(nm, most['subsector']))['list'], sortCriteria=sort_withholdings)
    
    return me.getValue(mp.get(nm, most['subsector']))


def req_6(data_structs, year):
    """
    Función que soluciona el requerimiento 6
    """
    mapa = mp.newMap()
    sector = ''
    secmax = 0
    info_año = me.getValue(mp.get(data_structs['data'], year))
    datos = lt.iterator(info_año)
    for i in datos:
        sec = i['Nombre sector económico']
        subsec = i['Código subsector económico']
        if mp.contains(mapa, sec) == False:
            mp.put(mapa, sec, mp.newMap(numelements=2))
            mapa_sector = me.getValue(mp.get(mapa, sec))
            mp.put(mapa_sector, 'infosec', mp.newMap(numelements=11))
            mp.put(mapa_sector, 'subsectores', mp.newMap())
            mapa_infosec = me.getValue(mp.get(mapa_sector, 'infosec'))
            mp.put(mapa_infosec, 'codsec', i['Código sector económico'])
            mp.put(mapa_infosec, 'nomsec', sec)
            mp.put(mapa_infosec, 'totaling', {'ing' : 0})
            mp.put(mapa_infosec, 'totalcg', {'cg' : 0})
            mp.put(mapa_infosec, 'totalsp', {'sp' : 0})
            mp.put(mapa_infosec, 'totalsf', {'sf' : 0})
            mp.put(mapa_infosec, 'submas', i['Código subsector económico'])
            mp.put(mapa_infosec, 'submin', i['Código subsector económico'])
            mp.put(mapa_infosec, 'vmas', int(i['Total ingresos netos']))
            mp.put(mapa_infosec, 'vmin', int(i['Total ingresos netos']))
            
        map_sec = me.getValue(mp.get(mapa, sec))
        mapa_infosec = me.getValue(mp.get(map_sec, 'infosec'))
        total_ingresos = me.getValue(mp.get(mapa_infosec, 'totaling'))
        total_ingresos['ing'] += int(i['Total ingresos netos'])
        total_cg = me.getValue(mp.get(mapa_infosec, 'totalcg'))
        total_cg['cg'] += int(i['Total costos y gastos'])
        total_sp = me.getValue(mp.get(mapa_infosec, 'totalsp'))
        total_sp['sp'] += int(i['Total saldo a pagar'])
        total_sf = me.getValue(mp.get(mapa_infosec, 'totalsf'))
        total_sf['sf'] += int(i['Total saldo a favor'])
        submax = me.getValue(mp.get(mapa_infosec, 'vmas'))
        submin = me.getValue(mp.get(mapa_infosec, 'vmin'))
        mapa_subsectores = me.getValue(mp.get(map_sec, 'subsectores'))
        n = total_ingresos['ing'] 
        if n > secmax:
            secmax = total_ingresos['ing']
            sector = sec
        if mp.contains(mapa_subsectores, subsec) == False:
            mp.put(mapa_subsectores, subsec, mp.newMap(numelements=2))
            mapa_subsector = me.getValue(mp.get(mapa_subsectores, subsec))
            mp.put(mapa_subsector, 'infosubsec', mp.newMap(numelements=11))
            mp.put(mapa_subsector, 'actividades', lt.newList(datastructure='ARRAY_LIST'))
            mapa_infosubsec = me.getValue(mp.get(mapa_subsector, 'infosubsec'))
            mp.put(mapa_infosubsec, 'codsubsec', subsec)
            mp.put(mapa_infosubsec, 'nomsubsec', i['Nombre subsector económico'])
            mp.put(mapa_infosubsec, 'totaling', {'ing': 0})
            mp.put(mapa_infosubsec, 'totalcg', {'cg': 0})
            mp.put(mapa_infosubsec, 'totalsp', {'sp': 0})
            mp.put(mapa_infosubsec, 'totalsf', {'sf': 0})
        mapa_subsector = me.getValue(mp.get(mapa_subsectores, subsec))
        mapa_infosubsec = me.getValue(mp.get(mapa_subsector, 'infosubsec'))
        total_ingresos_sub = me.getValue(mp.get(mapa_infosubsec, 'totaling'))
        total_ingresos_sub['ing'] += int(i['Total ingresos netos'])
        total_cg_sub = me.getValue(mp.get(mapa_infosubsec, 'totalcg'))
        total_cg_sub['cg'] += int(i['Total costos y gastos'])
        total_sp_sub = me.getValue(mp.get(mapa_infosubsec, 'totalsp'))
        total_sp_sub['sp'] += int(i['Total saldo a pagar'])
        total_sf_sub = me.getValue(mp.get(mapa_infosubsec, 'totalsf'))
        total_sf_sub['sf'] += int(i['Total saldo a favor'])    
        
        if total_ingresos_sub['ing'] > submax:
            submax = total_ingresos_sub
            mp.put(mapa_infosec, 'submas', subsec)
        elif total_ingresos_sub['ing'] < submin:
            submin = total_ingresos_sub
            mp.put(mapa_infosec, 'submin', subsec)  
        lista = me.getValue(mp.get(mapa_subsector, 'actividades'))
        lt.addLast(lista, i)
    mapa_sector = me.getValue(mp.get(mapa, sector))    
    mapa_infosec = me.getValue(mp.get(mapa_sector, 'infosec'))
    submas = me.getValue(mp.get(mapa_infosec, 'submas'))   
    submen = me.getValue(mp.get(mapa_infosec, 'submin'))  
    mapa_subsectores = me.getValue(mp.get(mapa_sector, 'subsectores'))
    mapmax = me.getValue(mp.get(mapa_subsectores, submas))
    mapmin = me.getValue(mp.get(mapa_subsectores, submen))
    listmax = me.getValue(mp.get(mapmax, 'actividades'))
    listmin = me.getValue(mp.get(mapmin, 'actividades'))
    sort(listmax, orderingAlg='4', sortCriteria=sort_ingresos)
    sort(listmin, orderingAlg='4', sortCriteria=sort_ingresos)
    
    info = me.getValue(mp.get(mapa, sector))
    return info


def req_7(data_structs, year, id):
    """
    Función que soluciona el requerimiento 7
    """
    actividades = lt.newList(datastructure='ARRAY_LIST')
    info_año = me.getValue(mp.get(data_structs['data'], year))
    datos = lt.iterator(info_año)
    for i in datos:
        cod = i['Código subsector económico']
        if cod == id:
            lt.addLast(actividades,i)
    sort(actividades, orderingAlg='4', sortCriteria=sort_costos_y_gastos)
    return actividades


def req_8(data_structs, year):
    """
    Función que soluciona el requerimiento 8
    """
    mapa = mp.newMap()
    lista_subsectores = lt.newList(datastructure='ARRAY_LIST')
    info_año = me.getValue(mp.get(data_structs['data'], year))
    datos = lt.iterator(info_año)
    for i in datos:
        subsec = i['Código subsector económico']
        if mp.contains(mapa, subsec) == False:
            mp.put(mapa, subsec, lt.newList(datastructure='ARRAY_LIST'))
            lista = me.getValue(mp.get(mapa, subsec))
            lista['codesec'] = i['Código sector económico']
            lista['nomsec'] = i['Nombre sector económico']
            lista['codesubsec'] = subsec
            lista['nomsubsec'] = i['Nombre subsector económico']
            lista['ic'] = 0
            lista['ing'] = 0
            lista['cg'] = 0
            lista['sp'] = 0
            lista['sf'] = 0
        lista = me.getValue(mp.get(mapa, subsec))
        lista['ic'] += int(i['Total Impuesto a cargo'])
        lista['ing'] += int(i['Total ingresos netos'])
        lista['cg'] += int(i['Total costos y gastos'])
        lista['sp'] += int(i['Total saldo a pagar'])
        lista['sf'] += int(i['Total saldo a favor'])
        lt.addLast(lista, i)
    cods = mp.keySet(mapa)
    x = lt.iterator(cods)
    for c in x:
        sub = me.getValue(mp.get(mapa, c))
        sort(sub, orderingAlg='4', sortCriteria=sort_impuestos_a_cargo2)
        lt.addLast(lista_subsectores, sub)
    sort(lista_subsectores, orderingAlg='4', sortCriteria=sort_impuestos_a_cargo)
    
        
    return lista_subsectores

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(key, elem):
    """
    Función encargada de comparar dos datos
    """
    if key > elem['key']:
        return 1
    elif key < elem['key']:
        return -1
    else:
        return 0
    

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data_1 (dict): Diccionario del dato 1 a comparar
        data_2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    l1 = len(data_1['Código actividad económica'])
    l2 = len(data_2['Código actividad económica'])
    
    return ('0' * (4 - l1) + data_1['Código actividad económica']) < ('0' * (4 - l2) + data_2['Código actividad económica'])

def sort_retenciones(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar
    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Total retenciones']) < int(d2['Total retenciones'])

def sort_nomina(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Costos y gastos nómina']) < int(d2['Costos y gastos nómina'])

def sort_ingresos(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Total ingresos netos']) < int(d2['Total ingresos netos'])

def sort_impuestos_a_cargo(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return d1['ic'] > d2['ic']

def sort_impuestos_a_cargo2(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return d1['Total Impuesto a cargo'] > d2['Total Impuesto a cargo']

def sort_costos_y_gastos(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Total costos y gastos']) < int(d2['Total costos y gastos'])

def sort_withholdings(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Descuentos tributarios']) < int(d2['Descuentos tributarios'])

def sort(data_structs, orderingAlg='1', sortCriteria=sort_criteria):
    """
    Función encargada de ordenar la lista con los datos
    """
    if orderingAlg == '1':
        ins.sort(data_structs, sortCriteria)
    elif orderingAlg == '2':
        se.sort(data_structs, sortCriteria)
    elif orderingAlg == '3':
        sa.sort(data_structs, sortCriteria)
    elif orderingAlg == '4':
        merg.sort(data_structs, sortCriteria)
    elif orderingAlg == '5':
        quk.sort(data_structs, sortCriteria)
