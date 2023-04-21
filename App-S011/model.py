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
# #Global Variables
codes_sector=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
codes_sub_sector=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')

# Construccion de modelos

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """#numlements=10   #loadfactor=1
    #TODO: Inicializar las estructuras de datos
    data_structs={'data':mp.newMap(numelements=10,loadfactor=1,maptype='PROBING')}
    return data_structs

# Funciones para agregar informacion al modelo
def add_data(data_structs,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    if mp.contains(data_structs['model']['data'],data['Año']):
        lt.addLast(mp.get(data_structs['model']['data'],data['Año'])['value'],data)
    else:
        value=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(value,data)
        mp.put(data_structs['model']['data'],data['Año'],value)

    return data_structs

# Funciones para creacion de datos
def req_1_2(data_structs,year,code_sector,cmp_function):
    """
    Función que soluciona el requerimiento 1_2
    """
    # TODO: Realizar el requerimiento 1
    for i in lt.iterator(data_structs['model']['data']['table']):
        if i['key']==str(year):
            for j in lt.iterator(sort(i['value'],cmp_function)):
                if code_sector==j['Código sector económico']:
                    return j
                                
def req_1(data_structs,year,code_sector):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    return req_1_2(data_structs,year,code_sector,cmp_req1)
    
def req_2(data_structs,year,code_sector):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    return req_1_2(data_structs,year,code_sector,cmp_req2)

def req_3_4_5(data_structs,year,cmp_function,cmp_function_dict,condition_1,condition_2):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    list_by_code_best_dict=lt.newList(datastructure='ARRAY_LIST')
    list_by_code_general=lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(data_structs['model']['data']['table']):
        if i['key']==year:
            for j in codes_sector:
                list_by_code=lt.newList(datastructure='ARRAY_LIST')
                list_by_code['key']=j
                for k in codes_sub_sector:
                    list_by_code_sub=lt.newList(datastructure="ARRAY_LIST")
                    list_by_code_sub['key']=k
                    for l in lt.iterator(i['value']):
                        if l['Año']==str(year) and l['Código sector económico']==j and l['Código subsector económico']==k:
                            lt.addFirst(list_by_code_sub,l)
                    if list_by_code_sub['size']!=0:
                        dict_={'Código sector económico':j,'Nombre sector económico':lt.firstElement(list_by_code_sub)['Nombre sector económico'],'Código subsector económico':k,'Nombre subsector económico':lt.firstElement(list_by_code_sub)['Nombre subsector económico'],condition_1:0,'Total ingresos netos del subsector económico':0,'Total costos y gastos del subsector económico':0,'Total saldo a pagar del subsector económico':0,'Total saldo a favor del subsector económico':0}
                        for q in lt.iterator(list_by_code_sub):
                            dict_[condition_1]+=int(q[condition_2])
                            dict_['Total ingresos netos del subsector económico']+=int(q['Total ingresos netos'])
                            dict_['Total costos y gastos del subsector económico']+=int(q['Total costos y gastos'])
                            dict_['Total saldo a pagar del subsector económico']+=int(q['Total saldo a pagar'])
                            dict_['Total saldo a favor del subsector económico']+=int(q['Total saldo a favor'])     
                        lt.addLast(list_by_code_best_dict,dict_)
                        list_by_code_sub=sort(list_by_code_sub,cmp_function)
                        lt.addFirst(list_by_code,list_by_code_sub)
                        lt.addFirst(list_by_code_general,list_by_code)
    list_by_code_best_dict=lt.firstElement(sort(list_by_code_best_dict,cmp_function_dict))
    for i in lt.iterator(list_by_code_general):
        if i['key']==list_by_code_best_dict['Código sector económico']:
            for j in lt.iterator(i):
                if j['key']==list_by_code_best_dict['Código subsector económico']:
                    return j,list_by_code_best_dict
               
def req_3(data_structs,year):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    return req_3_4_5(data_structs,year,cmp_req3,cmp_req3_dict,"Total de retenciones del subsector económico","Total retenciones")
  
def req_4(data_structs,year):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    return req_3_4_5(data_structs,year,cmp_req4,cmp_req4_dict,"Total de costos y gastos nómina del subsector económico","Costos y gastos nómina")

def req_5(data_structs,year):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    return req_3_4_5(data_structs,year,cmp_req5,cmp_req5_dict,"Total de descuentos tributarios del subsector económico","Descuentos tributarios")

def req_6(data_structs,year):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    list_by_code_best_dict=lt.newList(datastructure='ARRAY_LIST')
    list_by_code_general=lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(data_structs['model']['data']['table']):
        if i['key']==year:
            for j in codes_sector:
                list_by_code=lt.newList(datastructure='ARRAY_LIST')
                list_by_code['key']=j
                dict_={'Código sector económico':j,'Nombre sector económico':None,'Total ingresos netos del subsector económico':0,'Total costos y gastos del subsector económico':0,'Total saldo a pagar del subsector económico':0,'Total saldo a favor del subsector económico':0}
                for k in codes_sub_sector:
                    list_by_code_sub=lt.newList(datastructure="ARRAY_LIST")
                    list_by_code_sub['key']=k
                    for l in lt.iterator(i['value']):
                        if l['Año']==str(year) and l['Código sector económico']==j and l['Código subsector económico']==k:
                            lt.addFirst(list_by_code_sub,l)
                    if list_by_code_sub['size']!=0:
                        dict_['Nombre sector económico']=lt.firstElement(list_by_code_sub)['Nombre sector económico']
                        for q in lt.iterator(list_by_code_sub):
                            dict_['Total ingresos netos del subsector económico']+=int(q['Total ingresos netos'])
                            dict_['Total costos y gastos del subsector económico']+=int(q['Total costos y gastos'])
                            dict_['Total saldo a pagar del subsector económico']+=int(q['Total saldo a pagar'])
                            dict_['Total saldo a favor del subsector económico']+=int(q['Total saldo a favor'])     
                        lt.addLast(list_by_code_best_dict,dict_)
                        list_by_code_sub=sort(list_by_code_sub,cmp_req6)
                        lt.addFirst(list_by_code,list_by_code_sub)
                        lt.addFirst(list_by_code_general,list_by_code)
            
    list_by_code_best_dict=lt.firstElement(sort(list_by_code_best_dict,cmp_req6_dict))
    codigo_sector=list_by_code_best_dict['Código sector económico']
    
    best_worst_list=lt.newList(datastructure='ARRAY_LIST')

    for i in lt.iterator(list_by_code_general):
        if i['key']==codigo_sector:
            for j in lt.iterator(i):
                dict_={'Código subsector económico':j['key'],'Nombre subsector económico':None,'Total ingresos netos del subsector económico':0,'Total costos y gastos del subsector económico':0,'Total saldo a pagar del subsector económico':0,'Total saldo a favor del subsector económico':0}
                for q in lt.iterator(j):
                    dict_['Nombre subsector económico']=q['Nombre subsector económico']
                    dict_['Total ingresos netos del subsector económico']+=int(q['Total ingresos netos'])
                    dict_['Total costos y gastos del subsector económico']+=int(q['Total costos y gastos'])
                    dict_['Total saldo a pagar del subsector económico']+=int(q['Total saldo a pagar'])
                    dict_['Total saldo a favor del subsector económico']+=int(q['Total saldo a favor'])
                lt.addFirst(best_worst_list,dict_)
    best_worst_list=sort(best_worst_list,cmp_req6_dict)
    
    best_worst_list=lt.firstElement(best_worst_list),lt.lastElement(best_worst_list) 

    list_by_code_best_dict['Subsector económico que más aporto'],list_by_code_best_dict['Subsector económico que menos aporto']=best_worst_list[0]['Código subsector económico'],best_worst_list[1]['Código subsector económico']


    list_best_aportation_best_worst,list_worst_aportation_best_worst=lt.newList(datastructure='ARRAY_LIST'),lt.newList(datastructure='ARRAY_LIST')
    
    for i in lt.iterator(list_by_code_general):
        if i['key']==codigo_sector:
            for j in lt.iterator(i):
                if j['key']==best_worst_list[0]['Código subsector económico'] and int(list_best_aportation_best_worst['size'])<2:#mayor
                    lt.addLast(list_best_aportation_best_worst,lt.firstElement(j))#mejor
                    lt.addLast(list_best_aportation_best_worst,lt.lastElement(j))#menor
                if j['key']==best_worst_list[1]['Código subsector económico']and int(list_worst_aportation_best_worst['size'])<2: #menor
                   
                    lt.addLast(list_worst_aportation_best_worst,lt.firstElement(j))#mejor
                    lt.addLast(list_worst_aportation_best_worst,lt.lastElement(j))#menor

    
    best_worst_list[0]['Actividad económica que más aporto']=lt.firstElement(list_best_aportation_best_worst)
    best_worst_list[0]['Actividad económica que menos aporto']=lt.lastElement(list_best_aportation_best_worst)
    
    best_worst_list[1]['Actividad económica que más aporto']=lt.firstElement(list_worst_aportation_best_worst)
    best_worst_list[1]['Actividad económica que menos aporto']=lt.lastElement(list_worst_aportation_best_worst)
    
    # #diccionario mejor sector  #diccionario subsector que contribuyo mas #diccioanrio subsector que contribuyo menos #acts_econo_mas aportaron  #acts_econom_meno aportaron
    return list_by_code_best_dict,best_worst_list[0],best_worst_list[1]

def req_7(data_structs,year,sub_code):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    list_1=lt.newList(datastructure="ARRAY_LIST")

    for i in lt.iterator(data_structs['model']['data']['table']):
        if i['key']==year:
            for element in lt.iterator(i['value']):
                if element['Año']==year and element['Código subsector económico']==sub_code:
                    lt.addFirst(list_1,element)
    return sort(list_1,cmp_req7)
    
def req_8(data_structs,year,top):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    contador=0
    sub=lt.newList(datastructure="ARRAY_LIST")
    act=lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(data_structs['model']['data']['table']):
        if i['key']==year:
            for element in lt.iterator(i['value']):
                if element['Año']==year:
                    x={"Código actividad económica":element["Código actividad económica"],"Nombre actividad económica":element["Nombre actividad económica"],"Código subsector económico":element["Código subsector económico"],"Nombre subsector económico":element["Nombre subsector económico"],"Código sector económico":element["Código sector económico"],"Nombre sector económico":element["Nombre sector económico"],"Total Impuesto a cargo":int(element["Total Impuesto a cargo"]),"Total ingresos netos":int(element["Total ingresos netos"]),"Total costos y gastos":int(element["Total costos y gastos"]),"Total saldo a pagar":int(element["Total saldo a pagar"]),"Total saldo a favor":int(element["Total saldo a favor"])}
                    lt.addFirst(act,x)
                    y={"Código subsector económico":element["Código subsector económico"],"Nombre subsector económico":element["Nombre subsector económico"],"Código sector económico":element["Código sector económico"],"Nombre sector económico":element["Nombre sector económico"],"Total Impuesto a cargo":int(element["Total Impuesto a cargo"]),"Total ingresos netos":int(element["Total ingresos netos"]),"Total costos y gastos":int(element["Total costos y gastos"]),"Total saldo a pagar":int(element["Total saldo a pagar"]),"Total saldo a favor":int(element["Total saldo a favor"])}
                    contador=0
                    resultado=-1
                    for cua in lt.iterator(sub):
                        if cua["Código subsector económico"] == y["Código subsector económico"]:
                            resultado=contador
                            sub["elements"][resultado]["Total Impuesto a cargo"] += int(y["Total Impuesto a cargo"])
                            sub["elements"][resultado]["Total ingresos netos"]+=int(y["Total ingresos netos"])
                            sub["elements"][resultado]["Total costos y gastos"]+=int(y["Total costos y gastos"])
                            sub["elements"][resultado]["Total saldo a pagar"]+=int(y["Total saldo a pagar"])
                            sub["elements"][resultado]["Total saldo a favor"]+=int(y["Total saldo a favor"])                             
                        contador +=1
                    if resultado==-1:
                        lt.addFirst(sub,y)
    sub_ord=sort(sub,cmp_req8)
    act_ord=sort(act,cmp_req81)
    act_ord_org_sub_listas=lt.newList(datastructure="ARRAY_LIST")
    
    for j in codes_sub_sector:
        sub_list=lt.newList(datastructure="ARRAY_LIST")
        sub_list['key']=j
        for i  in lt.iterator(act_ord):
            if i["Código subsector económico"]==j:
                lt.addLast(sub_list,i)
        if sub_list['size']!=0:
            lt.addLast(act_ord_org_sub_listas,sub_list)

    return sub_ord,act_ord_org_sub_listas

# Funciones utilizadas para comparar elementos dentro de una lista
def sort(data_structs,cmp_function):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    return quk.sort(data_structs,cmp_function)
def cmp_ec_act_code(data_1,data_2):
    return  int(data_1['Código actividad económica'].translate({ord(i):'/' for i in 'Yy-'}).split('/')[0])<=int(data_2['Código actividad económica'].translate({ord(i):'/' for i in 'Yy-'}).split('/')[0])

def cmp_by_year(data_1,data_2):
    if data_2['key']==None or data_1['key']== None:
        return False
    else:
        return int(data_1['key'])<=int(data_2['key'])
    
def cmp_req1(data_1,data_2):
    return  int(data_1['Total saldo a pagar'])>=int(data_2['Total saldo a pagar'])

def cmp_req2(data_1,data_2):
    return  int(data_1['Total saldo a favor'])>=int(data_2['Total saldo a favor'])

def cmp_req3(data_1,data_2):
    return int(data_1['Total retenciones'])<=int(data_2['Total retenciones'])

def cmp_req3_dict(data_1,data_2):
    return int(data_1['Total de retenciones del subsector económico'])<=int(data_2['Total de retenciones del subsector económico'])

def cmp_req4(data_1,data_2):
    return int(data_1['Costos y gastos nómina'])<=int(data_2['Costos y gastos nómina'])

def cmp_req4_dict(data_1,data_2):
    return int(data_1['Total de costos y gastos nómina del subsector económico'])>=int(data_2['Total de costos y gastos nómina del subsector económico'])

def cmp_req5(data_1,data_2):
    return int(data_1['Descuentos tributarios'])<=int(data_2['Descuentos tributarios'])

def cmp_req5_dict(data_1,data_2):
    return int(data_1['Total de descuentos tributarios del subsector económico'])>=int(data_2['Total de descuentos tributarios del subsector económico'])

def cmp_req6(data_1,data_2):
    return int(data_1['Total ingresos netos'])>=int(data_2['Total ingresos netos'])

def cmp_req6_dict(data_1,data_2):
    return int(data_1['Total ingresos netos del subsector económico'])>=int(data_2['Total ingresos netos del subsector económico'])

def cmp_req7(data_1,data_2):
    return int(data_1['Total costos y gastos'])<=int(data_2['Total costos y gastos'])
def cmp_req8(data_1,data_2):
    return int(data_1["Total Impuesto a cargo"])>=int(data_2["Total Impuesto a cargo"])

def cmp_req81(data_1,data_2):
    if data_1["Código subsector económico"] == data_2["Código subsector económico"]:
        return int(data_1["Total Impuesto a cargo"])>=int(data_2["Total Impuesto a cargo"])
    
