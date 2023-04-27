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

#-----------------Funciones generales de la vista-------#

def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    n = chooseMapType()
    a = chooseFileSize()
    al = chooseLoadFactor(n)
    control = controller.new_controller(n,a,al)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Obtener la actividad económica con mayor saldo a pagar para un sector económico y un año específico")
    print("3- Obtener la actividad económica con mayor saldo a favor para un sector económico y un año específico")
    print("4- Encontrar el subsector económico con el menor total de retenciones para un año específico")
    print("5- Encontrar el subsector económico con los mayores costos y gastos de nómina para un año específico")
    print("6- Encontrar el subsector económico con los mayores descuentos tributarios para un año específico")
    print("7- Encontrar el sector económico con el mayor total de ingresos netos para un año específico")
    print("8- Listar el TOP (N) de las actividades económicas con el menor total de costos y gastos para un subsector y un año específicos")
    print("9- EListar el TOP (N) de actividades económicas de cada subsector con los mayores totales de impuestos a cargo para un año específico")
    print("0- Salir")


def load_data(control,filename,memflag):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data = controller.load_data(control, filename,memflag)
    return data

#-----------------------------------------------------#

    
#-------Funciones de inputs generales del reto--------#

def chooseMapType():
    
    print('1: PROBING')
    print('2: CHAINING')
    
    working = True
    while working:
        inputs = input('Seleccione el tipo de lista que desea implementar: ')

        if int(inputs) == 1:   
            return int(inputs)
        elif int(inputs) == 2:
            return int(inputs)
        else: 
            print('Presione un numero valido') 
            
def chooseFileSize():
    print("==================== Bienvenidos al Reto 2 ====================\n")
    print('1: Datos al 5%')
    print('2: Datos al 10%')
    print('3: Datos al 20%')
    print('4: Datos al 30%')
    print('5: Datos al 50%')
    print('6: Datos al 80%')
    print('7: Datos al 100%')
    print('8: Datos small\n')
    
    working = True 
    while working:
        inputs = input('Seleccione el porcentaje de datos que quiere utilizar: ')
        if int(inputs) == 1:   
            return int(inputs)
        elif int(inputs) == 2:
            return int(inputs)
        elif int(inputs) == 3:
            return int(inputs)
        elif int(inputs) == 4:
            return int(inputs)
        elif int(inputs) == 5:
            return int(inputs)
        elif int(inputs) == 6:
            return int(inputs)
        elif int(inputs) == 7:
            return int(inputs)
        elif int(inputs) == 8:
            return int(inputs)        
        else: 
            print('Presione un numero valido') 
            
def chooseLoadFactor(n):
    if n == 1: 
        print('1: PROBING 0.1')
        print('2: PROBING 0.5')
        print('3: PROBING 0.7')
        print('4: PROBING 0.9')
        working = True
        while working:
            inputs = input('Seleccione el load factor que desea utilizar: ')

            if int(inputs) == 1:   
                return 0.1
            elif int(inputs) == 2:
                return 0.5
            elif int(inputs) == 3:
                return 0.7
            elif int(inputs) == 4:
                return 0.9 
            else: 
                print('Presione una opcion valida')
    if n == 2:
        print('1: CHAINING 2.00 ')
        print('2: CHAINING 4.00 ')
        print('3: CHAINING 6.00 ')
        print('4: CHAINING 8.00 ')
        working = True
        while working:
            inputs = input('Seleccione el load faactor que desea utilizar: ')

            if int(inputs) == 1:   
                return 2
            elif int(inputs) == 2:
                return 4
            elif int(inputs) == 3:
                return 6
            elif int(inputs) == 4:
                return 8  


def chooseYear():
    print('1: 2012')
    print('2: 2013')
    print('3: 2014')
    print('4: 2015')
    print('5: 2016')
    print('6: 2017')
    print('7: 2018')
    print('8: 2019')
    print('9: 2020')
    print('10: 2021')
    
    working = True
    while working:
        inputs = input('Seleccione el año que desea conocer la actividad con mayor cantidad de ingresos netos: ')

        if int(inputs) == 1:
            return int(inputs)
        elif int(inputs) == 2:
            return int(inputs)
        elif int(inputs) == 3:
            return int(inputs)
        elif int(inputs) == 4:
            return int(inputs) 
        elif int(inputs) == 5:
            return int(inputs)
        elif int(inputs) == 6:
            return int(inputs)
        elif int(inputs) == 7:
            return int(inputs)
        elif int(inputs) == 8:
            return int(inputs)
        elif int(inputs) == 9:
            return int(inputs)
        elif int(inputs) == 10:
            return int(inputs)

def chooseEconomicSector():
    print('Ingrese el numero de sector economico que desea conocer (entre 0 y 11): ')

    working = True
    while working:
        inputs = input('Seleccione el año que desea conocer la actividad con mayor cantidad de ingresos netos: ')
        if int(inputs) == 0:
            return int(inputs)
        elif int(inputs) == 1:
            return int(inputs)
        elif int(inputs) == 2:
            return int(inputs)
        elif int(inputs) == 3:
            return int(inputs)
        elif int(inputs) == 4:
            return int(inputs) 
        elif int(inputs) == 5:
            return int(inputs)
        elif int(inputs) == 6:
            return int(inputs)
        elif int(inputs) == 7:
            return int(inputs)
        elif int(inputs) == 8:
            return int(inputs)
        elif int(inputs) == 9:
            return int(inputs)
        elif int(inputs) == 10:
            return int(inputs)
        elif int(inputs) == 11:
            return int(inputs)

#------------------------------------------------------------------------#


#-------Funciones que imprimen la cantidad de mem usada y el  tiempo que usa cada req---------#
              
def printLoadDataAnswer(answer, mem):
    """
    Imprime los datos de tiempo y memoria de la carga de datos y los requerimientos
    """
    if mem == True:
        print("Tiempo [ms]: ", f"{answer[1]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[2]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer[1]:.3f}")

def printReqAnswer(answer):
    
    '''
    f
    Imprime los datos de tiempo y memoria de los requerimientos 1 y 2
    
    '''
    
    if len(answer) == 3:
        print("Tiempo [ms]: ", f"{answer[1]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[2]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer[1]:.3f}")

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False
        
#--------------------------------------------------------------------------------------------#
        

#Funciones que implementan la libreria tabulate para la impresion de los resultados de los requerimientos

def tabulateLindo(list, headers):
    matriz = []
    for registro in lt.iterator(list):
        fila = []
        for header in headers:
            fila.append(registro[header])
        matriz.append(fila)
    print(tabulate(matriz, headers, tablefmt="grid",maxcolwidths=14, maxheadercolwidths=14))
   
def tabulateLindo2(list, headers):
    matriz = []
    fila = []
    for header in headers:
        for registro in lt.iterator(list):
            if registro[0] == header:
                fila.append(registro[1])
    matriz.append(fila)
    print(tabulate(matriz, headers, tablefmt="grid",maxcolwidths=14, maxheadercolwidths=14)) 
    
def tabulateLindo3(list, headers1, headers2):
    matriz = []
    fila = []
    for header in headers1:
        for registro in lt.iterator(list):
            if registro[0] == header:
                if header == 'Actividad economica que mas aporto'or header == 'Actividad economica que menos aporto':
                    new = tabulateLindo4(registro[1], headers2)
                    fila.append(new)
                else:
                    fila.append(registro[1])
    matriz.append(fila)
    print(tabulate(matriz, headers1, tablefmt="grid",maxcolwidths=[14,14,14,14,14,14,54,54], maxheadercolwidths=[14,14,14,14,14,14,54,54]))     #[14,14,14,14,14,14,52,52]
def tabulateLindo4(registro, headers):
    matriz = []
    for header in headers:
        fila = []
        x = registro[header]
        fila.append(header)
        fila.append(x)
        matriz.append(fila)
    return tabulate(matriz, tablefmt="grid",disable_numparse=True,maxcolwidths=[18,32], maxheadercolwidths=[14,30])
def tabulateLindo5(lista, headers):
    matriz = []
    for j in range(1,lt.size(lista)+1):
        fila = []
        for header in headers:
            for registro in lt.iterator(lt.getElement(lista,j)):
               if registro[0] == header:
                    fila.append(registro[1])
        matriz.append(fila)
    print(tabulate(matriz, headers, tablefmt="grid",maxcolwidths=14, maxheadercolwidths=14))
    
#--------------------------------------------------------------------------#

#----------------Funcion que imprime la carga de datos--------------#
def impresionCargaData(dic, llave, h):
    
    imp = mp.get(dic, llave)
    lista1 = me.getValue(imp)
    lista2 = lista1['impuesto']
    lista3 = useMerge(lista2, 1)
    tam = lt.size(lista2)
    if  tam < 6:
        print("Solo hay "+str(tam)+" actividades economicas para el ano "+str(llave)+"\n")
        tabulateLindo(lista3, h)
    else: 
        lista4 = controller.recortarLista(lista3)
        print("Se imprimen las primeras 3 y ultimas 3 cargas para el ano "+str(llave)+"\n")
        tabulateLindo(lista4, h)
#-------------------------------------------------------------------#


def useMerge(lista, F):
    return controller.useMerge(lista,F)

#--------------Funciones para preguntar el año de los req 3, 4, 5, 6, 7 y 8-------#

def yearReq3():
    
    yearIn = input('Ingrese el año que desea conocer: ')
    return yearIn

def preguntarREQ4():
    anio = input("INGRESE EL ANIO QUE DESEA: ")
    return anio

def preguntarREQ7():
    anio = input("INGRESE EL ANIO QUE DESEA: ")
    SS = input("INGRESE EL SUBSECTOR QUE DESEA: ")
    top = input("INGRESE EL TOP QUE DESEA: ")
    return SS, anio, top

def preguntarREQ8():
    anio = input("INGRESE EL ANIO QUE DESEA: ")
    TOP = input("INGRESE EL TOP QUE DESEA: ")
    return anio, TOP

#-------------------------------------------------------------------------#

# Se crea el controlador asociado a la vista
control, filename  = new_controller()


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
                headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 
                           'Nombre subsector económico', 'Código subsector económico', 'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 
                           'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                data = load_data(control,filename, mem)
                map = data[0]['anio']
                llaves  =  mp.keySet(data[0]['anio'])
                llaves2 = useMerge(llaves, 2)
                size = lt.size(data[0]['impuestos'])
                for i in lt.iterator(llaves2):
                    impresionCargaData(map,i,headers)
                printLoadDataAnswer(data,mem)
                print(f'El tamaño de muestras cargadas es: {size}.')

            elif int(inputs) == 2:
                year = chooseYear()
                code = chooseEconomicSector()
                headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 
                           'Nombre subsector económico', 'Código subsector económico', 'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 
                           'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                answer = controller.req_1(control, mem, year, code)
                req1 = answer[0]
                sector = req1['elements'][0]['Código sector económico'] 
                anio = req1['elements'][0]['Año']
                print(f'La actividad economica con el mayor saldo a pagar en el {anio} del sector {sector}')

                tabulateLindo(req1, headers)
                printReqAnswer(answer)

            elif int(inputs) == 3:
                year = chooseYear()
                code = chooseEconomicSector()
                headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 
                           'Nombre subsector económico', 'Código subsector económico', 'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 
                           'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                answer = controller.req_2(control, mem, year, code)
                req2 = answer[0]
                sector = req2['elements'][0]['Código sector económico']
                anio = req2['elements'][0]['Año']
                
                print(f'La actividad economica con el mayor saldo a favor en el {anio} del sector {sector}')

                tabulateLindo(req2, headers)
                printReqAnswer(answer)
            
            elif int(inputs) == 4:

                headers=['Código sector económico','Nombre sector económico','Código subsector económico',
                         'Nombre subsector económico','Total retenciones','Total ingresos netos',
                         'Total costos y gastos','Total saldo a pagar','Total saldo a favor'] 
                headers2 = ['Código actividad económica', 'Nombre actividad económica', 'Total retenciones', 
                            'Total ingresos netos','Total costos y gastos','Total saldo a pagar', 'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                year_req3 = yearReq3()
                answer = controller.req_3(control,mem,year_req3, headers)
                req3 = answer[0]
                
                if mem == True:
                    flag = req3[1]
                    respuesta2 = req3[2]
                    subsector = req3[3]
                else:
                    flag = req3[1]
                    respuesta2 = req3[2]
                    subsector = req3[3]
                print(f'SUBSECTOR ECONOMICO CON LA MENOR CANTIDAD DE RETENCIONES TOTALES DEL AÑO {year_req3}')
                tabulateLindo2(req3[0],headers)
                if flag == False: 
                    print(f'Hay {lt.size(respuesta2)} actividades economicas en el subsector {subsector} para el año {year_req3}')
                    tabulateLindo(req3[2], headers2)  
                else: 
                    print(f'Las primeras 3 y ultimas 3 actividades economicas del subsector {subsector} para el año {year_req3} que mas aportaron fueron')
                    tabulateLindo(req3[2], headers2)
                printLoadDataAnswer(answer,mem)              

            elif int(inputs) == 5:
                headers=['Código sector económico','Nombre sector económico','Código subsector económico',
                         'Nombre subsector económico','Costos y gastos nómina','Total ingresos netos',
                         'Total costos y gastos','Total saldo a pagar','Total saldo a favor'] 
                headers2=['Código actividad económica', 'Nombre actividad económica','Costos y gastos nómina',
                          'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                anio = preguntarREQ4()
                r = controller.req_4(control,anio,headers, mem)
                r1 = r[0]
                
                
                if mem == True:
                    flag  = r[3]
                    r2 = r[4]
                    CM = r[5]
                else:
                    flag = r[2]
                    r2 = r[3]
                    CM = r[4]
                print("--------------SUBSECTOR ECONOMICO CON EL MAYOR COSTOA Y GASTOS DE NOMINA EN EL ANIO "+anio+"------------------\n")
                tabulateLindo2(r1,headers)  
                print("---------------------------ACTIVIDADES ECONOMICAS------------------------\n")
                if flag ==  False:
                    print("Hay solamente "+str(lt.size(r2))+" actividades economicas en el subsector "+str(CM)+" para el anio "+str(anio))
                else:  
                    print("Primeras 3 y ultimas actividades economicas en el subsector "+str(CM)+" para el anio "+str(anio)+" que mas aportaron")
                tabulateLindo(r2,headers2)
                
                printLoadDataAnswer(r,mem)

            elif int(inputs) == 6:
                headers=['Código sector económico','Nombre sector económico','Código subsector económico',
                         'Nombre subsector económico','Descuentos tributarios','Total ingresos netos',
                         'Total costos y gastos','Total saldo a pagar','Total saldo a favor'] 
                headers2=['Código actividad económica', 'Nombre actividad económica','Descuentos tributarios',
                          'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                anio = preguntarREQ4()
                r = controller.req_5(control,anio,headers, mem)
                r1 = r[0]
                
                
                if mem == True:
                    flag  = r[3]
                    r2 = r[4]
                    CM = r[5]
                else:
                    flag = r[2]
                    r2 = r[3]
                    CM = r[4]
                print("--------------SUBSECTOR ECONOMICO CON LOS MAYORES DESCUENTOS TRIBUTARIOS EN EL ANIO "+anio+"------------------\n")
                tabulateLindo2(r1,headers)  
                print("---------------------------ACTIVIDADES ECONOMICAS------------------------\n")
                if flag ==  False:
                    print("Hay solamente "+str(lt.size(r2))+" actividades economicas en el subsector "+str(CM)+" para el anio "+str(anio))
                else:  
                    print("Primeras 3 y ultimas actividades economicas en el subsector "+str(CM)+" para el anio "+str(anio)+" que mas aportaron")
                tabulateLindo(r2,headers2)
                
                printLoadDataAnswer(r,mem)

            elif int(inputs) == 7:
                headers = ['Código sector económico', 'Nombre sector económico','Total ingresos netos', 
                           'Total costos y gastos','Total saldo a pagar', 'Total saldo a favor','Subsector que mas aporto','Subsector que menos aporto']
                headers2 = ['Código subsector económico','Nombre subsector económico','Total ingresos netos',
                         'Total costos y gastos','Total saldo a pagar','Total saldo a favor', 'Actividad economica que mas aporto', 'Actividad economica que menos aporto']  
                headers3 = ['Código actividad económica', 'Nombre actividad económica', 
                            'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                anio = preguntarREQ4()
                r = controller.req_6(control,anio,headers,headers2, mem)
                r1 = r[0]
                if mem ==  False:
                    r2 = r[2]
                    r3 = r[3]
                else:  
                    r2 = r[3]
                    r3 = r[4]
                print("--------------SECTOR ECONOMICO CON EL MAYOR INGRESO NETO EN EL ANIO "+anio+"------------------\n")
                tabulateLindo2(r1,headers)  
                print("---------------------------SUBSECTORES ECONOMICOS------------------------\n")
                tabulateLindo3(r2,headers2,headers3)  
                tabulateLindo3(r3,headers2,headers3)  
                printLoadDataAnswer(r,mem)

            elif int(inputs) == 8:
                headers = ['Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 
                            'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                SS, anio, top = preguntarREQ7()
                r = controller.req_7(control,SS, anio, top, mem)
                r1 = r[0]
                if mem == True:
                    flag  = r[3]
                else:
                    flag = r[2]
                if flag ==  True:
                    print("Top "+str(top)+" actividades economicas en el subsector "+str(SS)+" para el anio "+str(anio))
                else:  
                    print("Hay "+str(lt.size(r1))+" actividades economicas en el subsector "+str(SS)+" para el anio "+str(anio))
                tabulateLindo(r1,headers)
                printLoadDataAnswer(r,mem)
            elif int(inputs) == 9:
                headers=['Código sector económico','Nombre sector económico','Código subsector económico',
                         'Nombre subsector económico','Total Impuesto a cargo','Total ingresos netos',
                         'Total costos y gastos','Total saldo a pagar','Total saldo a favor'] 
                headers2=['Código actividad económica', 'Nombre actividad económica','Total Impuesto a cargo',
                          'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                anio,TOP = preguntarREQ8()
                r = controller.req_8(control,anio,headers,TOP, mem)
                r1 = r[0]
                
                if mem == True:
                    #flag  = r[4]
                    r2 = r[3]
                    LC = r[5]
                else:
                    #flag = r[3]
                    r2 = r[2]    
                    LC = r[4]
                print("--------------SUBSECTORES ECONOMICOS CON EL MAYOR TOTAL IMPUETSO A CARGO EN EL ANIO "+anio+"------------------\n")
                tabulateLindo5(r1,headers)  
                cont = 1
                for i in lt.iterator(r2):
                    print("---------------------------ACTIVIDADES ECONOMICAS QUE MAS APORTARON------------------------\n")    
                    if int(TOP) > 12:
                        if lt.size(i) < 6:
                            print("Hay solamente "+str(lt.size(i))+" actividades economicas en el subsector "+str((lt.getElement(LC,cont)))+" para el anio "+str(anio))
                        else:  
                            print("Primeras 3 y ultimas actividades economicas del TOP "+TOP+ "en el subsector "+str((lt.getElement(LC,cont)))+" para el anio "+str(anio)+" que mas aportaron")
                        tabulateLindo(i, headers2)
                        cont +=1 
                    else: 
                        if lt.size(i) < int(TOP):
                            print("Hay solamente "+str(lt.size(i))+" actividades economicas en el subsector "+str((lt.getElement(LC,cont)))+" para el anio "+str(anio))
                        else:  
                            print("TOP "+ TOP +" actividades economicas en el subsector "+str((lt.getElement(LC,cont)))+" para el anio "+str(anio)+" que mas aportaron")
                        tabulateLindo(i, headers2)
                        cont +=1 
                printLoadDataAnswer(r,mem)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
