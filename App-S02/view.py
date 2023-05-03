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


def new_controller(map_type,factorCharge):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(map_type,factorCharge)
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Actividades de mayor saldo de pago anual (Req1)")
    print("3- Actividades de mayor recaudacion a favor anual (Req2)")
    print("4- Buscar subsector con menos retención anual (Req3)")
    print("5- Buscar subsector con mayor costo y gastos de nomina anual (Req4)")
    print("6- Buscar subsector con mayor descuento tributiario anual (Req5)")
    print("7- Buscar actividad economica con mayor total de ingresos netos anuales por sector (Req6)")
    print("8- Top de Actividades económicas de menor costo y gasta por periodo (Req7)")
    print("9- Top de Actividades económicas de mayor cargo de impuesto por periodo (Req8)")
    print("10- Seleccionar Tipo de Algoritmo de Ordenamiento (Lab4-5)")
    print("0- Salir")
    
    
def print_size_data_menu():
    print("Seleccione el tamaño de la muestra para continuar:")
    print("1. 5pct")
    print("2. 10pct")
    print("3. 20pct")
    print("4. 30pct")
    print("5. 50pct")
    print("6. 80pct")
    print("7. large")
    print("8. small")


def print_map_menu():
    print("Seleccione el tipo de solución a colisión para continuar:")
    print("1. SEPARATE CHAINING")
    print("2. LINEAR PROBING")


def load_data(control,data_size):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename = cf.data_dir + f'DIAN/Salida_agregados_renta_juridicos_AG-{data_size}.csv'
    controller.load_data(control, filename)
    return control

def printYearsResume(control):
    yearsMap = controller.printYearsResume(control)
    yearsKeys = mp.keySet(yearsMap)
    sortYears = controller.sortYears(yearsKeys)
    for year in lt.iterator(sortYears):
        año = mp.get(yearsMap,year)['value']
        yearReg = lt.firstElement(año)['Año']
        if lt.size(año) > 6:
            print(f'The first three and last three economic activities load in "{yearReg}" are')
            printSortResults(año,cargaDict,sample=3)
        else:
            print(f'there are only {lt.size(año)} in "{yearReg}"')
            printSortResults(año,cargaDict,sample=-1)


def print_req_1(control, year, sector):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    
    print("\n=========== Req No 1 Answer =================")
    
    
    # TODO: Imprimir el resultado del requerimiento 1
    response, time, memory = controller.req_1(control, year, sector)
    printSortResults(response, req_1_Dict, -1)
    print(f'the requiriment 1 was executed in {time:.3f} ms and occuped {memory:.3f}kb of memory')


def print_req_2(control, year, sector):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    
    print("\n=========== Req No 2 Answer =================")
    
    
    # TODO: Imprimir el resultado del requerimiento 2
    response, time, memory  = controller.req_2(control, year, sector)
    printSortResults(response, req_2_Dict, sample=-1)
    print(f'the requiriment 2 was executed in {time:.3f} ms and occuped {memory:.3f}kb of memory')


def print_req_3(control, year):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    print("\n=========== Req No 3 Answer =================")
    
    # TODO: Imprimir el resultado del requerimiento 3
    response, time, memory = controller.req_3(control, year)
    printSortResults(response, req_3_Dict, 0)
    
    size = lt.size(response)
    subsector = response["elements"][0]["Código subsector económico"]
        
    if (size >= 6):
        print(f"\nThe three economic activities that contributed the least and the three that contributed the most in {year} and in {subsector} subsector")
        sample = 3
    else:
        print(f"There are only {size} economic activities in {year} and in {subsector} subsector")
        sample = -1
            
    printSortResults(response, req_3_Dict2, sample, "by menor total de retenciones por año")
    print(f'the requiriment 3 was executed in {time:.3f} ms and occuped {memory:.3f}kb of memory')


def print_req_4(control, year):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print("\n=========== Req No 4 Answer =================")
    
    # TODO: Imprimir el resultado del requerimiento 4
    response, time, memory = controller.req_4(control, year)
    printSortResults(response,req_4_Dict_1,sample=0)
    if lt.size(response) > 6:
        printSortResults(response,req_4_Dict_2,sample=3)
    else:
        printSortResults(response,req_4_Dict_2,sample=-1)
    print(f'the requiriment 4 was executed in {time:.3f} ms and occuped {memory:.3f}kb of memory')

def print_req_5(control, year):
    
    print("\n=========== Req No 5 Answer =================")
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    response, time, memory = controller.req_5(control, year)
    printSortResults(response,req_5_Dict,sample=0)
    if lt.size(response) > 6:
        printSortResults(response,req_5_Dict2,sample=3)
    else:
        printSortResults(response,req_5_Dict2,sample=-1)
        
    print(f'the requiriment 4 was executed in {time:.3f} ms and occuped {memory:.3f}kb of memory')
    
def print_req_6(control, year):
    
    print("\n=========== Req No 6 Answer =================")
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    mayor,menor, time, memory= controller.req_6(control, year)
    printSortResults(mayor, req_6_Dict,0)
    printSortResults(mayor, req_6_Dict_2,0)
    printSortResults(menor, req_6_Dict_2,0)
    print(f'the requiriment 6 was executed in {time:.3f} ms and occuped {memory:.3f}kb of memory')


def print_req_7(control, top, year, subsector):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    response, time, memory = controller.req_7(control, top, year, subsector)
    size = lt.size(response)
    
    print("\n=========== Req No 7 Answer =================")
        
    if (size >= int(top)):
        print(f"Find the top {top} economic activities with the lowest total costs and expenses in {year} and in subsector {subsector}")

    else:
        print(f"There are only {size} economic activities in {year} and in {subsector} subsector")
            
    printSortResults(response, req_7_Dict, -1) 
    print(f'the requiriment 7 was executed in {time:.3f} ms and occuped {memory:.3f}kb of memory')


def print_req_8(control, top, year):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    
    print("\n=========== Req No 8 Answer =================")
    sorted_list, response, keys_sorted, time, memory = controller.req_8(control, year)
    
    printSortResults(sorted_list, req_8_Dict, -1)
    
    for key in lt.iterator(keys_sorted):
        
        data = mp.get(response, key)["value"]
        subsector = data["elements"][0]["Código subsector económico"]
        size = lt.size(data)
        
        if (size >= int(top)):
            print(f"Top {top} activities in subsector {subsector}")

        else:
            print(f"There are only {size} activities in subsector {subsector} ")
             
        printSortResults(data, req_8_Dict2, -1)
    print(f'the requiriment 7 was executed in {time:.3f} ms and occuped {memory:.3f}kb of memory')

        

#Funciones de impresión en la terminal - Tabulate
def printSortResults(sort_data, styleDict, sample=3, cmpfunction="by year"):
    """
        Función que imprime una tabla de forma organizada a partir de una lista:
        argument:
            sort_data: list width the elements to display
            styleDict: dict in wich there are the specifications to display the table in terminal, this dict had three keys:
                       "keys" : columns to display in the table
                       "maxcolwidths": width of each column in the table
            sample: width of the rows in the table, if sample is equal to -1 the table show the total of rows
            cmpfunction: str to indicate the type of cmpfunction that was used to sort the data
    """
    if (sort_data == None):
        print("No se encontró registro para la consulta realizada")
        return
    
    size = lt.size(sort_data)
    print("\n")
    table = lt.newList(datastructure="ARRAY_LIST")
    notFormating=["Año", "Código actividad económica"]
    if sample != -1 and sample != 0:
        print(f'The first {sample} and last {sample} titles in content range are...')
    else:
        print(f'Showing {size} titles the total of the content...')
    print(f'Content sorted {cmpfunction}:')

    if sample != -1 and sample != 0:
        i = 1
        while i <= sample:
            data_item = lt.getElement(sort_data, i)
            item = {}
            for key_value in styleDict["keys"]:
                try:
                    tipe = int(data_item[key_value])
                    if key_value in notFormating:
                        tipe = None
                except ValueError:
                    tipe = None
                if tipe != None:
                    item[key_value] = ("{:,}".format(int(data_item[key_value])))
                else:
                    item[key_value] = data_item[key_value]
            lt.addLast(table, item)
            i += 1
        i = size - sample + 1
        while i <= size:
            data_item = lt.getElement(sort_data, i)
            item = {}
            for key_value in styleDict["keys"]:
                try:
                    tipe = int(data_item[key_value])
                    if key_value in notFormating:
                        tipe = None
                except ValueError:
                    tipe = None
                if tipe != None:
                    item[key_value] = ("{:,}".format(int(data_item[key_value])))
                else:
                    item[key_value] = data_item[key_value]
            lt.addLast(table, item)
            i += 1
    elif sample == -1:
        for i in range(1,size+1):
            data_item = lt.getElement(sort_data, i)
            item = {}
            for key_value in styleDict["keys"]:
                try:
                    tipe = int(data_item[key_value])
                    if key_value in notFormating:
                        tipe = None
                except ValueError:
                    tipe = None
                if tipe != None:
                    item[key_value] = ("{:,}".format(int(data_item[key_value])))
                else:
                    item[key_value] = data_item[key_value]
            lt.addLast(table, item)
    else:
        data_item = lt.getElement(sort_data, 1)
        item = {}
        for key_value in styleDict["keys"]:
            try:
                tipe = int(data_item[key_value])
                if key_value in notFormating:
                    tipe = None
            except ValueError:
                tipe = None
            if tipe != None:
                item[key_value] = ("{:,}".format(int(data_item[key_value])))
            else:
                item[key_value] = data_item[key_value]
        lt.addLast(table, item)
        
    print(tabulate(table['elements'], headers="keys", tablefmt="grid", maxcolwidths=styleDict["maxcolwidths"], maxheadercolwidths=styleDict["maxcolwidths"],numalign="left",))
    print("\n")
    
# Parámetros para estilizar el tabulate y parámetros de columnas por requirimiento
cargaDict = {"keys":["Año","Código actividad económica","Nombre actividad económica", "Código sector económico", "Nombre sector económico", 
              "Código subsector económico", "Nombre subsector económico","Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"],
              "maxcolwidths":[5,10,15,10,15,10,15,10,10,10,10]}
# Requerimiento 1 
req_1_Dict = {"keys":["Código actividad económica", "Nombre actividad económica", "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], "maxcolwidths":[12,15,12,15,12,12,12,12]}

# Requierimiento 2 
req_2_Dict = {"keys":["Código actividad económica", "Nombre actividad económica",  "Código subsector económico" , "Nombre subsector económico",
                      "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"],
              "maxcolwidths":[12,15,12,15,12,12,12,12]}
# Requerimiento 3
req_3_Dict = {"keys":["Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico",
                      "Total retenciones del subsector económico", "Total ingresos netos del subsector económico", "Total costos y gastos del subsector económico", "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"],
              "maxcolwidths":[12,12,12,15,12,12,12,12,12]}
req_3_Dict2 = {"keys":["Código actividad económica", "Nombre actividad económica", "Total retenciones","Total ingresos netos",
                       "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], "maxcolwidths":[12,15,12,12,12,12,12]}
# Requerimiento 4
req_4_Dict_1 = {"keys":["Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico",
                 "Total de costos y gastos nómina del subsector económico", "Total ingresos netos del subsector económico", "Total costos y gastos del subsector económico", "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"],
             "maxcolwidths":[10,15,10,15,15,15,15,15,15,10]}
req_4_Dict_2 = {"keys":["Código actividad económica", "Nombre actividad económica","Costos y gastos nómina", "Total ingresos netos",
                        "Total costos y gastos","Total saldo a pagar","Total saldo a favor"], "maxcolwidths":[15,30,15,15,15,15,15]}
# Requerimiento 5 
req_5_Dict = {"keys":["Año", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico",
                      "Total descuentos tributarios del subsector económico", "Total ingresos netos del subsector económico", "Total costos y gastos del subsector económico", "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"],
                      "maxcolwidths":[5,12,12,12,15,12,12,12,12,12]}

req_5_Dict2 = {"keys":["Código actividad económica", "Nombre actividad económica", "Descuentos tributarios","Total ingresos netos",
                       "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], "maxcolwidths":[12,15,12,12,12,12,12]}


# Requirimiento 6
req_6_Dict = {"keys":["Código sector económico", "Nombre sector económico","Total ingresos netos del sector económico","Total costos y gastos del sector económico",
                        "Total saldo a pagar del sector económico","Total saldo a favor del sector económico","Subsector económico que más aporto","Subsector económico que menos aporto"], "maxcolwidths":[10,20,15,15,15,15,15,15,15]}
req_6_Dict_2 = {"keys":["Código subsector económico", "Nombre subsector económico","Total ingresos netos del subsector económico","Total costos y gastos del subsector económico",
                        "Total saldo a pagar del subsector económico","Total saldo a favor del subsector económico","Actividad económica que más aporto","Actividad económica que menos aporto"], "maxcolwidths":[10,15,10,10,10,10,None,None]}

# Requerimiento 7
req_7_Dict = {"keys":["Código actividad económica","Nombre actividad económica", "Código sector económico", "Nombre sector económico","Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"],
              "maxcolwidths":[10,15,10,15,10,10,10,10]}

# Requerimiento 8
req_8_Dict = {"keys":["Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", 
                      "Total impuestos a cargo para el subsector económico", "Total ingresos netos del subsector económico", "Total costos y gastos del subsector económico", "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"], "maxcolwidths":[5,12,12,12,15,12,12,12,12,12]}
req_8_Dict2 = {"keys":["Código actividad económica", "Nombre actividad económica", "Total Impuesto a cargo", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], "maxcolwidths":[12,12,12,12,12,12,12]}


#Fix para evitar problemas de recursión
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

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
                map_type = None
                size_data = None
                factorCharge = None
                while size_data == None:
                    print_size_data_menu()
                    input_size = input("Seleccione una opción para continuar:\n")
                    try:
                        if int(input_size) == 1:
                            size_data = "5pct"
                        elif int(input_size) == 2:
                            size_data = "10pct"
                        elif int(input_size) == 3:
                            size_data = "20pct"
                        elif int(input_size) == 4:
                            size_data = "30pct"
                        elif int(input_size) == 5:
                            size_data = "50pct"
                        elif int(input_size) == 6:
                            size_data = "80pct"
                        elif int(input_size) == 7:
                            size_data = "large"
                        elif int(input_size) == 8:
                            size_data = "small"
                        else:
                            print("Elija una opción válida para continuar")
                    except ValueError:
                        print("Elija una opción válida para continuar")
                while map_type == None:
                    print_map_menu()
                    input_map = input("Seleccione una opción para continuar:\n")
                    try:
                        if int(input_map) == 1:
                            map_type = "CHAINING"
                        elif int(input_map) == 2:
                            map_type = "PROBING"
                        else:
                            print("Elija una opción válida para continuar")
                    except ValueError:
                        print("Elija una opción válida para continuar")
                while factorCharge == None:
                    try: 
                        factorCharge = float(input(f"Ingrese un factor de carga para la tabla de hash tipo {map_type}:\n→ "))
                        if map_type == "PROBING" and factorCharge > 1:
                            factorCharge = None
                            print("Ingrese un valor correcto")
                        if map_type == "CHAINING" and factorCharge < 1:
                            factorCharge = None
                            print("Ingrese un valor correcto")
                    except:
                        print("Ingreso un valor válido")
                # Se crea el controlador asociado a la vista
                print("Cargando información de los archivos ....\n")
                control = new_controller(map_type,factorCharge)
                control = load_data(control,size_data)
                printYearsResume(control)
                
            elif int(inputs) == 2:
                print("Ingrese el año en el que desea encontrar la actividad económica mayor saldo a pagar:")
                year = input("→ ")
                print("Ingrese el sector en el que desea encontrar la actividad económica mayor saldo a pagar:")
                sector = input("→ ")
                print_req_1(control, year, sector)

            elif int(inputs) == 3:
                print("Ingrese el año en el que desea encontrar la actividad económica mayor saldo a favor:")
                year = input("→ ")
                print("Ingrese el sector en el que desea encontrar la actividad económica mayor saldo a favor:")
                sector = input("→ ")
                print_req_2(control, year, sector)

            elif int(inputs) == 4:
                print("Ingrese el año en el que desea encontrar  el subsector económico que tuvo el menor total de retenciones:")
                year = input("→ ")
                print_req_3(control, year)

            elif int(inputs) == 5:
                print("Ingrese el año en el que desea buscar el subsector económico que tuvo los mayores costos y gastos por nómina:")
                year = input("→ ")
                print_req_4(control, year)

            elif int(inputs) == 6:
                print("Ingrese el año en el que desea buscar el subsector económico que tuvo los mayores descuentos triburarios")
                year = input("→ ")
                print_req_5(control, year)

            elif int(inputs) == 7:
                print("Ingrese el año en el que desea buscar el subsector económico que tuvo los mayores costos y gastos por nómina:")
                year = input("→ ")
                print_req_6(control, year)

            elif int(inputs) == 8:
                print("Ingrese el rango del top a conocer de las actividades económicas con el menor total de costos y gastos:")
                top = input("→ ")
                print("Ingrese el año en el que desea conocer el top de las actividades económicas con el menor total de costos y gastos:")
                year = input("→ ")
                print("Ingrese el subsector en el que desea conocer de las actividades económicas con el menor total de costos y gastos:")
                subsector = input("→ ")
                print_req_7(control, top, year, subsector)

            elif int(inputs) == 9:
                print("Ingrese el rango del top a conocer de las actividades económicas con los mayores totales de impuestos a cargo:")
                top = input("→ ")
                print("Ingrese el año en el que desea conocer el top de las actividades económicas con los mayores totales de impuestos a cargo:")
                year = input("→ ")
                print_req_8(control, top, year)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
