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
from DISClib.Algorithms.Sorting import quicksort as quk
from DISClib.DataStructures import mapentry as me
assert cf
import tabulate
import traceback
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
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
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control=controller.new_controller()
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

def tabulate_data(data_set,header):
    data_set_org=[]
    for i in data_set:
        i=dict([(key,val) for key,val in i.items() if key in header])
        data_set_org.append(i)
    rows=[x.values() for x in data_set_org]
    print(tabulate.tabulate(rows,list(data_set_org[0].keys()),tablefmt='grid',stralign='center',maxheadercolwidths=13,maxcolwidths=13))

def tabulate_data_req6(data_set,header,option):
    data_set_org=[]
    for i in data_set:
        i=dict([(key,val) for key,val in i.items() if key in header])
        data_set_org.append(i)
    rows=[x.values() for x in data_set_org]
    if option==1:
        return tabulate.tabulate(rows,list(data_set_org[0].keys()),tablefmt='grid',stralign='center',maxheadercolwidths=13)
    else:
        return tabulate.tabulate(zip(*[list(data_set_org[0].keys()),list(data_set_org[0].values())]), tablefmt='grid',maxcolwidths=14)

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data=controller.load_data(control)['model']['data']['table']
    header=["Año","Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    for i in data['elements']:
        if i['key']!=None:
            j=i['value']['elements']
            print('\n')
            if i['value']['size']>=6:
                print(f"There are only '{6}' economic activities in '{i['key']}': ")
                tabulate_data(j[:3]+j[-3:],header)
            else:
                print(f"There are only '{len(j)}' economic activities in '{i['key']}': ")
                tabulate_data(j,header)

def print_req_1_2(req_w):
    header=["Código actividad económica","Nombre actividad económica","Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    year=input("In what 'Año' do you want to search? :")
    code_sector=input("In what 'Código actividad económica' do you want to search? :")
    print('\n')
    print(f"{f'Req No. {req_w} Inputs':=^40}")
    print(f"Find the economic activity with the highest balance due (Total saldo a pagar) for the year '{year}' and economic sector code '{code_sector}'")
    print('\n')
    print(f"{f'Req No. {req_w} Answer':=^40}")
    return header,year,code_sector

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    h=print_req_1_2(1)
    tabulate_data([controller.req_1(control,h[1],h[2])],h[0])
      
def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    
    # TODO: Imprimir el resultado del requerimiento 2
    h=print_req_1_2(2)
    tabulate_data([controller.req_2(control,h[1],h[2])],h[0])
    
def print_req_3_4_5(req_w,year,data,condition_1,condition_2):
    """
        Función que imprime la solución del Requerimiento 3-4-5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3-4-5
    header=["Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico",condition_2,"Total ingresos netos del subsector económico","Total costos y gastos del subsector económico","Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"]
    header_2=["Código actividad económica","Nombre actividad económica",condition_1,"Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    print(f"{f'Req No. {req_w} Answer':=^40}")
    print('\n')
    print(f"Economic sub_sectors with the '{condition_2}' in '{year}'")
    tabulate_data([data[1]],header)
    print('\n')
    print(f"{f' Contributions from activities ':-^40}")
    print('\n')
    if data[0]['size']>=6:
        tabulate_data(data[0]['elements'][:3]+data[0]['elements'][-3:],header_2)
    else:
        print(f"There are only '{data[0]['size']}' economic activities in '{data[0]['size']} economic subsector': ")
        tabulate_data(data[0]['elements'],header_2)

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    year=input("In what 'Año' do you want to search? :")
    data=controller.req_3(control,year)
    print_req_3_4_5(3,year,controller.req_3(control,year),"Total retenciones",'Total de retenciones del subsector económico')
    
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    year=input("In what 'Año' do you want to search? :")
    print_req_3_4_5(4,year,controller.req_4(control,year),"Costos y gastos nómina","Total de costos y gastos nómina del subsector económico")

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    year=input("In what 'Año' do you want to search? :")
    print_req_3_4_5(5,year,controller.req_5(control,year),"Descuentos tributarios","Total de descuentos tributarios del subsector económico")

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6

    year=input("In what 'Año' do you want to search? :")
    header_1=['Código sector económico', 'Nombre sector económico', 'Total ingresos netos del subsector económico', 'Total costos y gastos del subsector económico', 'Total saldo a pagar del subsector económico', 'Total saldo a favor del subsector económico', 'Subsector económico que más aporto', 'Subsector económico que menos aporto']
    header_2=["Código subsector económico","Nombre subsector económico","Total ingresos netos del subsector económico","Total costos y gastos del subsector económico", "Total saldo a pagar del subsector económico","Total saldo a favor del subsector económico","Actividad económica que más aporto","Actividad económica que menos aporto"]
    header_3=["Código actividad económica","Nombre actividad económica","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    data=controller.req_6(control,year)
    data_1=data[1].copy()
    print(f"{f' Req No. 6 Inputs ':=^40}")
    print(f"Find the economic activity with the highest total net income for each economic sector in '{year}")
    print('\n')
    print(f"{f' Req No. 6 Answers ':=^40}")
    tabulate_data([data[0]],header_1)
    print(f"{f' Economic subsector that contributed the most ':=^80}")
    data_1['Actividad económica que más aporto']=tabulate_data_req6([data_1['Actividad económica que más aporto']],header_3,2)
    data_1['Actividad económica que menos aporto']=tabulate_data_req6([data_1['Actividad económica que menos aporto']],header_3,2)
    print(tabulate_data_req6([data_1],header_2,1))
    data[2]['Actividad económica que más aporto']=tabulate_data_req6([data[2]['Actividad económica que más aporto']],header_3,2)
    data[2]['Actividad económica que menos aporto']=tabulate_data_req6([data[2]['Actividad económica que menos aporto']],header_3,2)
    print(f"{f' Economic subsector that contributed the less ':=^80}")
    print(tabulate_data_req6([data[2]],header_2,1))

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    header=["Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    year=input("In what 'Año' do you want to search? :")
    sub_code=input("What subsector? :")
    size_data=int(input("Insert the integer number that indicates top N:"))
    data=controller.req_7(control,year,sub_code)
    tabulate_data(data['elements'],header) if data['size']<=int(size_data) else tabulate_data(data['elements'][:size_data],header)

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    year=input("In what 'Año' do you want to search? :")
    top= int(input("Which top 'Actividades económicas' do you want to see?: "))
    data=controller.req_8(control,year,top)
    
    header_2=["Código actividad económica","Nombre actividad económica","Código subsector económico","Nombre subsector económico","Código sector económico","Nombre sector económico","Total Impuesto a cargo","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    print(f"{f'Req No. 8 Answer':=^40}")
    tabulate_data(data[0]["elements"],list((data[0]["elements"][0]).keys()))

    for i in lt.iterator(data[1]):
        a=i['key']
        print(f"{f'Top {top} activities in subsector {a}':=^60}")
        tabulate_data(i['elements'][:top],header_2)
        print('\n')
    
# Se crea el controlador asociado a la vista
control = new_controller()

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
                data = load_data(control)
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
