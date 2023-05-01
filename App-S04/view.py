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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

default_limit = 1000 
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(struc_list,struc_map,load_factor):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(struc_list,struc_map,load_factor)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Actividades económicas con mayor total saldo a pagar ")
    print("3- Actividades económicas con mayor total saldo a favor")
    print("4- Subsector económico con el menor total de retenciones")
    print("5- Subsector económico con los mayores costos y gastos de nómina ")
    print("6- Subsector económico con los mayores descuentos tributarios")
    print("7- Sector económico con el mayor total de ingresos netos para un año específico")
    print("8- TOP de las actividades económicas con el menor total de costos y gastos")
    print("9- TOP de actividades económicas de cada subsector con los mayores totales de impuestos a cargo")
    print("10- Obtener dato dado un ID")
    print("0- Salir")


def load_data(control,memflag):
    """
    Carga los datos, retorna el numero de datos cargados
    """
    print('\nCuántos datos desea cargar?')
    print('1: 0.5% de los datos')
    print('2: 5% de los datos')
    print('3: 10% de los datos')
    print('4: 20% de los datos')
    print('5: 30% de los datos')
    print('6: 50% de los datos')
    print('7: 80% de los datos')
    print('8: 100% de los datos')
    resp=input()
    if resp=="1":
        archiv='small.csv'
    elif resp=="2":
        archiv='5pct.csv'
    elif resp=="3":
        archiv='10pct.csv'
    elif resp=="4":
        archiv='20pct.csv'
    elif resp=="5":
        archiv='30pct.csv'
    elif resp=="6":
        archiv='50pct.csv'
    elif resp=="7":
        archiv='80pct.csv'
    elif resp=="8":
        archiv='large.csv'
    print("Cargando información de los archivos ....\n")
    nombre_archivo="Salida_agregados_renta_juridicos_AG-"+archiv
    tuple_info_carga_datos = controller.load_data(control, nombre_archivo,memflag)       
    print('\nSeleccione el método de filtrado mediante el cual desea organizar los datos:')
    print('1: Selection sort')
    print('2: Insertion sort')
    print('3: Shell sort')
    print('4: Quick sort')
    print('5: Merge sort')
    metodo=input()
    if metodo=="1":
        time_filtrado=controller.sort(control,metodo)
    elif metodo=="2":
        time_filtrado=controller.sort(control,metodo)
    elif metodo=="3":
        time_filtrado=controller.sort(control,metodo)
    elif metodo=="4":
        time_filtrado=controller.sort(control,metodo)
    elif metodo=="5":
        time_filtrado=controller.sort(control,metodo)
    else:
        print("Se presentaran los datos sin filtrar ya que no se escogio un método de filtrado correcto")
    
    data_size=tuple_info_carga_datos[0]
    time_carga=tuple_info_carga_datos[1]
    print("Total datos cargados:",data_size)
    print("Tiempo de carga total[ms]: ",time_carga)
    if len(tuple_info_carga_datos)==3:
        memory_used=tuple_info_carga_datos[2]
        print("Total memoria usada[kB]: ",memory_used)
        
    
    

def print_tabulated_data(control):
    headers=["Año",
             "Código actividad económica",
             "Nombre actividad económica",
             "Código sector económico",
             "Nombre sector económico",
             "Código subsector económico",
             "Nombre subsector económico",
             "Total ingresos netos",
             "Total costos y gastos",
             "Total saldo a pagar",
             "Total saldo a favor"]
    table=[]
    for i in range (2012,2022):
        registros=me.getValue(mp.get(control["model"],str(i)))
        if lt.size(registros)>6:
            first=controller.get_primeros(control,str(i))
            last=controller.get_ultimos(control,str(i))
            for registro in lt.iterator(first):
                temporal_list=[]
                for header in headers:
                    temporal_list.append(registro["info"][header])
                table.append(temporal_list)
            for registro in lt.iterator(last):
                temporal_list=[]
                for header in headers:
                    temporal_list.append(registro["info"][header])
                table.append(temporal_list)
        else:
            for registro in lt.iterator(registros):
                temporal_list=[]
                for header in headers:
                    temporal_list.append(registro["info"][header])
                table.append(temporal_list)
            
    print(tabulate(table,headers,tablefmt="grid",maxcolwidths=8))
          
def tabulate_data(control):
    print_tabulated_data(control)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)

def print_req_1(control,anio,sector,memflag):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    #Obtener informacion relacionada a la actividad con mayor saldo a pagar de dicho año y  sector
    tuple_info=controller.req_1(control,anio,sector,memflag)
    actividad=tuple_info[0]
    #Obtener informacion relacionada a los tiempos de ejecucion y memoria ocupada
    time=tuple_info[1]
    if len(tuple_info)==3:
        memory=tuple_info[2]
    #Alistar los datos necesarios para tabular
    headers=["Código actividad económica",
             "Nombre actividad económica",
             "Código subsector económico",
             "Nombre subsector económico",
             "Total ingresos netos",
             "Total costos y gastos",
             "Total saldo a pagar",
             "Total saldo a favor"]
    table=[]
    for header in headers:
        table.append(actividad["info"][header])
    #Se ajusta el formato de la tabla puesto a que solo es un valor, es decir hay una relacion 1-1 header-valor
    list2tabulate=[headers,table]
    #Imprimir el resultado con respecto al requerimiento
    print("============== Req No. 1 Inputs ==============")
    print("Find the economic activity with the highest balance due(Total saldo a pagar) for the year'"+str(anio)+"' and economic sector code '"+str(sector)+"'.")
    print("============== Req No. 1 Answer ==============")
    print(tabulate(list2tabulate,tablefmt="grid",maxcolwidths=13))
    #Imprimir la informacion relacionada a tiempo de ejecución y memoria
    print("Tiempo de ejecución total[ms]: ",time)
    if len(tuple_info)==3:
        memory=tuple_info[2]
        print("Total memoria usada[kB]: ",memory)
    
def print_req_2(control,anio,sector,memflag):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    #Obtener informacion relacionada a la actividad con mayor saldo a pagar de dicho año y  sector
    tuple_info=controller.req_2(control,anio,sector,memflag)
    actividad=tuple_info[0]
    #Obtener informacion relacionada a los tiempos de ejecucion y memoria ocupada
    time=tuple_info[1]
    if len(tuple_info)==3:
        memory=tuple_info[2]
    #Alistar los datos necesarios para tabular
    headers=["Código actividad económica",
             "Nombre actividad económica",
             "Código subsector económico",
             "Nombre subsector económico",
             "Total ingresos netos",
             "Total costos y gastos",
             "Total saldo a pagar",
             "Total saldo a favor"]
    table=[]
    for header in headers:
        table.append(actividad["info"][header])
    #Se ajusta el formato de la tabla puesto a que solo es un valor, es decir hay una relacion 1-1 header-valor
    list2tabulate=[headers,table]
    #Imprimir el resultado con respecto al requerimiento
    print("============== Req No. 2 Inputs ==============")
    print("Find the economic activity with the highest balance due(Total saldo a pagar) for the year'"+str(anio)+"' and economic sector code '"+str(sector)+"'.")
    print("============== Req No. 2 Answer ==============")
    print(tabulate(list2tabulate,tablefmt="grid",maxcolwidths=22))
    #Imprimir la informacion relacionada a tiempo de ejecución y memoria
    print("Tiempo de ejecución total[ms]: ",time)
    if len(tuple_info)==3:
        memory=tuple_info[2]
        print("Total memoria usada[kB]: ",memory)


def print_req_3(control,anio,memflag):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    #Obtener información a imprimir del subsector y actividades correspondientes
    subsector=controller.req_3(control,anio,memflag)[0]
    actividades= controller.req_3(control,anio,memflag)[1]
    #Obtener información de tiempo y memoria
    time=controller.req_3(control,anio,memflag)[2]
    
    #Encabezados para imprimir el subsector
    headers_subsector=["Código sector económico", 
             "Nombre sector económico",
             "Código subsector económico",
             "Nombre subsector económico",
             "Total de retenciones del subsector económico",
             "Total ingresos netos del subsector económico",
             "Total costos y gastos del subsector económico",
             "Total saldo a pagar del subsector económico",
             "Total saldo a favor del subsector económico"]
    
    #Lista para agregar información de los subsectores
    table_subsector=[]
    #Añadir la información correspondiente a cada encabezado
    for header in headers_subsector:
         table_subsector.append((me.getValue(mp.get(subsector,header))))
    list_subsector=[headers_subsector,table_subsector] 
    #Imprimir información susbsector
    print("=============== Req. No. 3 Answer ============== ")    
    print(f"Economic sub-sectors with the lowest total withholdings (total retenciones) in {anio}")         
    print(tabulate(list_subsector,tablefmt="grid",maxcolwidths=22))

    #Encabezados para imprimir las actividades
    headers_actividades=["Código actividad económica",
             "Nombre actividad económica",
             "Total retenciones",
             "Total ingresos netos",
             "Total costos y gastos",
             "Total saldo a pagar",
             "Total saldo a favor"]
    table_actividades=[]
    #Información para cada una de las actividades
    for actividad in lt.iterator(actividades): 
        info_actividad=[]
        for header in headers_actividades:
            info_actividad.append(actividad["info"][header])
        table_actividades.append(info_actividad)
    
    #Imprimir las actividades para el subsector correspondiente
    print("\n------------Contributions from economic activities-------- ")
    if lt.size(actividades)<6:
        print(f'There are only {lt.size(actividades)} economic activities in {table_subsector[2]} subsector')
    else:
        print(f'Economic activities in {table_subsector[2]} subsector')
    print(tabulate(table_actividades,headers_actividades,tablefmt="grid",maxcolwidths=22))   

    #Imprimir tiempo y memoria
    print("Tiempo de ejecución total[ms]: ",time)
    if len(controller.req_3(control,anio,memflag))==4:
        memory=controller.req_3(control,anio,memflag)[3]
        print("Total memoria usada[kB]: ",memory) 
    

def print_req_4(control,anio,memflag):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    #Obtener información a imprimir del subsector y actividades correspondientes
    subsector=controller.req_4(control,anio,memflag)[0]
    actividades= controller.req_4(control,anio,memflag)[1]
    #Obtener información de tiempo y memoria
    time=controller.req_4(control,anio,memflag)[2]
    
    #Encabezados para imprimir el subsector
    headers_subsector=["Código sector económico", 
             "Nombre sector económico",
             "Código subsector económico",
             "Nombre subsector económico",
             "Total de costos y gastos de nomina del subsector económico",
             "Total ingresos netos del subsector económico",
             "Total costos y gastos del subsector económico",
             "Total saldo a pagar del subsector económico",
             "Total saldo a favor del subsector económico"]
    
    #Lista para agregar información de los subsectores
    table_subsector=[]
    #Añadir la información correspondiente a cada encabezado
    for header in headers_subsector:
         table_subsector.append((me.getValue(mp.get(subsector,header))))
    list_subsector=[headers_subsector,table_subsector] 
    #Imprimir información susbsector
    print("=============== Req. No. 4 Answer ============== ")    
    print(f"Economic sub-sectors with the lowest total withholdings (total retenciones) in {anio}")         
    print(tabulate(list_subsector,tablefmt="grid",maxcolwidths=10))

    #Encabezados para imprimir las actividades
    headers_actividades=["Código actividad económica",
             "Nombre actividad económica",
             "Total costos y gastos",
             "Total ingresos netos",
             "Total costos y gastos",
             "Total saldo a pagar",
             "Total saldo a favor"]
    table_actividades=[]
    #Información para cada una de las actividades
    for actividad in lt.iterator(actividades): 
        info_actividad=[]
        for header in headers_actividades:
            info_actividad.append(actividad["info"][header])
        table_actividades.append(info_actividad)
    
    #Imprimir las actividades para el subsector correspondiente
    print("\n------------Contributions from economic activities-------- ")
    if lt.size(actividades)<6:
        print(f'There are only {lt.size(actividades)} economic activities in {table_subsector[2]} subsector')
    else:
        print(f'Economic activities in {table_subsector[2]} subsector')
    print(tabulate(table_actividades,headers_actividades,tablefmt="grid",maxcolwidths=22))   

    #Imprimir tiempo y memoria
    print("Tiempo de ejecución total[ms]: ",time)
    if len(controller.req_4(control,anio,memflag))==4:
        memory=controller.req_4(control,anio,memflag)[3]
        print("Total memoria usada[kB]: ",memory) 


def print_req_5(control,anio,memflag):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    #Obtener informacion relacionada a la actividad con mayor saldo a pagar de dicho año y  sector
    tuple_info=controller.req_5(control,anio,memflag)
    subsector=tuple_info[0]
    actividades=tuple_info[1]
    #Obtener informacion relacionada a los tiempos de ejecucion y memoria ocupada
    time=tuple_info[2]
    if len(tuple_info)==4:
        memory=tuple_info[3]
    #Alistar los datos necesarios para tabular de la tabla 1
    headers_table_1=["Código sector económico", 
             "Nombre sector económico",
             "Código subsector económico",
             "Nombre subsector económico",
             "Total de descuentos tributarios del subsector económico",
             "Total ingresos netos del subsector económico",
             "Total costos y gastos del subsector económico",
             "Total saldo a pagar del subsector económico",
             "Total saldo a favor del subsector económico"]
    table_1=[]
    for header in headers_table_1:
        table_1.append(me.getValue(mp.get(subsector,header)))
    #Alistar los datos necesarios para tabular de la tabla 2
    headers_table_2=["Código actividad económica",
             "Nombre actividad económica",
             "Descuentos tributarios",
             "Total ingresos netos",
             "Total costos y gastos",
             "Total saldo a pagar",
             "Total saldo a favor"] 
    #Se ajusta el formato de la tabla puesto a que solo es un valor, es decir hay una relacion 1-1 header-valor
    list2tabulate_1=[headers_table_1,table_1]
    #Imprimir el resultado con respecto al requerimiento del subsector
    print("============== Req No. 5 Answer ==============")
    print(f"Economic sub-sectors with the highest total withholdings(Descuentos Tributarios) in '{anio}'")
    print(tabulate(list2tabulate_1,tablefmt="grid",maxcolwidths=13))
    print("\n------------Contributions from economic activities-------- ") 
    #Se verifica si hay mas de 6 actividades
    if lt.size(actividades)>6:
        print(f"The three economic activities that contributed the least and the three that contributed the most in '{me.getValue(mp.get(subsector,'Código subsector económico'))}' economic subsector")
        table_2=[]
        for i in range(1,4):
            #Se crea una lista temporal para cada registro
            temporal=[]
            #Se accede a la posición de la lista i
            element=lt.getElement(actividades,i)
            for header in headers_table_2:
                temporal.append(element["info"][header])
            table_2.append(temporal)
        for j in range(0,3):
            #Se crea una lista temporal para cada registro
            temporal=[]
            pos=len(table_2)-j
            #Se accede a la posición de la lista -i
            element=lt.getElement(actividades,lt.size(actividades)-j)
            for header in headers_table_2:
                temporal.append(element["info"][header])
            table_2.insert(pos,temporal)
        print(tabulate(table_2,headers_table_2,tablefmt="grid",maxcolwidths=13))
    else:
        print(f"The  economic activities  in '{me.getValue(mp.get(subsector,'Código subsector económico'))}' economic subsector")
        table_3=[]
        for k in range(1,lt.size(actividades)+1):
            #Se crea una lista temporal para cada registro
            temporal=[]
            #Se accede a la posición de la lista k
            element=lt.getElement(actividades,k)
            for header in headers_table_2:
                temporal.append(element["info"][header])
            table_3.append(temporal)
        print(tabulate(table_3,headers_table_2,tablefmt="grid",maxcolwidths=13))
    
    print("Tiempo de ejecución total[ms]: ",time)
    if len(tuple_info)==4:
        memory=tuple_info[3]
        print("Total memoria usada[kB]: ",memory)
            

def small_table(actividad):
        indices=["Código actividad económica",
                 "Nombre actividad económica",
                 "Total ingresos netos",
                 "Total costos y gastos",
                 "Total saldo a pagar",
                 "Total saldo a favor"]
        list_a_tabular=[]
        for indice in indices:
            list_a_tabular.append([indice,actividad["info"][indice]])
        tabla=tabulate(list_a_tabular,tablefmt="grid",maxcolwidths=20)
        return tabla
    
def print_req_6(control,anio,memflag):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    #Obtener informacion relacionada al sector con mayor ingreso neto
    tuple_info=controller.req_6(control,anio,memflag)
    sector=tuple_info[0]
    subsector_most=tuple_info[1]
    subsector_less=tuple_info[2]
    actividad_mas_aporto_1=tuple_info[3]
    actividad_menos_aporto_1=tuple_info[4]
    actividad_mas_aporto_2=tuple_info[5]
    actividad_menos_aporto_2=tuple_info[6]
    time=tuple_info[7]
    if len(tuple_info)==9:
        memory=tuple_info[8]
    #Alistar los datos necesarios para tabular de la tabla 1
    headers_table_1=["Código sector económico", 
             "Nombre sector económico",
             "Total ingresos netos del sector económico",
             "Total costos y gastos del sector económico",
             "Total saldo a pagar del sector económico",
             "Total saldo a favor del sector económico",
             "Subsector económico que más aporto",
             "Subsector económico que menos aporto"]
    table_1=[]
    for header in headers_table_1:
        table_1.append(me.getValue(mp.get(sector,header)))
    #Se ajusta el formato de la tabla puesto a que solo es un valor, es decir hay una relacion 1-1 header-valor
    list2tabulate_1=[headers_table_1,table_1]
    #Imprimir el resultado con respecto al requerimiento
    print("============== Req No. 5 Inputs ==============")
    print(f"Find the economic activity with the highest total net income for each economic sector in '{anio}'")
    print("============== Req No. 1 Answer ==============")
    print(tabulate(list2tabulate_1,tablefmt="grid",maxcolwidths=20))
    #Alistar los datos necesarios para tabular de la tabla 2 y 3
    headers_table_2_and_3=["Código subsector económico", 
             "Nombre subsector económico",
             "Total ingresos netos del subsector económico",
             "Total costos y gastos del subsector económico",
             "Total saldo a pagar del subsector económico",
             "Total saldo a favor del subsector económico",
             "Actividad económica que más aporto",
             "Actividad económica que menos aporto"]
    table_2=[]
    #Se recorren los headers de la tabla 2 y tres omitiendo 
    #las actividades económicas
    for i in range(0,6):
        header=headers_table_2_and_3[i]
        table_2.append(me.getValue(mp.get(subsector_most,header)))
    #Se crean las tablas internas
    table_mas_aporto_1=small_table(actividad_mas_aporto_1)
    table_menos_aporto_1=small_table(actividad_menos_aporto_1)
    #Se añaden las tablas internas
    table_2.append(table_mas_aporto_1)
    table_2.append(table_menos_aporto_1)
    #Se ajusta el formato de la tabla puesto a que solo es un valor, es decir hay una relacion 1-1 header-valor
    list2tabulate_2=[headers_table_2_and_3,table_2]
    #Imprimir el resultado con respecto al requerimiento de subsector mas contributivo
    print("============== Economic subsector that contributed the most ==============")
    print(tabulate(list2tabulate_2,tablefmt="grid"))
    #Se alistan los datos 
    table_3=[]
    #Se recorren los headers de la tabla 2 y 3 omitiendo 
    #las actividades económicas
    for i in range(0,6):
        header=headers_table_2_and_3[i]
        table_3.append(me.getValue(mp.get(subsector_less,header)))
    #Se crean las tablas internas
    table_mas_aporto_2=small_table(actividad_mas_aporto_2)
    table_menos_aporto_2=small_table(actividad_menos_aporto_2)
    #Se añaden las tablas internas
    table_3.append(table_mas_aporto_2)
    table_3.append(table_menos_aporto_2)
    #Se ajusta el formato de la tabla puesto a que solo es un valor, es decir hay una relacion 1-1 header-valor
    list2tabulate_3=[headers_table_2_and_3,table_3]
    #Imprimir el resultado con respecto al requerimiento de subsector mas contributivo
    print("============== Economic subsector that contributed the less ==============")
    print(tabulate(list2tabulate_3,tablefmt="grid"))
    print("Tiempo de ejecución total[ms]: ",time)
    if len(tuple_info)==9:
        memory=tuple_info[8]
        print("Total memoria usada[kB]: ",memory)
    
def print_req_7(control,anio,subsector,n,memflag):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    #Obtener informacion relacionada a las actividades
    tuple_info=controller.req_7(control,anio,subsector,n,memflag)
    list_actividades=tuple_info[0]
    time=tuple_info[1]
    if len(tuple_info)==3:
        memory=tuple_info[2]
    #Alistar los datos necesarios para tabular
    headers=["Código actividad económica",
             "Nombre actividad económica",
             "Código sector económico",
             "Nombre sector económico",
             "Total ingresos netos",
             "Total costos y gastos",
             "Total saldo a pagar",
             "Total saldo a favor"]
    table=[]
    for actividad in lt.iterator(list_actividades):
        temporal=[]
        for header in headers:
            temporal.append(actividad["info"][header])
        table.append(temporal)
    print("========== Req No.7 Inputs ===============")
    print(f"Find the top '{n}' economic activities with the lowest total costs and expenses in '{anio}' and in subsector '{subsector}'")
    print("========== Req No.7 Answer ===============")
    if lt.size(list_actividades)>=int(n):
        print(f"The top '{n}' economic activities in subsector '{subsector}' and in year '{anio}' are:")
    else:
        print(f"There are only {lt.size(list_actividades)} economic activities in '{subsector}' subsector and in the year '{anio}'")
    print(tabulate(table,headers,tablefmt="grid",maxcolwidths=30))
    #Imprimir la informacion relacionada a tiempo de ejecución y memoria
    print("Tiempo de ejecución total[ms]: ",time)
    if len(tuple_info)==3:
        memory=tuple_info[2]
        print("Total memoria usada[kB]: ",memory)
    


def print_req_8(control,anio,top,memflag):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    #Obtener información a imprimir del subsector y actividades correspondientes
    subsectores=controller.req_8(control,anio,top,memflag)[0]
    actividades=controller.req_8(control,anio,top,memflag)[1]
    #Obtener información de tiempo y memoria
    time=controller.req_3(control,anio,memflag)[2]
    
    #Encabezados para imprimir el subsector
    headers_subsector=["Código sector económico", 
             "Nombre sector económico",
             "Código subsector económico",
             "Nombre subsector económico",
             "Total de impuestos a cargo para el subsector económico",
             "Total ingresos netos del subsector económico",
             "Total costos y gastos del subsector económico",
             "Total saldo a pagar del subsector económico",
             "Total saldo a favor del subsector económico"]
    #Lista para agregar información de los subsectores
    table_subsectors=[]
    #Añadir la información correspondiente a cada encabezado
    for subsector in lt.iterator(subsectores):
        info_subsector=[]
        for header in headers_subsector:
            info_subsector.append((me.getValue(mp.get(subsector,header))))
        table_subsectors.append(info_subsector)
    #Imprimir información susbsector
    print("=============== Req. No. 8 Inputs ============== ")  
    print(f"Find the top {top} economic activities of each-subsector with the highest total taxes payable in {anio}")   
    print("\n=============== Req. No. 8 Answer ============== ")
    print(tabulate(table_subsectors,headers_subsector,tablefmt="grid",maxcolwidths=22))

    #Encabezados para imprimir las actividades
    headers_actividades=["Código actividad económica",
             "Nombre actividad económica",
             "Total Impuesto a cargo",
             "Total ingresos netos",
             "Total costos y gastos",
             "Total saldo a pagar",
             "Total saldo a favor"]

    for subsector in lt.iterator(mp.keySet(actividades)):
        tamanio=lt.size(me.getValue(mp.get(actividades,subsector)))
        table_actividades=[]
        for act in lt.iterator(me.getValue(mp.get(actividades,subsector))):
            info_actividad=[]
            for header in headers_actividades:
                info_actividad.append(act["info"][header])
            table_actividades.append(info_actividad)
        if int(top) > tamanio:
            print(f"=============== There is only {tamanio} activities in {subsector}===============")
            print(tabulate(table_actividades,headers_actividades,tablefmt="grid",maxcolwidths=22)) 
        else:
            print(f"=============== Top {top} activities in {subsector}===============")
            print(tabulate(table_actividades,headers_actividades,tablefmt="grid",maxcolwidths=22)) 

    #Imprimir tiempo y memoria
    print("Tiempo de ejecución total[ms]: ",time)
    if len(controller.req_8(control,anio,top,memflag))==4:
        memory=controller.req_8(control,anio,top,memflag)[3]
        print("Total memoria usada[kB]: ",memory) 
    
    

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False



# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    control=None
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                label_list = input("\nDigita 1 para cargar en ARRAY_LIST o 2 para SINGLED_LISTED los tados de un mismo año: ")
                label_map = input("\nDigita 1 para cargar en CHAINING o 2 para PROBING el mapa de los años: ")
                if label_list in ["1","2"]:
                    if label_list in ["1","2"]:
                        if label_list =='1':
                            struc_list='ARRAY_LIST'
                        elif label_list =='2':
                            struc_list='SINGLE_LINKED'
                        if label_map =='1':
                            struc_map="CHAINING"
                        elif label_map =='2':
                            struc_map='PROBING'
                        load_factor=float(input("Seleccione el factor de carga que desea utilizar: "))
                        control=new_controller(struc_list,struc_map,load_factor)
                        memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                        load_data(control, memflag)
                        tabulate_data(control)
                    else:
                        print("Ingrese una opcion válida")
                else:
                    print("Ingrese una opcion válida")
                    
            elif int(inputs) == 2:
                anio=input("Ingrese el año de interés:")
                sector=input("Ingrese el sector económico de interés: ")
                memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                print_req_1(control,anio,sector,memflag)

            elif int(inputs) == 3:
                anio=input("Ingrese el año de interés:")
                sector=input("Ingrese el sector económico de interés: ")
                memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                print_req_2(control,anio,sector,memflag)

            elif int(inputs) == 4:
                anio=input("Ingrese el año de interés:")
                memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                print_req_3(control,anio,memflag)
                

            elif int(inputs) == 5:
                anio=input("Ingrese el año de interés:")
                memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                print_req_4(control,anio,memflag)

            elif int(inputs) == 6:
                anio=input("Ingrese el año de interés:")
                memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                print_req_5(control,anio,memflag)

            elif int(inputs) == 7:
                anio=input("Ingrese el año de interés:")
                memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                print_req_6(control,anio,memflag)

            elif int(inputs) == 8:
                anio=input("Ingrese el año de interés:")
                subsector=input("Ingrese el subsector de interés:")
                n=input("Ingrese el N del top N que desea consultar:")
                memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                print_req_7(control,anio,subsector,n,memflag)

            elif int(inputs) == 9:
                anio=input("Ingrese el año de interés:")
                top=input("Ingrese el número de actividades que desea visualizar:")
                memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                print_req_8(control,anio,top,memflag)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
