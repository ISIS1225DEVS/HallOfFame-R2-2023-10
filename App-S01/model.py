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
from tabulate import tabulate
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(data_type):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None
    }

    data_structs["data"] = mp.newMap(12,
                                    maptype = data_type,
                                    loadfactor = 4)

    return data_structs

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["Año"], 
    data["Código actividad económica"], 
    data["Nombre actividad económica"], 
    data["Código sector económico"], 
    data["Nombre sector económico"], 
    data["Código subsector económico"], 
    data["Nombre subsector económico"], 
    data["Total ingresos netos"], 
    data["Total costos y gastos"], 
    data["Total saldo a pagar"], 
    data["Total saldo a favor"],
    data["Total retenciones"],
    data["Costos y gastos nómina"],
    data["Total Impuesto a cargo"],
    data["Descuentos tributarios"])

    dato = mp.contains(data_structs["data"], int(data["Año"]))

    if dato:
        entry = mp.get(data_structs["data"], int(data["Año"]))
        lista = me.getValue(entry)
        lt.addLast(lista, d)
    else:
        lista = lt.newList(datastructure= "ARRAY_LIST", cmpfunction=compare_cod)
        lt.addLast(lista, d)
        mp.put(data_structs["data"], int(data["Año"]), lista)

    return data_structs

def sorted_map_cod(data_structs):


    lista_ordenada = lt.newList("ARRAY_LIST")

    for key in range(2012,2022):
        year = mp.get(data_structs['data'],key)
        act = me.getValue(year)
        merg.sort(act,compare_cod_mayor)
        lt.addLast(lista_ordenada,act)

    return lista_ordenada


def new_data(Año, Cod_act_eco, Nom_act_econ, Cod_sec_eco, Nom_sec_eco, Cod_sub_eco, Nom_sub_eco, Tta_ing_net, Tta_cost_gas, Tta_sld_pag, Tta_sld_fav, Tta_ret, Cos_nom, Tta_impuesto_cargo, Des_Tri):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {"Año":Año, 
    "Código actividad económica":Cod_act_eco,
    "Nombre actividad económica":Nom_act_econ,
    "Código sector económico":Cod_sec_eco, 
    "Nombre sector económico":Nom_sec_eco, 
    "Código subsector económico":Cod_sub_eco,
    "Nombre subsector económico":Nom_sub_eco, 
    "Total ingresos netos":Tta_ing_net, 
    "Total costos y gastos":Tta_cost_gas,  
    "Total saldo a pagar":Tta_sld_pag, 
    "Total saldo a favor":Tta_sld_fav,
    "Total retenciones": Tta_ret,
    "Costos y gastos nómina": Cos_nom,
    "Total Impuesto a cargo": Tta_impuesto_cargo,
    "Descuentos tributarios": Des_Tri}

    return data
    
def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return mp.size(data_structs["data"])


def req_1(data_structs, anio, cod):
    """
    Función que soluciona el requerimiento 1
    """
    entry = mp.get(data_structs, anio)
    lista = me.getValue(entry)
    max_elemento = lt.firstElement(lista)
    
    for elemento in lt.iterator(lista):
       
        if int(elemento["Código sector económico"]) == int(cod):
            if int(max_elemento["Total saldo a pagar"]) < int(elemento["Total saldo a pagar"]):
                max_elemento = elemento 
                
    

    return max_elemento

def req_2(data_structs, anio, cod):
    """
    Función que soluciona el requerimiento 2
    """
    entry = mp.get(data_structs, anio)
    lista = me.getValue(entry)
    max_elemento = lt.firstElement(lista)
    
    
    for elemento in lt.iterator(lista):
        
        if int(elemento["Código sector económico"]) == int(cod):
            if int(max_elemento["Total saldo a favor"]) < int(elemento["Total saldo a favor"]):
                max_elemento = elemento
                
            
    return max_elemento

def req_3(data_structs, anio):
    """
    Función que soluciona el requerimiento 3
    """

    entry = mp.get(data_structs, anio)
    lista = me.getValue(entry)

    div_subsectores = mp.newMap(12, 
                                maptype= "CHAINING",
                                loadfactor= 4)
    
    for elemento in lt.iterator(lista):
        dato = mp.contains(div_subsectores, int(elemento["Código subsector económico"]))
        if dato == True:
            entry = mp.get(div_subsectores, int(elemento["Código subsector económico"]))
            all_subsectores = me.getValue(entry)
            for subsector in lt.iterator(all_subsectores):
                costos = int(subsector["Total costos y gastos"]) + int(elemento["Total costos y gastos"])
                ingresos = int(subsector["Total ingresos netos"]) + int(elemento["Total ingresos netos"])
                retenciones = int(subsector["Total retenciones"]) + int(elemento["Total retenciones"])
                saldo_pagar = int(subsector["Total saldo a pagar"]) + int(elemento["Total saldo a pagar"])
                saldo_favor = int(subsector["Total saldo a favor"]) + int(elemento["Total saldo a favor"])
                dic = {'Código sector económico': elemento["Código sector económico"], 
                        'Nombre sector económico': elemento["Nombre sector económico"], 
                        'Código subsector económico': elemento["Código subsector económico"], 
                        'Nombre subsector económico': elemento["Nombre subsector económico"],
                        'Total retenciones': retenciones,
                        'Total ingresos netos': ingresos,  
                        'Total costos y gastos': costos,
                        'Total saldo a pagar': saldo_pagar, 
                        'Total saldo a favor': saldo_favor}
                lt.changeInfo(all_subsectores, 1, dic)
        else:
            new_list = lt.newList("ARRAY_LIST", cmpfunction=compare_subcod)
            lt.addLast(new_list, elemento)
            mp.put(div_subsectores, int(elemento["Código subsector económico"]), new_list)

    subsectores = mp.valueSet(div_subsectores)
    valor = lt.firstElement(subsectores)
    valor_2 = lt.firstElement(valor)
    valor_retenciones = int(valor_2["Total retenciones"])
    cod = int(valor_2["Código subsector económico"])

    for sub_elementos in lt.iterator(subsectores):
        for llave in lt.iterator(sub_elementos):
            if int(llave["Total retenciones"]) < valor_retenciones:
                cod = int(llave["Código subsector económico"])
                valor_retenciones = int(llave["Total retenciones"])

    entry = mp.get(div_subsectores, cod)
    lista_min = me.getValue(entry)

    act_eco = lt.newList("ARRAY_LIST")

    for actividad in lt.iterator(lista):
        if int(actividad["Código subsector económico"]) == cod:
            lt.addLast(act_eco,actividad)
        
    merg.sort(act_eco, compare_retenciones)

    tabla_grande = []
    table = []

    if lt.size(act_eco) <= 6:
        for actividad in lt.iterator(act_eco):
            table = [actividad["Código actividad económica"],
                    actividad["Nombre actividad económica"],
                    actividad["Total retenciones"], 
                    actividad["Total ingresos netos"], 
                    actividad["Total costos y gastos"],
                    actividad["Total saldo a pagar"], 
                    actividad["Total saldo a favor"]]
            if table not in tabla_grande:
                tabla_grande.append(table)
    
    else:
        peores = lt.subList(act_eco,1,3)
        mejores = lt.subList(act_eco,lt.size(act_eco)-3,3)
    
        for elemento in peores["elements"]:
            table = [elemento["Código actividad económica"], 
                    elemento["Nombre actividad económica"],
                    elemento["Total retenciones"], 
                    elemento["Total ingresos netos"], 
                    elemento["Total costos y gastos"],
                    elemento["Total saldo a pagar"], 
                    elemento["Total saldo a favor"]]
            if table not in tabla_grande:
                tabla_grande.append(table)
        for elemento in mejores["elements"]:
            table = [elemento["Código actividad económica"], 
                    elemento["Nombre actividad económica"],
                    elemento["Total retenciones"], 
                    elemento["Total ingresos netos"], 
                    elemento["Total costos y gastos"],
                    elemento["Total saldo a pagar"], 
                    elemento["Total saldo a favor"]]
            if table not in tabla_grande:
                tabla_grande.append(table)
        
    return lista_min['elements'][0], tabla_grande



def req_4(data_structs, anio):
    """
    Función que soluciona el requerimiento 4
    """
    entry = mp.get(data_structs, anio)
    lista = me.getValue(entry)

    mapa_subsectores = mp.newMap(12,
                                maptype = 'PROBING' ,
                                loadfactor = 0.5)

    for elemento in lt.iterator(lista):
        if mp.contains(mapa_subsectores, int(elemento["Código subsector económico"])):
            entry = mp.get(mapa_subsectores, int(elemento["Código subsector económico"]))
            lista_subsectores = me.getValue(entry)
            for subsector in lt.iterator(lista_subsectores):
                nomina = int(subsector["Costos y gastos nómina"]) + int(elemento["Costos y gastos nómina"])
                ingresos = int(subsector["Total ingresos netos"]) + int(elemento["Total ingresos netos"])
                costos_gastos = int(subsector["Total costos y gastos"]) + int(elemento["Total costos y gastos"])
                saldo_pagar = int(subsector["Total saldo a pagar"]) + int(elemento["Total saldo a pagar"])
                saldo_favor = int(subsector["Total saldo a favor"]) + int(elemento["Total saldo a favor"])

                nuevo_dic = {'Código sector económico': elemento["Código sector económico"], 'Nombre sector económico': elemento["Nombre sector económico"], 
                         'Código subsector económico': elemento["Código subsector económico"], 'Nombre subsector económico': elemento["Nombre subsector económico"],
                         'Costos y gastos nómina': nomina,
                         'Total ingresos netos': ingresos, 
                         'Total costos y gastos': costos_gastos, 'Total saldo a pagar': saldo_pagar, 
                         'Total saldo a favor': saldo_favor}

                lt.changeInfo(lista_subsectores,1, nuevo_dic)

        else:
            nueva_lista = lt.newList('ARRAY_LIST', compare_subcod)
            lt.addLast(nueva_lista, elemento)
            mp.put(mapa_subsectores, int(elemento["Código subsector económico"]), nueva_lista)

    
    info_subsectores = mp.valueSet(mapa_subsectores)

    valor_nomina = 1000

    for lista_subsector in lt.iterator(info_subsectores):
        for subsector in lt.iterator(lista_subsector):
            if int(subsector["Costos y gastos nómina"]) > valor_nomina:
                cod = int(subsector["Código subsector económico"])
                valor_nomina = int(subsector["Costos y gastos nómina"])

    codigo_mayor = mp.get(mapa_subsectores,cod)
    lista_maximo = me.getValue(codigo_mayor)

    actividades_economicas = lt.newList("ARRAY_LIST")

    for act in lt.iterator(lista):
        if int(act["Código subsector económico"]) == cod:
            lt.addLast(actividades_economicas,act)
        
    merg.sort(actividades_economicas,compare_nomina_act)

    tabla_grande = []
    table = []

    if lt.size(actividades_economicas) <= 6:
        for actividad in lt.iterator(actividades_economicas):
             table = [actividad["Código actividad económica"], actividad["Nombre actividad económica"],
                        actividad["Costos y gastos nómina"],actividad["Total ingresos netos"], actividad["Total costos y gastos"],
                        actividad["Total saldo a pagar"],actividad["Total saldo a favor"]]
             if table not in tabla_grande:
                tabla_grande.append(table)
    
    else:
        peores = lt.subList(actividades_economicas,1,3)
        mejores = lt.subList(actividades_economicas,lt.size(actividades_economicas)-3,3)
    
        for elemento in peores["elements"]:
            table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Costos y gastos nómina"],elemento["Total ingresos netos"], elemento["Total costos y gastos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
            if table not in tabla_grande:
                tabla_grande.append(table)
        for elemento in mejores["elements"]:
            table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Costos y gastos nómina"],elemento["Total ingresos netos"], elemento["Total costos y gastos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
            if table not in tabla_grande:
                tabla_grande.append(table)
        

    return lista_maximo['elements'][0], tabla_grande


def req_5(data_structs, year):
    """
    Función que soluciona el requerimiento 5
    """
    anio = mp.get(data_structs, year)
    if anio == None:
        return None
    data = me.getValue(anio)
    
    subsectores = mp.newMap(30,
                            maptype = "CHAINING",
                            loadfactor = 4)
    
    for dato in lt.iterator(data):     
        add_to(subsectores, dato, "subsector")
    get_sum(subsectores, True)
    
    sub = get_max_min(subsectores, "subsector", None, 4)
    actividades = sub[1]
    
    merg.sort(actividades, compare_descuentos)
    if lt.size(actividades) <= 6:
        a = turn_to_list(actividades)
        act = []
        act.append(a[0])
        h = a[1]
    else:
        act = []
        act_min = lt.subList(actividades, 1, 3)
        act_max = lt.subList(actividades, lt.size(actividades) - 3, 3)
        a_max = turn_to_list(act_max)
        a_min = turn_to_list(act_min)
        for a in a_min[0]:
            act.append(a)
        for a in a_max[0]:
            act.append(a)
        h = a_max[1]

    return sub[0], act, h


def req_6(data_structs, year):
    """
    Función que soluciona el requerimiento 6
    """
    anio = mp.get(data_structs, year)
    if anio == None:
        return None
    data = me.getValue(anio)
    
    sectores = mp.newMap(30,
                        maptype = "CHAINING",
                        loadfactor = 4)
    subsectores = mp.newMap(30, 
                            maptype = "CHAINING",
                            loadfactor = 4)
    max_actividades = mp.newMap(30, 
                                maptype = "CHAINING",
                                loadfactor = 4)
    min_actividades = mp.newMap(30, 
                                maptype = "CHAINING",
                                loadfactor = 4)
    
    for dato in lt.iterator(data):     
        add_to(sectores, dato, "sector")
    get_sum(sectores)

    sec = get_max_min(sectores, "sector")
    max_sec = sec[0]
    
    for dato_sec in lt.iterator(sec[2]):
        add_to(subsectores, dato_sec, "subsector")
    get_sum(subsectores)
    
    sub = get_max_min(subsectores, "subsector", max_sec[0])
    
    for dato_suma in lt.iterator(sub[2]):
        add_to(max_actividades, dato_suma, "actividad")
    get_sum(max_actividades)
    for dato_sumi in lt.iterator(sub[3]):
        add_to(min_actividades, dato_sumi, "actividad")
    get_sum(min_actividades)
    
    max_act = get_max_min(max_actividades, "actividad", sub[0][0])
    min_act = get_max_min(min_actividades, "actividad", sub[1][0])
    return max_sec, sub, max_act, min_act


def add_to(map: map, data, type: str) -> None:
    if type == "actividad":
        added = "Código " + type + " económica"
    else:
         added = "Código " + type + " económico"
    inside = mp.contains(map, data[added])
    
    if inside:
        entry = mp.get(map, data[added])
        members = me.getValue(entry)
        lt.addLast(members, data)
    else:
        members = lt.newList(datastructure= "ARRAY_LIST")
        lt.addLast(members, data)
        mp.put(map, data[added], members)
    
    return None


def get_sum(mapa: map, des: bool = False) -> None:
    lis = None
    for element in lt.iterator(mp.keySet(mapa)):
        s = mp.get(mapa, element)
        del lis
        lis = me.getValue(s)
        sum_dt = 0
        sum_in = 0
        sum_cg = 0
        sum_sp = 0
        sum_sf = 0
        for act in lt.iterator(lis):
            sum_dt = sum_dt + int(act["Descuentos tributarios"])
            sum_in = sum_in + int(act["Total ingresos netos"])
            sum_cg = sum_cg + int(act["Total costos y gastos"])
            sum_sp = sum_sp + int(act["Total saldo a pagar"])
            sum_sf = sum_sf + int(act["Total saldo a favor"])
        if des:
            lt.addLast(lis, sum_dt)
        lt.addLast(lis, sum_in)
        lt.addLast(lis, sum_cg)
        lt.addLast(lis, sum_sp)
        lt.addLast(lis, sum_sf)
    return None


def get_max_min(mapa: map, type: str, table: list = None, pos: int = 3) -> tuple:
    if pos != 3:
        des = True
    else:
        des = False
    if mp.size(mapa) == 1:
        elemento = me.getValue(mp.get(mapa, lt.firstElement(mp.keySet(mapa))))
        if des:
            data = set_up_table(elemento, type, des)
            return data, elemento
        else:
            data = set_up_table(elemento, type)
            if table:
                if len(table) < 8:
                    table.append(data[0][0])
                    table.append(data[0][0])
            return data, data, elemento, elemento
    else:
        max = me.getValue(mp.get(mapa, lt.firstElement(mp.keySet(mapa))))
        min = me.getValue(mp.get(mapa, lt.firstElement(mp.keySet(mapa))))
        in_max = lt.getElement(max, lt.size(max) - pos)
        in_min = lt.getElement(min, lt.size(min) - pos)
        for element in lt.iterator(mp.keySet(mapa)):
            s = mp.get(mapa, element)
            usable = me.getValue(s)
            in_u = lt.getElement(usable, lt.size(usable) - pos)
            if int(in_u) > int(in_max):
                max = usable
                in_max = lt.getElement(max, lt.size(max) - pos)
            if int(in_min) > int(in_u):
                min = usable
                in_min = lt.getElement(min, lt.size(min) - pos)
        if des:
            max_data = set_up_table(max, type, des)
            return max_data, max
        else:
            max_data = set_up_table(max, type)
            min_data = set_up_table(min, type)
            if table:
                if len(table) < 8:
                    table.append(max_data[0][0])
                    table.append(min_data[0][0])
            return max_data, min_data, max, min


def set_up_table(data: lt, type: str, des: bool = False) -> list:
    suf = " del "+ type + " económico"
    tot_in = "Total ingresos netos"
    tot_cg = "Total costos y gastos"
    tot_sp = "Total saldo por pagar"
    tot_sf = "Total saldo a favor"
    add = 0
    
    if type == "actividad":
        cod = "Código " + type + " económica"
        name = "Nombre " + type + " económica"
        headers = [cod, name, tot_in, tot_cg, tot_sp, tot_sf]
    else:
        cod = "Código " + type + " económico"
        name = "Nombre " + type + " económico"
        if type == "sector":
            mas = "Subsector económico que más aportó"
            menos = "Subsector económico que menos aportó"
        else:
            mas = "Actividad económica que más aportó"
            menos = "Actividad económica que menos aportó"
        headers = [cod, name, tot_in + suf, tot_cg + suf, tot_sp + suf, tot_sf + suf, mas, menos]
        if des:
            tot_dt = "Total descuentos tributarios" + suf
            cod_prev = "Código sector económico"
            name_prev = "Nombre sector económico"
            add = 1
            headers = [cod_prev, name_prev, cod, name, tot_dt, tot_in + suf, tot_cg + suf, tot_sp + suf, tot_sf + suf]
    dato = data["elements"][0]
    datos = st.newStack()
    table = []
    if des:
        table.append(dato[cod_prev])
        table.append(dato[name_prev])
    table.append(dato[cod])
    table.append(dato[name])
    for i in range(4 + add):
        st.push(datos, lt.removeLast(data))
    for j in range(4 + add):
        table.append(st.pop(datos))
    return table, headers


def turn_to_list(lst: lt) -> tuple:
    headers = [
        "Código actividad económica",
        "Nombre actividad económica",
        "Descuentos tributarios",
        "Total ingresos netos",
        "Total costos y gastos",
        "Total saldo a pagar",
        "Total saldo a favor"
    ]
    table = []
    
    for act in lt.iterator(lst):
        row = []
        for header in headers:
            if header in act:
                row.append(act[header])
        table.append(row)
    return table, headers


def req_7(data_structs, anio,n,cod):
    """
    Función que soluciona el requerimiento 7
    """
    entry = mp.get(data_structs, anio)
    lista = me.getValue(entry)
    actividades_sub = lt.newList('ARRAY_LIST')

    for act in lt.iterator(lista):
        if int(act['Código subsector económico']) == cod:
            lt.addLast(actividades_sub,act)
    
    merg.sort(actividades_sub,compare_costos_gastos_act)

    tabla_grande = []
    table = []
    
    answer = False

    if lt.size(actividades_sub) <= n and lt.size(actividades_sub)!= 0:
        for actividad in lt.iterator(actividades_sub):
             table = [actividad["Código actividad económica"], actividad["Nombre actividad económica"],
                      actividad['Código sector económico'], actividad['Nombre sector económico'],
                        actividad["Total ingresos netos"],actividad["Total costos y gastos"],
                        actividad["Total saldo a pagar"],actividad["Total saldo a favor"]]
             tabla_grande.append(table)

    if lt.size(actividades_sub) == 0:
        answer = True
             

    if lt.size(actividades_sub) > n:
        sublista = lt.subList(actividades_sub,1,n)
        for actividad in lt.iterator(sublista):
            table = [actividad["Código actividad económica"], actividad["Nombre actividad económica"],
                    actividad['Código sector económico'], actividad['Nombre sector económico'],
                    actividad["Total ingresos netos"],actividad["Total costos y gastos"],
                    actividad["Total saldo a pagar"],actividad["Total saldo a favor"]]
            tabla_grande.append(table)


    
    return tabla_grande, answer
    

def req_8(data_structs,anio,n):
    """
    Función que soluciona el requerimiento 8
    """

    entry = mp.get(data_structs, anio)
    lista = me.getValue(entry)

    mapa_subsectores = mp.newMap(20,
                                maptype = "PROBING",
                                loadfactor = 0.5)
    
    mapa_subsectores_suma = mp.newMap(20,
                                maptype = "PROBING",
                                loadfactor = 0.5)
    

    for elemento in lt.iterator(lista):
        if mp.contains(mapa_subsectores, int(elemento["Código subsector económico"])):
            entry = mp.get(mapa_subsectores, int(elemento["Código subsector económico"]))
            lista_subsectores = me.getValue(entry)
            lt.addLast(lista_subsectores,elemento)

        else:
            lista_subsectores = lt.newList('ARRAY_LIST', compare_subcod)
            lt.addLast(lista_subsectores, elemento)
            mp.put(mapa_subsectores, int(elemento["Código subsector económico"]), lista_subsectores)

    for elemento in lt.iterator(lista):
        if mp.contains(mapa_subsectores_suma, int(elemento["Código subsector económico"])):
            entry = mp.get(mapa_subsectores_suma, int(elemento["Código subsector económico"]))
            lista_subsectores = me.getValue(entry)
            for subsector in lt.iterator(lista_subsectores):
                impuestos = int(subsector["Total Impuesto a cargo"]) + int(elemento["Total Impuesto a cargo"])
                ingresos = int(subsector["Total ingresos netos"]) + int(elemento["Total ingresos netos"])
                costos_gastos = int(subsector["Total costos y gastos"]) + int(elemento["Total costos y gastos"])
                saldo_pagar = int(subsector["Total saldo a pagar"]) + int(elemento["Total saldo a pagar"])
                saldo_favor = int(subsector["Total saldo a favor"]) + int(elemento["Total saldo a favor"])

                nuevo_dic = {'Código sector económico': elemento["Código sector económico"], 'Nombre sector económico': elemento["Nombre sector económico"], 
                         'Código subsector económico': elemento["Código subsector económico"], 'Nombre subsector económico': elemento["Nombre subsector económico"],
                         'Total Impuesto a cargo': impuestos,
                         'Total ingresos netos': ingresos, 
                         'Total costos y gastos': costos_gastos, 'Total saldo a pagar': saldo_pagar, 
                         'Total saldo a favor': saldo_favor}

                lt.changeInfo(lista_subsectores,1, nuevo_dic)

        else:
            lista_subsectores = lt.newList('ARRAY_LIST', compare_subcod)
            lt.addLast(lista_subsectores, elemento)
            mp.put(mapa_subsectores_suma, int(elemento["Código subsector económico"]), lista_subsectores)


    keys = mp.keySet(mapa_subsectores)
    lista_ordenada = lt.newList("ARRAY_LIST")
    lista_act_ordenada = lt.newList("ARRAY_LIST")
    
    
    for key in lt.iterator(keys):
      
        entry_act = mp.get(mapa_subsectores,key)
        lista_act = me.getValue(entry_act)
        entry_sub = mp.get(mapa_subsectores_suma,key)
        lista_sub = me.getValue(entry_sub)
        merg.sort(lista_act,compare_impuesto_cargo_act)

        lt.addLast(lista_act_ordenada,lista_act)

        for elemento in lt.iterator(lista_sub):
            lt.addLast(lista_ordenada,elemento)

    merg.sort(lista_ordenada,compare_impuesto_cargo_act)

    return lista_ordenada, lista_act_ordenada

    
    


# Funciones utilizadas para comparar elementos dentro de una lista

def compare_retenciones(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    if int(data_1["Total retenciones"]) < int(data_2["Total retenciones"]):
        return True
    else: 
        return False
    
def compare_subcod(data_1, data_2):
    """
    Función encargada de comparar el año de dos datos.
    """
    if data_1 < data_2["Código actividad económica"]:
        return -1
    elif data_1 > data_2["Código actividad económica"]:
        return 1
    
    else:
        return 0

def compare_cod_mayor(data_1, data_2):

    
        if 'y' in data_1["Código actividad económica"].lower() or 'y' in data_2["Código actividad económica"].lower():
            if (data_1["Código actividad económica"]) < (data_2["Código actividad económica"]):
                return True
            else: 
                return False
        
        elif '/' in data_1["Código actividad económica"] or '/' in data_2["Código actividad económica"]:
            if (data_1["Código actividad económica"]) < (data_2["Código actividad económica"]):
                return True
            else: 
                return False
        
        elif '*' in data_1["Código actividad económica"] or '*' in data_2["Código actividad económica"]:
            if (data_1["Código actividad económica"]) < (data_2["Código actividad económica"]):
                return True
            else: 
                return False
        
        else:
            if int(data_1["Código actividad económica"]) < int(data_2["Código actividad económica"]):
                return True
            else: 
                return False
   

    
def compare_cod(data_1, data_2):
    """
    Función encargada de comparar el año de dos datos.
    """
    if data_1 < data_2["Código actividad económica"]:
        return -1
    elif data_1 > data_2["Código actividad económica"]:
        return 1
    
    else:
        return 0
    
def compare_subcod(data_1, data_2):
    """
    Función encargada de comparar el año de dos datos.
    """
    if data_1 < data_2["Código actividad económica"]:
        return -1
    elif data_1 > data_2["Código actividad económica"]:
        return 1
    
    else:
        return 0
    
def compare_nomina_act(data_1, data_2):
    """
    Función encargada de comparar el año de dos datos.
    """
    if int(data_1["Costos y gastos nómina"]) < int(data_2["Costos y gastos nómina"]):
        return True
    else: 
        return False
    
def compare_costos_gastos_act(data_1, data_2):
    """
    Función encargada de comparar el año de dos datos.
    """
    if int(data_1["Total costos y gastos"]) < int(data_2["Total costos y gastos"]):
        return True
    elif int(data_1["Total costos y gastos"]) > int(data_2["Total costos y gastos"]):
        return False
    
    else:
        if data_1["Código actividad económica"] < data_2["Código actividad económica"]:
            return True
        
def compare_impuesto_cargo_act(data_1, data_2):
    """
    Función encargada de comparar el año de dos datos.
    """
    if int(data_1["Total Impuesto a cargo"]) > int(data_2["Total Impuesto a cargo"]):
        return True
    elif int(data_1["Total Impuesto a cargo"]) < int(data_2["Total Impuesto a cargo"]):
        return False
    
    else:
        if data_1["Nombre subsector económico"][0] > data_2["Nombre subsector económico"][0]:
            return True

def compare_impuesto_cargo_sub(data_1, data_2):
    """
    Función encargada de comparar el año de dos datos.
    """
    if int(data_1["Total Impuesto a cargo"]) < int(data_2["Total Impuesto a cargo"]):
        return True
    elif int(data_1["Total Impuesto a cargo"]) > int(data_2["Total Impuesto a cargo"]):
        return False
    
    else:
        if data_1["Nombre subsector económico"][0] < data_2["Nombre subsector económico"][0]:
            return True
    

def compare_ingreso_neto(data_1, data_2):
    """
    Función encargada de comparar el ingreso neto de dos datos.
    """
    dat1 = data_1["elements"][0]
    dat2 = data_2["elements"][0]
    if int(dat1["Total ingresos netos"]) > int(dat2["Total ingresos netos"]):
        return True
    else:
        return False
    

def compare_descuentos(data1, data2):
    if int(data1["Descuentos tributarios"]) < int(data2["Descuentos tributarios"]):
        return True
    else:
        return False

    
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


def sortDataMap(data_structs):
    anios = mp.keySet(data_structs)
    
    for anio in lt.iterator(anios):
        a = mp.get(data_structs, anio)
        sortable = me.getValue(a)
        merg.sort(sortable, compare_cod_mayor)
    return None

"""
def sort(data_structs):
    
    #TODO: Crear función de ordenamiento
    y = data_structs["model"]
    x = mp.valueSet(data_structs)
    lista = mp.valueSet(y)
    for elemento in lt.iterator(lista):
        x = elemento
    lista = mp.valueSet(data_structs["model"])
    merg.sort(lista, compare)
    return lista
"""