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


# Modificación del límite de recursiones
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(ds, lf, n=41):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(ds, lf, n)
    return control


def print_menu():
    print("\nBienvenido")
    print("1- Cargar información")
    print("2- [Req 1]: Obtener la actividad económica con mayor saldo a pagar para un sector económico y un año específico.")
    print("3- [Req 2]: Obtener la actividad económica con mayor saldo a favor para un sector económico y un año específico.")
    print("4- [Req 3]: Encontrar el subsector económico con el menor total de retenciones para un año específico.")
    print("5- [Req 4]: Encontrar el subsector económico con los mayores costos y gastos de nómina para un año específico.")
    print("6- [Req 5]: Encontrar el subsector económico con los mayores descuentos tributarios para un año específico.")
    print("7- [Req 6]: Encontrar el sector económico con el mayor total de ingresos netos para un año específico.")
    print("8- [Req 7]: Listar el TOP (N) de las actividades económicas con el menor total de costos y gastos para un subsector y un año específicos.")
    print("9- [Req 8]: Listar el TOP (N) de actividades económicas de cada subsector con los mayores totales de impuestos a cargo para un año específico.")
    print("0- Salir")


def load_data(control, dataPercentage, orderingAlg, boolmem):
    """
    Carga los datos
    """
    
    data = controller.load_data(control, cf.data_dir + 
                                'DIAN/Salida_agregados_renta_juridicos_AG-' + 
                                controller.selectPercentage(dataPercentage) + '.csv',
                                orderingAlg, boolmem)
    return data


def printInfo(data):
    """Imprime los datos cargados por consola

    Args:
        data (dict): Catalogo completo de datos de la DIAN
    """
    contador = 0
    año = 2012
    years = []
    headers = ["Año", 'Código actividad económica', "Nombre actividad económica", 'Código sector económico', 'Nombre sector económico', 
                           'Código subsector económico', 'Nombre subsector económico', 'Total ingresos netos', 
                           'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']   
    while contador < 10:
        llave = str(año)
        lista_año = me.getValue(mp.get(data, llave))
        tam = lista_año['size']
        if tam < 6:
            for i in range (1, tam+1):
                elem = lt.getElement(lista_año, i)
                tabla_year = [elem['Año'], elem['Código actividad económica'], elem['Nombre actividad económica'], elem['Código sector económico'],
                              elem['Nombre sector económico'], elem['Código subsector económico'], elem['Nombre subsector económico'],
                              elem['Total ingresos netos'], elem['Total costos y gastos'], elem['Total saldo a pagar'], elem['Total saldo a favor']]
                years.append(tabla_year)
        else:
            indices = [1, 2, 3, tam-2, tam-1, tam]
            for num in indices:
                elem = lt.getElement(lista_año, num)
                tabla_year = [elem['Año'], elem['Código actividad económica'], elem['Nombre actividad económica'], elem['Código sector económico'],
                              elem['Nombre sector económico'], elem['Código subsector económico'], elem['Nombre subsector económico'],
                              elem['Total ingresos netos'], elem['Total costos y gastos'], elem['Total saldo a pagar'], elem['Total saldo a favor']]
                years.append(tabla_year)
        contador +=1
        año += 1
    print(tabulate(years, headers, tablefmt="grid", maxcolwidths=[6, 7, 15, 7, 15, 7, 15, 6, 6, 6, 6], maxheadercolwidths=[6, 7, 15, 7, 15, 7, 15, 6, 6, 6, 6]))            


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    if data == None:
        print('\nNo hay un dato con el ID \'{0}\'\n'.format(id))
    else:
        print("\nEl dato con el ID", id, "es:", data['data'], '\n')


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    print('\n' + '=' * 40 + 'Requisito 1' + '=' * 40 + '\n')
    print("\nDesea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = recibir_bool(mem)
    
    year = input('Ingrse el año de consulta: ')
    id = input('Ingrese el código del sector económico que desea consultar: ')
    
    if mem:
        start = controller.memoryStart()
        
    a, t = controller.req_1(control, year, id)
    
    if mem: 
        end = controller.memoryEnd()
        memoria = controller.delta_memory(end, start)
    
    if a is '':
        print('No se encontró un sector económico con ese código.')
    else:
        headers = ['Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 'Total ingresos netos', 
                   'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
        tabla = [[a['Código actividad económica'], a['Nombre actividad económica'], a['Código sector económico'], a['Nombre sector económico'],
                  a['Total ingresos netos'], a['Total costos y gastos'], a['Total saldo a pagar'], a['Total saldo a favor']]]
        print('La actividad económica con el mayor saldo a pagar para el año ' + year + ' en el sector económico ' + id + ' fue: ')
        print(tabulate(tabla, headers, tablefmt='grid', maxcolwidths=14, maxheadercolwidths=14))
    
    if mem == True:
        print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
    print('El tiempo de la carga de datos fue de ' + str(t) + ' ms')


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    print('\n' + '=' * 40 + 'Requisito 2' + '=' * 40 + '\n')
    print("\nDesea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = recibir_bool(mem)
    
    year = input('Ingrese el año de consulta: ')
    id = input('Ingrese el código del sector económico que desea consultar: ')
    
    if mem:
        start = controller.memoryStart()
        
    a, t = controller.req_2(control, year, id)
    
    if mem: 
        end = controller.memoryEnd()
        memoria = controller.delta_memory(end, start)
        
    if a == '':
        print('No se encontro una actividad económica con el mayor saldo a favor para el año: ' + year + ' y con el codigo: ' + id) 
    else: 
        headers = ['Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 'Total ingresos netos', 
                'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
        tabla = [[a['Código actividad económica'], a['Nombre actividad económica'], a['Código sector económico'], a['Nombre sector económico'],
                            a['Total ingresos netos'], a['Total costos y gastos'], a['Total saldo a pagar'], a['Total saldo a favor']]]
        print('La actividad económica con el mayor saldo a favor para el año ' + year + ' en el sector económico ' + id + ' fue: ')
        print(tabulate(tabla, headers, tablefmt='grid', maxcolwidths=14, maxheadercolwidths=14))
        
    if mem == True:
        print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
    print('El tiempo de la carga de datos fue de ' + str(t) + ' ms')


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    print('\n' + '=' * 40 + 'Requisito 3' + '=' * 40 + '\n')
    print("\nDesea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = recibir_bool(mem)
    
    # imprime la tabla con el menor total de retenciones
    year = input("Ingrese el año de consulta: ")
    
    if mem:
        start = controller.memoryStart()
        
    info, t = controller.req_3(control, year)
    
    if mem: 
        end = controller.memoryEnd()
        memoria = controller.delta_memory(end, start)
        
    tabla1_Headers = ['Código sector económico', 
                      'Nombre sector económico', 
                      'Código subsector económico',
                      'Nombre subsector económico', 
                      'Total retenciones', 
                      'Total ingresos netos del subsector económico', 
                      'Total costos y gastos del subsector económico', 
                      'Total saldo a pagar del subsector económico', 
                      'Total saldo a favor del subsector económico']
    tabla1 = [[info['Código sector económico'], 
               info['Nombre sector económico'], 
               info['Código subsector económico'], 
               info['Nombre subsector económico'], 
               info['Total retenciones'], 
               info['Total ingresos netos'], 
               info['Total costos y gastos'], 
               info['Total saldo a pagar'], 
               info['Total saldo a favor']]]
    dataSize = info['size']
    print('\nEl subsector económico con el menor total de retenciones en el año ' + year + 'es: ')
    print(tabulate(tabla1, tabla1_Headers, tablefmt='grid', maxcolwidths=16, maxheadercolwidths=16))
 
    sub_tabla_Headers = ['Código actividad económica', 
                        'Nombre actividad económica', 
                        'Total retenciones', 
                        'Total ingresos netos', 
                        'Total costos y gastos', 
                        'Total saldo por pagar', 
                        'Total saldo a favor']
    tabla_que_menos_aportaron = []
    tabla_sub_que_mas_aportaron = []
    if dataSize < 6:
        print('Hay ' + str(dataSize) + ' actividad(es) económica(s) en el subsector')
        for i in range(1, dataSize+1):
            elem = lt.getElement(info, i)
            tabla_aux = [elem['Código actividad económica'], 
                         elem['Nombre actividad económica'], 
                         elem['Total retenciones'],
                         elem['Total ingresos netos'], 
                         elem['Total costos y gastos'], 
                         elem['Total saldo a pagar'], 
                         elem['Total saldo a favor']]
            tabla_que_menos_aportaron.append(tabla_aux)
        print(tabulate(tabla_que_menos_aportaron, sub_tabla_Headers, tablefmt='grid', maxcolwidths=16, maxheadercolwidths=16))           
    
    else:
        for i in range(1,3):
            elem = lt.getElement(info, i)
            tabla_aux = [elem['Código actividad económica'], 
                         elem['Nombre actividad económica'], 
                         elem['Total retenciones'],
                         elem['Total ingresos netos'], 
                         elem['Total costos y gastos'], 
                         elem['Total saldo a pagar'], 
                         elem['Total saldo a favor']]
            tabla_que_menos_aportaron.append(tabla_aux)
        print('Las 3 actividades que menos aportaron al valor total de retenciones del subsector fueron: ')
        print(tabulate(tabla_que_menos_aportaron, sub_tabla_Headers, tablefmt='grid', maxcolwidths=13, maxheadercolwidths=13))
        indices = [dataSize-2, dataSize-1, dataSize]
        for i in indices:
            elem = lt.getElement(info, i)
            tabla_aux = [elem['Código actividad económica'], 
                         elem['Nombre actividad económica'], 
                         elem['Total retenciones'],
                         elem['Total ingresos netos'], 
                         elem['Total costos y gastos'], 
                         elem['Total saldo a pagar'], 
                         elem['Total saldo a favor']]
            tabla_sub_que_mas_aportaron.append(tabla_aux)  
        print('Las 3 actividades que más aportaron al valor total de retenciones del subsector fueron: ')
        print(tabulate(tabla_sub_que_mas_aportaron, sub_tabla_Headers, tablefmt='grid', maxcolwidths=13, maxheadercolwidths=13))
        
    if mem == True:
        print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
    print('El tiempo de la carga de datos fue de ' + str(t) + ' ms')


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print('\n' + '=' * 40 + 'Requisito 4' + '=' * 40 + '\n')
    print("\nDesea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = recibir_bool(mem)
    
    year = input("Ingrese el año de consulta: ")
    
    if mem:
        start = controller.memoryStart()
        
    info, t = controller.req_4(control, year)
    
    if mem: 
        end = controller.memoryEnd()
        memoria = controller.delta_memory(end, start)
        
    Headers_1 = ['Código sector económico', 'Nombre sector económico', 'Código subsector económico',
                 'Nombre subsector económico', 'Total de costos y gastos de nómina del subsector económico', 
                 'Total ingresos netos del subsector económico', 'Total costos y gastos del subsector económico', 
                 'Total saldo a pagar del subsector económico', 'Total saldo a favor del subsector económico']
    Headers_2 = ['Código actividad económica', 'Nombre actividad económica', 'Costos y gastos nómina', 'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
    tabla1 = [[info['codsec'], info['nomsec'], info['codsub'], info['nomsub'], info['totalcyg'], info['totaling'], info['totalcg'], info['totalsp'], info['totalsf']]]
    tam = info['size']
    tabla2 = []
    tabla3 = []
    print('Subsector económico con los costos y gastos de nómina totales más altos en el año '+ year)
    print(tabulate(tabla1, Headers_1, tablefmt='grid', maxcolwidths=16, maxheadercolwidths=16))
    if tam < 6:
        print('Solo hay ' + str(tam) + ' actividades económicas en el subsector')
        for n in range (1, tam+1):
            elem = lt.getElement(info, n)
            tabla_aux = [elem['Código actividad económica'], elem['Nombre actividad económica'], elem['Costos y gastos nómina'],
                         elem['Total ingresos netos'], elem['Total costos y gastos'], elem['Total saldo a pagar'], elem['Total saldo a favor']]
            tabla2.append(tabla_aux)
        print(tabulate(tabla2, Headers_2, tablefmt='grid', maxcolwidths=16, maxheadercolwidths=16))
            
    else:
        indices2 = [1, 2, 3]
        indices3 = [tam-2, tam-1, tam]
        for i in indices2:
            elem = lt.getElement(info, i)
            tabla_aux = [elem['Código actividad económica'], elem['Nombre actividad económica'], elem['Costos y gastos nómina'],
                         elem['Total ingresos netos'], elem['Total costos y gastos'], elem['Total saldo a pagar'], elem['Total saldo a favor']]
            tabla2.append(tabla_aux)
        for x in indices3:
            elem = lt.getElement(info, x)
            tabla_aux = [elem['Código actividad económica'], elem['Nombre actividad económica'], elem['Costos y gastos nómina'],
                         elem['Total ingresos netos'], elem['Total costos y gastos'], elem['Total saldo a pagar'], elem['Total saldo a favor']]
            tabla3.append(tabla_aux)
        print('Las 3 actividades que menos contribuyeron al total de costos y gastos de nómina del subsector fueron: ')
        print(tabulate(tabla2, Headers_2, tablefmt='grid', maxcolwidths=13, maxheadercolwidths=13))
        print('Las 3 actividades que más contribuyeron al total de costos y gastos de nómina del subsector fueron: ')
        print(tabulate(tabla3, Headers_2, tablefmt='grid', maxcolwidths=13, maxheadercolwidths=13))
        
    if mem == True:
        print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
    print('El tiempo de la carga de datos fue de ' + str(t) + ' ms')


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    print('\n' + '=' * 40 + 'Requisito 5' + '=' * 40 + '\n')
    print("\nDesea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = recibir_bool(mem)
    
    year = input('\nIngrese el año del que desea conocer el subsector económico de mayores descuentos tributarios: ')
    
    if mem: 
        start = controller.memoryStart()
        
    out, t = controller.req_5(control, year)
    
    if mem: 
        end = controller.memoryEnd()
        memoria = controller.delta_memory(end, start)
    
    print('\n' + '-' * 40 + 'Información general del subsector económico de mayores retenciones en {}'.format(year) + '-' * 40)
    info = lt.getElement(out['list'], 1)
    gridMain = [[info['Código sector económico'],
                info['Nombre sector económico'],
                info['Código subsector económico'],
                info['Nombre subsector económico'],
                str(out['sum']),
                str(out['income']),
                str(out['spending']),
                str(out['debt']),
                str(out['profit'])]]
    
    titlesMain = ['Código sector económico',
                  'Nombre sector económico',
                  'Código subsector económico',
                  'Nombre subsector económico',
                  'Total descuentos tributarios del subsector en el año',
                  'Total ingresos netos del subsector en el año',
                  'Total costos y gastos del subsector en el año',
                  'Total saldo a pagar del subsector en el año',
                  'Total saldo a favor del subsector en el año']
    
    print(tabulate(gridMain, headers=titlesMain, tablefmt="grid", maxcolwidths=14, maxheadercolwidths=14))
    
    l = lt.size(out['list'])
    gridSub = []
    if l >= 6:
        print('\n' + '-' * 30 + 'Las tres actividades económicas con mayores y menores aportes de descuentos tributarios al subsector para el año {}'.format(year) + '-' * 30)
        for i in [1, 2, 3, l - 2, l - 1, l]:
            elem = lt.getElement(out['list'], i)
            gridSub.append([elem['Código actividad económica'],
                            elem['Nombre actividad económica'],
                            elem['Descuentos tributarios'],
                            elem['Total ingresos netos'],
                            elem['Total costos y gastos'],
                            elem['Total saldo a pagar'],
                            elem['Total saldo a favor']])
    else:
        print('\n' + '-' * 40 + 'Hubo {} actividades económicas para el año {}'.format(l, year) + '-' * 40)
        for elem in lt.iterator(out['list']):
            gridSub.append([elem['Código actividad económica'],
                            elem['Nombre actividad económica'],
                            elem['Descuentos tributarios'],
                            elem['Total ingresos netos'],
                            elem['Total costos y gastos'],
                            elem['Total saldo a pagar'],
                            elem['Total saldo a favor']])

    titlesSub = ['Código actividad económica', 
                 'Nombre actividad económica',
                 'Descuentos tributarios',
                 'Ingresos netos',
                 'Costos y gastos',
                 'Saldo a pagar',
                 'Saldo a favor']
    
    print(tabulate(gridSub, headers=titlesSub, tablefmt="grid", maxcolwidths=15, maxheadercolwidths=15))
    
    if mem == True:
        print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
    print('El tiempo de la carga de datos fue de ' + str(t) + ' ms')
    

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    print('\n' + '=' * 40 + 'Requisito 6' + '=' * 40 + '\n')
    print("\nDesea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = recibir_bool(mem)
    
    year = input("Ingrese el año de consulta: ")
    
    if mem: 
        start = controller.memoryStart()
        
    info, t = controller.req_6(control, year)
    
    if mem: 
        end = controller.memoryEnd()
        memoria = controller.delta_memory(end, start)
        
    headers = ['Código sector económico', 'Nombre sector económico', 'Total ingresos netos del sector económico', 'Total costos y gastos del sector económico',
               'Total saldo a pagar del sector económico', 'Total saldo a favor del sector económico', 
               'Subsector económico que más aportó', 'Subsector económico que menos aportó']
    headers2 = ['Código subsector económico', 'Nombre subsector económico', 'Total ingresos netos del subsector económico', 'Total costos y gastos del subsector económico', 
                'Total saldo a pagar del subsector económico', 'Total saldo a favor del subsector económico', 'Actividad económica que más aportó', 'Actividad económica que menos aportó']
    infosec = me.getValue(mp.get(info, 'infosec'))
    tabla = [[me.getValue(mp.get(infosec, 'codsec')), me.getValue(mp.get(infosec, 'nomsec')), me.getValue(mp.get(infosec, 'totaling'))['ing'],
              me.getValue(mp.get(infosec, 'totalcg'))['cg'], me.getValue(mp.get(infosec, 'totalsp'))['sp'], me.getValue(mp.get(infosec, 'totalsf'))['sf'],
              me.getValue(mp.get(infosec, 'submas')), me.getValue(mp.get(infosec, 'submin'))]]
    print('EL sector económico con mayores ingresos netos en el año ' + year + ' fue: ')
    print(tabulate(tabla, headers, tablefmt='grid', maxcolwidths=14, maxheadercolwidths=14))
    infosub = me.getValue(mp.get(info, 'subsectores'))
    subin_mayor = me.getValue(mp.get(infosec, 'submas'))
    subin_menor = me.getValue(mp.get(infosec, 'submin'))
    infosub_mayor = me.getValue(mp.get(infosub, subin_mayor))
    infosub_menor = me.getValue(mp.get(infosub, subin_menor))
    submayor = me.getValue(mp.get(infosub_mayor, 'infosubsec'))
    submenor = me.getValue(mp.get(infosub_menor, 'infosubsec'))
    acts_mayor = me.getValue(mp.get(infosub_mayor, 'actividades'))
    mayorf = lt.firstElement(acts_mayor)
    mayorl = lt.lastElement(acts_mayor)
    acts_menor = me.getValue(mp.get(infosub_menor, 'actividades'))
    menorf = lt.firstElement(acts_menor)
    menorl = lt.lastElement(acts_menor)
    tabla_mayor = [[me.getValue(mp.get(submayor, 'codsubsec')), me.getValue(mp.get(submayor, 'nomsubsec')), me.getValue(mp.get(submayor, 'totaling'))['ing'],
                    me.getValue(mp.get(submayor, 'totalcg'))['cg'], me.getValue(mp.get(submayor, 'totalsp'))['sp'], me.getValue(mp.get(submayor, 'totalsf'))['sf'],
                    tabulate([['Código actividad económica', mayorl['Código actividad económica']], ['Nombre actividad económica', mayorl['Nombre actividad económica']],
                              ['Total ingresos netos', mayorl['Total ingresos netos']], ['Total costos y gastos', mayorl['Total costos y gastos']],
                              ['Total saldo a pagar', mayorl['Total saldo a pagar']], ['Total saldo a favor', mayorl['Total saldo a favor']]], tablefmt='grid', maxcolwidths=14),
                    tabulate([['Código actividad económica', mayorf['Código actividad económica']], ['Nombre actividad económica', mayorf['Nombre actividad económica']],
                              ['Total ingresos netos', mayorf['Total ingresos netos']], ['Total costos y gastos', mayorf['Total costos y gastos']],
                              ['Total saldo a pagar', mayorf['Total saldo a pagar']], ['Total saldo a favor', mayorf['Total saldo a favor']]], tablefmt='grid', maxcolwidths=14)]]
    tabla_menor = [[me.getValue(mp.get(submenor, 'codsubsec')), me.getValue(mp.get(submenor, 'nomsubsec')), me.getValue(mp.get(submenor, 'totaling'))['ing'],
                    me.getValue(mp.get(submenor, 'totalcg'))['cg'], me.getValue(mp.get(submenor, 'totalsp'))['sp'], me.getValue(mp.get(submenor, 'totalsf'))['sf'],
                    tabulate([['Código actividad económica', menorl['Código actividad económica']], ['Nombre actividad económica', menorl['Nombre actividad económica']],
                              ['Total ingresos netos', menorl['Total ingresos netos']], ['Total costos y gastos', menorl['Total costos y gastos']],
                              ['Total saldo a pagar', menorl['Total saldo a pagar']], ['Total saldo a favor', menorl['Total saldo a favor']]], tablefmt='grid', maxcolwidths=21),
                    tabulate([['Código actividad económica', menorf['Código actividad económica']], ['Nombre actividad económica', menorf['Nombre actividad económica']],
                              ['Total ingresos netos', menorf['Total ingresos netos']], ['Total costos y gastos', menorf['Total costos y gastos']],
                              ['Total saldo a pagar', menorf['Total saldo a pagar']], ['Total saldo a favor', menorf['Total saldo a favor']]], tablefmt='grid', maxcolwidths=21)]]
    print('El subsector económico que más contribuyó fue: ')
    print(tabulate(tabla_mayor, headers2, tablefmt="grid", maxcolwidths=[12,12,12,12,12,12,40,40], maxheadercolwidths=[12,12,12,12,12,12,40,40]))
    print('El subsector económico que menos contribuyó fue: ')
    print(tabulate(tabla_menor, headers2, tablefmt="grid", maxcolwidths=[12,12,12,12,12,12,40,40], maxheadercolwidths=[12,12,12,12,12,12,40,40]))
    
    if mem == True:
        print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
    print('El tiempo de la carga de datos fue de ' + str(t) + ' ms')


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    print('\n' + '=' * 40 + 'Requisito 7' + '=' * 40 + '\n')
    print("\nDesea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = recibir_bool(mem)
    
    year = input('Ingrse el año de consulta: ')
    id = input('Ingrese el código del subsector económico que desea consultar: ')
    n = int(input('Ingrese la cantidad de actividades que desea listar: '))
    
    if mem: 
        start = controller.memoryStart()
        
    info, t = controller.req_7(control, year, id)
    
    if mem: 
        end = controller.memoryEnd()
        memoria = controller.delta_memory(end, start)
        
    tam  = lt.size(info)
    headers = ['Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 'Total ingresos netos consolidados para el periodo', 
               'Total costos y gastos consolidados para el periodo', 'Total saldo a pagar consolidados para el periodo', 'Total saldo a favor consolidados para el periodo']
    tabla = []
    if tam <= n:
        it = lt.iterator(info)
        for a in it:
            tabla_aux = [a['Código actividad económica'], a['Nombre actividad económica'], a['Código sector económico'], a['Nombre sector económico'],
                         a['Total ingresos netos'], a['Total costos y gastos'], a['Total saldo a pagar'], a['Total saldo a favor']]
            tabla.append(tabla_aux)
        print('Solo hay ' + str(tam) + ' actividades en el subsector ' + id + ' en el año ' + year)
    else: 
        contador = 1
        while contador < n+1:
            a = lt.getElement(info, contador)
            tabla_aux = [a['Código actividad económica'], a['Nombre actividad económica'], a['Código sector económico'], a['Nombre sector económico'],
                         a['Total ingresos netos'], a['Total costos y gastos'], a['Total saldo a pagar'], a['Total saldo a favor']]
            tabla.append(tabla_aux)
            contador += 1
        print('Las ' + str(n) + ' actividades con menores costos y gastos para el subsector ' + id + ' en el año ' + year + ' son: ')
    print(tabulate(tabla, headers, tablefmt='grid', maxcolwidths=14, maxheadercolwidths=14))

    if mem == True:
        print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
    print('El tiempo de la carga de datos fue de ' + str(t) + ' ms')


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    print('\n' + '=' * 40 + 'Requisito 8' + '=' * 40 + '\n')
    print("\nDesea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = recibir_bool(mem)
    
    year = input('Ingrese el año que desea consultar: ')
    n = int(input('Ingrese el número de subsectores económicos que desea identificar: '))
    
    if mem: 
        start = controller.memoryStart()
        
    subsectores, t = controller.req_8(control, year)
    
    if mem: 
        end = controller.memoryEnd()
        memoria = controller.delta_memory(end, start)
    
    iterador = lt.iterator(subsectores)
    tabla1 = []
    headers1 = ['Código sector económico', 'Nombre sector económico', 'Código subsector económico', 'Nombre subsector económico', 'Total impuestos a cargo para el subsector', 
                'Total ingresos netos para el subsector económico', 'Total costos y gastos para el subsector', 'Total saldo a pagar para el subsector', 'Total saldo a favor para el subsector']
    tam = lt.size(subsectores)
    if tam > n:
        contador = 1
        while contador < n+1:
            sub = lt.getElement(subsectores, contador)
            tabla_aux = [sub['codesec'], sub['nomsec'], sub['codesubsec'], sub['nomsubsec'], sub['ic'], sub['ing'], sub['cg'], sub['sp'], sub['sf']]
            tabla1.append(tabla_aux)
            contador += 1
    else:
        for sub in iterador:
            tabla_aux = [sub['codesec'], sub['nomsec'], sub['codesubsec'], sub['nomsubsec'], sub['ic'], sub['ing'], sub['cg'], sub['sp'], sub['sf']]
            tabla1.append(tabla_aux)
    if n > 12 and tam > 12:
        ta = []
        ta.append(tabla1[0])
        ta.append(tabla1[1])
        ta.append(tabla1[2])
        ta.append(tabla1[-1])
        ta.append(tabla1[-2])
        ta.append(tabla1[-3])
        print(tabulate(ta, headers1, tablefmt='grid', maxcolwidths=15, maxheadercolwidths=15))
    else:
        print(tabulate(tabla1, headers1, tablefmt='grid', maxcolwidths=15, maxheadercolwidths=15))
    
    headers2 = ['Código actividad económica', 'Nombre actividad económica', 'Total impuestos a cargo para el subsector', 
                'Total ingresos netos para el subsector económico', 'Total costos y gastos para el subsector', 'Total saldo a pagar para el subsector', 'Total saldo a favor para el subsector']
    if tam >= n:
        if n > 12:
            ind = [1,2,3, tam-2, tam-1, tam]
            for s in ind:
                actividades = []
                codigo = sub['codesubsec']
                sub = lt.getElement(subsectores, s)
                size = lt.size(sub)
                if size >= 3:
                    pos = 1
                    while pos < 4:
                        act = lt.getElement(sub, pos)
                        acti = [act['Código actividad económica'], act['Nombre actividad económica'], act['Total Impuesto a cargo'], act['Total ingresos netos'],
                                act['Total costos y gastos'], act['Total saldo a pagar'], act['Total saldo a favor']]
                        actividades.append(acti)
                        pos += 1
                    print('Top 3 de actividades con mayor total de impuesto a cargo en el subsector ' + codigo)
                else:
                    a = lt.iterator(sub)
                    for ac in a:
                        activi = [ac['Código actividad económica'], ac['Nombre actividad económica'], ac['Total Impuesto a cargo'], ac['Total ingresos netos'],
                                ac['Total costos y gastos'], ac['Total saldo a pagar'], ac['Total saldo a favor']]
                        actividades.append(activi) 
                    print('Solo hay ' + str(size) + ' actividades en el subsector ' + codigo)
                print(tabulate(actividades, headers2, tablefmt='grid', maxcolwidths=15, maxheadercolwidths=15))
        else:                
            contador2 = 1
            while contador2 < n+1:
                actividades = []
                sub = lt.getElement(subsectores, contador2)
                codigo = sub['codesubsec']
                size = lt.size(sub)
                if size >= 3:
                    pos = 1
                    while pos < 4:
                        act = lt.getElement(sub, pos)
                        acti = [act['Código actividad económica'], act['Nombre actividad económica'], act['Total Impuesto a cargo'], act['Total ingresos netos'],
                                act['Total costos y gastos'], act['Total saldo a pagar'], act['Total saldo a favor']]
                        actividades.append(acti)
                        pos += 1
                    print('Top 3 de actividades con mayor total de impuesto a cargo en el subsector ' + codigo)
                else:
                    a = lt.iterator(sub)
                    for ac in a:
                        activi = [ac['Código actividad económica'], ac['Nombre actividad económica'], ac['Total Impuesto a cargo'], ac['Total ingresos netos'],
                                ac['Total costos y gastos'], ac['Total saldo a pagar'], ac['Total saldo a favor']]
                        actividades.append(activi)  
                    print('Solo hay ' + str(size) + ' actividades en el subsector ' + codigo)
                print(tabulate(actividades, headers2, tablefmt='grid', maxcolwidths=15, maxheadercolwidths=15))
                contador2 += 1
    else:
        if n > 12:
            ind = [1,2,3, tam-2, tam-1, tam]
            for s in ind:
                actividades = []
                codigo = sub['codesubsec']
                sub = lt.getElement(subsectores, s)
                size = lt.size(sub)
                if size >= 3:
                    pos = 1
                    while pos < 4:
                        act = lt.getElement(sub, pos)
                        acti = [act['Código actividad económica'], act['Nombre actividad económica'], act['Total Impuesto a cargo'], act['Total ingresos netos'],
                                act['Total costos y gastos'], act['Total saldo a pagar'], act['Total saldo a favor']]
                        actividades.append(acti)
                        pos += 1
                    print('Top 3 de actividades con mayor total de impuesto a cargo en el subsector ' + codigo)
                else:
                    a = lt.iterator(sub)
                    for ac in a:
                        activi = [ac['Código actividad económica'], ac['Nombre actividad económica'], ac['Total Impuesto a cargo'], ac['Total ingresos netos'],
                                ac['Total costos y gastos'], ac['Total saldo a pagar'], ac['Total saldo a favor']]
                        actividades.append(activi) 
                    print('Solo hay ' + str(size) + ' actividades en el subsector ' + codigo)
                print(tabulate(actividades, headers2, tablefmt='grid', maxcolwidths=15, maxheadercolwidths=15))
        else:
            for sb in iterador:
                actividades = []
                size = lt.size(sb)
                if size > 3:
                    pos = 1
                    while pos < 4:
                        act = lt.getElement(sb, pos)
                        acti = [act['Código actividad económica'], act['Nombre actividad económica'], act['Total Impuesto a cargo'], act['Total ingresos netos'],
                                act['Total costos y gastos'], act['Total saldo a pagar'], act['Total saldo a favor']]
                        actividades.append(acti)
                        pos += 1
                    print('Top 3 de actividades con mayor total de impuesto a cargo en el subsector ' + codigo)
                else:
                    a = lt.iterator(sb)
                    for acts in a:
                        actii = [acts['Código actividad económica'], acts['Nombre actividad económica'], acts['Total Impuesto a cargo'], acts['Total ingresos netos'],
                                acts['Total costos y gastos'], acts['Total saldo a pagar'], acts['Total saldo a favor']]
                        actividades.append(actii)  
                    print(tabulate(actividades, headers2, tablefmt='grid', maxcolwidths=15, maxheadercolwidths=15))
                print(tabulate(actividades, headers2, tablefmt='grid', maxcolwidths=15, maxheadercolwidths=15))
            
    if mem == True:
        print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
    print('El tiempo de la carga de datos fue de ' + str(t) + ' ms')


def recibir_bool(inf):
    """
    Convierte un valor a booleano
    """
    if inf.lower() in ('true', 't', '1'):
        return True
    else:
        return False

# Se crea el controlador asociado a la vista
control = new_controller(ds='CHAINING', lf=0.5)

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
                
                print('\n¿Qué porcentaje de datos desea cargar?')
                print('1. 1%\n2. 5%\n3. 10%\n4. 20%\n5. 30%\n6. 50%\n7. 80%\n8. 100%')
                dataPercentage = input()
                
                print('\n¿Qué estructura de datos desea utilizar?')
                print('1. \'Separate Chaining\'\n2. \'Linear Probing\'')
                dataStructure = input()
                
                print('\n¿Con qué factor de carga quiere ordenar los datos?')
                if dataStructure == '1':
                    print('1. 2\n2. 4\n3. 6\n4. 8')
                elif dataStructure == '2':
                    print('1. 0.1\n2. 0.5\n3. 0.7\n4. 0.9')
                loadFactor = input()
                
                control = new_controller(dataStructure, loadFactor)
                
                print("\nDesea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = recibir_bool(mem)
                
                datos = load_data(control, dataPercentage, '4', mem)

                if mem == True:
                    data, tiempo, memoria = datos
                else: 
                    data, tiempo = datos
                infor = data['model']['data']   
                printInfo(infor)
                if mem == True:
                    print('El espacio en memoria consumido es '+ str(memoria) + ' Kb ')
                print('El tiempo de la carga de datos fue de ' + str(tiempo) + ' ms')
                
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
