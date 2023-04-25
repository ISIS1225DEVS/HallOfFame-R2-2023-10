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
import pandas as pd
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

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control , memoria, tamanio):
    """
    Carga los datos
    """
    data = controller.mega_load(control , memoria, tamanio)
    return data

def get_value(hash,key):
    return controller.get_value(hash,key)

def diccionario_tabulable(lista,filtros):
    
    new_dic = {}
    
    for dato in lt.iterator(lista):
        
        for llave in dato:
            if llave in filtros:
    
                if new_dic.get(llave,"no") == "no":
                    new_dic[llave] = [dato[llave]]
                else:
                    new_dic[llave].append(dato[llave])
    
    return new_dic
    
    
def lista_primeros_y_utlimos_3(lista):
        
    size = lt.size(lista)
    new_data = lt.newList("ARRAY_LIST")
     
    if size > 6:
        #primeros ordenados
        i = 1
        while i <= 3:
            elemento = lt.getElement(lista,i)
            lt.addLast(new_data, elemento)
            i += 1
        
        #ultimos ordenados 
        i = size - 2
        while i <= size:
            elemento = lt.getElement(lista, i)
            lt.addLast(new_data,elemento)
            i += 1
    else:
        new_data = lista
    
    return new_data


def print_carga_de_datos(answer):
    """
        Función que imprime la carga de datos
    """
    filtros = ["Año", "Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", 
               "Código subsector económico", "Nombre subsector económico","Total ingresos netos", "Total costos y gastos", 
               "Total saldo a pagar", "Total saldo a favor"]
    
    print("============================================")
    print(f"Se cargaron exitosamente: {answer[1]} datos")
    print("============================================\n")
    for year in range(2012,2022):

        lista_year_info = get_value(get_value(answer[0]["data"],str(year)),"info")
        lista = lista_primeros_y_utlimos_3(lista_year_info)
        dic_tabulable = diccionario_tabulable(lista,filtros)
        
        size = len(dic_tabulable["Año"])
        if size < 6:
            print(f"There are only {size} economic activities in {year}")
        else:
            print(f"The first three and last three economic activities in {year} are")
            
        print(tabulate(dic_tabulable, headers = "keys", tablefmt="grid", maxcolwidths=12, maxheadercolwidths=12,floatfmt=".0f"))
        print("\n\n")
        
        
    pass

def mini_diccionario_tabulable(answer,filtros):
    
    new_dic = {}
    for llave in answer:
        if llave in filtros:
            new_dic[llave] = [answer[llave]]
            
    return new_dic

def lista_tabulable_para_6(answer,filtros):
    new_list = []
    for llave in answer:
        if llave in filtros:
            new_list.append([llave,answer[llave]])

    return new_list

def print_req_1_y_2(answer,num,message):
    """ 
    Función que imprime el dataframe del requerimiento 1 y 2
    """
    
    filtros = ["Código actividad económica", "Nombre actividad económica", "Código subsector económico", "Nombre subsector económico",
               "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    
    new_dic = mini_diccionario_tabulable(answer,filtros)
            
    print(f"=============== REQ No.{num} Inptus ===============")
    print(message + "\n")
    print(f"=============== REQ No.{num} Answer ===============")
    print(tabulate(new_dic, headers="keys", tablefmt="grid", maxcolwidths=15, maxheadercolwidths=15,floatfmt=".0f"))
    
    pass
    
def print_req_1(control,anio,sector,memory):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    req_1 = controller.req_1(control,anio,sector,memory)
    message = f"Find the economic activity with the highest balance due (Total saldo a pagar) for the year {anio} and economic sector code {sector} "
    print_req_1_y_2(req_1[0],1,message)
    printTiempoMemoria(req_1)
    pass


def print_req_2(control,anio,sector,memory):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    req_2 = controller.req_2(control,anio,sector,memory)
    message = f"Find the economic activity with the highest balance in favor (Total saldo a favor) for the year {anio} and economic sector code {sector} "
    print_req_1_y_2(req_2[0],2,message)
    printTiempoMemoria(req_2)
    pass

def print_req_3_4_y_5(dic1,dic2, num , message1, message2,head):
    
    print(f"=============== REQ No.{num} Answer =============== \n")
    print(message1 + "\n")
    print(tabulate(dic1, headers = head, tablefmt="grid", maxcolwidths=13, maxheadercolwidths=13,floatfmt=".0f"))
    print("\n")
    print(f"------- Contribution from economic activities ------- \n")
    print(message2 + "\n")
    print(tabulate(dic2 ,headers = "keys", tablefmt="grid", maxcolwidths=13, maxheadercolwidths=13,floatfmt=".0f"))
    pass

def print_req_3(control,anio,memory):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    req_3 = controller.req_3(control,anio,memory)
    
    filtro1 = ["Código sector económico", "Nombre sector económico", "Código subsector económico",
               "Nombre subsector económico", "Total retenciones", "Total ingresos netos", "Total costos y gastos",
               "Total saldo a pagar", "Total saldo a favor"]
    
    filtro2 = ["Código actividad económica", "Nombre actividad económica", "Total retenciones", "Total ingresos netos", "Total costos y gastos",
                      "Total saldo a pagar", "Total saldo a favor"]
    
    header = ["Código sector económico", "Nombre sector económico", "Código subsector económico",
               "Nombre subsector económico", "Total retenciones del subsector económico", "Total ingresos netos del subsector económico", "Total costos y gastos del subsector económico",
               "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"]
    
    first_dic = mini_diccionario_tabulable(req_3[0][0], filtro1)
    first_dic_ordered = {}
    second_dic_ordered = {}
    second_dic = diccionario_tabulable(lista_primeros_y_utlimos_3(req_3[0][1]),filtro2)
    
    for llave in filtro1:
        first_dic_ordered[llave] = first_dic[llave]
    
    for llave in filtro2:
        second_dic_ordered[llave] = second_dic[llave]
        
    message1 = f"Economic sub-sectors with the lowest total withholdings (Total retenciones) in {anio}"
    size = lt.size(req_3[0][1])
    subsector = req_3[0][0]["Código subsector económico"]
    message2 = f"There are only {size} economic activities in the economic subsector {subsector}"
    
    print_req_3_4_y_5(first_dic_ordered,second_dic_ordered,3,message1,message2,header)
    printTiempoMemoria(req_3)
    pass


def print_req_4(control,anio,memory):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    req_4 = controller.req_4(control,anio,memory)
    
    filtro1 = ["Código sector económico", "Nombre sector económico", "Código subsector económico",
               "Nombre subsector económico", "Costos y gastos nómina", "Total ingresos netos", "Total costos y gastos",
               "Total saldo a pagar", "Total saldo a favor"]
    
    filtro2 = ["Código actividad económica", "Nombre actividad económica", "Costos y gastos nómina", "Total ingresos netos", "Total costos y gastos",
                      "Total saldo a pagar", "Total saldo a favor"]
    
    header = ["Código sector económico", "Nombre sector económico", "Código subsector económico",
               "Nombre subsector económico", "Total de costos y gastos nómina del subsector económico", "Total ingresos netos del subsector económico", "Total costos y gastos del subsector económico",
               "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"]
    
    first_dic = mini_diccionario_tabulable(req_4[0][0], filtro1)
    first_dic_ordered = {}
    second_dic_ordered = {}
    second_dic = diccionario_tabulable(lista_primeros_y_utlimos_3(req_4[0][1]),filtro2)
    
    for llave in filtro1:
        first_dic_ordered[llave] = first_dic[llave]
    
    for llave in filtro2:
        second_dic_ordered[llave] = second_dic[llave]
        
    message1 = f"Economic sub-sectors with the highest total withholdings (Costos y gastos nómina) in {anio}"
    size = lt.size(req_4[0][1])
    subsector = req_4[0][0]["Código subsector económico"]
    message2 = f"There are only {size} economic activities in the economic subsector {subsector}"
    
    print_req_3_4_y_5(first_dic_ordered,second_dic_ordered,4,message1,message2,header)
    printTiempoMemoria(req_4)

    pass


def print_req_5(control,anio,memoria):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    req_5 = controller.req_5(control,anio,memoria)
    
    filtro1 = ["Código sector económico", "Nombre sector económico", "Código subsector económico",
               "Nombre subsector económico", "Descuentos tributarios", "Total ingresos netos", "Total costos y gastos",
               "Total saldo a pagar", "Total saldo a favor"]
    
    filtro2 = ["Código actividad económica", "Nombre actividad económica", "Descuentos tributarios", "Total ingresos netos", "Total costos y gastos",
                      "Total saldo a pagar", "Total saldo a favor"]
    
    header = ["Código sector económico", "Nombre sector económico", "Código subsector económico",
               "Nombre subsector económico", "Total de descuentos tributarios del subsector económico", "Total ingresos netos del subsector económico", "Total costos y gastos del subsector económico",
               "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"]
    
    first_dic = mini_diccionario_tabulable(req_5[0][0], filtro1)
    first_dic_ordered = {}
    second_dic_ordered = {}
    second_dic = diccionario_tabulable(lista_primeros_y_utlimos_3(req_5[0][1]),filtro2)
    
    for llave in filtro1:
        first_dic_ordered[llave] = first_dic[llave]
    
    for llave in filtro2:
        second_dic_ordered[llave] = second_dic[llave]
        
    message1 = f"Economic sub-sectors with the highest tax discounts (Descuentos Tributarios) in {anio}"
    size = lt.size(req_5[0][1])
    subsector = req_5[0][0]["Código subsector económico"]
    message2 = f"There are only {size} economic activities in the economic subsector {subsector}"
    
    print_req_3_4_y_5(first_dic_ordered,second_dic_ordered,3,message1,message2,header)
    printTiempoMemoria(req_5)
    
    pass

def wrapping_time(nombre):
    
    lista = list(nombre)
    i = 0
    for letra in lista:
        if i%15 == 0:
            lista.insert(i,"\n")
        i += 1
        
    mensaje = ""
    for data in lista:
        mensaje += data
    
    return mensaje
            
    
def corregir_diccionario(diccionario):
    
    filtros = ["Código actividad económica", "Nombre actividad económica", "Total ingresos netos", "Total costos y gastos", 
               "Total saldo a pagar", "Total saldo a favor"]
    
    dic_1 = lista_tabulable_para_6(diccionario["Actividad económica que más aportó"],filtros)
    dic_2 = lista_tabulable_para_6(diccionario["Actividad económica que menos aportó"],filtros)
    
    new_dic = {}
    
    for llave in diccionario:
        if llave == "Nombre subsector económico":
            new_dic[llave] = wrapping_time(diccionario[llave])
        elif llave == "Actividad económica que más aportó":
            new_dic[llave] = tabulate(dic_1,tablefmt="grid",maxcolwidths=18, maxheadercolwidths=18,floatfmt=".0f")
        elif llave == "Actividad económica que menos aportó":
            new_dic[llave] =  tabulate(dic_2,tablefmt="grid",maxcolwidths=18, maxheadercolwidths=18,floatfmt=".0f")
        else:
            new_dic[llave] = diccionario[llave]
    
    return new_dic

def print_req_6(control,anio,memoria):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    req_6 = controller.req_6(control,anio,memoria)
    answer = req_6[0]
    
    filtro1 = ["Código sector económico", "Nombre sector económico", "Total ingresos netos", "Total costos y gastos",
               "Total saldo a pagar", "Total saldo a favor"]
    
    filtro2 = ["Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor",
               "Actividad económica que más aportó", "Actividad económica que menos aportó"]
    
    head1 = ["Código sector económico", "Nombre sector económico", "Total ingresos netos del sector económico", "Total costos y gastos del sector económico",
               "Total saldo a pagar del sector económico", "Total saldo a favor del sector económico", "Subsector económico que más aportó", "Subsector económico que menos aportó"]
    
    head2 = ["Código subsector económico", "Nombre subsector económico", "Total ingresos netos del subsector económico", "Total costos y gastos del subsector económico", 
             "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico" ,"Actividad económica que más aportó", 
             "Actividad económica que menos aportó"]
    
    primer_diccionario = mini_diccionario_tabulable(answer[0],filtro1)
    primer_diccionario["Subsector económico que más aportó"] = [answer[1]["Código subsector económico"]]
    primer_diccionario["Subsector económico que menos aportó"] = [answer[2]["Código subsector económico"]]
    
    dic1 = corregir_diccionario(answer[1])
    dic2 = corregir_diccionario(answer[2])
    
    segundo_diccionario = mini_diccionario_tabulable(dic1,filtro2)
    tercer_diccionario = mini_diccionario_tabulable(dic2,filtro2)
        
    print("================== Req No.6 Inputs ==================")
    print(f"Find the economic activity with the highest total net income for each economic sector in {anio} \n")
    print("================== Req No.6 Answer ==================")
    
    print(tabulate(primer_diccionario,headers = head1,tablefmt="grid",maxcolwidths=15, maxheadercolwidths=15, floatfmt=".0f"))
    print("================== Economic subsector that contributed the most ==================")
    print(tabulate(segundo_diccionario,headers=head2,tablefmt="grid",maxheadercolwidths=12, floatfmt=".0f"))
    print("================== Economic subsector that contributed the least ==================")
    print(tabulate(tercer_diccionario,headers=head2,tablefmt="grid", maxheadercolwidths=12, floatfmt=".0f"))
    printTiempoMemoria(req_6)
    
    pass


def print_req_7(control,anio,subsector,top,memory):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    req_7 = controller.req_7(control,anio,subsector,top,memory)
    
    filtros = ["Código actividad económica", "Nombre actividad económica","Código sector económico", "Nombre sector económico",
               "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    
    head = ["Código actividad económica", "Nombre actividad económica","Código sector económico", "Nombre sector económico",
               "Total ingresos netos consolidados para el periodo", "Total costos y gastos consolidados para el periodo", 
               "Total saldo a pagar consolidados para el periodo", "Total saldo a favor consolidados para el periodo"]
    
    diccionario = diccionario_tabulable(req_7[0],filtros)
    print("==================== Req No. 7 inputs ====================")
    print(f"Find the top {top} economic activities with the lowest total costs and expenses in {anio} and in subsector {subsector} \n")
    print("==================== Req No. 7 Answer ==================== \n")
    
    size = lt.size(req_7[0])
    if size < int(top):
        print(f"There were only {size} activities in subsector {subsector} and year {anio}")
    else:
        print(f"The top {top} activities are")
    
    print(tabulate(diccionario,headers=head,tablefmt="grid",maxcolwidths=15, maxheadercolwidths=15, floatfmt=".0f"))
    printTiempoMemoria(req_7)
    pass


def print_req_8(control,top,anio,memory):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    req_8 = controller.req_8(control,top,anio,memory)
    answer = req_8[0]
    
    filtro1 = ["Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico", "Total Impuesto a cargo", "Total ingresos netos", 
               "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    
    filtro2 = ["Código actividad económica","Nombre actividad económica","Total Impuesto a cargo","Total ingresos netos","Total costos y gastos","Total saldo a pagar",
               "Total saldo a favor"]
    
    head = ["Código sector económico","Nombre sector económico", "Código subsector económico","Nombre subsector económico", "Total de impuestos a cargo para el subsector", "Total ingresos netos para el subsector", 
            "Total costos y gastos para el subsector", "Total saldo a pagar para el subsector","Total saldo a favor para el subsector"]
    
    primer_diccionario = diccionario_tabulable(answer[0],filtro1)
    
    dic_imprimir = {}
    
    for llaves in filtro1:
        dic_imprimir[llaves] = primer_diccionario[llaves]
    
    print("===================== Req No.8 Inputs =====================")
    print(f"Find the top {top} economic activities of each sub-sector with the highest total taxes payable in {anio} \n")
    print("===================== Req No.8 Answer =====================")
    print(tabulate(dic_imprimir,headers = head,tablefmt="grid",maxcolwidths=15,maxheadercolwidths=15, floatfmt=".0f"))
    print("\n")
    
    for subsector in lt.iterator(answer[1]):
        segundo_diccionario = diccionario_tabulable( lista_primeros_y_utlimos_3(subsector),filtro2)
        
        segundo_dic_imprimir = {}
        for data in filtro2:
            segundo_dic_imprimir[data] = segundo_diccionario[data]
            
        num_subsector = lt.firstElement(subsector)["Código subsector económico"]
        size = lt.size(subsector)
        
        if size < int(top):
            print(f"=============== There were only {size} activities in subsector {num_subsector} ===============")
        else:
            print(f"=============== There top {top} activities in subsector {num_subsector} are ===============")
            
        print(tabulate(segundo_dic_imprimir, headers="keys" , tablefmt="grid" , maxcolwidths=15, maxheadercolwidths=15, floatfmt=".0f"))
        print("\n")
        
    printTiempoMemoria(req_8)
    pass
    
def printMemoria():
    """
    Muestra al usuario un menu de las opciones de si desea memoria, las opciones es TRUE o FALSE
    """
    
    print("Desea que se calcule la memoria")
    print("1. True")
    print("2. False")
    
    pass

def obtenerMemoria(opcion):
    
    """ 
    Declara segun la respuesta del usuario, el tipo de lista que se va a utilizar.
    """
    opcion = int(opcion)
    
    if opcion == 1:
        estructura = True
    elif opcion == 2:
        estructura = False
        
    return  estructura

def printTamanio():
    
    print("Que cantidad de datos desea cargar:")
    print("1. 1%")
    print("2. 5%")
    print("3. 10%")
    print("4. 20%")
    print("5. 30%")
    print("6. 50%")
    print("7. 80%")
    print("8. 100%")
    
    pass

def obtener_porcentaje(opcion):
    
    """ 
    Declara segun la respuesta del usuario, el nombre del archivo que se va a utilizar segun su tamaño.
    """
    opcion = int(opcion)
    
    if opcion == 1:
        porcentaje = "small"
    elif opcion == 2:
        porcentaje = "5pct"
    elif opcion == 3:
        porcentaje = "10pct"
    elif opcion == 4:
        porcentaje = "20pct"
    elif opcion == 5:
        porcentaje = "30pct"
    elif opcion == 6:
        porcentaje = "50pct"
    elif opcion == 7:
        porcentaje = "80pct"
    elif opcion == 8:
        porcentaje = "large"
    
    return porcentaje

def printTiempoMemoria(answer):
    
    """
    Imprime el tiempo y memoria que toma un proceso
    """
    if isinstance(answer, (list, tuple)) is True:
        
        if len(answer) == 2:
            time = answer[1]
            print("Tiempo [ms]: ", f"{time:.3f}")
            
        elif len(answer) == 3:
            time = answer[1]
            memory = answer[2]
            print('Tiempo [ms]: ', f"{time:.3f}", '||',
                  'Memoria [kB]: ', f"{memory:.3f}")
    else:
        print("No cargo correctamente.\n")

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                control = new_controller()
                printTamanio()
                tamanio = obtener_porcentaje(input())
                printMemoria()
                memoria = obtenerMemoria(input())
                data = load_data(control,memoria,tamanio)
                print_carga_de_datos(data[0])
                printTiempoMemoria(data)
                
            elif int(inputs) == 2:
                anio = input("Ingrese el año a consultar \n")
                sector = input("Ingrese el sector a consultar \n")
                printMemoria()
                memoria = obtenerMemoria(input())
                print_req_1(control,anio,sector,memoria)

            elif int(inputs) == 3:
                anio = input("Ingrese el año a consultar \n")
                sector = input("Ingrese el sector a consultar \n")
                printMemoria()
                memoria = obtenerMemoria(input())
                print_req_2(control,anio,sector,memoria)

            elif int(inputs) == 4:
                anio = input("Ingrese el año a consultar \n")
                printMemoria()
                memoria = obtenerMemoria(input())
                print_req_3(control,anio,memoria)

            elif int(inputs) == 5:
                anio = input("Ingrese el año a consultar \n")
                printMemoria()
                memoria = obtenerMemoria(input())
                print_req_4(control,anio,memoria)

            elif int(inputs) == 6:
                anio = input("Ingrese el año a consultar \n")
                printMemoria()
                memoria = obtenerMemoria(input())
                print_req_5(control,anio,memoria)

            elif int(inputs) == 7:
                anio = input("Ingrese el año a consultar \n")
                printMemoria()
                memoria = obtenerMemoria(input())
                print_req_6(control,anio,memoria)

            elif int(inputs) == 8:
                anio = input("Ingrese el año a consultar \n")
                subsector = input("Ingrese el subsector a consultar \n")
                top = input("Ingrese el top(n) que desea \n")
                printMemoria()
                memoria = obtenerMemoria(input())
                print_req_7(control,anio,subsector,top,memoria)

            elif int(inputs) == 9:
                top = input("Ingrese el top(n) que desea \n")
                anio = input("Ingrese el año a consultar \n")
                printMemoria()
                memoria = obtenerMemoria(input())
                print_req_8(control,top,anio,memoria)
                  
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)




