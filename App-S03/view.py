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
from DISClib.Algorithms.Sorting import mergesort as merg
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
    #TODO COMPLETADO: Llamar la función del controlador donde se crean las estructuras de datos
    print ('Antes de que el programa empiece, escoja el tipo de esquema de colision con el que quiera ejecutar el programa.')
    decision = input('1. Chaining \n2. Probing \n')
    if decision == '1' or decision == '2':
        
        if int(decision) == 1:
            print ('Elija el factor de carga. (ej 2.00, 8.00, etc)')
            decision_factcarg = input('2.00 \n4.00 \n6.00 \n8.00\n')
        
        elif int(decision) == 2:
            print ('Elija el factor de carga. (ej 0.1, 0.9, etc)')
            decision_factcarg = input('0.1 \n0.5 \n0.7 \n0.9\n')
        control = controller.new_controller(decision, decision_factcarg)
        return control
        
    else:
        print('La opcion que ingreso no es valida. Por favor vuela a correr el programa.')
        
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

def castBoolean(value):
    """
    Convierte un valor a booleano
    UTIL PARA memflag de la carga de datos
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False
def load_data(control, filename_elegido):
    """
    Carga los datos
    """
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    
    if mem == False:
        delta_tiempo = controller.load_data(control, filename_elegido, memflag=mem)
        print ('El programa se demoro ' + str(round(delta_tiempo, 2)) + ' [ms] en correr')
    else: 
        delta_tiempo, delta_memory = controller.load_data(control, filename_elegido, memflag=mem)
        print ('El programa se demoro ' + str(round(delta_tiempo, 2)) + ' [ms] en correr')
        print ('El programa ocupa ' + str(round(delta_memory, 2)) + ' [kB] espacio en la memoria')
  
def tabular_p3_u3(control):
      
    lista_dict_tab = []
    map_keylist = mp.keySet((control["model"])["map_anio"])
    sorted_map_keylist = merg.sort(map_keylist, lambda anio1, anio2: int(anio1) < int(anio2))
    menor_anio = lt.firstElement(sorted_map_keylist)
    mayor_anio = lt.lastElement(sorted_map_keylist)
    
    entry_anio_p = mp.get((control["model"])["map_anio"], str(menor_anio))    
    primer_anio = me.getValue(entry_anio_p)
    lista_impuestos_p_a  = primer_anio["impuestos"]

    i = 1
    for impuesto_p in lt.iterator(lista_impuestos_p_a):
        if i <= 3:
            lista_dict_tab.append(impuesto_p)
        i+=1
    
    entry_anio_u = mp.get(control["model"]["map_anio"], str(mayor_anio)) 
    ultimo_anio = me.getValue(entry_anio_u)
    lista_impuestos_u_a = ultimo_anio["impuestos"]

    size_last_anio = controller.data_size_lista(lista_impuestos_u_a) 
    j = size_last_anio-2
    
    for impuesto_u in lt.iterator(lista_impuestos_u_a):
        if j <= size_last_anio:
            lista_dict_tab.append(impuesto_u)
        j+=1

    encabezados = ["Año", "Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    print(tabulate([ [dicti[key] for key in encabezados] for dicti in lista_dict_tab], headers=encabezados, tablefmt='grid', maxcolwidths=50))
    lista_anios = [anio for anio in lt.iterator( mp.keySet(control['model']['map_anio']) ) ]
    print("-------------------------------------------------------------------------------------------------------------")
    print(f'Información para los siguientes anios: {lista_anios}')

def elegir_archivo():
    """
        Función que permite que el usuario pueda seleccionar el tamaño
        que desea para la muestra"""
    print("Seleccione el tipo de archivo que desea.")
    print("1. -5pct")
    print("2. -10pct")
    print("3. -20pct")
    print("4. -30pct")
    print("5. -50pct")
    print("6. -80pct")
    print("7. -100pct (Large)")
    print("8. -0.5pct (Small)")
    num_elegido  = input("Ingrese el número: ")
    return int(num_elegido)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    anio= input("Ingrese el año a buscar: ")
    cse= input("Ingrese el codigo del sector económico a buscar: ") 
    res, delta_t= (controller.req_1(control, anio, cse))
    print(delta_t)
    print(tabulate(res, headers="keys", tablefmt= "grid", maxcolwidths=50))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    year = input('ingrese el anio que desea buscar (ej 2012 - 2021): \n')
    codigo = input('Ingrese el codigo del sector economico que desea buscar (ej 0 - 11): \n')
    final, headz, time = controller.req_2(control, year, codigo)
    print ('el requerimiento se demoró ' + str(round(time,2)) + '[ms] en correr.\n')
    final_tabbed = tabulate(final['elements'], headers=headz, maxcolwidths=50)
    print ('La actividad economica con mayor saldo a pagar en el anio ' + str(year) + ' y en el sector economico con el codigo ' + str(codigo) + ' es: \n')
    print (final_tabbed)

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    anio= input("Ingrese el año a buscar: ")
    res, delta_t=(controller.req_3(control, anio))
    print(delta_t)
    if len(res)==2:
        res1, res2= res
        print(tabulate(res1, headers="keys", tablefmt= "grid", maxcolwidths=50))
        print(tabulate(res2["elements"], headers="keys", tablefmt= "grid", maxcolwidths=50))
    else:
        res1, res2, res3= res
        print(tabulate(res1, headers="keys", tablefmt= "grid", maxcolwidths=50))
        print(tabulate(res2["elements"], headers="keys", tablefmt= "grid", maxcolwidths=50))
        print(tabulate(res3["elements"], headers="keys", tablefmt= "grid", maxcolwidths=50))

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    anio = (input("Ingrese el año: "))
    req_4 , delta_t = (controller.req_4(control,int(anio)))
    
    lista_llaves_tab_1 = ['Código sector económico', 'Nombre sector económico','Código subsector económico', 'Nombre subsector económico', 'Costos y gastos nómina', 
                     'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
    res_subsector = {}
    for llave in lista_llaves_tab_1:
        res_subsector[llave] = req_4[llave]

    encabezados_actividades = ['Código actividad económica','Nombre actividad económica', 'Costos y gastos nómina','Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar','Total saldo a favor']
    
    print(delta_t)

    print(tabulate([[res_subsector[key] for key in lista_llaves_tab_1]], headers=lista_llaves_tab_1, tablefmt='grid', maxcolwidths=50)) ### TABULA UN UNICO ELEMENTO, RECIBE 1 DICCIONARIO

    print(tabulate([[impuesto[key] for key in encabezados_actividades] for impuesto in req_4['Actividades económicas']['elements']], headers=lista_llaves_tab_1, tablefmt='grid', maxcolwidths=50))

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    year = input('ingrese el anio que desea buscar (ej 2012, 2016): \n')
    final, headz_1, mayndmen, headz_2, time = controller.req_5(control, year)
    trys= [final['elements']]
    final_tabbed = tabulate(trys, headers=headz_1, maxcolwidths=50)
    actecon_tabbed = tabulate(mayndmen, headers=headz_2, maxcolwidths=50)
    print ('\n')
    print ('el requerimiento se demoró ' + str(round(time,2)) + '[ms] en correr.\n')
    print ('El subsector economico con mayor descuento tributario en '+ str(year) + '\n')
    print(final_tabbed)
    if len(mayndmen) < 6:
        print('El subsector tiene menos de seis actividades economicas. Las siguientes son las actividades economicas del subsector, \n listadas de menor a mayor aporte por el valor total de descuentos tributarios \n\n')
        print (actecon_tabbed)
    else:
        print ('Las tres actividades economicas que menos aportaron y mas aportaron al total de descuentos tributarios son las siguientes: \n Tomar en cuenta que las primeras tres son las que MENOS aportaron, y las siguientes tres son las que MAS aportaron.\n\n')
        print (actecon_tabbed)

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    anio = (input("Ingrese el año: "))
    req_6 , delta_t = (controller.req_6(control,int(anio)))
    #print(req_6)
    print(f'El delta es {delta_t}')

    lista_llaves_tab_1 = ['Código sector económico', 'Nombre sector económico', 'Costos y gastos nómina', 
                     'Total saldo a pagar', 'Total saldo a favor']
    res_sector = {'Subsector económico que más aporto':  req_6["Mejor subsector"]['Código subsector económico'], 
                     'Subsector económico que menos aportó':  req_6["Peor subsector"]['Código subsector económico']}
    for llave in lista_llaves_tab_1:
        res_sector[llave] = req_6[llave]


    print(tabulate([[res_sector[key] for key in list(res_sector.keys())]], headers = list(res_sector.keys()), tablefmt='grid', maxcolwidths=50)) ### TABULA UN UNICO ELEMENTO, RECIBE 1 DICCIONARIO
   
    for tipo_subsector in ["Mejor subsector", "Peor subsector"]:
        dict_mejor_subsector = req_6[tipo_subsector]

        encabezados_subsectores = ['Código subsector económico', 'Nombre subsector económico', 'Costos y gastos nómina', 
                        'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']

        res_subsector = {}
        for llave in encabezados_subsectores:
            res_subsector[llave] = dict_mejor_subsector[llave]

        encabezados_actividades = ['Código actividad económica','Nombre actividad económica', 'Costos y gastos nómina','Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar','Total saldo a favor']
        
        # MINI TABULACIONES
        res_subsector["Actividad económica que más aportó"] = tabulate([[dict_mejor_subsector["Mejor actividad"][key] for key in encabezados_actividades]], headers=encabezados_actividades, tablefmt='grid') 
        res_subsector["Actividad económica que menos aportó"] = tabulate([[dict_mejor_subsector["Peor actividad"][key] for key in encabezados_actividades]], headers=encabezados_actividades, tablefmt='grid')

        print(f"--------------------------{tipo_subsector}-------------------------")
        print(tabulate([[res_subsector[key] for key in list(res_subsector.keys())]], headers=list(res_subsector.keys()), tablefmt='grid', maxcolwidths=70)) ### TABULA UN SUBSECTOR
        print()
    

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    top= input("Ingrese el número de actividades a conocer: ")
    anio= input("Ingrese el año a buscar: ")
    csse= input("Ingrese el codigo del subsector económico a buscar: ")
    res, delta_t= (controller.req_7(control, top, anio, csse))
    print(delta_t)
    print(tabulate(res['elements'], headers="keys", tablefmt= "grid", maxcolwidths=50))

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass
    headz = ['Código sector económico', 'Nombre sector económico', 'Código subsector económico', 'Nombre subsector económico',
                    'Total Impuesto a cargo',"Total ingresos netos", "Costos y gastos nómina", "Total saldo a pagar","Total saldo a favor"]
    headz_2 = ['Código subsector económico', "Código actividad económica","Nombre actividad económica",
                    'Total Impuesto a cargo',"Total ingresos netos", "Costos y gastos nómina", "Total saldo a pagar","Total saldo a favor"]
    top = input('que top de actividades quiere identificar? (ej, top 3, top 5, etc)\n')
    year = input('que anio quiere buscar? (ej 2012 - 2021) \n')
    dict_sumas, final_final, delta_t = controller.req_8(control, top, year)
    print ('\nel programa se demoro '+ str(delta_t) + '[ms] en correr \n')
    print ('Tabla con los subsectores del anio ' + str(year))
    aja = []
    for sub in dict_sumas.values():
        tab= sub['elements']
        aja.append(tab)
    print (tabulate(aja, headz, tablefmt= "grid", maxcolwidths=50))
    print ('\n')
    
    for valores in final_final.values():
        if len(valores) < int(top):
            print ('\nhay solo ' + str(len(valores)) + ' actividades economicas en el subsector ' + str(valores[0][0]))
            print (tabulate(valores, headers=headz_2, tablefmt= "grid", maxcolwidths=50))
        else:
            print('\ntop ' +top + ' de actividades economicas en el subsector ' + str(valores[0][0]))
            print (tabulate(valores, headers=headz_2, tablefmt= "grid", maxcolwidths=50))

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
                                
                filename = ""
                numero_elegido = elegir_archivo()
                
                if numero_elegido == 1:
                    filename = "Salida_agregados_renta_juridicos_AG-5pct.csv"
                elif numero_elegido == 2:
                    filename = "Salida_agregados_renta_juridicos_AG-10pct.csv"
                elif numero_elegido == 3:
                    filename = "Salida_agregados_renta_juridicos_AG-20pct.csv"
                elif numero_elegido == 4:
                    filename = "Salida_agregados_renta_juridicos_AG-30pct.csv"
                elif numero_elegido == 5:
                    filename = "Salida_agregados_renta_juridicos_AG-50pct.csv"
                elif numero_elegido == 6:
                    filename = "Salida_agregados_renta_juridicos_AG-80pct.csv"
                elif numero_elegido == 7:
                    filename = "Salida_agregados_renta_juridicos_AG-large.csv"
                elif numero_elegido == 8:
                    filename = "Salida_agregados_renta_juridicos_AG-small.csv"
                else:
                    ("número inválido")
                
                data = load_data(control,filename)
                print("Años cargados: " + str(controller.map_size(control)))
                tabular_p3_u3(control)
                #print("Tiempo [ms]: ",data)
                
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
#extras que pueden ser utiles
