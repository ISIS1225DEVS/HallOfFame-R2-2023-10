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

def new_data_structs(decision,   decision_factcarg):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO COMPLETADO: Inicializar las estructuras de datos ------ 
    data_structs = {"map_anio":None}
    
    if decision == "1":
        data_structs['map_anio']=  mp.newMap(10,
                                    maptype='CHAINING',
                                    loadfactor=float(decision_factcarg),
                                    cmpfunction=compareAnio)
    elif decision == "2":
        
        data_structs['map_anio']=  mp.newMap(10,
                                    maptype='PROBING',
                                    loadfactor=float(decision_factcarg),
                                    cmpfunction=compareAnio)
    return data_structs
# Funciones para agregar informacion al modelo
# SE CREARON COMPARE ANIO PARA EL MAP Y COMPARE CODIGO ACTIVIDAD PARA LA INFORMACION DENTRO DEL MAP
def compareAnio(keyanio, entry_anio): 
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    entry_anio_key = me.getKey(entry_anio)
    if (int(keyanio) == int(entry_anio_key)):
        return 0
    elif (int(keyanio) > int(entry_anio_key)):
        return 1
    else:
        return -1
    
def newAnio(numero_Anio):
    """
    añade el año como llave en un map
    """
    anio = {'numero': "",
              "impuestos": None}
    anio['numero'] = numero_Anio
    anio['impuestos'] = lt.newList('SINGLE_LINKED', compareCodigoActividad)
    return anio
def compareCodigoActividad(impuesto_1,impuesto_2):
    """
    Función encargada de comparar dos datos
    """
    if impuesto_1['Código actividad económica'] > impuesto_2['Código actividad económica']:
        return 1
    elif impuesto_1['Código actividad económica'] < impuesto_2['Código actividad económica']:
        return -1
    else:
        return 0
def add_impuesto(data_structs, impuesto):
    """ 
    Función que adiciona un impuesto a la lista de impuestos, adicionalmente
    lo guarda en un Map usando como llave 
    """
    add_impuestoAnio(data_structs, impuesto)
def add_impuestoAnio(data_structs, impuesto):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO COMPLETADO: Crear la función para agregar elementos a una lista 
    try:
        anio = impuesto["Año"]
        anios = data_structs["map_anio"]
        exist_anio = mp.contains(anios,anio)
        if exist_anio:
            entry = mp.get(anios,anio)
            anio_para_añadir = me.getValue(entry)
        else: 
            anio_para_añadir= newAnio(anio)
            mp.put(anios,anio, anio_para_añadir)
        lt.addLast(anio_para_añadir['impuestos'],impuesto)
    except Exception:
        return None

# Funciones para creacion de datos

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
    #TODO COMPLETADO: Crear la función para obtener el tamaño de una lista
    return mp.size(data_structs["map_anio"])

def req_1(data_structs, anio, cse):
    """
    Función que soluciona el requerimiento 3
    """
    lista_del_anio= ""
    if mp.contains(data_structs["map_anio"], anio):
        lista_del_anio= mp.get(data_structs["map_anio"], anio)
    impuestos= lista_del_anio['value']['impuestos']
    lista_cse= lt.newList("ARRAY_LIST")
    for x in lt.iterator(impuestos):
        if cse== x['Código sector económico']:
            lt.addLast(lista_cse, x)
    mayor_s_a_p= -1
    mayor= ""
    for c in lt.iterator(lista_cse):
        if int(c['Total saldo a pagar'])> mayor_s_a_p:
            mayor_s_a_p= int(c['Total saldo a pagar'])
            mayor = c
    dic_final= {'Código actividad económica': [mayor['Código actividad económica']], 'Nombre actividad económica':[mayor['Nombre actividad económica']], 'Código subsector económico':[mayor['Código subsector económico']],
                 'Nombre subsector económico':[mayor['Nombre subsector económico']],'Total ingresos netos':[mayor['Total ingresos netos']], 'Total costos y gastos': [mayor['Total costos y gastos']], 'Total saldo a pagar': [mayor['Total saldo a pagar']],
                 'Total saldo a favor': [mayor['Total saldo a favor']] }
    return dic_final

def req_2(data_structs, year, codigo):
    """
    Función que soluciona el requerimiento 2
    Obtener la actividad económica con mayor saldo a pagar para un sector económico y un año específico.
    """
    # TODO: Realizar el requerimiento 2
    pass
    
    year_entry = mp.get(data_structs['map_anio'], year)
    year_datos = me.getValue(year_entry)
    lista_actecon = year_datos['impuestos']
    aja = lt.newList('ARRAY_LIST')
    
    for act_econ in lt.iterator(lista_actecon):
        lt.addLast(aja, act_econ)
        
    lst_act_eco_filt = lt.newList('ARRAY_LIST')
    for act_eco_filt in lt.iterator(aja):
        if act_eco_filt['Código sector económico'] == codigo:
            lt.addLast(lst_act_eco_filt, act_eco_filt)
    
    merg.sort(lst_act_eco_filt, cmp_saf)
    final_enarray = lt.getElement(lst_act_eco_filt, lt.size(lst_act_eco_filt))
    headers = ['Código actividad económica', 'Nombre actividad económica', 'Nombre subsector económico', 
               "Total ingresos netos", "Costos y gastos nómina", "Total saldo a pagar","Total saldo a favor"]
    final = lt.newList('ARRAY_LIST')
    for elemento in headers:
        lt.addLast(final,final_enarray[elemento])
    
    return final, headers
def cmp_saf (data1, data2):
    return int(data1['Código sector económico']) > int(data2['Código sector económico'])

def req_3(data_structs, anio):
    """
    Función que soluciona el requerimiento 3
    """
    lista_del_anio= ""
    if mp.contains(data_structs["map_anio"], anio):
        lista_del_anio= mp.get(data_structs["map_anio"], anio)
    impuestos= lista_del_anio['value']['impuestos']
    map_sub_sec= mp.newMap(numelements= lt.size(impuestos))
    for z in lt.iterator(impuestos):
        subsector= z['Código subsector económico']
        cant_ret= 0
        for x in lt.iterator(impuestos):
            if subsector == x['Código subsector económico']:
                cant_ret += int(x['Total retenciones'])
        if subsector not in  map_sub_sec:
            mp.put(map_sub_sec, subsector, cant_ret)
    cont= 1
    ind= 0
    men_tot_ret= 1000000000000000000000000
    for c in lt.iterator(mp.valueSet(map_sub_sec)):
        if int(c)< men_tot_ret:
            men_tot_ret = int(c)
            ind= cont
        cont += 1
    cod_menor_ret= lt.getElement(mp.keySet(map_sub_sec),ind)
    tot_ret= 0
    tot_in_net= 0
    tot_c_y_g= 0
    tot_s_a_p= 0
    tot_s_a_f= 0
    for v in lt.iterator(impuestos):
        if v['Código subsector económico'] == cod_menor_ret:
            cod_sec= v['Código sector económico']
            nom_sec= v['Nombre sector económico']
            cod_s_sec= v['Código subsector económico']
            nom_s_sec= v['Nombre subsector económico']
            tot_ret += int(v['Total retenciones'])
            tot_in_net += int(v['Total ingresos netos'])
            tot_c_y_g += int(v['Total costos y gastos'])
            tot_s_a_p += int(v['Total saldo a pagar'])
            tot_s_a_f += int(v['Total saldo a favor'])
    dic_final= {"Código sector económico": [cod_sec],'Nombre sector económico': [nom_sec], 'Código subsector económico' : [cod_s_sec] , 'Nombre subsector económico': [nom_s_sec],'Total retenciones': [tot_ret],
                 'Total ingresos netos': [tot_in_net], 'Total costos y gastos': [tot_c_y_g], 'Total saldo a pagar': [tot_s_a_p],'Total saldo a favor': [tot_s_a_f] }
    list_fin= lt.newList('ARRAY_LIST')
    for b in lt.iterator(impuestos):
        if b['Código subsector económico'] == cod_menor_ret:
            lt.addLast(list_fin, {"Código actividad económica": b['Código actividad económica'], 'Nombre actividad económica': b['Nombre actividad económica'], 'Total retenciones': b['Total retenciones'], 
                                  'Total ingresos netos': b['Total ingresos netos'], 'Total costos y gastos': b['Total costos y gastos'], 'Total saldo a pagar':b['Total saldo a pagar'], 'Total saldo a favor':b['Total saldo a favor']})
    if lt.size(list_fin)< 6:
        return dic_final, list_fin
    else:
        lista_a_usar= list_fin.copy()
        list_mas= lt.newList("ARRAY_LIST")
        qpa= 3
        while qpa!=0:
            mayor_apoyo= -1
            m= ""
            mayor= ""  
            qu = 0
            for x in lt.iterator(lista_a_usar):
                 qu += 1
                 if int(x["Total retenciones"]) > mayor_apoyo:
                    mayor_apoyo= int(x["Total retenciones"])
                    mayor= qu
                    m= x
            lt.addLast(list_mas, m)
            lt.deleteElement(lista_a_usar, mayor)
            qpa -=1
        qpa2= 3
        list_menos= lt.newList("ARRAY_LIST")
        while qpa2!=0:
            menor_apoyo= 100000000000000000000
            m= ""
            menor= ""  
            qu = 0
            for x in lt.iterator(list_fin):
                 qu += 1
                 if int(x["Total retenciones"]) > menor_apoyo:
                    menor_apoyo= int(x["Total retenciones"])
                    menor= qu
                    m= x
            lt.addLast(list_menos, m)
            lt.deleteElement(list_fin, menor)
            qpa2 -=1
        return dic_final, list_mas, list_menos

def req_4(data_structs,anio):
    """
    Función que soluciona el requerimiento 4. Como analista económico Deseo identificar el subsector económico que tuvo los mayores costos y gastos de nómina (Costos y gastos nómina) para un año especifico.
    """
    lista_totales =   ["Costos y gastos nómina", "Total ingresos netos","Total costos y gastos","Total saldo a pagar", "Total saldo a favor"]
    entry_anio = mp.get(data_structs['map_anio'], str(anio))
    datos_anio = me.getValue(entry_anio) #ESTO NO ES LA LISTA, SON LOS DATOS
    lista_impuestos = datos_anio["impuestos"]
    subsectores_del_anio =  mp.newMap(30,
                                    maptype='CHAINING',
                                    loadfactor=(4),
                                    cmpfunction=compareCodigoSubsector)
    cod_mayor_subs, mayor_cost_y_nom  = -1 , 0

    for impuesto in lt.iterator(lista_impuestos):
        codigo_subsector = int(impuesto["Código subsector económico"])
        if cod_mayor_subs == -1 and mayor_cost_y_nom ==0:
            cod_mayor_subs = codigo_subsector
            mayor_cost_y_nom = int(impuesto["Costos y gastos nómina"])

        if not mp.contains(subsectores_del_anio, codigo_subsector):
            actividades_eco = lt.newList(datastructure="ARRAY_LIST", cmpfunction= compareCodigoActividad)
            lt.addLast(actividades_eco,impuesto)
            info_subsector = {"Nombre sector económico":impuesto["Nombre sector económico"],"Código sector económico":impuesto["Código sector económico"],
                              "Nombre subsector económico":impuesto["Nombre subsector económico"],"Código subsector económico": codigo_subsector, 
                              "Actividades económicas": actividades_eco}  

            for total in lista_totales:
                info_subsector[total] = int(impuesto[total])
            mp.put(subsectores_del_anio, codigo_subsector, info_subsector)

            if mayor_cost_y_nom < info_subsector["Costos y gastos nómina"]:
                cod_mayor_subs = codigo_subsector
                mayor_cost_y_nom = info_subsector["Costos y gastos nómina"]     
        else:
            entry_info_subsector = mp.get(subsectores_del_anio,codigo_subsector)
            info_subsector = me.getValue(entry_info_subsector)
            for total in lista_totales:
                info_subsector[total] = int(impuesto[total]) + int(info_subsector[total])

            lt.addLast(info_subsector["Actividades económicas"], impuesto)
            mp.put(subsectores_del_anio, codigo_subsector, info_subsector)
            
            if mayor_cost_y_nom < info_subsector["Costos y gastos nómina"]:
                cod_mayor_subs = codigo_subsector
                mayor_cost_y_nom = info_subsector["Costos y gastos nómina"]       

    entry_mayor_subsector = mp.get(subsectores_del_anio,cod_mayor_subs)
    mayor_subsector = me.getValue(entry_mayor_subsector)
    mayor_subsector["Actividades económicas"] = merg.sort(mayor_subsector["Actividades económicas"], sort_criteria_nomina) #LAS ORDENAMOS PARA LUEGO TOMAR LAS 3 PRIMERAS Y LAS 3 ULTIMAS
    actividades_toreplace = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compareCodigoActividad)
    i = 1

    for actividad in lt.iterator(mayor_subsector["Actividades económicas"]):
        if  (i <=3)  or   (i >=  data_size_lista( mayor_subsector["Actividades económicas"] )-2):
            lt.addLast(actividades_toreplace,actividad)
        i+=1

    mayor_subsector["Actividades económicas"] = actividades_toreplace
            
    return mayor_subsector
def compareCodigoSubsector(key_id, entry_impuesto_2): 
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    key_entry_impuesto_2 = me.getKey(entry_impuesto_2)
    if (key_id == key_entry_impuesto_2):
        return 0
    elif (key_id > key_entry_impuesto_2):
        return 1
    else:
        return -1
def sort_criteria_nomina(impuesto1, impuesto2): #men a may
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    """
    return int(impuesto1["Costos y gastos nómina"]) < int(impuesto2["Costos y gastos nómina"])
def compareCodigoSubsector_dañadolist(id1, impuesto_2):
    """
    Función encargada de comparar dos datos
    """
    if id1 > int(impuesto_2['Código subsector económico']):
        return 1
    elif id1 < int(impuesto_2['Código subsector económico']):
        return -1
    else:
        return 0
def compareCodigoSubsector_notworking(impuesto_1, impuesto_2):
    """
    Función encargada de comparar dos datos
    """
    if impuesto_1['Código subsector económico'] > impuesto_2['Código subsector económico']:
        return 1
    elif impuesto_1['Código subsector económico'] < impuesto_2['Código subsector económico']:
        return -1
    else:
        return 0
def data_size_lista(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs)

def req_5(data_structs,year):
    """
    Función que soluciona el requerimiento 5
    """
    sumas_q_me_piden = ['Código sector económico', "Nombre sector económico", "Nombre subsector económico", 'Código subsector económico', "Descuentos tributarios", "Total ingresos netos", "Total costos y gastos", 
                        "Total saldo a pagar", "Total saldo a favor"]
    year_entry = mp.get(data_structs['map_anio'], year)
    year_datos = me.getValue(year_entry)
    lista_actecon = year_datos['impuestos']
    aja = lt.newList('ARRAY_LIST')
    for act_econ in lt.iterator(lista_actecon):
        lt.addLast(aja, act_econ)
    por_subsector = {}
    for i in lt.iterator(aja):
        if i ['Código subsector económico'] not in por_subsector:
            por_subsector[i ['Código subsector económico']]=lt.newList(datastructure= "ARRAY_LIST")
            lt.addLast( por_subsector[i['Código subsector económico']] ,i)           
        else:
            lt.addLast(por_subsector[i['Código subsector económico']], i)
    lista_sqmepiden = [[[x[sumas_q_me_piden[0]], x[sumas_q_me_piden[1]], x[sumas_q_me_piden[2]],x[sumas_q_me_piden[3]], x[sumas_q_me_piden[4]], x[sumas_q_me_piden[5]], x[sumas_q_me_piden[6]], 
                         x[sumas_q_me_piden[7]], x[sumas_q_me_piden[8]]] for x in por_subsector[subsector]['elements']]for subsector in por_subsector]
    final1 = lt.newList("ARRAY_LIST")
    mayor = 0
    mayor_codigosub = 0
    for sub in lista_sqmepiden:
        suma_descuentos = 0
        for actividades in sub:
            suma_descuentos += int(actividades[4])
            suma_porsub = suma_descuentos
            if suma_porsub > mayor:
                mayor = suma_porsub
                mayor_nombresub = actividades[2]
                mayor_codigosub = actividades[3]
    theoneandonly= mayor_codigosub
    lt.addLast(final1, mayor_nombresub)            
    lt.addLast(final1, mayor_codigosub)
    lt.addLast(final1, str(mayor))
    for sub in lista_sqmepiden:
        total_ing = 0
        total_cyg = 0
        total_sap = 0
        total_saf = 0
        for actividades in sub:
            if theoneandonly == actividades[3]:
                total_ing += int(actividades[5])
                total_cyg += int(actividades[6])
                total_sap += int(actividades[7])
                total_saf += int(actividades[8])
                mayor_ing = str(total_ing)
                mayor_cyg = str(total_cyg)
                mayor_sap = str(total_sap)
                mayor_saf = str(total_saf)
    lt.addLast(final1, mayor_ing)
    lt.addLast(final1, mayor_cyg)
    lt.addLast(final1, mayor_sap)
    lt.addLast(final1, mayor_saf)
    subsector_actecon= por_subsector[mayor_codigosub]
    merg.sort(subsector_actecon, cmp_descuentostrib)
    mayndmen = lt.newList('ARRAY_LIST')
    if lt.size(subsector_actecon) > 6:
        lt.addLast(mayndmen, lt.getElement(subsector_actecon, 1))
        lt.addLast(mayndmen, lt.getElement(subsector_actecon, 2))
        lt.addLast(mayndmen, lt.getElement(subsector_actecon, 3))
        lt.addLast(mayndmen, lt.getElement(subsector_actecon, lt.size(subsector_actecon)))
        lt.addLast(mayndmen, lt.getElement(subsector_actecon, lt.size(subsector_actecon)-1))
        lt.addLast(mayndmen, lt.getElement(subsector_actecon, lt.size(subsector_actecon)-2))
    else:
        for i in lt.iterator(subsector_actecon):
            lt.addLast(mayndmen, i)
    headz_1 = ["Nombre subsector económico", 'Código subsector económico', "Total descuentos tributarios", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    headz_2 = ["Código actividad económica","Nombre actividad económica","Descuentos tributarios", "Total ingresos netos", "Costos y gastos nómina", "Total saldo a pagar","Total saldo a favor"] 
    mayndmen_final = [[x[headz_2[0]], x[headz_2[1]], x[headz_2[2]],x[headz_2[3]], x[headz_2[4]], x[headz_2[5]], x[headz_2[6]]]for x in mayndmen['elements']]
    return final1, headz_1, mayndmen_final, headz_2
def cmp_descuentostrib (data1, data2):
    return int(data1['Descuentos tributarios']) < int(data2['Descuentos tributarios'])

def req_6(data_structs,anio):
    """ Función que soluciona el requerimiento 6 """
    lista_totales =   ["Costos y gastos nómina", "Total ingresos netos","Total costos y gastos","Total saldo a pagar", "Total saldo a favor"]
    entry_anio = mp.get(data_structs["map_anio"], str(anio))
    datos_anio = me.getValue(entry_anio) #ESTO NO ES LA LISTA, SON LOS DATOS
    lista_impuestos = datos_anio["impuestos"]
    sectores_del_anio =  mp.newMap(40,
                                    maptype='CHAINING',
                                    loadfactor=(4),
                                    cmpfunction=compareCodigoSector)
    cod_mayor_sec, mayor_total_net_sec = -1 , 0
    
    for impuesto in lt.iterator(lista_impuestos):
        codigo_sector = int(impuesto["Código sector económico"])
        codigo_subsector = int(impuesto["Código subsector económico"])

        if cod_mayor_sec == -1:
            cod_mayor_sec = codigo_sector
            mayor_total_net_sec = int(impuesto["Total ingresos netos"])

        if not mp.contains(sectores_del_anio, codigo_sector):
            subsectores_del_anio =  mp.newMap(40,
                                maptype='CHAINING',
                                loadfactor=(4),
                                cmpfunction=compareCodigoSector)
            actividades_eco = lt.newList(datastructure="ARRAY_LIST", cmpfunction= compareCodigoActividad)
            lt.addLast(actividades_eco,impuesto)

            info_subsector = {"Código subsector económico": codigo_subsector, "Nombre subsector económico":impuesto["Nombre subsector económico"], "Actividades económicas": actividades_eco}  

            for total in lista_totales:
                info_subsector[total] = int(impuesto[total])
            mp.put(subsectores_del_anio, codigo_subsector, info_subsector)

            info_sector = {"Nombre sector económico":impuesto["Nombre sector económico"],"Código sector económico":impuesto["Código sector económico"],
                           "Subsector económico": subsectores_del_anio} 
            for total in lista_totales:
                info_sector[total] = int(impuesto[total])
            mp.put(sectores_del_anio, codigo_sector, info_sector)
    
        else:
            entry_info_sector = mp.get(sectores_del_anio,codigo_sector)
            info_sector = me.getValue(entry_info_sector)
            for total in lista_totales:
                info_sector[total] = int(impuesto[total]) + int(info_sector[total])
          
            if not mp.contains(info_sector["Subsector económico"], codigo_subsector):
                actividades_eco = lt.newList(datastructure="ARRAY_LIST", cmpfunction= compareCodigoActividad)
                lt.addLast(actividades_eco,impuesto)
                info_subsector = {"Código subsector económico": codigo_subsector, "Nombre subsector económico":impuesto["Nombre subsector económico"], "Actividades económicas": actividades_eco}  

                for total in lista_totales:
                    info_subsector[total] = int(impuesto[total])
                mp.put(info_sector["Subsector económico"], codigo_subsector, info_subsector)

            else:
                entry_info_subsector = mp.get(info_sector["Subsector económico"],codigo_subsector)
                info_subsector = me.getValue(entry_info_subsector)
                for total in lista_totales:
                    info_subsector[total] = int(impuesto[total]) + int(info_subsector[total])
                lt.addLast(info_subsector["Actividades económicas"], impuesto)
                mp.put(info_sector["Subsector económico"], codigo_subsector, info_subsector)

            if mayor_total_net_sec < int(info_sector["Total ingresos netos"]):
                cod_mayor_sec = codigo_sector
                mayor_total_net_sec= int(info_sector["Total ingresos netos"]) 

            mp.put(sectores_del_anio, codigo_sector, info_sector)

    entry_mejor_sector = mp.get(sectores_del_anio, cod_mayor_sec)
    mejor_sector = me.getValue(entry_mejor_sector)
    cod_mayor_subs, mayor_total_net_subs  = -1 , 0
    cod_menor_subs, menor_total_net_subs  = -1 , 0
    codigos_subs_map_sec = mp.keySet(mejor_sector["Subsector económico"])

    for key in lt.iterator(codigos_subs_map_sec):
        entry_subsetor_get = mp.get(mejor_sector["Subsector económico"], key)
        info_subsector_get = me.getValue(entry_subsetor_get)

        if (cod_mayor_subs == -1) or  mayor_total_net_subs < info_subsector["Total ingresos netos"]:
            cod_mayor_subs = key
            mayor_total_net_subs = int(info_subsector_get["Total ingresos netos"])

        if (cod_menor_subs == -1) or  menor_total_net_subs > info_subsector["Total ingresos netos"]:
            cod_menor_subs = key
            menor_total_net_subs = int(info_subsector_get["Total ingresos netos"])

    entry_mayor_subsector = mp.get(mejor_sector["Subsector económico"] ,cod_mayor_subs)
    mayor_subsector = me.getValue(entry_mayor_subsector)
    entry_menor_subsector = mp.get(mejor_sector["Subsector económico"] ,cod_menor_subs)
    menor_subsector = me.getValue(entry_menor_subsector)

    # Procedimiento para ajustar el MEJOR SUBSECTOR y eliminar su lista de actividades
    mejor_act_del_mejorsubs = lt.firstElement(mayor_subsector["Actividades económicas"])
    peor_act_del_mejorsubs = lt.firstElement(mayor_subsector["Actividades económicas"])

    for actividad in lt.iterator(mayor_subsector["Actividades económicas"]):

        if  int(mejor_act_del_mejorsubs["Total ingresos netos"]) < int(actividad["Total ingresos netos"]):
            mejor_act_del_mejorsubs = actividad

        if  int(peor_act_del_mejorsubs["Total ingresos netos"]) < int(actividad["Total ingresos netos"]):
            peor_act_del_mejorsubs = actividad

    mayor_subsector["Mejor actividad"] = mejor_act_del_mejorsubs
    mayor_subsector["Peor actividad"] = peor_act_del_mejorsubs
    mayor_subsector.pop("Actividades económicas",-1)

    # PROCEDIMIENTO PARA LO MISMO PERO EN EL PEOR SUBSECTOR 
    mejor_act_del_peorsubs = lt.firstElement(menor_subsector["Actividades económicas"])
    peor_act_del_peorsubs = lt.firstElement(menor_subsector["Actividades económicas"])

    for actividad in lt.iterator(menor_subsector["Actividades económicas"]):
 
        if  int(mejor_act_del_mejorsubs["Total ingresos netos"]) < int(actividad["Total ingresos netos"]):
            mejor_act_del_peorsubs = actividad

        if  int(peor_act_del_mejorsubs["Total ingresos netos"]) < int(actividad["Total ingresos netos"]):
            peor_act_del_peorsubs = actividad

    menor_subsector["Mejor actividad"] = mejor_act_del_peorsubs
    menor_subsector["Peor actividad"] = peor_act_del_peorsubs
    menor_subsector.pop("Actividades económicas",-1)

    #Borrar map de subsectores y meter el mejor y el peor
    mejor_sector["Mejor subsector"] = mayor_subsector
    mejor_sector["Peor subsector"] = menor_subsector
    mejor_sector.pop("Subsector económico",-1) 

    return mejor_sector
def sort_criteria_neto(impuesto1, impuesto2): #men a may
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    """
    return int(impuesto1["Total ingresos netos"]) < int(impuesto2["Total ingresos netos"])
def compareCodigoSector(key_id, entry_impuesto_2): 
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    key_entry_impuesto_2 = me.getKey(entry_impuesto_2)
    if (key_id == key_entry_impuesto_2):
        return 0
    elif (key_id > key_entry_impuesto_2):
        return 1
    else:
        return -1

def req_7(data_structs, top, anio, csse):
    """
    Función que soluciona el requerimiento 7
    """
    lista_del_anio= ""
    if mp.contains(data_structs["map_anio"], anio):
        lista_del_anio= mp.get(data_structs["map_anio"], anio)
    impuestos= lista_del_anio['value']['impuestos']
    lista_csse= lt.newList("ARRAY_LIST")
    for x in lt.iterator(impuestos):
        if csse== x['Código subsector económico']:
            lt.addLast(lista_csse, x)
    map_act_e= mp.newMap(numelements= lt.size(lista_csse))
    for c in lt.iterator(lista_csse):
        act= c['Código actividad económica']
        t_c_y_g= 0
        for v in lt.iterator(lista_csse):
            if act == v['Código actividad económica']:
                t_c_y_g += int(v["Total costos y gastos"])
        if act not in map_act_e:
            mp.put(map_act_e, act, t_c_y_g)
    lista_fin= lt.newList("ARRAY_LIST")
    if int(top) >= mp.size(map_act_e):
        t= mp.size(map_act_e)
        while t!=0:
            cont= 1
            ind= 0
            men_tot_c_y_g= 1000000000000000000000000
            for c in lt.iterator(mp.valueSet(map_act_e)):
                if int(c)< men_tot_c_y_g:
                    men_tot_c_y_g = int(c)
                    ind= cont
                cont += 1
            cod_menor_c_y_g= lt.getElement(mp.keySet(map_act_e),ind)
            tot_ret= 0
            tot_in_net= 0
            tot_c_y_g= 0
            tot_s_a_p= 0
            tot_s_a_f= 0
            for v in lt.iterator(lista_csse):
                if v['Código actividad económica'] == cod_menor_c_y_g:
                    cod_sec= v['Código sector económico']
                    nom_sec= v['Nombre sector económico']
                    cod_s_sec= v['Código subsector económico']
                    nom_s_sec= v['Nombre subsector económico']
                    tot_ret += int(v['Total retenciones'])
                    tot_in_net += int(v['Total ingresos netos'])
                    tot_c_y_g += int(v['Total costos y gastos'])
                    tot_s_a_p += int(v['Total saldo a pagar'])
                    tot_s_a_f += int(v['Total saldo a favor'])
            dic_final= {"Código sector económico": cod_sec,'Nombre sector económico': nom_sec, 'Código subsector económico' : cod_s_sec , 'Nombre subsector económico': nom_s_sec,
                        'Total ingresos netos': tot_in_net, 'Total costos y gastos': tot_c_y_g, 'Total saldo a pagar': tot_s_a_p,'Total saldo a favor': tot_s_a_f }
            lt.addLast(lista_fin, dic_final)
            mp.remove(map_act_e, cod_menor_c_y_g)
            t -=1
    else:
        t= int(top)
        while t!=0:
            cont= 1
            ind= 0
            men_tot_c_y_g= 1000000000000000000000000
            for c in lt.iterator(mp.valueSet(map_act_e)):
                if int(c)< men_tot_c_y_g:
                    men_tot_c_y_g = int(c)
                    ind= cont
                cont += 1
            cod_menor_c_y_g= lt.getElement(mp.keySet(map_act_e),ind)
            tot_ret= 0
            tot_in_net= 0
            tot_c_y_g= 0
            tot_s_a_p= 0
            tot_s_a_f= 0
            for v in lt.iterator(lista_csse):
                if v['Código actividad económica'] == cod_menor_c_y_g:
                    cod_sec= v['Código sector económico']
                    nom_sec= v['Nombre sector económico']
                    cod_s_sec= v['Código subsector económico']
                    nom_s_sec= v['Nombre subsector económico']
                    tot_ret += int(v['Total retenciones'])
                    tot_in_net += int(v['Total ingresos netos'])
                    tot_c_y_g += int(v['Total costos y gastos'])
                    tot_s_a_p += int(v['Total saldo a pagar'])
                    tot_s_a_f += int(v['Total saldo a favor'])
            dic_final= {"Código sector económico": cod_sec,'Nombre sector económico': nom_sec, 'Código subsector económico' : cod_s_sec , 'Nombre subsector económico': nom_s_sec,
                        'Total ingresos netos': tot_in_net, 'Total costos y gastos': tot_c_y_g, 'Total saldo a pagar': tot_s_a_p,'Total saldo a favor': tot_s_a_f }
            lt.addLast(lista_fin, dic_final)
            mp.remove(map_act_e, cod_menor_c_y_g)
            t -=1
    return lista_fin

def req_8(data_structs, top, year):
    year_entry = mp.get(data_structs['map_anio'], year)
    year_data = me.getValue(year_entry)
    lista_actecon = year_data['impuestos']
    map_subsect = mp.newMap(numelements= lt.size(lista_actecon))
    sumas =['Total Impuesto a cargo',"Total ingresos netos", "Costos y gastos nómina", "Total saldo a pagar","Total saldo a favor"]
    for cadauna in lt.iterator(lista_actecon):
        subsector = int(cadauna['Código subsector económico'])
        if not mp.contains(map_subsect, subsector):
            actividades_eco = lt.newList(datastructure="ARRAY_LIST", cmpfunction= compareCodigoActividad)
            lt.addLast(actividades_eco,cadauna)
            info_subsector = {"Nombre sector económico":cadauna["Nombre sector económico"],
                              "Código sector económico":cadauna["Código sector económico"],"Código subsector económico": subsector, "Actividades económicas": actividades_eco}  
            for total in sumas:
                info_subsector[total] = int(cadauna[total])
            mp.put(map_subsect, subsector, info_subsector)
        else:
            entry_info_subsector = mp.get(map_subsect,subsector)
            info_subsector = me.getValue(entry_info_subsector)
            for total in sumas:
                info_subsector[total] = int(cadauna[total]) + int(info_subsector[total])
            lt.addLast(info_subsector["Actividades económicas"], cadauna)
            mp.put(map_subsect, subsector, info_subsector)
    llaves = mp.keySet(map_subsect)
    dict_sumas = {}
    dict_act = {}
    final_final = {}
    for llave in lt.iterator(llaves):
        subsect_entry = mp.get(map_subsect, llave)
        subsect_data = me.getValue(subsect_entry)
        lista_totales = lt.newList('ARRAY_LIST')
        for titulo in sumas:
            lt.addLast(lista_totales, str(subsect_data[titulo]))         
        for caract in lt.iterator(subsect_data['Actividades económicas']):
            lt.addFirst(lista_totales, caract['Nombre subsector económico'])
            lt.addFirst(lista_totales, caract['Código subsector económico'])
            lt.addFirst(lista_totales, caract['Nombre sector económico'])
            lt.addFirst(lista_totales, caract['Código sector económico'])
        dict_sumas[llave] = lista_totales
        lista_actecon_sub = subsect_data['Actividades económicas']
        dict_act[llave] = lista_actecon_sub
        merg.sort(dict_act[llave], cmp_totimpacarg)
        headz = ['Código subsector económico', "Código actividad económica","Nombre actividad económica",
                    'Total Impuesto a cargo',"Total ingresos netos", "Costos y gastos nómina", "Total saldo a pagar","Total saldo a favor"]
        if int(top) > lt.size(dict_act[llave]):
            final_1 = dict_act[llave]['elements']
            final = [[x[headz[0]], x[headz[1]], x[headz[2]],x[headz[3]], x[headz[4]], x[headz[5]], x[headz[6]], x[headz[7]]]for x in final_1]
            final_final[subsect_data['Código subsector económico']] = final
        else:
            final_1 = lt.subList(dict_act[llave], 1, int(top))
            final = [[x[headz[0]], x[headz[1]], x[headz[2]],x[headz[3]], x[headz[4]], x[headz[5]], x[headz[6]], x[headz[7]]]for x in lt.iterator(final_1)]
            final_final[subsect_data['Código subsector económico']] = final
    return dict_sumas, final_final    
def cmp_totimpacarg(data1, data2):
    return int(data1['Total Impuesto a cargo']) > int(data2['Total Impuesto a cargo'])


# Funciones utilizadas para comparar elementos dentro de una lista
def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass
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
