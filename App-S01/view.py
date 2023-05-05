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

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(data_type):
    """
        Se crea una instancia del controlador
    """ 
    control = controller.new_controller(data_type)
    return control 


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Actividad economica con mayor saldo a pagar para un sector economico y año especifico")
    print("3- Actividad economica con mayor saldo a favor para un sector economico y año especifico")
    print("4- Subsector economico con el menor total de retenciones para una año especifico")
    print("5- Subsector economico con los mayores costos y gastos de nomina para una año especifico")
    print("6- Subsector economico con los mayores descuentos tributarios para una año especifico")
    print("7- Sector economico con el mayor total de ingresos netos para un año especifico")
    print("8- Top de actividades economicas con el menor total de costos y gastos para un subsector para un año especifico")
    print("9- Top de actividades economicas de cada subsector con los mayores totales de impuestos a cargo para un año especifico")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    data= controller.load_data(control)
    return data

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer:.3f}")

def print_req_1(control, anio, cod):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    
    dato, a = controller.req_1(control, anio, cod)
    headers = ["Código actividad económica",
                    "Nombre actividad económica",
                    "Código subsector económico",
                    "Nombre subsector económico",
                    "Total ingresos netos",
                    "Total costos y gastos",
                    "Total saldo a pagar",
                    "Total saldo a favor"]
    
    
    table = []
    row = []

    for key in dato:
        if key in headers:
            row.append(dato[key])
    table.append(row)

    print("----------------Req 1------------------- ")
    print("Encuentre la actividad economica con mayor total saldo a pagar para el año " + dato["Año"] + " y el sector economico " + dato["Código sector económico"])
    print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    printLoadDataAnswer(a)
    
    

def print_req_2(control,anio, cod):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    dato, a = controller.req_2(control, anio, cod)
    headers = ["Código actividad económica",
                    "Nombre actividad económica",
                    "Código subsector económico",
                    "Nombre subsector económico",
                    "Total ingresos netos",
                    "Total costos y gastos",
                    "Total saldo a pagar",
                    "Total saldo a favor"]
    
    
    table = []
    row = []

    for key in dato:
        if key in headers:
            row.append(dato[key])
    table.append(row)

    print("----------------Req 2------------------- ")
    print("Encuentre la actividad economica con mayor total saldo a favor para el año " + dato["Año"] + " y el sector economico " + dato["Código sector económico"])
    print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    printLoadDataAnswer(a)

def print_req_3(control, anio):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    elemento, table, a = controller.req_3(control, anio)
    codigo = elemento['Código sector económico']

    headers1 = ['Código sector económico','Nombre sector económico', 'Código subsector económico', 
               'Nombre subsector económico','Total de retenciones del subsector economico', 
               'Total ingresos netos del subsector economico', 'Total costos y gastos del subsector', 
               'Total saldo a pagar del subsector','Total saldo a favor del subsector']
    
    table1 = [[elemento['Código sector económico'], elemento['Nombre sector económico'], elemento['Código subsector económico'],
               elemento['Nombre subsector económico'], elemento['Total retenciones'], elemento['Total ingresos netos'],
               elemento['Total costos y gastos'], elemento['Total saldo a pagar'], elemento['Total saldo a favor']]]
    
    headers = ["Código actividad económica","Nombre actividad económica","Total retenciones", 
                "Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    
    
    print("\n")
    print("----------------Req 3------------------- ")
    print("El subsector economico con el menor total de retenciones en el " + str(anio))
    print(tabulate(table1,headers1,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    if len(table) < 6:
        print("Solo hay " + str(len(table)) + " actvidades economicas en el subsector economico " + codigo)
        print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    else:
        print("Las 6 actividades economicas en el subsector economico " + codigo)
        print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    printLoadDataAnswer(a)
    

def print_req_4(control,anio):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """

    elemento_max, table, a = controller.req_4(control,anio)
    codigo = elemento_max['Código sector económico']

    headers1 = ['Código sector económico','Nombre sector económico', 'Código subsector económico', 
               'Nombre subsector económico','Total de costos y gastos nomina del subsector economico', 
               'Total ingresos netos del subsector economico', 'Total costos y gastos del subsector', 
               'Total saldo a pagar del subsector','Total saldo a favor del subsector']
    
    table1 = [[elemento_max['Código sector económico'], elemento_max['Nombre sector económico'], elemento_max['Código subsector económico'],
               elemento_max['Nombre subsector económico'], elemento_max['Costos y gastos nómina'], elemento_max['Total ingresos netos'],
               elemento_max['Total costos y gastos'], elemento_max['Total saldo a pagar'], elemento_max['Total saldo a favor']]]
    
    headers = ["Código actividad económica","Nombre actividad económica","Total costos y gastos nómina", 
                   "Total ingresos netos", "Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    
    
    print("\n")
    print("----------------Req 4------------------- ")
    print("El subsector economico con el mayor total de costos y gastos nominas en el " + str(anio))
    print(tabulate(table1,headers1,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    if len(table) < 6:
        print("Solo hay " + str(len(table)) + " actvidades economicas en el subsector economico " + codigo)
        print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    else:
        print("Las 6 actividades economicas en el subsector economico " + codigo)
        print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    printLoadDataAnswer(a)



def print_req_5(control, anio):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    dato , a = controller.req_5(control, anio)
    if dato == None:
        return print("No se encontro actividades con el año dado\n")
    table = []
    table.append(dato[0][0])
    if dato == None:
        return print("No se encontro actividades con el año dado\n")
    print("\n---------------------------------Requerimiento 5---------------------------------")
    print("\nSubector economico con el mayor descuento tributario en", anio)
    print(tabulate(table,dato[0][1],tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    if len(dato[1][0]) < 6:
        print("Solo hay", len(dato[1][0]), "en el subsector economico", dato[0][0][0])
        print(tabulate(dato[1][0],dato[2],tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    else:
        print("Las 6 actividades economicas en el subsector economico", dato[0][0][0])
        print(tabulate(dato[1],dato[2],tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    printLoadDataAnswer(a)
    

def print_req_6(control, anio):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    max_sec, sub, max_act, min_act, a = controller.req_6(control,anio)

    print("\n---------------------------------Requerimiento 6---------------------------------")

    headers1 = ['Código sector económico','Nombre sector económico', 'Total ingresos netos del sector economico',
               'Total costos y gastos del sector economico','Total saldo a pagar del sector economico', 
               'Total saldo a favor del sector economico', 'Subsector economico que mas aporto', 'Subsector economico que menos aporto']
    

    headers3 = ["Código actividad económica","Nombre actividad económica","Total ingresos netos","Total costos y gastos", "Total saldo a pagar","Total saldo a favor",
                "Actividad economica que mas aporto", "Actividad economica que menos aporto"]

    tabla_max = []
    for pos in range(0,6):
        tabla_max.append(max_sec[0][pos])
    tabla_max.append(sub[0][0][0])
    tabla_max.append(sub[1][0][0])

    tabla_grande_max = []
    tabla_grande_max.append(tabla_max)

    print(tabulate(tabla_grande_max, headers1,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")


    tabla_sec_max = []
    tabla_sec_min = []

    for pos in range(0,6):
        tabla_sec_max.append(sub[0][0][pos])
        tabla_sec_min.append(sub[1][0][pos])

    
    act_mas_max = []
    act_min_max = []
    act_mas_min = []
    act_min_min = []
    for pos in range(0,6):
        act_mas_max.append(max_act[0][0][pos])
        act_min_max.append(max_act[1][0][pos])
        act_mas_min.append(min_act[0][0][pos])
        act_min_min.append(min_act[1][0][pos])
    
    tabla_max_act_mas = []
    tabla_max_act_min = []
    tabla_min_act_mas = []
    tabla_min_act_min = []

    
    for pos in range(0,6):
        columna1 = []
        columna2 = []
        columna3 = []
        columna4 = []

        columna1.append(max_act[0][1][pos])
        columna1.append(max_act[0][0][pos])
        columna2.append(max_act[1][1][pos])
        columna2.append(max_act[1][0][pos])
        tabla_max_act_mas.append(columna1)
        tabla_max_act_min.append(columna2)

        columna3.append(min_act[0][1][pos])
        columna3.append(min_act[0][0][pos])
        columna4.append(min_act[1][1][pos])
        columna4.append(min_act[1][0][pos])
        tabla_min_act_mas.append(columna3)
        tabla_min_act_min.append(columna4)

    act_max = tabulate(tabla_max_act_mas,tablefmt="fancy_grid",maxcolwidths=[14,14],stralign="left",numalign="left")
    act_min = tabulate(tabla_max_act_min,tablefmt="fancy_grid",maxcolwidths=[14,14],stralign="left",numalign="left")
    act_max2 = tabulate(tabla_min_act_mas,tablefmt="fancy_grid",maxcolwidths=[14,14],stralign="left",numalign="left")
    act_min2 = tabulate(tabla_min_act_min,tablefmt="fancy_grid",maxcolwidths=[14,14],stralign="left",numalign="left")


    tabla_sec_max.append(act_max)
    tabla_sec_max.append(act_min)
    tabla_sec_max_tabulate = []
    tabla_sec_max_tabulate.append(tabla_sec_max)

    tabla_sec_min.append(act_max2)
    tabla_sec_min.append(act_min2)
    tabla_sec_min_tabulate = []
    tabla_sec_min_tabulate.append(tabla_sec_min)



    print("------------------Subsector economico que mas aporto--------------------")
    print(tabulate(tabla_sec_max_tabulate, headers3, tablefmt="grid",maxcolwidths=[14,14,14,14,14,14,None,None], numalign="right"), "\n")
    print("Actividad economica que mas aporto: ")
    print(tabulate(tabla_max_act_mas,tablefmt="grid"),"\n")
    print("Actividad economica que menos aporto: ")
    print(tabulate(tabla_max_act_min,tablefmt="grid"),"\n")

    print("------------------Subsector economico que menos aporto--------------------")
    print(tabulate(tabla_sec_min_tabulate, headers3, tablefmt="grid",maxcolwidths=[14,14,14,14,14,14,None,None],numalign="right"), "\n")
    print("Actividad economica que mas aporto: ")
    print(tabulate(tabla_min_act_mas,tablefmt="grid"),"\n")
    print("Actividad economica que menos aporto: ")
    print(tabulate(tabla_min_act_min,tablefmt="grid"),"\n")
    
    printLoadDataAnswer(a)


 

def print_req_7(control,anio,n,cod):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    table, answer, a = controller.req_7(control,anio,n,cod)

    print("\n---------------------------------Requerimiento 7---------------------------------")
    

    headers = ["Código actividad económica", "Nombre actividad económica",
                "Código sector económico","Nombre sector económico",
                "Total ingesos netos consolidados en el periodo",
                "Total costos y gastos consolidados en el periodo", 
                "Total saldo a pagar consolidado en el periodo",
                "Total saldo a favor consolidado en el periodo"]

    if answer == False:
        print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    
    else:
         print("No hay actividades economicas con el codigo indicado\n")

    printLoadDataAnswer(a)

    
    


def print_req_8(control,anio,n):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    req_8, lista_act_ordenada, a = controller.req_8(control,anio,n)

    headers = ['Código sector económico','Nombre sector económico', 'Código subsector económico', 
             'Nombre subsector económico','Total de impuestos a cargo para el subsector', 
             'Total ingresos netos del subsector economico', 'Total costos y gastos del subsector', 
             'Total saldo a pagar del subsector','Total saldo a favor del subsector']
    
    headers2 = ["Código actividad económica","Nombre actividad económica","Total Impuesto a cargo", 
                   "Total ingresos netos","Total saldo a pagar","Total saldo a favor"]
    
    table_grande = []

    for element in lt.iterator(req_8):
        table = [element['Código sector económico'],element['Nombre sector económico'], element['Código subsector económico'], 
               element['Nombre subsector económico'],element['Total Impuesto a cargo'], 
               element['Total ingresos netos'], element['Total costos y gastos'], 
               element['Total saldo a pagar'],element['Total saldo a favor']]
        if table not in table_grande:
            table_grande.append(table)


    print("\n---------------------------------Requerimiento 8---------------------------------")
    print("Encontrar las top ", n," actividades economicas de cada subsector con el mayor total de impuestos a cargo en " + str(anio))
    print(tabulate(table_grande,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")



    for lista_act in lt.iterator(lista_act_ordenada):
        table_act = []
        table = []
        cod = None
        if n < 12:
        
            if lt.size(lista_act) <= n:
                
                for elemento in lt.iterator(lista_act):
                    cod = elemento['Código subsector económico']
                    table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total Impuesto a cargo"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                    if table not in table_act:
                        table_act.append(table)

            elif lt.size(lista_act)> n:
                
    
                top = lt.subList(lista,1,n)
            
                for elemento in lt.iterator(top):
                    cod = elemento['Código subsector económico']
                    table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total Impuesto a cargo"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                    if table not in table_act:
                        table_act.append(table)

        else:
            if lt.size(lista_act) <= 6:
                
                for elemento in lt.iterator(lista_act):
                    cod = elemento['Código subsector económico']
                    table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total Impuesto a cargo"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                    if table not in table_act:
                        table_act.append(table)
            else:

                peores = lt.subList(lista_act,1,3)
                mejores = lt.subList(lista_act,lt.size(lista_act)-3,3)
    
                for elemento in lt.iterator(peores):
                    cod = elemento['Código subsector económico']
                    table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total Impuesto a cargo"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                if table not in table_act:
                        table_act.append(table)
                
                for elemento in lt.iterator(mejores):
                    table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total Impuesto a cargo"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                if table not in table_act:
                        table_act.append(table)
               


        print("La(s)",len(table_act),"actividades economicas que más aportaron en el subsector " + cod + " son: ")

        print(tabulate(table_act,headers2,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    printLoadDataAnswer(a)


# Se crea el controlador asociado a la vista
control = new_controller(data_type="CHAINING")

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    data = None
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                
                dato = load_data(control)
                data = dato[0]
                answer = (dato[1], dato[2])
                
                headers = ["Año", 
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
                
                lista_ordenada = controller.sort(control)

                
                for lista in lt.iterator(lista_ordenada):
                    table = []
                    table_grande = []
                    if lt.size(lista) <= 6:
                        for element in lt.iterator(lista):
                                anio_valor = element["Año"]
                                table = [element["Año"], element['Código actividad económica'], element['Nombre actividad económica'], element['Código sector económico'],element['Nombre sector económico'], element['Código subsector económico'], 
                                element['Nombre subsector económico'],element['Total ingresos netos'], element['Total costos y gastos'], 
                                element['Total saldo a pagar'],element['Total saldo a favor']]

                                
                                table_grande.append(table)
                        print("Solo hay "+ str(len(table_grande)) + " actividades economicas en " + anio_valor)
                        print(tabulate(table_grande,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

                    else:
                        primeros = lt.subList(lista,1,3)
                        ultimos = lt.subList(lista,lt.size(lista)-3,3)

                        for element in lt.iterator(primeros):
                                table = [element["Año"], element['Código actividad económica'], element['Nombre actividad económica'], element['Código sector económico'],element['Nombre sector económico'], element['Código subsector económico'], 
                                element['Nombre subsector económico'],element['Total ingresos netos'], element['Total costos y gastos'], 
                                element['Total saldo a pagar'],element['Total saldo a favor']]
                                table_grande.append(table)

                        for element in lt.iterator(ultimos):
                                anio_valor = element["Año"]
                                table = [element["Año"], element['Código actividad económica'], element['Nombre actividad económica'], element['Código sector económico'],element['Nombre sector económico'], element['Código subsector económico'], 
                                element['Nombre subsector económico'],element['Total ingresos netos'], element['Total costos y gastos'], 
                                element['Total saldo a pagar'],element['Total saldo a favor']]


                                table_grande.append(table)

                    print("Los primeros y ultimos 3 datos cargados en " + anio_valor + " son: ")
                    print(tabulate(table_grande,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

                printLoadDataAnswer(answer)
                   
            elif int(inputs) == 2:
                anio = int(input("Ingrese el año que quiere consultar: "))
                cod = int(input("Ingrese el código que quiere consultar: "))
                print_req_1(data, anio, cod)
                
            elif int(inputs) == 3:
                anio = int(input("Ingrese el año que quiere consultar: "))
                cod = int(input("Ingrese el código que quiere consultar: "))
                print_req_2(data,anio,cod)

            elif int(inputs) == 4:
                anio = int(input("Ingrese el año que quiere consultar: "))
                print_req_3(data, anio)

            elif int(inputs) == 5:
                anio = int(input("Ingrese el año que quiere consultar: "))
                print_req_4(data, anio)

            elif int(inputs) == 6:
                anio = int(input("Ingrese el año que quiere consultar: "))
                print_req_5(data, anio)

            elif int(inputs) == 7:
                anio = int(input("Ingrese el año que quiere consultar: "))
                print_req_6(data, anio)

            elif int(inputs) == 8:
                anio = int(input("Ingrese el año que quiere consultar: "))
                n = int(input("Ingrese el numero de actividades que quiere consultar: "))
                cod = int(input("Ingrese el código que quiere consultar: "))
                print_req_7(data,anio,n,cod)

            elif int(inputs) == 9:
                anio = int(input("Ingrese el año que quiere consultar: "))
                n = int(input("Ingrese el numero de actividades que quiere consultar: "))
                print_req_8(data,anio,n)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
