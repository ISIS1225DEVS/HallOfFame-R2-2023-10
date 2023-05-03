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
from tabulate import tabulate
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
def new_catalog(map_type,factorCharge):
    """
        Se crea el catalogo general que guardará la información primero guarda todos los registros y en otro indice (map) guarda los registros 
        separados por año
    """
    catalog = {
                'content': None,
                'year': None,
                'sector': None,
                'subsector': None,
                'sectorSubsector': None,
    }
    catalog['content'] = lt.newList('ARRAY_LIST',cmp_impuestos_by_anio_CAE)
    catalog['year'] = mp.newMap(4,maptype=map_type,loadfactor=factorCharge,cmpfunction=cpm_map)
    catalog['sector'] = mp.newMap(4,maptype=map_type,loadfactor=factorCharge,cmpfunction=cpm_map)
    catalog['subsector'] = mp.newMap(4,maptype=map_type,loadfactor=factorCharge,cmpfunction=cpm_map)
    catalog['sectorSubsector'] = mp.newMap(4,maptype=map_type,loadfactor=factorCharge,cmpfunction=cpm_map)
    
    return catalog


def load_data(data_structs, data):
    datos = lt.newList('ARRAY_LIST')
    for register in data:
        add_data(datos, register)
    sort_datos = merg.sort(datos, cmp_impuestos_by_anio_CAE)
    
    #?Se guardan los datos ordenados por año y código de actividad económica
    data_structs['content'] = lt.subList(sort_datos,1,lt.size(sort_datos))
    
    #?Se separan los datos por año y se guardan en una tabla de hash
    byYears,years = separatedByValue(sort_datos,"Año")
    for i in range(1,lt.size(years)+1):
        mp.put(data_structs['year'],lt.getElement(years,i),lt.getElement(byYears,i))
        
    #?Se separan por sector económico y se guardan en una segunda tabla de hash req 1 y 2
    for i in range(1,lt.size(years)+1):
        bySector,sectors = separatedByValue(lt.getElement(byYears,i),"Código sector económico")
        actual_year = lt.getElement(years,i)
        mp.put(data_structs['sector'],actual_year,mp.newMap(4,maptype='PROBING',loadfactor=0.5))
        for k in range(1,lt.size(sectors)+1):
            hashYear = mp.get(data_structs['sector'],actual_year)['value']
            mp.put(hashYear, lt.getElement(sectors,k),lt.getElement(bySector,k))
            
    #?Se separan por subsector económico y se guardan en una segunda tabla de hash req 3, 4 ,5 , 7 y 8
    for i in range(1,lt.size(years)+1):
        bySubsector,subsectors = separatedByValue(lt.getElement(byYears,i),"Código subsector económico")
        actual_year = lt.getElement(years,i)
        mp.put(data_structs['subsector'],actual_year,mp.newMap(4,maptype='PROBING',loadfactor=0.5))
        for k in range(1,lt.size(subsectors)+1):
            hashYear = mp.get(data_structs['subsector'],actual_year)['value']
            sumatoriaSubsector(lt.getElement(bySubsector,k))
            mp.put(hashYear, lt.getElement(subsectors,k),lt.getElement(bySubsector,k))
                  
    #?Se separan por sector económico y subsector económico para posteriormente realizar una sumatoria y guardar en una tercera tabla de hash req 6
    for i in range(1,lt.size(years)+1):
        bySector,sectors = separatedByValue(lt.getElement(byYears,i),"Código sector económico")
        actual_year = lt.getElement(years,i)
        mp.put(data_structs['sectorSubsector'],actual_year,mp.newMap(4,maptype='PROBING',loadfactor=0.5))
        hashYear = mp.get(data_structs['sectorSubsector'],actual_year)['value']
        for k in range(1,lt.size(sectors)+1):
            bySubsector,subsectors = separatedByValue(lt.getElement(bySector,k),"Código subsector económico")
            actual_sector = lt.getElement(sectors,k)
            mp.put(hashYear,actual_sector,mp.newMap(4,maptype='PROBING',loadfactor=0.5))
            hashSector = mp.get(hashYear,actual_sector)['value']
            for j in range(1,lt.size(subsectors)+1):
                sumatoriaSubsector(lt.getElement(bySubsector,j))
                mp.put(hashSector, lt.getElement(subsectors,j),lt.getElement(bySubsector,j))
            sumatoriaSector(hashSector)
            

# Funciones para agregar informacion al modelo

def add_data(datos, registro):
    """
    Función para agregar nuevos elementos a la lista
    """
    item = new_data(registro)
    lt.addLast(datos, item)
    return datos


# Funciones para creacion de datos

def new_data(registro):
    """
    Crea una nueva estructura para modelar los datos
    """
    new_item = {}
    for key in registro.keys():
        new_item[key] = registro[key]
    return new_item


#Función para separa por Sector Económico
def separatedByValue(control, separator):
    listSectors = lt.newList("ARRAY_LIST")
    Sectores = lt.newList("ARRAY_LIST")
    for i in lt.iterator(control):
        if (lt.isPresent(Sectores,i[separator])==0):
            lt.addLast(Sectores,i[separator])
            lt.addLast(listSectors,lt.newList("ARRAY_LIST"))
            lt.addLast(lt.getElement(listSectors,lt.isPresent(Sectores,i[separator])),i)
        else:
            lt.addLast(lt.getElement(listSectors,lt.isPresent(Sectores,i[separator])),i)
    return listSectors,Sectores


def sumatoriaSubsector(data_structus):
    ToRetenciones = 0
    ToIngresosNetos = 0
    ToCostosGastos = 0
    ToSaldoPagar = 0
    ToSaldoFavor = 0
    ToCostosGastosNomina = 0
    ToDescuentosTributarios = 0
    ToImpuestos = 0
    for registro in lt.iterator(data_structus):
        ToRetenciones += int(registro['Total retenciones'])
        ToIngresosNetos += int(registro['Total ingresos netos'])
        ToCostosGastos += int(registro['Total costos y gastos'])
        ToSaldoPagar += int(registro['Total saldo a pagar'])
        ToSaldoFavor += int(registro['Total saldo a favor'])
        ToCostosGastosNomina += int(registro['Costos y gastos nómina'])
        ToDescuentosTributarios += int(registro['Descuentos tributarios'])
        ToImpuestos += int(registro['Total Impuesto a cargo'])
    for registro in lt.iterator(data_structus):
        registro['Total retenciones del subsector económico'] = ToRetenciones
        registro['Total ingresos netos del subsector económico'] = ToIngresosNetos
        registro['Total costos y gastos del subsector económico'] = ToCostosGastos
        registro['Total saldo a pagar del subsector económico'] = ToSaldoPagar
        registro['Total saldo a favor del subsector económico'] = ToSaldoFavor
        registro['Total de costos y gastos nómina del subsector económico'] = ToCostosGastosNomina
        registro['Total descuentos tributarios del subsector económico'] = ToDescuentosTributarios
        registro['Total impuestos a cargo para el subsector económico'] = ToImpuestos


def sumatoriaSector(data_structs):
    keys_subsectors = mp.keySet(data_structs)
    ToNetosSec = 0
    ToCostosSec = 0
    ToPagarSec = 0
    ToFavorSec = 0
    for key in lt.iterator(keys_subsectors):
        sector = mp.get(data_structs,key)['value']
        reg_random = lt.firstElement(sector)
        ToNetosSec += int(reg_random['Total ingresos netos del subsector económico'])
        ToCostosSec += int(reg_random['Total costos y gastos del subsector económico'])
        ToPagarSec += int(reg_random['Total saldo a pagar del subsector económico']) 
        ToFavorSec += int(reg_random['Total saldo a favor del subsector económico'])
    for key in lt.iterator(keys_subsectors):
        for registro in lt.iterator(mp.get(data_structs,key)['value']):
            registro['Total ingresos netos del sector económico'] = ToNetosSec
            registro['Total costos y gastos del sector económico'] = ToCostosSec
            registro['Total saldo a pagar del subsector económico'] = ToPagarSec
            registro['Total saldo a favor del subsector económico'] = ToFavorSec
            
            registro['Total saldo a pagar del sector económico'] = ToPagarSec
            registro['Total saldo a favor del sector económico'] = ToFavorSec

def printYearsResume(control):
    return control['year']

def req_1(data_structs, year, sector):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    if (mp.contains(data_structs["sector"], year)):
        response = mp.get(data_structs["sector"], year)["value"]
        if (mp.contains(response, sector)):
            response = mp.get(response, sector)["value"]
            response = merge_sort(response, cmp_mayor_saldo_a_pagar)  
            return new_sublist(response, 1, 1)
    return None


def req_2(data_structs,year,sector):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 1
    if (mp.contains(data_structs["sector"], year)):
        response = mp.get(data_structs["sector"], year)["value"]
        if (mp.contains(response, sector)):
            response = mp.get(response, sector)["value"]
            response = merge_sort(response, cmp_mayor_saldo_a_favor)  
            return new_sublist(response, 1, 1)
    return None


def req_3(data_structs, year):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    if (mp.contains(data_structs["subsector"], year)):
        response = mp.get(data_structs["subsector"], year)["value"]
        keys = mp.keySet(response)
        value = lt.firstElement(mp.get(response, lt.firstElement(keys))["value"])["Total retenciones del subsector económico"]
        subsector_code = lt.firstElement(keys)
        for code in lt.iterator(keys):
            temp_value = lt.firstElement(mp.get(response, code)["value"])["Total retenciones del subsector económico"]
            if (temp_value < value):
                value = temp_value
                subsector_code = code
        return merge_sort(mp.get(response, subsector_code)["value"], cmp_menor_total_retenciones)
    return None


def req_4(data_structs, year):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    if (mp.contains(data_structs['subsector'],year)):
        data = mp.get(data_structs['subsector'],year)['value']
        subsectores = mp.keySet(data)
        mayorNomina = 0
        mayorsub = "index"
        for sub in lt.iterator(subsectores):
            nominasub = lt.firstElement(mp.get(data, sub)['value'])['Total de costos y gastos nómina del subsector económico']
            if nominasub > mayorNomina:
                mayorNomina = nominasub
                mayorsub = sub
        return merge_sort(mp.get(data,mayorsub)['value'],cmp_mayor_nomina)
    return None


def req_5(data_structs, year):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    
    if (mp.contains(data_structs["subsector"], year)):
        value = mp.get(data_structs["subsector"], year)["value"]
        key_subsector = mp.keySet(value)
        mayor_descuento = 0
        mayor_subsector = "" 
        
        for subsector in lt.iterator(key_subsector):
            
            mayor_descuento_temp = lt.firstElement(mp.get(value, subsector)['value'])['Total descuentos tributarios del subsector económico']
            
            if mayor_descuento_temp > mayor_descuento:
                mayor_descuento = mayor_descuento_temp
                mayor_subsector = subsector
                
        return merge_sort(mp.get(value, mayor_subsector)['value'], cmp_mayor_descuento)
        
    return None

def req_6(data_structs, year):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    data = mp.get(data_structs['sectorSubsector'], year)['value']
    sectors = mp.keySet(data)
    mayoresNetos = 0
    mayorSec = 'index'
    for sector in lt.iterator(sectors):
        datasector = mp.get(data, sector)['value']
        subsectors = mp.keySet(datasector)
        netoSector = lt.firstElement(mp.get(datasector, lt.firstElement(subsectors))['value'])['Total ingresos netos del sector económico']
        if netoSector > mayoresNetos:
            mayoresNetos = netoSector
            mayorSec = sector
    data_sec = mp.get(data, mayorSec)['value']
    subsectors = mp.keySet(data_sec)
    menorNetSub = 9999999999999
    menorSub = 'index'
    mayorNetSub = 0
    mayorSub = 'index'
    for subsec in lt.iterator(subsectors):
        ingresoNeto = lt.firstElement(mp.get(data_sec,subsec)['value'])['Total ingresos netos del subsector económico']
        if ingresoNeto > mayorNetSub:
            mayorNetSub = ingresoNeto
            mayorSub = subsec
        if ingresoNeto < menorNetSub:
            menorNetSub = ingresoNeto
            menorSub = subsec
    mayor = merge_sort(mp.get(data_sec,mayorSub)['value'],cmp_mayor_ingreso_neto)
    menor = merge_sort(mp.get(data_sec,menorSub)['value'],cmp_mayor_ingreso_neto)
    
    for reg in lt.iterator(mayor):
        reg['Actividad económica que menos aporto'] = printActivityEconomic(lt.firstElement(mayor))
        reg['Actividad económica que más aporto'] = printActivityEconomic(lt.lastElement(mayor))
        reg['Subsector económico que menos aporto'] = menorSub
        reg['Subsector económico que más aporto'] = mayorSub
        
    for reg in lt.iterator(menor):
        reg['Actividad económica que menos aporto'] = printActivityEconomic(lt.firstElement(menor))
        reg['Actividad económica que más aporto'] = printActivityEconomic(lt.lastElement(menor))
        reg['Subsector económico que menos aporto'] = menorSub
        reg['Subsector económico que más aporto'] = mayorSub
    return mayor, menor


def req_7(data_structs, top, year, subsector):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    if (mp.contains(data_structs["subsector"], year)):
        response = mp.get(data_structs["subsector"], year)["value"]
        if (mp.contains(response, subsector)):
            response = mp.get(response, subsector)["value"]
            response = merge_sort(response, cmp_menor_costos_y_gastos)  
            if (lt.size(response) >= int(top)):
                return new_sublist(response, 1, int(top))
            else:
                return response
    return None


def req_8(data_structs, year):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    
    if (mp.contains(data_structs["subsector"], year)):
        response = mp.get(data_structs["subsector"], year)["value"]
        keys = mp.keySet(response)
        general_list = lt.newList("ARRAY_LIST")
        
        for code in lt.iterator(keys):
            temp_value = mp.get(response, code)["value"]
            lt.addLast(general_list, lt.firstElement(temp_value))
            merge_sort(temp_value, cmp_mayor_impuesto_a_cargo)
             
        sorted_list = merge_sort(general_list, cmp_mayor_total_impuesto_a_cargo)
        keys_sorted = merge_sort(keys, cmp_menor_a_mayor)
        return sorted_list, response, keys_sorted
    return None


# Funciones de ordenamiento
def sortYears(years):
    
    return merge_sort(years, cmp_menor_a_mayor)


def cmp_menor_a_mayor(dato1, dato2):
    
    return int(dato1) < int(dato2)
    
    
def cpm_map(impuesto1, impuesto2):
    
    impuesto2 = me.getKey(impuesto2)
    
    if int(impuesto1) > int(impuesto2):
        return 1
    elif int(impuesto1) < int(impuesto2):
        return -1
    else:
        return 0


def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2):
    """
    Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2,
    en caso de que sean iguales tenga en cuenta el código de la actividad económica,
    de lo contrario devuelva falso (False).
    Args:
        impuesto1: información del primer registro de impuestos que incluye el “Año” y el
                   “Código actividad económica”
        impuesto2: información del segundo registro de impuestos que incluye el “Año” y el
                   “Código actividad económica”
    """
    if (int(impuesto1["Año"]) < int(impuesto2["Año"])):
        return 1
    elif (int(impuesto1["Año"]) > int(impuesto2["Año"])):
        return 0
    else:
        impuesto_1 = int(impuesto1["Código actividad económica"].replace("/"," ").replace("y", " ").split(" ")[0])
        impuesto_2 = int(impuesto2["Código actividad económica"].replace("/"," ").replace("y", " ").split(" ")[0])
        if impuesto_1 < impuesto_2:
            return 1
        else:
            return 0
      
        
def cmp_mayor_saldo_a_pagar(impuesto1, impuesto2):
    
    return int(impuesto1["Total saldo a pagar"]) > int(impuesto2["Total saldo a pagar"])


def cmp_mayor_saldo_a_favor(impuesto1, impuesto2):
    
    return int(impuesto1["Total saldo a favor"]) > int(impuesto2["Total saldo a favor"])


def cmp_menor_total_retenciones(impuesto1, impuesto2):  
    
    return int(impuesto1["Total retenciones"]) < int(impuesto2["Total retenciones"])


def cmp_mayor_nomina(impuesto1, impuesto2):
    
    return int(impuesto1["Costos y gastos nómina"]) < int(impuesto2["Costos y gastos nómina"])


def cmp_mayor_descuento(impuesto1, impuesto2):
    
    return int(impuesto1["Descuentos tributarios"]) < int(impuesto2["Descuentos tributarios"])



def cmp_mayor_ingreso_neto(impuesto1, impuesto2):
    
    return int(impuesto1["Total ingresos netos"]) < int(impuesto2["Total ingresos netos"])


def printActivityEconomic(registro,keys=["Código actividad económica","Nombre actividad económica","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]):
    table = []
    for i in keys:
        table.append([i,registro[i]])
    return tabulate(table,tablefmt="grid",maxcolwidths=[15,25])


def cmp_menor_costos_y_gastos(impuesto1, impuesto2):
    
    if int(impuesto1["Total costos y gastos"]) < int(impuesto2["Total costos y gastos"]):
        return 1
    elif int(impuesto1["Total costos y gastos"]) > int(impuesto2["Total costos y gastos"]):
        return 0
    else:
        return int(impuesto1["Código actividad económica"]) < int(impuesto2["Código actividad económica"])
    
    
def cmp_mayor_total_impuesto_a_cargo(impuesto1, impuesto2):
    
    if int(impuesto1["Total impuestos a cargo para el subsector económico"]) > int(impuesto2["Total impuestos a cargo para el subsector económico"]):
        return 1
    elif int(impuesto1["Total impuestos a cargo para el subsector económico"]) < int(impuesto2["Total impuestos a cargo para el subsector económico"]):
        return 0
    else:
        return impuesto1["Nombre subsector económico"] < impuesto2["Nombre subsector económico"]
    
    
def cmp_mayor_impuesto_a_cargo(impuesto1, impuesto2):
    
    if int(impuesto1["Total Impuesto a cargo"]) > int(impuesto2["Total Impuesto a cargo"]):
        return 1
    elif int(impuesto1["Total Impuesto a cargo"]) < int(impuesto2["Total Impuesto a cargo"]):
        return 0
    else:
        return impuesto1["Nombre subsector económico"] < impuesto2["Nombre subsector económico"]
    

def merge_sort(data_structs, cmpfunction=cmp_impuestos_by_anio_CAE):
    """
    Función encargada de ordenar la lista con los datos
    """
    sorted_list = merg.sort(data_structs, cmpfunction)
    return sorted_list


def new_sublist(list, pos, numlem):
    """
    Función encargada de crear una sublista
    """
    new_sublist = lt.subList(list, pos, numlem)
    return new_sublist