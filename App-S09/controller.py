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
 """

import config as cf
import csv
import time
import model
import tracemalloc
assert cf

'''
   ╒═══════════════════════════════════════════════════════════════════════════════════════════════════╕
   │ .                                                                                               . │
   │ .                El controlador se encarga de mediar entre la vista y el modelo.                . │
   │ .                                                                                               . │
   ╘═══════════════════════════════════════════════════════════════════════════════════════════════════╛
'''
#╒════════════════════════════ Instancia al modelo ═══════════════════════════╕

def new_controller(mp_type):
    """
    Crea una instancia del modelo
    """
    control = {'model': model.newCatalog(mp_type)}
    return control

#╘════════════════════════════════════════════════════════════════════════════╛


# ======================================== CARGA DE DATOS ==========================================

def load_data(control, FS='small', memflag=False, path='./Data/Dian/Salida_agregados_renta_juridicos_AG-{0}.csv')->int:
    """
    Lee la información de todo el archivo CSV y la ordena en el catálogo contenido en control['model'].
    Retorna el número total de datos cargados
    """
    
    # Toma el tiempo al inicio del proceso
    start_time = get_time()
    
    if memflag:
        # Inicializa el proceso para medir memoria
        tracemalloc.start()
        start_memory = get_memory()
    
    registros = 0
    path = path.format(FS)
    # --------------------------------------- Lectura de la base de datos CSV ----------------------------------------
    with open(path, 'r', encoding='utf8') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        header = next(reader)
        indices = [0,  # Año
                   1,  # Código actividad económica
                   2,  # Nombre actividad económica
                   3,  # Código sector económico
                   4,  # Nombre sector económico
                   5,  # Código subsector económico
                   6,  # Nombre subsector económico
                   7,  # Costos y gastos nómina
                   25, # Total ingresos netos
                   31, # Total costos y gastos
                   45, # Descuentos tributarios
                   48, # Total Impuesto a cargo
                   53, # Total retenciones
                   57, # Total saldo a pagar
                   58  # Total saldo a favor
                   ] # Aquí están los índices de las columnas que nos interesa leer en realidad (15 de 59 hasta ahora)
        keys = [header[i] for i in indices] # Aquí estarán los nombres de dichas columnas...
        for row in reader:
            model.readRow(control['model'], row, indices, keys)
            registros += 1
    # ----------------------------------------------------------------------------------------------------------------
    # Toma el tiempo al final del proceso
    # y calcula la diferencia en tiempo
    stop_time = get_time()
    time = delta_time(start_time, stop_time)
    
    if memflag:
        # Finaliza el proceso para medir memoria
        stop_memory = get_memory()
        tracemalloc.stop()
        # Calcula la diferencia de memoria
        memory = delta_memory(stop_memory, start_memory)
        # Respuesta con los datos de tiempo y memoria
        return registros, time, memory
    else:
        # Respuesta sin medir memoria
        return registros, time

# ==================================================================================================
# ===================================== INICIO REQUERIMIENTOS ======================================

def req_1_2(control, anio, cod_sec, monto):
    """
    Retorna el resultado de los requerimientos 1 y 2
    """
    # Toma el tiempo al inicio del proceso
    start_time = get_time()
    retorno = model.req_1_2(control['model'], anio, cod_sec, monto)
    # Toma el tiempo al final del proceso
    # y calcula la diferencia en tiempo
    stop_time = get_time()
    time = delta_time(start_time, stop_time)
    return retorno, time

def req_3(control, year: int):
    """
    Retorna el resultado del requerimiento 3
    """
    # Toma el tiempo al inicio del proceso
    start_time = get_time()
    retorno = model.req_3_4_5(control['model'], year, 3)
    # Toma el tiempo al final del proceso
    # y calcula la diferencia en tiempo
    stop_time = get_time()
    time = delta_time(start_time, stop_time)
    return retorno, time
    

def req_4(control, year:int):
    """
    Retorna el resultado del requerimiento 4
    """
    # Toma el tiempo al inicio del proceso
    start_time = get_time()
    retorno = model.req_3_4_5(control['model'], year, 4)
    # Toma el tiempo al final del proceso
    # y calcula la diferencia en tiempo
    stop_time = get_time()
    time = delta_time(start_time, stop_time)
    return retorno, time

def req_5(control, year:int):
    """
    Retorna el resultado del requerimiento 5
    """
    # Toma el tiempo al inicio del proceso
    start_time = get_time()
    retorno = model.req_3_4_5(control['model'], year, 5)
    # Toma el tiempo al final del proceso
    # y calcula la diferencia en tiempo
    stop_time = get_time()
    time = delta_time(start_time, stop_time)
    return retorno, time

def req_6(control, year):
    """
    Retorna el resultado del requerimiento 6
    """
    # Toma el tiempo al inicio del proceso
    start_time = get_time()
    retorno = model.req_6(control['model'], year)
    # Toma el tiempo al final del proceso
    # y calcula la diferencia en tiempo
    stop_time = get_time()
    time = delta_time(start_time, stop_time)
    return retorno, time

def req_7(control, year:int, cantidad:int, cod_sub):
    """
    Retorna el resultado del requerimiento 7
    """
    # Toma el tiempo al inicio del proceso
    start_time = get_time()
    retorno = model.req_7(control["model"], year, cantidad, cod_sub)
    # Toma el tiempo al final del proceso
    # y calcula la diferencia en tiempo
    stop_time = get_time()
    time = delta_time(start_time, stop_time)
    return retorno, time

def req_8(control, year:int):
    """
    Retorna el resultado del requerimiento 8
    """
    # Toma el tiempo al inicio del proceso
    start_time = get_time()
    subslists, num = model.req_8(control['model'], year)
    # Toma el tiempo al final del proceso
    # y calcula la diferencia en tiempo
    stop_time = get_time()
    time = delta_time(start_time, stop_time)
    return subslists, num, time

# ==================================================================================================

# ========================================= MEDICIONES =============================================
# ------------------------- TIEMPO
def get_time():
    """
    Devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def delta_time(start, end):
    """
    Devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
# ------------------------- MEMORIA
def get_memory():
    """
    Toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()

def delta_memory(stop_memory, start_memory):
    """
    Calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

# ==================================================================================================

# ======================================== OTROS ÚTILES ============================================
# ------------------------- Funciones secundarias y auxiliares -------------------------
def getFirstnLast(tad_lst,sample=3):
    """
    Retorna una tupla con dos TAD list:
    Las primeras 3 y
    Las últimas 3
    Actividades de un TAD list más grande.
    """
    return model.first_and_last(tad_lst, sample)

def joinFirstnLast(first, last):
    """
    Fusiona dos TADs en un solo ARRAY
    """
    return model.join_first_and_last(first, last)

# ------------------ Funciones para la impresión de la carga de datos ------------------ 
def getYears(control:dict):
    """
    Retorda un TAD list con todos los años del registro.
    """
    return model.getSortedYears(control['model'])

def getActivities(control, year):
    """
    Retorna un TAD list con todas las actividades de un año.
    """
    return model.getActsFromYear(control['model'], year)

# ---------------------- Funciones utilizadas por el view ------------------------------
def columns(req:int, sub=1):
    """
    En esta función están centralizadas las columnas
    que nos interesa imprimir en el view.
    """
    rta = None
    if req == 0:
        rta = ('Año',
               'Código actividad económica','Nombre actividad económica',
               'Código sector económico','Nombre sector económico',
               'Código subsector económico','Nombre subsector económico',
               'Total ingresos netos','Total costos y gastos',
               'Total saldo a pagar','Total saldo a favor')
        # Aquí están los nombres de las columnas que nos 
        # interesa imprimir en la CARGA DE DATOS
    elif req in [1, 2]:
        rta = ('Código actividad económica','Nombre actividad económica',
               'Código subsector económico','Nombre subsector económico',
               'Total ingresos netos','Total costos y gastos',
               'Total saldo a pagar','Total saldo a favor')  
        # Aquí están los nombres de las columnas que nos 
        # interesa imprimir en los REQUERIMIENTOS 1 Y 2 
    elif req in [3, 4, 5]:
        columna = None
        if req == 3: columna = 'Total retenciones'
        elif req == 4: columna = 'Costos y gastos nómina'
        else: columna = 'Descuentos tributarios'
        if sub == 1 and (req == 4 or req == 5):
            rta = ('Código sector económico','Nombre sector económico',
                   'Código subsector económico','Nombre subsector económico',
                   f'Total {columna.lower()} del subsector económico', 
                   'Total ingresos netos del subsector económico','Total costos y gastos del subsector económico',
                   'Total saldo a pagar del subsector económico','Total saldo a favor del subsector económico')
        elif sub == 1 and req == 3:
            rta = ('Código sector económico','Nombre sector económico',
                   'Código subsector económico','Nombre subsector económico',
                   f'{columna} del subsector económico', 
                   'Total ingresos netos del subsector económico','Total costos y gastos del subsector económico',
                   'Total saldo a pagar del subsector económico','Total saldo a favor del subsector económico')
        else:
            rta = ('Código actividad económica','Nombre actividad económica',
                   columna, 
                   'Total ingresos netos','Total costos y gastos',
                   'Total saldo a pagar','Total saldo a favor')
    elif req==7:
        rta= ('Código actividad económica','Nombre actividad económica','Código sector económico',
              'Nombre sector económico','Total costos y gastos','Total ingresos netos',
             'Total saldo a pagar','Total saldo a favor')

    elif req == 8:
        if sub == 1:
            rta = ('Código sector económico','Nombre sector económico',
                   'Código subsector económico','Nombre subsector económico',
                   'Total de impuestos a cargo para el subsector',
                   'Total ingresos netos para el subsector','Total costos y gastos para el subsector',
                   'Total saldo a pagar para el subsector','Total saldo a favor para el subsector')
        else:
            rta = ('Código actividad económica','Nombre actividad económica',
                   'Total Impuesto a cargo', 
                   'Total ingresos netos','Total costos y gastos',
                   'Total saldo a pagar','Total saldo a favor')
    return rta

def condicionesFormat(v):
    """
    Determina si el valor de una columna
    debe formatearse o no.
    """
    c1 = ('Año'not in v)
    c2 = ('Código' not in v)
    c3 = ('Nombre' not in v)
    c4 = ('Periodo'not in v)
    c5 = ('aportó'not in v)
    return (c1 and c2 and c3 and c4 and c5)


# ===============
# PRUEBAS DE TIEMPO Y MEMORIA



def pruebas_de_tiempo(numero:int, structure:str):
    cantidad_para_promedio = numero
    columnas = ['Sufijo', 'Tamaño (#)','Carga [ms]', 'Req 1 [ms]', 'Req 2 [ms]', 'Req 3 [ms]', 'Req 4 [ms]', 'Req 5 [ms]', 'Req 6 [ms]', 'Req 7 [ms]', 'Req 8 [ms]']
    filas = ['small','5pct','10pct','20pct','30pct','50pct','80pct','large']
    tabla_de_resultados = [columnas]
    archivos_leidos = 0
    #---- Variables de ingreso a los reqs ----
    anho = 2021
    sector = 3     # Puse este sector porque es en el que existe más informacion para cada año... Tiene 150 actividades.
    subsector = 3  # Lo mismo para este subsector, pues todas las 150 actividades están en ese.
    top = 10
    #------------------------------------------
    for sufijo in filas:
        sumas_de_tiempos = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} 
        # Aquí están los números de cada opción en el menú (excepto el 0 que corrsponde a la opción 'salir')
        # Los valores de este diccionario se restablecen para cada sufijo
        registros = None
        for _ in range(cantidad_para_promedio): 
            # Debe hacerse todo el proceso (incluyendo la creación del control y también la carga)
            # tantas veces como el número de iteraciones para el promedio.
            control = new_controller(structure) # Se crea el control
            registros, tiempo_carga = load_data(control, sufijo) # Se cargan los datos
            sumas_de_tiempos[1] += tiempo_carga # Se suma el tiempo de la carga de datos en su llave correspondiente
            for option in range(2, 10): # El rango es de 2 a 9 ya que el 1 corresponde a la carga de datos
                if option == 2: resultados = req_1_2(control, anho, sector, 'Total saldo a pagar')
                elif option == 3: resultados = req_1_2(control, anho, sector, 'Total saldo a favor')
                elif option == 4: resultados = req_3(control, anho)
                elif option == 5: resultados = req_4(control, anho)
                elif option == 6: resultados = req_5(control, anho)
                elif option == 7: resultados = req_6(control, anho)
                elif option == 8: resultados = req_7(control, anho, top, subsector)
                elif option == 9: resultados = req_8(control, anho)

                tiempo_req = resultados[1] if option != 9 else resultados[2] # Sólo la opción 9 (req 8) tiene el tiempo en el índice 2 del resultado.
                
                sumas_de_tiempos[option] += tiempo_req # Se suma en el diccionario de los tiempos el tiempo del requerimiento correspondiente
                pass # Se acaba el ciclo de los resultados de cada requerimiento
        pass # Se acaba el ciclo de la suma de los tiempos
        
        # Al final, tendremos en "sumas de tiempos" las sumas totales 
        # de cada req (incluyendo la caga) para el archivo que se leyó

        # Falta llenar los resultados en la fila que corresponde al archivo que se leyó

        resultados_fila = [sufijo, registros] # la fila comienza siempre con el sufijo del archivo y la cantidad de registros correspondientes
        
        for req in range(1, 10): # Para cada requerimiento (del 1 al 9 porque se incluye la carga)
            result = (sumas_de_tiempos[req]/cantidad_para_promedio) # Se hace el promedio de tiemo que tomó
            resultados_fila.append(round(result, 2))                # Y se agrega a la fila del archivo
        tabla_de_resultados.append(resultados_fila)
        archivos_leidos += 1 
        print(f"\n\tArchivos completados:   {archivos_leidos}/8   -   {sufijo.ljust(5)} ✔")
    return tabla_de_resultados


def pruebas_de_memoria():
    
    columnas = ['\nSufijo', '\n Tamaño (#)','  Memoria ocupada por\n  el Catálogo con\n  Separate Chaining [kB]', '  Memoria ocupada por\n   el Catálogo con\n  Linear Probing [kB]']
    filas = ['small','5pct','10pct','20pct','30pct','50pct','80pct','large']
    tabla_de_resultados = [columnas]
    archivos_leidos = 0
    for sufijo in filas:
        CvsP = []
        results = None
        for structure in ['CHAINING', 'PROBING']:
            cntrlr = new_controller(structure)
            results = load_data(cntrlr, sufijo, True)
            CvsP.append(round(results[2], 2))
        resultados_fila = [sufijo, results[0], CvsP[0], CvsP[1]]
        tabla_de_resultados.append(resultados_fila)
        archivos_leidos += 1
        print(f"\n\tArchivos completados:   {archivos_leidos}/8   -   {sufijo.ljust(5)} ✔")
    return tabla_de_resultados
    