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


def new_data_structs(mt, lF):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {
        'impuestos':None,
        'anio': None,
    }
    data_structs['impuestos'] = lt.newList('ARRAY_LIST')
    data_structs['anio'] = mp.newMap(10,
                                   maptype= mt,
                                   loadfactor=lF,
                                   cmpfunction=compareMapYear)
    data_structs['anioSUBSEC'] = mp.newMap(22,
                                   maptype= mt,
                                   loadfactor=lF,
                                   cmpfunction=compareMapYear)
    data_structs['anioSEC'] = mp.newMap(22,
                                   maptype= mt,
                                   loadfactor=lF,
                                   cmpfunction=compareMapYear)
    data_structs['anio_SEC_SUBSEC'] = mp.newMap(22,
                                   maptype= mt,
                                   loadfactor=lF,
                                   cmpfunction=compareMapYear)
    return data_structs


# Funciones para agregar informacion al modelo

def add_register(data_structs, data):
    
    '''
    Funcion que añade la informacion de cada mapa a data_structs
    
    '''
    
    lt.addLast(data_structs['impuestos'], data)
    add_registerYear(data_structs,data)
    add_registerYearSubsec(data_structs,data)
    add_registerYearSec(data_structs,data)
    add_registerYearSecSubSec(data_structs,data)
    
def add_registerYear(data_structs,data):
    
    '''
    Añade la informacion al mapa de años
    '''
    
    try:
        years = data_structs['anio']
        impYear = data['Año']
        impYear = int(float(impYear))

        existyear = mp.contains(years, impYear)
        if existyear:
            entry = mp.get(years, impYear)
            year = me.getValue(entry)
        else:
            year = newYear(impYear)
            mp.put(years, impYear, year)
        lt.addLast(year['impuesto'], data)
    except Exception:
        return None

def add_registerYearSubsec(data_structs,data):
    
    '''
    Añade la informacion al mapa de años-subsectores
    '''
    
    try:
        years = data_structs['anioSUBSEC']
        impYear = data['Año']
        impCode = data['Código subsector económico']
        impYearCode = ""
        impYearCode = impYear+","+impCode
    
        existyear = mp.contains(years, impYearCode)
        if existyear:
            entry = mp.get(years, impYearCode)
            year = me.getValue(entry)
        else:
            year = newYear(impYearCode)
            mp.put(years, impYearCode, year)
        lt.addLast(year['impuesto'], data)
    except Exception:
        return None

    
def add_registerYearSec(data_structs,data):
    
    '''
    Añade la informacion al mapa de años-sectores
    
    '''
    
    
    try:
        years = data_structs['anioSEC']
        impYear = data['Año']
        impCode = data['Código sector económico']
        impYearCode = ""
        impYearCode = impYear+","+impCode
    
        existyear = mp.contains(years, impYearCode)
        if existyear:
            entry = mp.get(years, impYearCode)
            year = me.getValue(entry)
        else:
            year = newYear(impYearCode)
            mp.put(years, impYearCode, year)
        lt.addLast(year['impuesto'], data)
    except Exception:
        return None
def add_registerYearSecSubSec(data_structs,data):
    
    '''
    Añade la informacion al mapa de años-sectores-subsectores
    
    '''
    
    try:
        years = data_structs['anio_SEC_SUBSEC']
        impYear = data['Año']
        impCode = data['Código sector económico']
        impCode2 = data['Código subsector económico']
        impYearCode = ""
        impYearCode = impYear+","+impCode+","+impCode2
    
        existyear = mp.contains(years, impYearCode)
        if existyear:
            entry = mp.get(years, impYearCode)
            year = me.getValue(entry)
        else:
            year = newYear(impYearCode)
            mp.put(years, impYearCode, year)
        lt.addLast(year['impuesto'], data)
    except Exception:
        return None    
    
    
def newYear(impYear):
    """
    Esta funcion crea un año basado en un dato asociado.
    """
    entry = {'anio': "", 'impuesto': None}
    entry['anio'] = impYear
    entry['impuesto'] = lt.newList('ARRAY_LIST', compareYears)
    return entry


#----------funcion que recorta una lista con sus primeros 3 y ultimos 3 valores------#

def recortarLista(list):
    
    '''
    Funcion que retorna los primeros 3 y los ultimos 3 elementos de una lista dada.
    '''
    
    filtrado = lt.newList() #Lista que contiene las 3 primeras y las 3 ultimas
    first = lt.subList(list, 1, 3) #Mis tres primeros datos
    threelast =lt.size(list)-3 #Mis ultimos 3 datos  
    last = lt.subList(list, threelast+1, 3) #Sublista con los 3 ultimos 
    
    for element in lt.iterator(first): #Ciclo que une los tres primeros elementos
        lt.addLast(filtrado, element)
        
    for element in lt.iterator(last): #Ciclo que une los ultimos tres elementos
        lt.addLast(filtrado, element)
    return filtrado


#funcion que obtiene una lista de un mapa

def ListaFromMap(map):
    f = lt.newList('ARRAY_LIST')
    keys = mp.keySet(map)
    for i in lt.iterator(keys):
        if i != None:
            x = (i, me.getValue(mp.get(map,i)))
            lt.addLast(f,x)
    return f 

#----------------------------------------------------------------------------------#    

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

#-----Funciones utilizadas en el req 1----------#

def req_1(data_structs,yearIn, codeEcoIn):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    impuestosSorted = sortTaxbyYearSAP(data_structs, yearIn)
    listaImpustosCodigoDeseado = lt.newList('ARRAY_LIST')
    respuesta = lt.newList('ARRAY_LIST')
    for impuesto in lt.iterator(impuestosSorted):
        if codeEcoIn == int(impuesto['Código sector económico']):
            lt.addLast(listaImpustosCodigoDeseado, impuesto)
    mayordeseado = lt.getElement(listaImpustosCodigoDeseado, 1)
    lt.addLast(respuesta, mayordeseado)
    return respuesta


def compareSaldoAPagar(impuesto1, impuesto2):
    '''
    Funcion que retorna True si el saldo a pagar de la actividad economica de un impuesto1 es menor que el del impuesto2.
    
    Ademas verifica si dicho valor es numerico.
    '''  
    if impuesto1['Total saldo a pagar'].isnumeric() and impuesto2['Total saldo a pagar'].isnumeric():
        return int(impuesto1['Total saldo a pagar']) > int(impuesto2['Total saldo a pagar'])
    
    
def sortTaxbyYearSAP(data_structs, yearIn):
    
    '''
    Funcion que retorna una lista de impuestos ordenados por año y por saldo a pagar
    '''
    mapa_year = mp.get(data_structs['anio'], yearIn)
    
    if mapa_year:
        year_taxes = me.getValue(mapa_year)['impuesto']
        lista_ordenada = useMergeSort(year_taxes, compareSaldoAPagar)
    
    return lista_ordenada

#----------------------------------------------------------------#

#-----------Funciones utlizadas para el req 2--------------------#
def req_2(data_structs, yearIn, codeEcoIn):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    
    impuestosSorted = sortTaxbyYearSAF(data_structs, yearIn)
    listaImpustosCodigoDeseado = lt.newList('ARRAY_LIST')
    respuesta = lt.newList('ARRAY_LIST')
    for impuesto in lt.iterator(impuestosSorted):
        if codeEcoIn == int(impuesto['Código sector económico']):
            lt.addLast(listaImpustosCodigoDeseado, impuesto)
    mayordeseado = lt.getElement(listaImpustosCodigoDeseado, 1)
    lt.addLast(respuesta, mayordeseado)
    return respuesta


def compareSaldoAFavor(impuesto1, impuesto2):
    '''
    Funcion que retorna True si el saldo a pagar de la actividad economica de un impuesto1 es menor que el del impuesto2.
    
    Ademas verifica si dicho valor es numerico.
    '''  
    if impuesto1['Total saldo a favor'].isnumeric() and impuesto2['Total saldo a favor'].isnumeric():
        return int(impuesto1['Total saldo a favor']) > int(impuesto2['Total saldo a favor'])
    
def sortTaxbyYearSAF(data_structs, yearIn):
    
    '''
    Funcion que retorna una lista de impuestos ordenados por año y por saldo a favor
    '''
    mapa_year = mp.get(data_structs['anio'], yearIn)
    
    if mapa_year:
        year_taxes = me.getValue(mapa_year)['impuesto']
        lista_ordenada = useMergeSort(year_taxes, compareSaldoAFavor)
    
    return lista_ordenada

#---------------------------------------------------------------#

#--------------Funciones utilizadas para el req 3--------------#
    
    
def req_3(data_structs, yearIn, headers):
    
    '''
    Funcion que retorna una lista de impuestos ordenados por año y por saldo a favor
    
    Soluciona el req 3    
    '''
    
    #Lista de los subsectores del año que entra por parametro
    mapa = data_structs['anioSUBSEC']
    llaves = mp.keySet(mapa)
    listaSubSectores = lt.newList('ARRAY_LIST')
    for llave in lt.iterator(llaves):
        if (yearIn in llave) == True:
            impuesto = mp.get(mapa, llave)
            lt.addLast(listaSubSectores, impuesto)
    
    #Mapa que realiza las acumulaciones 
    
    lista_r1 = lt.newList('ARRAY_LIST')
    pos_min = 1
    pos = 1
    min_ = 10000000000000000000
    for tax in lt.iterator(listaSubSectores):
        mapaTemporal = mp.newMap(10, maptype='PROBING', loadfactor=0.7)
        for fila in headers:
            mp.put(mapaTemporal, fila, 0)
        for data in lt.iterator(tax['value']['impuesto']):                
            if me.getValue(mp.get(mapaTemporal, 'Código sector económico')) == 0:
                mp.put(mapaTemporal,'Código sector económico',data['Código sector económico'])
                mp.put(mapaTemporal,'Nombre sector económico',data['Nombre sector económico'])
                mp.put(mapaTemporal,'Código subsector económico',data['Código subsector económico'])
                mp.put(mapaTemporal,'Nombre subsector económico',data['Nombre subsector económico'])
            mp.put(mapaTemporal,'Total retenciones',me.getValue(mp.get(mapaTemporal,'Total retenciones'))+int(data['Total retenciones']))
            mp.put(mapaTemporal,'Total ingresos netos',me.getValue(mp.get(mapaTemporal,'Total ingresos netos'))+int(data['Total ingresos netos']))
            mp.put(mapaTemporal,'Total costos y gastos',me.getValue(mp.get(mapaTemporal,'Total costos y gastos'))+int(data['Total costos y gastos']))
            mp.put(mapaTemporal,'Total saldo a pagar',me.getValue(mp.get(mapaTemporal,'Total saldo a pagar'))+int(data['Total saldo a pagar']))
            mp.put(mapaTemporal,'Total saldo a favor',me.getValue(mp.get(mapaTemporal,'Total saldo a favor'))+int(data['Total saldo a favor']))
        lt.addLast(lista_r1, mapaTemporal)
        if min_ > me.getValue(mp.get(mapaTemporal, 'Total retenciones')):
            min_ = me.getValue(mp.get(mapaTemporal, 'Total retenciones'))
            pos_min = pos
        pos += 1
    
    respuesta1 = lt.getElement(lista_r1, pos_min)
    respuesta2 = listaFromMapReq3(respuesta1)
    
    codeMin = me.getValue(mp.get(respuesta1, 'Código subsector económico'))
    listaActividades = (me.getValue(mp.get(mapa,yearIn+","+str(codeMin))))['impuesto']
    listaActividadesSorted = useMergeSort(listaActividades, compareRetencionTotal)
    flag = None
    
    if lt.size(listaActividadesSorted) > 6:
        listaActividadesSorted = recortarLista(listaActividadesSorted)
        flag = True
    else: 
        listaActividadesSorted = listaActividades
        flag = False
      
    return respuesta2, flag, listaActividadesSorted, codeMin

def listaFromMapReq3(mapa):
    
    '''
    Crea una lista desde el mapa utilizado en el requerimiento 3
    '''
    
    respuesta2 = lt.newList('ARRAY_LIST')
    llaves = mp.keySet(mapa)
    for llave in lt.iterator(llaves):
        if llave != None:
            valor = (llave, me.getValue(mp.get(mapa, llave)))
            lt.addLast(respuesta2, valor)
    return respuesta2
        
def compareRetencionTotal(impuesto1, impuesto2):
    '''
    Funcion que retorna True si la retencion total de la actividad economica de un impuesto1 es menor que el del impuesto2.
    
    Ademas verifica si dicho valor es numerico.
    '''  
    return int(impuesto1['Total retenciones']) < int(impuesto2['Total retenciones'])
#--------------------------------------------------------------#

#-----------------funciones que soluciones el req 4------------------------------------#


def req_4(data_structs,anio,headers):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    #lista con los subsectores de un anio
    map = data_structs['anioSUBSEC']
    llaves  = mp.keySet(map)
    listaSS = lt.newList('ARRAY_LIST')
    for i in lt.iterator(llaves):
        if (anio in i) == True:
            imp = mp.get(map,i)
            lt.addLast(listaSS, imp)
    #acumilaciones
    '''
    headers=['Código sector económico','Nombre sector económico','Código subsector económico',
                         'Nombre subsector económico','Costos y gastos nómina','Total ingresos netos',
                         'Total costos y gastos','Total saldo a pagar','Total saldo a favor'] 
    '''
    #mapa 
    r1 = lt.newList('ARRAY_LIST')
    pos_max = 1
    pos = 1 
    max_ = 0
    for i in lt.iterator(listaSS):
        mapA = mp.newMap(10,maptype='PROBING',loadfactor=0.7)
        for j in headers: 
            mp.put(mapA,j,0)
        for k in lt.iterator(i['value']['impuesto']):
            if me.getValue(mp.get(mapA,'Código subsector económico'))==0:
                mp.put(mapA,'Código sector económico',k['Código sector económico'])
                mp.put(mapA,'Nombre sector económico',k['Nombre sector económico'])
                mp.put(mapA,'Código subsector económico',k['Código subsector económico'])
                mp.put(mapA,'Nombre subsector económico',k['Nombre subsector económico'])
            mp.put(mapA,'Costos y gastos nómina',me.getValue(mp.get(mapA,'Costos y gastos nómina'))+int(k['Costos y gastos nómina']))
            mp.put(mapA,'Total ingresos netos',me.getValue(mp.get(mapA,'Total ingresos netos'))+int(k['Total ingresos netos']))
            mp.put(mapA,'Total costos y gastos',me.getValue(mp.get(mapA,'Total costos y gastos'))+int(k['Total costos y gastos']))
            mp.put(mapA,'Total saldo a pagar',me.getValue(mp.get(mapA,'Total saldo a pagar'))+int(k['Total saldo a pagar']))
            mp.put(mapA,'Total saldo a favor',me.getValue(mp.get(mapA,'Total saldo a favor'))+int(k['Total saldo a favor']))
        lt.addLast(r1,mapA)
        if max_ < me.getValue(mp.get(mapA,'Costos y gastos nómina')):
                max_ = me.getValue(mp.get(mapA,'Costos y gastos nómina'))
                pos_max = pos
        pos += 1  
        rta1 = lt.getElement(r1, pos_max)
        rta2 = ListaFromMap(rta1)
    codeMAX =  me.getValue(mp.get(rta1,'Código subsector económico'))
    listaActs =  (me.getValue(mp.get(map,anio+","+str(codeMAX))))['impuesto']
    listaActsOrd = useMerge(listaActs, cmp_req_4)
    flag = None
    if lt.size(listaActsOrd) > 6:
        listaActsOrdRect = recortarLista(listaActsOrd)
        flag = True
    else:
        listaActsOrdRect = listaActsOrd
        flag = False
    return rta2, flag, listaActsOrdRect, codeMAX


    
def cmp_req_4(impuesto1, impuesto2):
    '''
    Funcion que retorna True si los costos y gastos nómina de un impuesto1 es menor que el del impuesto2.
    
    ''' 
    return int(impuesto1['Costos y gastos nómina']) < int(impuesto2['Costos y gastos nómina'])

#---------------------------------------------------------------------------------------------------------------#


#--------------------------------Funciones que soluciones el req 5-----------------------------------------------#


def req_5(data_structs, anio, headers):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    #lista con los subsectores de un anio
    map = data_structs['anioSUBSEC']
    llaves  = mp.keySet(map)
    listaSS = lt.newList('ARRAY_LIST')
    for i in lt.iterator(llaves):
        if (anio in i) == True:
            imp = mp.get(map,i)
            lt.addLast(listaSS, imp)
    #mapa 
    r1 = lt.newList('ARRAY_LIST')
    pos_max = 1
    pos = 1 
    max_ = 0
    for i in lt.iterator(listaSS):
        mapA = mp.newMap(10,maptype='PROBING',loadfactor=0.7)
        for j in headers: 
            mp.put(mapA,j,0)
        for k in lt.iterator(i['value']['impuesto']):
            if me.getValue(mp.get(mapA,'Código subsector económico'))==0:
                mp.put(mapA,'Código sector económico',k['Código sector económico'])
                mp.put(mapA,'Nombre sector económico',k['Nombre sector económico'])
                mp.put(mapA,'Código subsector económico',k['Código subsector económico'])
                mp.put(mapA,'Nombre subsector económico',k['Nombre subsector económico'])
            mp.put(mapA,'Descuentos tributarios',me.getValue(mp.get(mapA,'Descuentos tributarios'))+int(k['Descuentos tributarios']))
            mp.put(mapA,'Total ingresos netos',me.getValue(mp.get(mapA,'Total ingresos netos'))+int(k['Total ingresos netos']))
            mp.put(mapA,'Total costos y gastos',me.getValue(mp.get(mapA,'Total costos y gastos'))+int(k['Total costos y gastos']))
            mp.put(mapA,'Total saldo a pagar',me.getValue(mp.get(mapA,'Total saldo a pagar'))+int(k['Total saldo a pagar']))
            mp.put(mapA,'Total saldo a favor',me.getValue(mp.get(mapA,'Total saldo a favor'))+int(k['Total saldo a favor']))
        lt.addLast(r1,mapA)
        if max_ < me.getValue(mp.get(mapA,'Descuentos tributarios')):
                max_ = me.getValue(mp.get(mapA,'Descuentos tributarios'))
                pos_max = pos
        pos += 1  
        rta1 = lt.getElement(r1, pos_max)
        rta2 = ListaFromMap(rta1)
    codeMAX =  me.getValue(mp.get(rta1,'Código subsector económico'))
    listaActs =  (me.getValue(mp.get(map,anio+","+str(codeMAX))))['impuesto']
    listaActsOrd = useMerge(listaActs, cmp_req_5)
    flag = None
    if lt.size(listaActsOrd) > 6:
        listaActsOrdRect = recortarLista(listaActsOrd)
        flag = True
    else:
        listaActsOrdRect = listaActsOrd
        flag = False
    return rta2, flag, listaActsOrdRect, codeMAX

def cmp_req_5(impuesto1, impuesto2):
    
    '''
    Funcion que retorna True si los descuentros tributarios de un impuesto1 es menor que el del impuesto2.
    
    ''' 
    
    return int(impuesto1['Descuentos tributarios']) < int(impuesto2['Descuentos tributarios'])

#---------------Funciones utilizadas para el req 6----#

def req_6(data_structs, anio,headers, headers2):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    map = data_structs['anioSEC']
    llaves  = mp.keySet(map)
    listaSS = lt.newList('ARRAY_LIST')
    for i in lt.iterator(llaves):
        if (anio in i) == True:
            imp = mp.get(map,i)
            lt.addLast(listaSS, imp)
    #acumilaciones
    '''
    headers = ['Código sector económico', 'Nombre sector económico','Total ingresos netos', 
            'Total costos y gastos','Total saldo a pagar', 'Total saldo a favor','Subsector que mas aporto','Subsector que menos aporto']
    '''
    #mapa 
    r1 = lt.newList('ARRAY_LIST')
    pos_max = 1
    pos = 1 
    max_ = 0
    for i in lt.iterator(listaSS):
        mapA = mp.newMap(10,maptype='PROBING',loadfactor=0.7)
        for j in headers: 
            mp.put(mapA,j,0)
        for k in lt.iterator(i['value']['impuesto']):
            if me.getValue(mp.get(mapA,'Código sector económico'))==0:
                mp.put(mapA,'Código sector económico',k['Código sector económico'])
                mp.put(mapA,'Nombre sector económico',k['Nombre sector económico'])
            mp.put(mapA,'Total ingresos netos',me.getValue(mp.get(mapA,'Total ingresos netos'))+int(k['Total ingresos netos']))
            mp.put(mapA,'Total costos y gastos',me.getValue(mp.get(mapA,'Total costos y gastos'))+int(k['Total costos y gastos']))
            mp.put(mapA,'Total saldo a pagar',me.getValue(mp.get(mapA,'Total saldo a pagar'))+int(k['Total saldo a pagar']))
            mp.put(mapA,'Total saldo a favor',me.getValue(mp.get(mapA,'Total saldo a favor'))+int(k['Total saldo a favor']))
        lt.addLast(r1,mapA)
        if max_ < me.getValue(mp.get(mapA,'Total ingresos netos')):
                max_ = me.getValue(mp.get(mapA,'Total ingresos netos'))
                pos_max = pos
        pos += 1  
        rta1 = lt.getElement(r1, pos_max)
    codeMAX =  me.getValue(mp.get(rta1,'Código sector económico')) 
    #,ActMxSSma, ActMxSSmi, ActMiSSma, ActMiSSmi    
    code2max, code2min, subSecmax, subSecmin =  req6_p2(data_structs, anio, headers2,codeMAX)
    mp.put(rta1,'Subsector que mas aporto',code2max)
    mp.put(rta1,'Subsector que menos aporto',code2min)
    rta2 = ListaFromMap(rta1)
    
    return rta2, subSecmax, subSecmin

def req6_p2(data_structs, anio, headers,codeMAX):
    map = data_structs['anio_SEC_SUBSEC']
    llaves  = mp.keySet(map)
    listaSS = lt.newList('ARRAY_LIST')
    for i in lt.iterator(llaves):
        if (anio+","+codeMAX in i) == True:
            imp = mp.get(map,i)
            lt.addLast(listaSS, imp)
    #acumilaciones
    '''
     headers2 = ['Código subsector económico','Nombre subsector económico','Total ingresos netos',
                         'Total costos y gastos','Total saldo a pagar','Total saldo a favor', 'Actividad economica que mas aporto', 'Actividad economica que menos aporto']  
    '''
    #mapa 
    r1 = lt.newList('ARRAY_LIST')
    pos_max = 1
    pos = 1 
    max_ = 0
    #------
    pos_min = 1 
    pos2 = 1
    min_= 100_000_000_000_000
    for i in lt.iterator(listaSS):
        mapA = mp.newMap(10,maptype='PROBING',loadfactor=0.7)
        for j in headers: 
            mp.put(mapA,j,0)
        for k in lt.iterator(i['value']['impuesto']):
            if me.getValue(mp.get(mapA,'Código subsector económico'))==0:
                mp.put(mapA,'Código subsector económico',k['Código subsector económico'])
                mp.put(mapA,'Nombre subsector económico',k['Nombre subsector económico'])
            mp.put(mapA,'Total ingresos netos',me.getValue(mp.get(mapA,'Total ingresos netos'))+int(k['Total ingresos netos']))
            mp.put(mapA,'Total costos y gastos',me.getValue(mp.get(mapA,'Total costos y gastos'))+int(k['Total costos y gastos']))
            mp.put(mapA,'Total saldo a pagar',me.getValue(mp.get(mapA,'Total saldo a pagar'))+int(k['Total saldo a pagar']))
            mp.put(mapA,'Total saldo a favor',me.getValue(mp.get(mapA,'Total saldo a favor'))+int(k['Total saldo a favor']))
        lt.addLast(r1,mapA)
        if max_ < me.getValue(mp.get(mapA,'Total ingresos netos')):
                max_ = me.getValue(mp.get(mapA,'Total ingresos netos'))
                pos_max = pos
        pos += 1  
        if min_ > me.getValue(mp.get(mapA,'Total ingresos netos')):
                min_ = me.getValue(mp.get(mapA,'Total ingresos netos'))
                pos_min = pos2
        pos2 += 1  
        rta1_p2 = lt.getElement(r1, pos_max)
        rta1_1 = lt.getElement(r1, pos_min)
    codeMAX2 =  me.getValue(mp.get(rta1_p2,'Código subsector económico'))
    codeMIN =  me.getValue(mp.get(rta1_1,'Código subsector económico'))
    listaActs =  (me.getValue(mp.get(map,anio+","+codeMAX+","+str(codeMAX2))))['impuesto']
    listaActs2 =  (me.getValue(mp.get(map,anio+","+codeMAX+","+str(codeMIN))))['impuesto']
    listaActsOrd = useMerge(listaActs, cmp_req_6)
    listaActsOrd2 = useMerge(listaActs2, cmp_req_6)
    mp.put(rta1_p2,'Actividad economica que mas aporto',lt.firstElement(listaActsOrd))
    mp.put(rta1_p2,'Actividad economica que menos aporto',lt.lastElement(listaActsOrd))
    mp.put(rta1_1,'Actividad economica que mas aporto',lt.firstElement(listaActsOrd2))
    mp.put(rta1_1,'Actividad economica que menos aporto',lt.lastElement(listaActsOrd2))
    rta2 = ListaFromMap(rta1_p2)
    rta2_1 = ListaFromMap(rta1_1)
    return  codeMAX2, codeMIN,rta2, rta2_1

def cmp_req_6(impuesto1, impuesto2):
    
    '''

    Funcion que retorna True si los ingresos netos de un impuesto1 es mayor que el del impuesto2.
    
 
    '''
    
    return int(impuesto1['Total ingresos netos']) > int(impuesto2['Total ingresos netos'])


def req_7(data_structs, SS, anio,top):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    map = data_structs['anioSUBSEC']
    KEY = anio+","+SS
    imp = mp.get(map,KEY)
    lista1 = me.getValue(imp)
    lista2 = lista1['impuesto']
    lista3 = useMerge(lista2, cmp_req_7_tot)
    flag = None
    if int(top) <= lt.size(lista3):
        lista4 = lt.subList(lista3,1,int(top))
        flag = True
        return lista4, flag
    else: 
        flag = False
        return lista3, flag
    
    
def cmp_req_7(impuesto1, impuesto2):
    
    '''
    Funcion que retorna True si los Total costos y gastos de un impuesto1 es menor que el del impuesto2.
    '''
    
    return int(impuesto1['Total costos y gastos']) < int(impuesto2['Total costos y gastos'])
def cmp_req_7_1(impuesto1, impuesto2):
    return int(impuesto1['Código actividad económica']) > int(impuesto2['Código actividad económica'])
def cmp_req_7_tot(impuesto1, impuesto2):
    """
    Devuelve verdadero si el año de impuesto1 es menor que el de impuesto2 en el caso de que
    sean iguales, se revisa el código de actividad ecoonómica, de lo contrario retorna false.
    
    Arg:
    
    Impuesto1: Información del primer registro que incluye el año y el código de la actividad economica
    Impuesto2: Información del primer registro que incluye el año y el código de la actividad economica
    """
    if int(impuesto1['Año']) == int(impuesto2['Año']):
        return cmp_req_7(impuesto1, impuesto2)
    else:
        return cmp_req_7_1(impuesto1, impuesto2)

def req_8(data_structs, anio,headers,TOP):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    map = data_structs['anioSUBSEC']
    llaves  = mp.keySet(map)
    listaSS = lt.newList('ARRAY_LIST')
    for i in lt.iterator(llaves):
        if (anio in i) == True:
            imp = mp.get(map,i)
            lt.addLast(listaSS, imp)
    #acumilaciones
    '''
    headers=['Código sector económico','Nombre sector económico','Código subsector económico',
                         'Nombre subsector económico','Costos y gastos nómina','Total ingresos netos',
                         'Total costos y gastos','Total saldo a pagar','Total saldo a favor'] 
    '''
    #mapa 
    r1 = lt.newList('ARRAY_LIST')

    for i in lt.iterator(listaSS):
        mapA = mp.newMap(10,maptype='PROBING',loadfactor=0.7)
        for j in headers: 
            mp.put(mapA,j,0)
        for k in lt.iterator(i['value']['impuesto']):
            if me.getValue(mp.get(mapA,'Código subsector económico'))==0:
                mp.put(mapA,'Código sector económico',k['Código sector económico'])
                mp.put(mapA,'Nombre sector económico',k['Nombre sector económico'])
                mp.put(mapA,'Código subsector económico',k['Código subsector económico'])
                mp.put(mapA,'Nombre subsector económico',k['Nombre subsector económico'])
            mp.put(mapA,'Total Impuesto a cargo',me.getValue(mp.get(mapA,'Total Impuesto a cargo'))+int(k['Total Impuesto a cargo']))
            mp.put(mapA,'Total ingresos netos',me.getValue(mp.get(mapA,'Total ingresos netos'))+int(k['Total ingresos netos']))
            mp.put(mapA,'Total costos y gastos',me.getValue(mp.get(mapA,'Total costos y gastos'))+int(k['Total costos y gastos']))
            mp.put(mapA,'Total saldo a pagar',me.getValue(mp.get(mapA,'Total saldo a pagar'))+int(k['Total saldo a pagar']))
            mp.put(mapA,'Total saldo a favor',me.getValue(mp.get(mapA,'Total saldo a favor'))+int(k['Total saldo a favor']))
        lt.addLast(r1,mapA)

    listaMapsOrd = useMerge(r1, cmp_req_8 )
    listaRespuesta = lt.newList("ARRAY_LIST") 
    listarespuesta2 = lt.newList("ARRAY_LIST")
    LC = lt.newList("ARRAY_LIST")
    for i in lt.iterator(listaMapsOrd):
        lt.addLast(listaRespuesta,ListaFromMap(i))
        codigoSS = me.getValue(mp.get(i,'Código subsector económico'))
        lt.addLast(LC, codigoSS)
        listaActs = (me.getValue(mp.get(map,anio+","+str(codigoSS))))['impuesto']
        listaActsOrd = useMerge(listaActs, cmp_req_8_1)
        if lt.size(listaActsOrd) >= int(TOP):
            listaActsOrd2 = lt.subList(listaActsOrd,1,int(TOP))
        else:
            listaActsOrd2 = listaActsOrd
        flag = None
        if int(TOP) >= 12:
            if lt.size(listaActsOrd2) > 6:
                listaActsOrdRect = recortarLista(listaActsOrd2)
                flag = True
            else:
                listaActsOrdRect = listaActsOrd2
                flag = False
            lt.addLast(listarespuesta2,listaActsOrdRect)
        else:
            listaActsOrdRect = listaActsOrd2
            flag = False
            lt.addLast(listarespuesta2,listaActsOrdRect)
    return listaRespuesta, listarespuesta2, flag, LC #rta2, flag, listaActsOrdRect, codeMAX


def cmp_req_8(impuesto1, impuesto2):
    
    '''
    Funcion que retorna True si los Total Impuesto a cargo de un impuesto1 es mayor que el del impuesto2.
    '''
    return int(me.getValue(mp.get(impuesto1,'Total Impuesto a cargo'))) > int(me.getValue(mp.get(impuesto2,'Total Impuesto a cargo')))
def cmp_req_8_1(impuesto1, impuesto2):
    return int(impuesto1['Total Impuesto a cargo']) > int(impuesto2['Total Impuesto a cargo'])

# Funciones utilizadas para comparar elementos dentro de una lista


def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

#Funciones de comparacion generales 

def compareCodeActEco(impuesto1, impuesto2):
    try:
        return int(impuesto1['Código actividad económica']) < int(impuesto2['Código actividad económica'])
    except:
        return (impuesto1['Código actividad económica']) < (impuesto2['Código actividad económica'])

def compareAno2(impuesto1, impuesto2):
    return int(impuesto1) < int(impuesto2)


# Funciones de comparacion utilizadas en los mapas 

def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return -1
def compareSubSector(subcode1, subcode2):
    if (int(subcode1) == int(subcode2)):
        return 0
    elif (int(subcode1) > int(subcode2)):
        return 1
    else:
        return -1

def compareMapYear(year, impuesto):
    taxentry = me.getKey(impuesto)
    if (year == taxentry):
        return 0
    elif (year > taxentry):
        return 1
    else:
        return -1

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass




#Funciones de ordenamiento

def useSelectionSort(lista, criterio):
    return se.sort(lista, criterio) 

def useInsertionSort(lista, criterio):
    return ins.sort(lista, criterio) 

def useShellSort(lista, criterio):
    return sa.sort(lista, criterio) 

def useMergeSort(lista, criterio):
    return merg.sort(lista, criterio)

def useQuickSort(lista, criterio):
    return quk.sort(lista, criterio)

def useMerge(lista, F):
    if F == 1: 
        comp = compareCodeActEco
        return merg.sort(lista, comp)
    if F == 2:
        comp = compareAno2
        return merg.sort(lista, comp)

    else: 
        return merg.sort(lista, F)