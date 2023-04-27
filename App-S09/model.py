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
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import mergesort as merg
from tabulate import tabulate as tab
assert cf



'''
   ╒═══════════════════════════════════════════════════════════════════════════════════════════════════╕
   │ .                    Se define la estructura de un Catálogo de impuestos como                   . │
   │ .                   una tabla de hash cuyas llaves serán los años del registro                  . │
   │ .                  y sus valores serán tablas de hash secundarias que contengan                 . │
   │ .                   la información de todos los Sectores Económicos de ese año                  . │
   ╘═══════════════════════════════════════════════════════════════════════════════════════════════════╛
'''

def newCatalog(tipo):
    """
    Inicializa la estructura de datos principal del modelo.
    """
    fact = 4 if tipo == 'CHAINING' else 0.5
    catalog = mp.newMap(10,maptype=tipo, loadfactor=fact) 
    # numelements=10 porque se esperan 10 años
    return catalog
# ==============================================================================================================
# ================================= Creación de las estructuras ================================================

def depureCodAct(cod:str)->str: # Función auxiliar para crear una actividad
    """
    Estandariza el código de las actividades
    """
    if not cod.isnumeric():
        cod = (cod.replace('*', '').replace(' ', '')).lower()
        for i in cod:
            if not(i.isnumeric()):
                cod = cod.replace(i,'_')
                break
    return cod

def create_act(row:list, indices:list, columnas:list)->dict:
    act = {} # Se crea el dicionario que guardará la información del registro
    for i in range(len(indices)):
        # Se llena el <dict> 'act' a partir de las listas 'columnas' y 'row', donde las <keys>
        # son los elementos de 'columnas' y los <values> son los elementos correspondientes de 'row'
        llave = columnas[i]
        valor = row[indices[i]]
        if valor.isnumeric(): valor = int(valor)
        else: valor = (valor.lower()).capitalize()
        act[llave] = valor        
    impure_cod = str(act['Código actividad económica']) # Se extrae y luego 
    cod_act = depureCodAct(impure_cod) # se limpia el código de la actividad
    act['Código actividad económica'] = cod_act # Se guarda el cod_act limpio
    return act

def create_sub(act:dict)->dict:
    """
    Crea la estructura de un subsector a partir de la estructura de una actividad
    """
    sub = act.copy()
    del sub['Código actividad económica']  # <-- Se eliminan las llaves de la actividad
    del sub['Nombre actividad económica']  # <----┘
    sub['Actividades'] = lt.newList('ARRAY_LIST') # Se crea la lista de actividades del subsector
    lt.addLast(sub['Actividades'], act) # Se agrega la actividad a la lista
    return sub

def create_sec(act:dict)->dict:
    """
    Crea la estructura de un sector a partir de la estructura de un subsector.
    """
    sub = create_sub(act)
    sector = sub.copy()
    del sector['Código subsector económico']  # <-- Se eliminan las llaves del subsector
    del sector['Nombre subsector económico']  # <----┘|
    del sector['Actividades']                 # <-----┘
    sector['Subsectores'] = mp.newMap(4, maptype='CHAINING', loadfactor=2) 
    # numelements = 4 porque un Sector tiene máximo 4 Subsectores
    mp.put(sector['Subsectores'], sub['Código subsector económico'], sub)
    return sector

# ==============================================================================================================
# =============================== Funciones para agregar información al catálogo ===============================

def updateInfo(grupo, activity): # Función auxiliar para actualizar información
    """
    grupo: se refiere a Grupo Económico (puede ser Sector o Subsector)
    Se actualiza la información del grupo económico con la información de la actividad entrante.
    """
    columns = ['Costos y gastos nómina',
               'Total ingresos netos',
               'Total costos y gastos',
               'Descuentos tributarios',
               'Total Impuesto a cargo',
               'Total retenciones',
               'Total saldo a pagar',
               'Total saldo a favor'] # Las columnas que se deben actualizar
    for i in columns:
        # Se actualizan los valores del grupo
        grupo[i] += activity[i]
    pass

def incorporate_Activity(catalog, actividad): 
    """
    Incorpora una nueva actividad a la estructura del catálogo,
    clasificándola en el lugar al que pertenece.
    """
    anho = actividad['Año']
    cod_sec = actividad['Código sector económico']
    cod_sub = actividad['Código subsector económico']
    sectores = None
    # ------------------------------ Se evalúa la existencia del año --------------------------------------------
    if mp.contains(catalog, anho): # Si el año ya existe
        sector = None 
        sectores = mp.value(catalog, anho) # Se obtiene la tabla de sectores
        # --------------------- Se evalúa la existencia del sector ------------------------------------
        if mp.contains(sectores, cod_sec): # Si el sector existe
            sector = mp.value(sectores, cod_sec) # Se obtiene el sector
            updateInfo(sector, actividad)        # Y se actualiza la información del sector.
            sub = None
            subsecs = sector['Subsectores']  # Se obtiene la tabla de subsectores
            # ------- Se evalúa la existencia del subsector -----------------------
            if mp.contains(subsecs, cod_sub):    # Si el subsector existe
                sub = mp.value(subsecs, cod_sub) # Se obtiene el subsector
                updateInfo(sub, actividad)       # Se actualiza la información del subsector
                lt.addLast(sub['Actividades'], actividad) # Y se agrega la actividad a la lista de actividades del subsector
            else:
                sub = create_sub(actividad) # Si el subsector no existe, se crea con la actividad
            # ---------------------------------------------------------------------
            # De cualquier forma,
            mp.put(subsecs, cod_sub, sub) # Se actualiza (con 'put') el subsector
            sector['Subsectores'] = subsecs # Y se actualizan los subsectores en el diccionario del sector
        else:
            sector = create_sec(actividad) # Si el sector no existe, se crea con la actividad
        # ---------------------------------------------------------------------------------------------
    else: # Si el año no existe, no existe tampoco la estructura que lo acompaña...
        sector = create_sec(actividad) # Se crea el sector (y, a su vez, el sector y la lista de actividades)
        sectores = mp.newMap(12, maptype='PROBING', loadfactor=0.5) # Se crea la tabla de sectores del año
                            # numelements=12 porque un año puede tener hasta 12 Sectores
    # -----------------------------------------------------------------------------------------------------------
    # De cualquier forma se debe actualizar la información de la tabla de sectores asociada al año
    mp.put(sectores, cod_sec, sector) # Se agrega (o se actualiza) el sector en la tabla
    mp.put(catalog, anho, sectores)   # Se agrega (o se actualiza) la tabla de sectores del año
    pass
    
def readRow(catalog:dict, row:list, indices:list, columnas:list):
    """
    Esta función lee, filtra y organiza en el catálogo la 
    información de cada línea del CSV 
    Parámetros:
        catalog: La tabla de hash principal
        row:     Línea de información del CSV en forma de lista
        indices: Lista con los índices de las columnas en 'row'
        columnas:  Lista con los nombres de las columnas
    """
    actividad = create_act(row, indices, columnas)
    
    incorporate_Activity(catalog, actividad)
    
    pass

# ===================================== INICIO REQUERIMIENTOS ======================================
# __________________________________________________________________________________________________
# Reqs 1 y 2 ---------------------------------------------------------------------------------------
def req_1_2(catalog, anio:int, cod_sec:int, monto:str)->dict:
    """
    Busca la actividad de un sector específico
    que tenga el mayor 'monto'
    en un año específico.
    """
    secs = mp.value(catalog, anio)
    sec = mp.value(secs, cod_sec)
    subs = sec["Subsectores"]
    mayor, mayor_monto = (None, -1)
    for cod_sub in mp.iterator(subs):
        actvs = mp.value(subs, cod_sub)["Actividades"]
        for act in lt.iterator(actvs):
            if act[monto] > mayor_monto:
                mayor = act
                mayor_monto = act[monto]
    return mayor
# __________________________________________________________________________________________________
# Reqs 3, 4 y 5 ------------------------------------------------------------------------------------
def req_3_4_5(catalog, anho:int, req:int):
    """
    Función que identifica el subsector económico que tuvo el 
    mayor o menor 'MONTO' para un año especifico
    """
    # Se inicializan las variables que dependen del requerimiento en None
    # y posteriormente se le asignan los valores según corresponda.
    # La variable multiplicador se usa para que en el req 3 se retorne el sub
    # que menos aporta y no el que más.
    monto, cmp_function, multiplicador = None, None, 1
    if req == 3: monto, cmp_function, multiplicador = 'Total retenciones', cmp_retenciones, -1
    elif req == 4: monto, cmp_function = 'Costos y gastos nómina', cmp_nomina
    elif req == 5: monto, cmp_function = 'Descuentos tributarios', cmp_descuentos
    # -----------------------------------------
    # Se inicializan las variables que se utilizan para identificar el mayor Subsec 
    # en valores que con toda seguridad serán reemplazados (pues el mínimo real de los montos es 0, no -1)
    mayor, mayor_monto = (None, None)
    # -----------------------------------------
    secs = mp.value(catalog, anho) # Se obtiene la tabla hash que contiene los sectores del año
    for cod_sec in mp.iterator(secs): # Comienza el recorrido de la tabla de sectores. Este ciclo hará máximo 12 iteraciones (porque puede haber hasta 12 sectores)
        sec = mp.value(secs, cod_sec)
        subs = sec['Subsectores']
        for cod_sub in mp.iterator(subs): # Comienza el recorrido de los Subsectores de cada Sector. Este ciclo hará máximo 4 iteraciones (porque puede haber hasta 4 subsectores en un sector)
            sub = mp.value(subs, cod_sub)
            if mayor_monto is None or sub[monto]*multiplicador > mayor_monto*multiplicador: # Se compara el mondo del Subsec con el mayor monto que se haya almacenado
                mayor = sub              # Si es mayor, entonces se actualizan los valores de las variables correspondientes.
                mayor_monto = sub[monto]
    sub = mayor.copy() # Una vez terminan los ciclos, tendremos en la variable 'mayor' al subsector de respuesta. (Se hace una copia por seguridad, no por necesidad)
    # -----------------------------------------
    # Una vez se tiene el subsector, se editan las llaves que los requerimientos 
    # nos exigen imprimir de un modo específico (agregando 'Total {monto} del subsector económico')
    columnas_a_editar = [monto,
                         'Total ingresos netos',
                         'Total costos y gastos',
                         'Total saldo a pagar',
                         'Total saldo a favor']
    for old_column in columnas_a_editar:
        newKey = ('Total ' + old_column.lower()) if not('Total' in old_column) else old_column
        newKey += ' del subsector económico'
        valor = sub[old_column]
        sub[newKey] = valor
        del sub[old_column]
    # -----------------------------------------
    # Por último, se organizan las actividades del subsector según corresponda:
    #   - Según los 'Costos y gastos nómina' para el req 4
    #   - Según los 'Descuentos tributarios' para el req 5
    sort_get_first_and_last(sub['Actividades'], cmp_function, 3, 3)
    # -----------------------------------------
    return sub 
# __________________________________________________________________________________________________
# Req 6 --------------------------------------------------------------------------------------------
def req_6(data_structs, anho):
    """
    Función que identifica el sector económico que tuvo el 
    mayor 'Total ingresos netos' para un año especifico
    """
    
    sectores_anho = mp.value(data_structs, anho) # Se obtiene la tabla hash que contiene los sectores del año
    cod_sector_mayor = None #Se inicializa la variable en None
    aportaciones_sec_mayor = -1 # Se inicializa la variable en -1
    for cod_sector in mp.iterator(sectores_anho): # Comienza el recorrido de la tabla de sectores
        info_sec = mp.value(sectores_anho, cod_sector)
        aportaciones_sec = info_sec['Total ingresos netos']
        if aportaciones_sec > aportaciones_sec_mayor: # Se actualiza cual es el sector que más aportó
            aportaciones_sec_mayor = aportaciones_sec
            cod_sector_mayor = cod_sector
    sector_mayor = mp.value(sectores_anho, cod_sector_mayor) #Se extrae el sector que más aportó
    tabla_subsectores = sector_mayor['Subsectores'] #Se extrae la tabla de subsectores del sector que más aportó
    
    cod_sub_mas = None
    aportaciones_sub_mas = -1
    cod_sub_menos = None
    aportaciones_sub_menos = -1
    for cod_subsector in mp.iterator(tabla_subsectores): #Se recorren los subsectores del sector para determinar cuál aportó más y cuál menos
        info_sub = mp.value(tabla_subsectores, cod_subsector)
        aportaciones_sub = info_sub['Total ingresos netos']
        if aportaciones_sub > aportaciones_sub_mas:
            cod_sub_mas = cod_subsector
            aportaciones_sub_mas = aportaciones_sub
        if aportaciones_sub < aportaciones_sub_menos or aportaciones_sub_menos<0:
            cod_sub_menos = cod_subsector
            aportaciones_sub_menos = aportaciones_sub
    
    #Se editan las columnas del sector, para incluir sufijos e incluir subsector que más y que menos aportó
    edit_columns_aux_R6(sector_mayor, "sec")
    sector_mayor['Subsector económico que más aportó'] = cod_sub_mas
    sector_mayor['Subsector económico que menos aportó'] = cod_sub_menos
    
    #Se extraen de la tabla de subsectores el sub que más y que menos aportó
    sub_mas = mp.value(tabla_subsectores, cod_sub_mas)
    sub_menos = mp.value(tabla_subsectores, cod_sub_menos)
    
    #Se editan las columnas del subsector, para incluir sufijos
    edit_columns_aux_R6(sub_mas, "sub")
    edit_columns_aux_R6(sub_menos, "sub")
    
    #Se recorre la lista de actividades de cada sub para determinar qué act aporta más
    #o menos en los dos subsectores
    determinar_act_mas_y_menos_aporto_req_6(sub_mas)
    determinar_act_mas_y_menos_aporto_req_6(sub_menos)
    
    #Se hace una lista para cada retorno, para hacer el formateo en el view más fácil
    
    lista_sector = lt.newList("ARRAY_LIST")
    lt.addLast(lista_sector, sector_mayor)
    lista_sub_mas = lt.newList("ARRAY_LIST")
    lt.addLast(lista_sub_mas, sub_mas)
    lista_sub_menos = lt.newList("ARRAY_LIST")
    lt.addLast(lista_sub_menos, sub_menos)
    
    #Se crea la estructura final de retorno, que es una cola
    queue_return = qu.newQueue()
    qu.enqueue(queue_return, lista_sector)
    qu.enqueue(queue_return, lista_sub_mas)
    qu.enqueue(queue_return, lista_sub_menos)
    
    return queue_return

def edit_columns_aux_R6(sector, sec_o_sub: str):
    
    columnas_a_editar = ['Total ingresos netos',
                         'Total costos y gastos',
                         'Total saldo a pagar',
                         'Total saldo a favor']
    if sec_o_sub == 'sec': string = ' del sector económico' 
    elif sec_o_sub == 'sub': string = ' del subsector económico'
    for i in range(len(columnas_a_editar)):
        old_column = columnas_a_editar[i]
        newKey = old_column
        newKey += string
        valor = sector[old_column]
        sector[newKey] = valor
    return sector

def determinar_act_mas_y_menos_aporto_req_6(subsector):
    """Se recorren las actividades del subsector para determinar qué actividad aportó más en el total
    de ingresos netos. Actualiza directamente el subsector para que la actividad se pueda mostrar como
    tabla. 

    Args:
        subsector: El que se quiere cambiar para agregarle la act que más y que menos aportó
    """
    #Se recorren las actividades del subsector para determinar cuál aportó más y cuál menos
    act_mas = None
    aportaciones_act_mas = -1
    act_menos = None
    aportaciones_act_menos = -1
    for actividad in lt.iterator(subsector["Actividades"]):
        aportaciones_act = actividad['Total ingresos netos']
        if aportaciones_act > aportaciones_act_mas:
            act_mas = actividad
            aportaciones_act_mas = aportaciones_act
        if aportaciones_act < aportaciones_act_menos or aportaciones_act_menos<0:
            act_menos = actividad
            aportaciones_act_menos = aportaciones_act
    
    #Se crea la tabla de la actividad que más aportó:
    table_act_mas = [["Código actividad económica",act_mas["Código actividad económica"]],
                 ["Nombre actividad económica",act_mas["Nombre actividad económica"]],
                 ["Total ingresos netos",act_mas["Total ingresos netos"]],
                 ["Total costos y gastos",act_mas["Total costos y gastos"]],
                 ["Total saldo a pagar",act_mas["Total saldo a pagar"]],
                 ["Total saldo a favor",act_mas["Total saldo a favor"]]]
    
    #Se agrega la tabla de la actividad al diccionario del subsector:
    subsector["Actividad que más aportó"] = tab(table_act_mas, tablefmt='fancy_grid',
                stralign='left', numalign='left', maxcolwidths=[10,17])
    
    #Se crea la tabla de la actividad que menos aportó:
    table_act_menos = [["Código actividad económica",act_menos["Código actividad económica"]],
                 ["Nombre actividad económica",act_menos["Nombre actividad económica"]],
                 ["Total ingresos netos",act_menos["Total ingresos netos"]],
                 ["Total costos y gastos",act_menos["Total costos y gastos"]],
                 ["Total saldo a pagar",act_menos["Total saldo a pagar"]],
                 ["Total saldo a favor",act_menos["Total saldo a favor"]]]
    
    #Se agrega la tabla de la actividad al diccionario del subsector:
    subsector["Actividad que menos aportó"] = tab(table_act_menos, tablefmt='fancy_grid',
                stralign='left', numalign='left', maxcolwidths=[10,17])
# __________________________________________________________________________________________________
# Req 7 --------------------------------------------------------------------------------------------
def req_7(catalog, year:int, cantidad:int, cod_sub):
    """
    Recorre todas las actividades que hagan parte de un mismo subsector y año. Estas las añade a una lista y las organiza
    según la que tenga menor costos y gastos. 
    """
    secs = mp.value(catalog, year) # Se obtiene la tabla hash que contiene los sectores del año
    lista_return = None
    for cod_sec in mp.iterator(secs): # Hace el recorrido de la tabla de sectores
        sec=mp.value(secs, cod_sec)
        subs=sec["Subsectores"]
        if mp.contains(subs, cod_sub): #Busca si se contiene el codigo de subsector dado
            info_subsector = mp.value(subs, cod_sub).copy() #Si esta, copia su información
            lista_return = info_subsector["Actividades"] 
            sort_get_first_and_last(lista_return, cmp_cyg, cantidad, 0)
            break
    if lista_return is None: 
        return None
    
    if cantidad < lt.size(lista_return):
        lista_return = lt.subList(lista_return, 1, cantidad)
    return lista_return
# __________________________________________________________________________________________________
# Req 8 --------------------------------------------------------------------------------------------
def req_8(catalog, year:int)->tuple:
    """
    Guarda en un ARRAY LIST todos los Subsectores de un año específico.
    Este array se organiza de mayor a menor según el total de impuesto a cargo del subsector.
    Adicionalmente, la lista de actividades de cada subsector se organiza del mismo modo.
    """
    subs_list = lt.newList('ARRAY_LIST')
    secs = mp.value(catalog, year) # Se obtiene la tabla hash que contiene los sectores del año
    for cod_sec in mp.iterator(secs): # Comienza el recorrido de la tabla de sectores. 
        # Este ciclo hará máximo 12 iteraciones (porque puede haber hasta 12 sectores)
        sec = mp.value(secs, cod_sec)
        subs = sec['Subsectores']
        for cod_sub in mp.iterator(subs): # Comienza el recorrido de los Subsectores de cada Sector.
            # Este ciclo hará máximo 4 iteraciones (porque puede haber hasta 4 subsectores en un sector)
            original_sub = mp.value(subs, cod_sub)
            sub0 = original_sub.copy()      # Se crea una copia del subsector (por seguridad)
            sub = edit_columns_aux_R8(sub0) # Se editan las columnas con una función auxiliar
            sort_get_first_and_last(sub['Actividades'], cmp_cargo, 3, 3)
            lt.addLast(subs_list, sub)
    merg.sort(subs_list, cmp_cargo_subs)
    num = lt.size(subs_list)
    if num > 12:
        fst, lst = first_and_last(subs_list)
        subs_list = join_first_and_last(fst, lst)
    return subs_list, num

def edit_columns_aux_R8(subsector):
    """
    Se editan las columnas de un subsector
    agregando al final '... para el subsector'
    Las columnas antiguas se eliminan
    """
    columnas_a_editar = ['Total Impuesto a cargo',
                         'Total ingresos netos',
                         'Total costos y gastos',
                         'Total saldo a pagar',
                         'Total saldo a favor']
    for i in range(len(columnas_a_editar)):
        old_column = columnas_a_editar[i]
        valor = subsector.get(old_column)
        if valor is None: # Cuando esto sucede, significa que
            continue      # el subsector ya estuvo aquí antes... ¿Por qué?
        newKey = 'Total de impuestos a cargo' if i == 0 else old_column
        newKey += ' para el subsector'
        subsector[newKey] = valor
        del subsector[old_column]
    return subsector
# __________________________________________________________________________________________________
# ======================================= FIN REQUERIMIENTOS =======================================


# ==================================== FUNCIONES DE COMPARACIÓN ====================================

def cmp_anhos(a1:int, a2:int)->bool:
    """
    a1 = Año 1
    a2 = Año 2
    Se compara si el año1 es menor al año2
    """
    return (a1 < a2)

def cmp_cods_acts(act1:dict, act2:dict)->bool:
    """
    Recibe dos actividades económicas y compara 
    si el código de la primera es menor al de la segunda
    """
    c1, c2 = act1['Código actividad económica'], act2['Código actividad económica']
    if not(c1.isnumeric()):
        c1 = c1.split('_')[0]
    if not(c2.isnumeric()):
        c2 = c2.split('_')[0]
    return (int(c1) < int(c2))

def cmp_retenciones(act1:dict, act2:dict)->bool:
    # Función de comparación para el req 3
    r1, r2 = act1['Total retenciones'], act2['Total retenciones']
    return r1 < r2

def cmp_nomina(act1:dict, act2:dict)->bool:
    # Función de comparación para el req 4
    n1, n2 = act1['Costos y gastos nómina'], act2['Costos y gastos nómina']
    return n1 < n2

def cmp_descuentos(act1:dict, act2:dict)->bool:
    # Función de comparación para el req 5
    d1, d2 = act1['Descuentos tributarios'], act2['Descuentos tributarios']
    return d1 < d2

def cmp_cyg(act1:dict, act2:dict)->bool:
    #Función de comparación para el req 7
    rta = None
    cg1, cg2 = act1['Total costos y gastos'], act2['Total costos y gastos']
    rta = cg1 < cg2 if cg1 != cg2 else act1['Nombre actividad económica'] < act2['Nombre actividad económica']
    return rta

def cmp_cargo(act1:dict, act2:dict)->bool:
    # Función de comparación para el req 8
    """
    Compara dos actividades según su Total Impuesto a cargo.
    Si son iguales, compara sus nombres.
    """
    rta = None
    cg1, cg2 = act1['Total Impuesto a cargo'], act2['Total Impuesto a cargo']
    rta = cg1 > cg2 if cg1 != cg2 else act1['Nombre actividad económica'] < act2['Nombre actividad económica']
    return rta

def cmp_cargo_subs(sub1:dict, sub2:dict)->bool:
    """
    Compara dos subsectores de MAYOR a MENOR
    según su Total Impuesto a cargo.
    Si son iguales, compara sus nombres.
    """
    column = 'Total de impuestos a cargo para el subsector'
    rta = None
    cg1, cg2 = sub1[column], sub2[column]
    rta = cg1 > cg2 if cg1 != cg2 else sub1['Nombre subsector económico'] < sub2['Nombre subsector económico']
    return rta

# ==================================================================================================

# ===================================== FUNCIONES ADICIONALES ======================================

def getSortedYears(catalog):
    years = mp.keySet(catalog)
    merg.sort(years, cmp_anhos)
    return years

def getActsFromYear(catalog, year):
    all_actvs = lt.newList('ARRAY_LIST')
    secs = mp.value(catalog, year)
    for cod_sec in mp.iterator(secs):
        sec = mp.value(secs, cod_sec)
        subs = sec['Subsectores']
        for cod_sub in mp.iterator(subs):
            sub = mp.value(subs, cod_sub)
            actvs = sub['Actividades']
            for act in lt.iterator(actvs):
                lt.addLast(all_actvs, act)
    sort_get_first_and_last(all_actvs, cmp_cods_acts, 3, 3)
    return all_actvs

def first_and_last(tad_lst, num=3)->tuple:
    """
    Retorna los primeros y últimos 'num' elementos de un TAD list
    """
    rta = None
    if lt.size(tad_lst) >= num*2:
        first = lt.subList(tad_lst, 1, num)
        pos = lt.size(tad_lst) - num + 1
        last = lt.subList(tad_lst, pos, num)
        rta = (first, last)
    else:
        rta = (None, tad_lst)
    return rta

def join_first_and_last(first, last):
    new_tad = lt.newList('ARRAY_LIST')
    for element in lt.iterator(first):
        lt.addLast(new_tad, element)
    for element in lt.iterator(last):
        lt.addLast(new_tad, element)
    return new_tad

# ==================================================================================================

# ===================================== FUNCIÓN ORDENAMIENTO =======================================

def sort_get_first_and_last(tad_list, sort_crit, first:int, last:int):
    """
    Organiza tad_list de forma tal que los 'first' elementos menores queden al frente
    organizados de menor a mayor y los  y los 'last' elementos mayores queden atras
    también organizados de forma mayor:
    """
    size = lt.size(tad_list) 
    if size <= first+last: 
        merg.sort(tad_list, sort_crit) # El merg.sort no retorna nada, sólo organiza la lista
    else:
        i = 1
        while i <= first:
            minimum = i
            for j in range(i, size+1):
                if sort_crit(lt.getElement(tad_list, j), lt.getElement(tad_list, minimum)):
                    minimum = j
            lt.exchange(tad_list, i, minimum)
            i+=1
        i = size
        while i > (size - last):
            maximum = i
            for j in range(first+1, i):
                if sort_crit(lt.getElement(tad_list, maximum), lt.getElement(tad_list, j)):
                    maximum = j
            lt.exchange(tad_list, i, maximum)
            i -= 1
    return tad_list