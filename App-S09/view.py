"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import sys
import controller
import config as cf
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
from DISClib.ADT import queue as qu
from tabulate import tabulate as tab
assert cf



'''
   ╒═══════════════════════════════════════════════════════════════════════════════════════════════════╕
   │ .                     La vista se encarga de la interacción con el usuario.                     . │
   │ .                       Presenta el menu de opciones y por cada seleccion                       . │
   │ .                      se hace la solicitud al controlador para ejecutar la                     . │
   │ .                                      operación solicitada                                     . │
   ╘═══════════════════════════════════════════════════════════════════════════════════════════════════╛
'''

# ══════════════════════════════ Instancia al controller ═════════════════════════════

def new_controller(datastructure='CHAINING'):
    """
    Se crea una instancia del controlador
    """
    return controller.new_controller(datastructure)

# ════════════════════════════════════════════════════════════════════════════════════

# Funciones auxiliares para impresión de tablas e interacción con el usuario.
# (Estructuras de tablas y depuración de ingresos)

def tablas(func:str, fmt='fancy_outline')->list:
    """
    En esta función están centralizadas las tablas de 
    interacción con el usuario relacionadas con la carga de datos.
    """
    msje = None
    tabla = None
    if func == 'y/n':
        tabla = [[' 1  »  Sí'], 
                 [' 0  »  No']]
        msje = tab(tabla, tablefmt=fmt)
    elif func == 'DS':
        tabla = [["     Estructuras disponibles"],
                 ["Ingrese 1 para » SEPARATE CHAINING"],
                 ["Ingrese 2 para »   LINEAR PROBING"]]
        msje = tab(tabla, headers='firstrow', tablefmt=fmt) 
    elif func == 'FS':
        tabla = [[" Archivos disponibles"],
                 ["Ingrese 1 para » small"],
                 ["Ingrese 2 para »   5%"],
                 ["Ingrese 3 para »  10%"],
                 ["Ingrese 4 para »  20%"],
                 ["Ingrese 5 para »  30%"],
                 ["Ingrese 6 para »  50%"],
                 ["Ingrese 7 para »  80%"],
                 ["Ingrese 8 para » large"]]
        msje = tab(tabla, headers='firstrow', tablefmt=fmt) 
    elif func == 'menu':
        tabla = [['✔','Menú Principal'.center(90)],
            ['1','Cargar información en el catálogo'],                               # Carga de datos ✔
            ['2','Actividad de un sector con mayor SALDO A PAGAR en un año'],        # REQ 1 (G) ✔
            ['3','Actividad de un sector con mayor SALDO A FAVOR en un año'],        # REQ 2 (G) ✔
            ['4','Subsector con el menor TOTAL DE RETENCIONES en un año'],           # REQ 3 (I) ✔
            ['5','Subsector con los mayores COSTOS Y GASTOS DE NÓMINA para un año'], # REQ 4 (I) ✔
            ['6','Subsector con los mayores DESCUENTOS TRIBUTARIOS para un año'],    # REQ 5 (I) ✔
            ['7','Sector con el mayor total de INGRESOS NETOS para un año'],         # REQ 6 (G) ✔
            ['8','TOP (N) - Actividades de un Subsector con menor TOTAL COSTOS Y GASTOS para un año'], # REQ 7 (G)
            ['9','TOP (N) - Actividades de cada Subsector con mayor TOTAL de IMPUESTOS A CARGO para un año'], # REQ 8 (B) ✔
            ['0','Salir'] # ✔
            ] 
        msje = tab(tabla,headers='firstrow', tablefmt='fancy_outline',stralign='left', maxcolwidths=[3, 90])
    return msje

def printMenu():
    print('\n')
    Menu = tablas('menu')
    print(Menu)
    pass

def formatNumber(value, mdelim='´', thdelim='.',dedelim=',')->str:
    """
    Recibe el valor de un número entero (ya sea como int o str)
    y retorna un str del número ahora con separadores de miles, millones
    y el separador decimal
    Args:
        value: el número que se quiere formatear, 
        _      puede ser int o un int expresado como str.
        mdelim: Delimitador de millones
        thdelim: Delimitador de miles
        dedelim: Delimitador decimal
    """
    msje = ''
    value = str(value)
    i = -1
    digits = 0
    mill = 1
    while i >= (-len(value)):
        msje = value[i] + msje 
        digits += 1
        if digits%6 == 0: 
            msje = mdelim*mill + msje
            mill += 1
        elif digits%3 == 0: msje = thdelim + msje
        i -= 1
        pass
    msje = (msje.lstrip(thdelim).lstrip(mdelim))
    msje += (dedelim + '0')
    return msje

def printElements(tad_lst:dict,columns:tuple, ancho_celda=15)->None:
    """
    Esta función imprime todos los elementos de la lsita <tad_lst>
    con el formato de Tabulate().
    Parámetros:
        <tad_lst>: Es un TAD List no vacío
        <columns>: Es una tupla ordenada que contiene los nombres de las columnas que
        .          se quieren imprimir de las actividades contenidas en la <tad_lst> (depende del caso).
    """    
    # ---------------------------------------------------------
    # Se construye el encabezado ------------------------------
    encabezado = []
    for i in columns:
        column = (i.replace(' ', '\n')).center(5)
        encabezado.append(column)
    # ---------------------------------------------------------
    # Se construye la tabla -----------------------------------
    tabla = [encabezado]
    for element in lt.iterator(tad_lst):
        row = []
        for value in columns:
            valor = element[value]
            if controller.condicionesFormat(value):
                valor = formatNumber(valor)
            row.append(valor)
        tabla.append(row)
    # ---------------------------------------------------------
    # Se imprime la tabla -------------------------------------
    print('\n')
    print(tab(tabla,headers='firstrow', tablefmt='fancy_grid', stralign='left', numalign='left',
              maxcolwidths=[ancho_celda for _ in range(len(encabezado))]))
    pass

#------------------------------------
def depureOption(msje:str)->int:
    """
    Parámetro 'msje':
    Es el mensaje que se le quiere dar al usuario cada vez que se le pide seleccionar una opción.
    Por ej.:
        Seleccione una estructura, un algoritmo, sí o no, etc.
    Se asegura de que la opción ingresada por el usuario sea un número y luego lo retorna
    De esta manera, no se generan errores que corten el funcionamiento del programa.
    """
    print(msje)
    option = input('\n\t > ')
    while not(option.isnumeric()):
        print("\n\t(x) Error, la opción ingresada debe ser un número.\n")
        print(msje)
        option = input('\n\t > ')
    return int(option)

def depureInputs(inputs:str, control:dict, errorlimit=3)->int:
    """
    Esta función verifica 2 posibes errores:
    1) Que la opción seleccionada no sea un número
    2) Que la opción seleccionada sea diferente de 1 o 0
    .  cuando los datos no han sido cargados
    Esto se hace para evitar futuros problemas si se intenta ejecutar un 
    requerimiento sin que exista información en el catálogo.
    """
    if not(inputs.isnumeric()):
        inputs = str(depureOption('\nSeleccione una opción válida para continuar:'))
    inputs = int(inputs)
    if control is None:
        # Si el catálogo es None, significa que no se ha hecho la carga de datos.
        # En este caso, las únicas opciones válidas pueden ser:
        # >  1 (Cargar los datos)
        # >  0 (Salir de la aplicación)
        # >  3117 (función oculta para las pruebas)
        cont_errores = 0
        while (inputs != 0) and (inputs != 1) and(inputs != 3117):
            if cont_errores >= errorlimit:
                print('\n\n\tDemasiados intentos fallidos')
                inputs = 0
            else:
                print('\n\t(x) Error, la carga de datos aún no se ha realizado')
                inputs = depureOption('\nSeleccione una opción válida para continuar:')
                cont_errores +=1
            pass
    return inputs

def select_DS()->str:
    """
    DS = DataStructure
    Como su nombre lo indica, esta función solicita al usuario seleccionar 
    la estructura de datos que desea implementar para el catálogo
    return:
        El str que contiene la clave para crear la estructura
        'CHAINING' o 'PROBING'
    """
    print("\n- Seleccione la estructura que desea implementar para el catálogo:\n")
    msje = tablas('DS')
    option = depureOption(msje)
    if option == 1: DS = 'CHAINING'
    elif option == 2: DS = 'PROBING'
    else:
        print(f"\n\t(x) No existe la opción {option}, inténtelo de nuevo...\n")
        DS = select_DS() # Se hace uso de la recursividad
    return DS

def select_FS()->str:
    """
    FS = File Size
    Como su nombre lo indica, esta función solicita al usuario seleccionar 
    el tamaño del archivo que desea cargar. Para cada tamaño se cargará un archivo diferente
    return:
        El sufijo respectivo de cada archivo
    """
    print("\n- Elija el tamaño del archivo que desea cargar:\n")
    msje = tablas('FS')
    option = depureOption(msje)
    if option == 1: FS = 'small'
    elif option == 2: FS = '5pct'
    elif option == 3: FS = '10pct'
    elif option == 4: FS = '20pct'
    elif option == 5: FS = '30pct'
    elif option == 6: FS = '50pct'
    elif option == 7: FS = '80pct'
    elif option == 8: FS = 'large'
    else:
        print(f"\n\t(x) No existe la opción {option}, inténtelo de nuevo...\n")
        FS = select_FS() # Se hace uso de la recursividad
    return FS

def select_YesOrNo(msje:str)->int:
    """
    Retorna 1 o 0 (sí o no).
    """
    print(msje)
    question = tablas('y/n')
    confirm = depureOption(question)
   #--------------------------------------#
    errores = 0
    while (confirm != 1) and (confirm != 0):
        if errores >= 3:
            print("\n\t(x) Demasiados intentos fallidos.\n")
            confirm = 0
        else:
            print("\n\t(x) Error, la opción ingresada debe ser 1 o 0.\n")
            confirm = depureOption(question)
        errores += 1
        pass
   #--------------------------------------#
    return confirm

def askPrint(cont):
    confirm = select_YesOrNo('\n¿Desea imprimir los resultados para cada año cargado?')
    if confirm == 1:
        print_LoadedData(cont)
    else:
        print('\n  ✔ No se imprimieron los resultados.\n')
    pass
    
def load_data()->dict: # Ejecutar Carga de datos
    structure = select_DS()
    file_size = select_FS()
    cont = new_controller(structure)
    # Se determina si se muestra o no memoria
    memflag = (select_YesOrNo('\n¿Desea observar el uso de memoria?') == 1)

    print("\n- Cargando información de los archivos ...\n")

    results = controller.load_data(cont, file_size, memflag)
    print('\n\t✔  Los registros se cargaron exitosamente')
    print(f"\t   > Se leyeron y cargaron {results[0]} líneas de información.\n")
    
    msje = f"\t> Tiempo de carga [ms]: {results[1]:.2f}"
    if len(results) == 3: msje += f" || > Memoria utilizada [kB]: {results[2]:.2f}"
    print(msje)
    askPrint(cont)
    return cont

def load_again(cont:dict):
    print('\n\t(!) ADVERTENCIA\n\t    La carga de datos ya ha sido realizada.\n')
    confirm = select_YesOrNo('\n¿Desea volver a cargar los datos?')
    if confirm == 1:
        cont = load_data()
    else:
        print('\n  ✔  No se realizaron cambios.\n')
    return cont

def print_LoadedData(control:dict):
    start_time = controller.get_time()
    anhos = controller.getYears(control)
    for i in lt.iterator(anhos):
        actvs = controller.getActivities(control, i)
        fst, lst = controller.getFirstnLast(actvs)
        columnsR0 = controller.columns(0)
        if fst is None:
            print(f'\n> Sólo se encontraron {lt.size(actvs)} actividades para el {i}:')
            printElements(actvs, columnsR0)
            pass
        else:
            print(f'\n> Se encontraron {lt.size(actvs)} actividades para el {i}:')
            print(f'\n\t- Las primeras 3 son:')
            printElements(fst, columnsR0)
            print(f'\n\t- Las últimas 3 son:')
            printElements(lst, columnsR0)
            pass
    end_time = controller.get_time()
    time = controller.delta_time(start_time, end_time)
    print(f"\n\t> Tiempo que tomó la impresión de la carga [ms]: {time:.2f}")
    pass

# ===================================== IMPRESIÓN DE LOS REQUERIMIENTOS ======================================

def print_req_1_2(control:dict, req:int):
    monto = 'Total saldo a pagar' if req == 1 else 'Total saldo a favor'
    anho = depureOption('\nIngrese el año de interés:')
    if mp.contains(control['model'],anho):
        cod_sec = depureOption('\nIngrese el código del sector de interés:')
        secs = mp.value(control['model'], anho)
        if mp.contains(secs, cod_sec): 
            mayor_act, time = controller.req_1_2(control, anho, cod_sec, monto)
            printList = lt.newList('ARRAY_LIST')
            lt.addLast(printList, mayor_act)
            columnsR1_2 = controller.columns(1)
            print(f'\n\n> La actividad con mayor {monto.upper()} del Sector {cod_sec} para el {anho} fue:')
            printElements(printList, columnsR1_2, 20)
            print(f"\n\t> Tiempo que tomó el requerimiento [ms]: {round(time,2)}")
            pass
        else:
            print(f"\n\t(!) Aunque existe información del año {anho}, no")
            print(f"\t    se encontraron registros para el sector '{cod_sec}'\n")
            pass
    else:
        print(f"\n\t(!) No se encontraron registros para el año '{anho}'\n")
        pass
    pass

def print_req_3(control):
    anho = depureOption('\nIngrese el año de interés:')
    if mp.contains(control['model'],anho):
        # Se imprime el subsector -----------------
        sub, time = controller.req_3(control, anho)
        printList = lt.newList('ARRAY_LIST')
        lt.addLast(printList, sub)
        columnsR3 = controller.columns(3, 1)
        print(f'\n\n> El Subsector con el menor TOTAL RETENCIONES para el {anho} fue:')
        printElements(printList, columnsR3)
        # Se imprimen las actividades -----------------
        actvs = sub['Actividades']
        cod_sub = sub['Código subsector económico']
        fst, lst = controller.getFirstnLast(actvs)
        columnsR3 = controller.columns(3, 2)
        print('\n- Adicionalmente:')
        if fst is None:
            print(f'\n> Sólo se encontraron {lt.size(actvs)} actividades contribuyentes para el subsector {cod_sub} en el año {anho}:\n')
            printElements(actvs, columnsR3)
        else:
            print(f'\n> Se encontraron {lt.size(actvs)} actividades contribuyentes para el subsector {cod_sub} en el año {anho}:\n')
            print(f'\n\t- Las 3 que menos contribuyeron al TOTAL RETENCIONES fueron:')
            printElements(fst, columnsR3)
            print(f'\n\t- Las 3 que más contribuyeron al TOTAL RETENCIONES fueron:')
            printElements(lst, columnsR3)
        print(f"\n\t> Tiempo que tomó el requerimiento [ms]: {round(time,2)}")
    else:
        print(f"\n\t(!) No se encontraron registros para el año '{anho}'\n")
    pass
    
def print_req_4(control):
    anho = depureOption('\nIngrese el año de interés:')
    if mp.contains(control['model'],anho):
        # Se imprime el subsector -----------------
        sub, time = controller.req_4(control, anho)
        printList = lt.newList('ARRAY_LIST')
        lt.addLast(printList, sub)
        columnsR4 = controller.columns(4, 1)
        print(f'\n\n> El Subsector con el mayor TOTAL COSTOS Y GASTOS DE NÓMINA para el {anho} fue:')
        printElements(printList, columnsR4)
        # Se imprimen las actividades -----------------
        actvs = sub['Actividades']
        cod_sub = sub['Código subsector económico']
        fst, lst = controller.getFirstnLast(actvs)
        columnsR4 = controller.columns(4, 2)
        print('\n- Adicionalmente:')
        if fst is None:
            print(f'\n> Sólo se encontraron {lt.size(actvs)} actividades contribuyentes para el subsector {cod_sub} en el año {anho}:\n')
            printElements(actvs, columnsR4)
        else:
            print(f'\n> Se encontraron {lt.size(actvs)} actividades contribuyentes para el subsector {cod_sub} en el año {anho}:\n')
            print(f'\n\t- Las 3 que menos contribuyeron al total de COSTOS Y GASTOS DE NÓMINA fueron:')
            printElements(fst, columnsR4)
            print(f'\n\t- Las 3 que más contribuyeron al total de COSTOS Y GASTOS DE NÓMINA fueron:')
            printElements(lst, columnsR4)
        print(f"\n\t> Tiempo que tomó el requerimiento [ms]: {round(time,2)}")
    else:
        print(f"\n\t(!) No se encontraron registros para el año '{anho}'\n")
        pass
    pass

def print_req_5(control):
    anho = depureOption('\nIngrese el año de interés:')
    if mp.contains(control['model'],anho):
        # Se imprime el subsector -----------------
        sub, time = controller.req_5(control, anho)
        printList = lt.newList('ARRAY_LIST')
        lt.addLast(printList, sub)
        columnsR5 = controller.columns(5, 1)
        print(f'\n\n> El Subsector con los mayores DESCUENTOS TRIBUTARIOS para el {anho} fue:')
        printElements(printList, columnsR5)
        # Se imprimen las actividades -----------------
        actvs = sub['Actividades']
        cod_sub = sub['Código subsector económico']
        fst, lst = controller.getFirstnLast(actvs)
        columnsR5 = controller.columns(5, 2)
        print('\n- Adicionalmente:')
        if fst is None:
            print(f'\n> Sólo se encontraron {lt.size(actvs)} actividades contribuyentes para el subsector {cod_sub} en el año {anho}:\n')
            printElements(actvs, columnsR5)
        else:
            print(f'\n> Se encontraron {lt.size(actvs)} actividades contribuyentes para el subsector {cod_sub} en el año {anho}:\n')
            print(f'\n\t- Las 3 que menos contribuyeron al total de DESCUENTOS TRIBUTARIOS fueron:')
            printElements(fst, columnsR5)
            print(f'\n\t- Las 3 que más contribuyeron al total de DESCUENTOS TRIBUTARIOS fueron:')
            printElements(lst, columnsR5)
        print(f"\n\t> Tiempo que tomó el requerimiento [ms]: {round(time,2)}")
    else:
        print(f"\n\t(!) No se encontraron registros para el año '{anho}'\n")
        pass
    pass

def print_req_6(control):
    anho = depureOption('\nIngrese el año de interés:')
    if mp.contains(control['model'], anho):
        queue_return, time = controller.req_6(control, anho)
        sector = qu.dequeue(queue_return)
        sub_mas = qu.dequeue(queue_return)
        sub_menos = qu.dequeue(queue_return)
        sec_columns = ["Código sector económico", "Nombre sector económico", "Total ingresos netos del sector económico",
         "Total costos y gastos del sector económico", "Total saldo a pagar del sector económico",
         "Total saldo a favor del sector económico", "Subsector económico que más aportó", "Subsector económico que menos aportó"]
        widths = [1,15,13,13,13,13,1,1]
        print(f'\n> El sector económico que tuvo los mayores ingresos netos en el año {anho}:')
        table = table_format(sector, sec_columns)
        print_table(table,widths)
        
        columns = ["Código subsector económico", "Nombre subsector económico",
               "Total ingresos netos del subsector económico",
         "Total costos y gastos del subsector económico", "Total saldo a pagar del subsector económico",
         "Total saldo a favor del subsector económico", "Actividad que más aportó", "Actividad que menos aportó"]
        widths = [1,15,13,13,13,13,None,None]
        table_mas = table_format(sub_mas, columns)
        table_menos = table_format(sub_menos, columns)
    
        print(f'\n> El subsector económico que tuvo los mayores ingresos netos en el sector {lt.firstElement(sector)["Código sector económico"]} en el año {anho}:')
        print_table(table_mas, widths)
    
        print(f'\n> El subsector económico que tuvo los menores ingresos netos en el sector {lt.firstElement(sector)["Código sector económico"]} en el año {anho}:')
        print_table(table_menos, widths)
        
        print(f"\n\t> Tiempo que tomó el requerimiento [ms]: {round(time,2)}")
    else:
        print(f"\n\t(!) No se encontraron registros para el año '{anho}'\n")

def print_req_7(control):
    year = depureOption('\nIngrese el año de interés:')
    if mp.contains(control['model'],year):
        cod_sub=depureOption("\nIngrese el codigo del subsector de interés: ")
        top = depureOption('\nIngrese el TOP que desea:')
        if top == 0:
            print('\n\t(?) No existe el Top 0')
        else: 
            sublist, time = controller.req_7(control, year, top, cod_sub)
            tamanho = lt.size(sublist)
            if sublist is None:
                print(f"\n\t(!) No se encontraron registros para el subsector {cod_sub}\n")
            else:
                columnsR7 = controller.columns(7)
                if tamanho >= top:
                    print(f'\n> El top {top} actividades con menores COSTOS Y GASTOS del subsector {cod_sub} en el año {year}:')
                else:
                    print(f'\n> Se encontraron solo {tamanho} actividades en el subsector {cod_sub} en el año {year}. El top es:')
                printElements(sublist, columnsR7)
                print(f"\n\t> Tiempo que tomó el requerimiento [ms]: {round(time,2)}")
    else:
        print(f"\n\t(!) No se encontraron registros para el año '{year}'\n")
    pass

def print_req_8(control):
    anho = depureOption('\nIngrese el año de interés:')
    if mp.contains(control['model'],anho):
        top = depureOption('\nIngrese el TOP que desea:')
        if top == 0:
            print('\n\t(?) No existe el Top 0')
        else:
            subs_list, num, time = controller.req_8(control, anho)
            if num > 12: print(f'\n\n> Puesto que hay {num} Subsectores para el TOP {top} de actividades, sólo se mostrará la información de los primeros y últimos 3:')
            else: print(f'\n\n> Se encontraron {num} Subsectores en el TOP {top} de actividades para el {anho}:')
            columnsR8 = controller.columns(8, 1)
            printElements(subs_list, columnsR8)
            columnsR8 = controller.columns(8, 2)
            # Se imprimen las actividades de cada Subsector ----------------------------------------------
            for sub in lt.iterator(subs_list):
                cod_sub = sub['Código subsector económico']
                actvs = sub['Actividades']
                fsts, lsts = controller.getFirstnLast(actvs)
                tamanho = lt.size(actvs)
                # Menor al top ----------------------------------------------
                if tamanho < top: 
                    if (tamanho < 6): # Menor a 6
                        print(f'\n\n> Sólo se encontraron {tamanho} actividades para el subsector {cod_sub} en el año {anho}:')
                        printElements(actvs, columnsR8)
                    else: # Mayor o igual que 6
                        ms = f'\n\n> Aunque se encontraron menos actividades que el TOP solicitado ({tamanho}/{top}) para el subsector {cod_sub} en el año {anho},'
                        ms += f'\n  sólo se mostrará a infomación de las primeras y últimas 3 debido a que son más de 6:' if tamanho > 6 else '\n  se mostrarán los resultados de todas:'
                        print(ms)
                        actvs = controller.joinFirstnLast(fsts, lsts)
                        printElements(actvs, columnsR8)
                # Igual al top ----------------------------------------------
                elif tamanho == top:
                    if (tamanho <= 6): # Menor o igual a 6
                        print(f'\n\n> El TOP {top} de actividades para el subsector {cod_sub} en el año {anho} es:')
                        printElements(actvs, columnsR8)
                    else: # Mayor que 6
                        print(f'\n\n> Puesto que el TOP {top} supera la cantidad de 6 actividades para el subsector {cod_sub}\n  en el año {anho}, sólo se mostrará la información de las primeras y últimas 3:')
                        actvs = controller.joinFirstnLast(fsts, lsts)
                        printElements(actvs, columnsR8)
                # Mayor al top ----------------------------------------------
                else:
                    printList = lt.newList('ARRAY_LIST')
                    x = 0
                    flag = top if top <= 6 else 6
                    for act in lt.iterator(actvs):
                        lt.addLast(printList, act)
                        x += 1
                        if x >= flag: break
                    if top <= 6:
                        print(f'\n> El TOP {top} de actividades para el subsector {cod_sub} en el año {anho} es:')
                        printElements(printList, columnsR8)
                    else:
                        print(f'\n> Puesto que el TOP {top} supera la cantidad de 6 actividades para el subsector {cod_sub} \n')
                        print(f'  en el año {anho}, sólo se mostrará la información de las primeras y últimas 3:')
                        printElements(printList, columnsR8)
            # --------------------------------------------------------------------------------------------
            print(f"\n\t> Tiempo que tomó el requerimiento [ms]: {round(time,2)}")
    else:
        print(f"\n\t(!) No se encontraron registros para el año '{anho}'\n")
    pass
# ============================================================================================================

# ---------------------------- Formato de tablas ----------------------------
def table_format(list_rows, column_values):
    """Recibe una lista de DISClib con las filas a imprimir y
    una lista de python con las columnas que se deben imprimir   
    Retorna:
    Una lista que se puede imprimir como tabla usando print_table
    """
    table = [column_values]
    for element in lt.iterator(list_rows):
        row = []
        for value in column_values:
            valor = element[value]
            if controller.condicionesFormat(value):
                valor = formatNumber(valor)
            row.append(valor)
        table.append(row)
    #Lo que se hizo atrás fue crear una lista de listas donde cada "sublista" es una fila de la tabla
    column_values_formatted = []
    for name in column_values:
        name_changed = ""
        for i in range(len(name)):
            if name[i]==" " and " " not in name[i+1:i+4]:
                name_changed+="\n"
            else:
                name_changed += name[i]
        column_values_formatted.append(name_changed)
    #Lo que se hizo fue formatear los nombres de las columnas para que imprima bonita la tabla
    table[0] = column_values_formatted #Asignando a la primera fila los nombres de las columnas ya formateados
    return table

def print_table(table, widths):
    """Imprime una tabla a partir de una lista de listas y una lista con los grosores de las columnas para dar formato.
    """
    print(tab(table, headers='firstrow', tablefmt='fancy_grid',
                   stralign='left', numalign='left',maxcolwidths=widths))
# ---------------------------------------------------------------------------
def print_pruebas_tiempo(structure):
    # ---------------- Depuración del número para el promedio ----------------------------
    numero = depureOption('\n¿Entre cuántos valores quieres promediar el resultado?')
    intentos = 0
    while intentos < 3 and numero <= 0:
        ("\n\t(x) Error, la opción ingresada debe ser un número entero positivo\n")
        numero = depureOption('\n¿Entre cuántos valores quiere promediar el resultado?')
        if numero > 0:
            break
        intentos += 1
        if intentos == 3:
            print('\n\t(x) Demasiados intentos fallidos')
            print('\n\nSe ha establecido el número de valores como 30\n')
            numero = 30
    # ------------------------------------------------------------------------------------
    tabla_de_resultados = controller.pruebas_de_tiempo(numero, structure)
    print(f"\n\n{'TABLA DE RESULTADOS'.center(162)}\n")
    print(tab(tabla_de_resultados, headers='firstrow', tablefmt='fancy_grid',stralign='left', numalign='center'))
    pass

def print_pruebas_memoria():
    tabla_de_resultados = controller.pruebas_de_memoria()
    print(f"\n\n{'TABLA DE RESULTADOS'.center(82)}\n")
    print(tab(tabla_de_resultados, headers='firstrow', tablefmt='fancy_grid',stralign='left', numalign='center'))
    pass
    

def ejecutar_pruebas():
    print('\n\n\n')
    msje = [[f".{'SECCIÓN DE PRUEBAS DE TIEMPO Y MEMORIA'.center(95)}."]]
    print(tab(msje, tablefmt='fancy_grid'))
    print('\n\n')
    tabla = [[' 1  »  Pruebas de tiempo'], [' 2  »  Pruebas de memoria']]
    run = True
    while run:
        print('¿Qué pruebas quieres realizar?')
        print(tab(tabla, tablefmt='fancy_outline'))
        option = depureOption('\nSelecciona una opción:')
        if option == 1:
            structure = select_DS()
            print_pruebas_tiempo(structure)
        elif option == 2:
            print_pruebas_memoria()
        else:
            print('\n\t(!) No hay más opciones, intenta otra vez...')
        volver = select_YesOrNo('\n¿Deseas volver al menú de la aplicación?')
        run = (volver == 0)
        pass    
    print('\n\n')
    print(tab([[f".{'Hasta la próxima ;)'.center(95)}."]], tablefmt='fancy_grid'))
    pass


# ============================================================================================================
#
#                    ╒══════════════════════════════════════════════════════════╕
#                    │                  Ciclo de la aplicación                  │
#                    ╘══════════════════════════════════════════════════════════╛
#
#
# Centinelas globales
control = None
working = True

print('\n\n')
print('¡Bienvenido!'.center(106)) 
while working:
    printMenu()
    primeringreso = (input('\nSeleccione una opción para continuar:\n\n\t > ')).strip()
    inputs  = depureInputs(primeringreso, control)        

    if inputs == 1: 
        control = load_data() if control is None else load_again(control) # Carga ✔
    
    elif inputs == 2: print_req_1_2(control, 1) # REQ 1 (G) ✔
        
    elif inputs == 3: print_req_1_2(control, 2) # REQ 2 (G) ✔
        
    elif inputs == 4: print_req_3(control)      # REQ 3 (I) ✔
    
    elif inputs == 5: print_req_4(control)      # REQ 4 (I) ✔
    
    elif inputs == 6: print_req_5(control)      # REQ 5 (I) ✔

    elif inputs == 7: print_req_6(control)      # REQ 6 (G) ✔

    elif inputs == 8: print_req_7(control)      # REQ 7 (G) ✔
    
    elif inputs == 9: print_req_8(control)      # REQ 8 (G) ✔
        
    elif inputs == 0: working = False           # Salir de la App ✔
    
    elif inputs == 3117: ejecutar_pruebas()
    
    else: # La opción seleccionada no existe ✔
        print('\n\t(x) No existen funciones con esta numeración')
        print('\t  - Seleccione una opción válida para continuar...\n')
    pass

print('\n\n\tGracias por utilizar la aplicación.\n\n\t¡Hasta luego!\n\n')
# ============================================================================================================

sys.exit(0)

