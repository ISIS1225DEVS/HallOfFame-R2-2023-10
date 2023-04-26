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
import tabulate as tb
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#Llamado del Controller

def new_controller():

    control=controller.new_controller()
    
    return control

#Menu

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

##tipo de archivo

def load_data(control,file,memoria):
    """
    Carga los datos
    """
    
    if file==1:
        data = controller.load_data(control, "Data\Challenge-2\DIAN\Salida_agregados_renta_juridicos_AG-small.csv", memoria)
    elif file==2:
        data = controller.load_data(control, "Data\Challenge-2\DIAN\Salida_agregados_renta_juridicos_AG-5pct.csv",memoria)
    elif file==3:
        data = controller.load_data(control, "Data\Challenge-2\DIAN\Salida_agregados_renta_juridicos_AG-10pct.csv", memoria)
    elif file==4:
        data = controller.load_data(control, "Data\Challenge-2\DIAN\Salida_agregados_renta_juridicos_AG-20pct.csv", memoria)
    elif file==5:
        data = controller.load_data(control, "Data\Challenge-2\DIAN\Salida_agregados_renta_juridicos_AG-30pct.csv", memoria)
    elif file==6:
        data = controller.load_data(control, "Data\Challenge-2\DIAN\Salida_agregados_renta_juridicos_AG-50pct.csv", memoria)
    elif file==7:
        data = controller.load_data(control, "Data\Challenge-2\DIAN\Salida_agregados_renta_juridicos_AG-80pct.csv", memoria)
    elif file==8:
        data = controller.load_data(control, "Data\Challenge-2\DIAN\Salida_agregados_renta_juridicos_AG-large.csv", memoria)
    else:
        print("Archivo no encontrado")

    return data
    pass

def print_data(data):
    """
        Función que imprime un dato dado su ID
    """
    
    if len(data)==3:
        tiempo, memoria, respuesta=data
        listamenores,listamayores=respuesta
        print("Primeras 3 actividades por año")
        print("\n")
        print("\n")
        print (tb.tabulate(lt.iterator(listamenores),headers="keys",maxcolwidths=3,maxheadercolwidths=3,tablefmt="double_grid"))
        print("\n")
        print("\n")
        print("\n")
        print("ultimas 3 actividades por año")
        print("\n")
        print("\n")
        print("\n")
        print (tb.tabulate(lt.iterator(listamayores),headers="keys",maxcolwidths=3,maxheadercolwidths=3,tablefmt="double_grid"))
    
        print("Tiempo [ms]: ", f"{tiempo:.2f}","||",
              "Memoria [kB]: ", f"{memoria:.2f}") 
        
    else:
        tiempo,respuesta=data 
        listamenores,listamayores,=respuesta
        print("Primeras 3 actividades por año")
        print("\n")
        print("\n")
        print (tb.tabulate(lt.iterator(listamenores),headers="keys",maxcolwidths=5,maxheadercolwidths=5,tablefmt="double_grid"))
        print("\n")
        print("\n")
        print("\n")
        print("ultimas 3 actividades por año")
        print("\n")
        print("\n")
        print("\n")
        print (tb.tabulate(lt.iterator(listamayores),headers="keys",maxcolwidths=5,maxheadercolwidths=5,tablefmt="double_grid"))
    
    
        print("Tiempo [ms]: ", f"{tiempo:.2f}")
        
    #TODO: Realizar la función para imprimir un elemento
    pass

##Funciones de impresión requerimientos

def print_req_1(control,año,codigose,memoria):
    retorno=controller.req_1(control,año,codigose,memoria)
    if len(retorno)==3:
        respuesta,tiempo,memoria=retorno
        tabla=[["codigo actividad economica","nombre actividad economica","codigo subsector economico",
                "nombre subsector economico","saldo a pagar","saldo a favor","total costos gastos","total ingresos netos"],
                [respuesta["codigo actividad economica"],respuesta["nombre actividad economica"],
                respuesta["codigo subsector economico"], respuesta["nombre subsector economico"],
                respuesta["saldo a pagar"], respuesta["saldo a favor"],respuesta["total costos gastos"], respuesta["total ingresos netos"]]]
    
        print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
        
    
        print("Tiempo [ms]: ", f"{tiempo:.2f}","Memoria [kB]: ", f"{memoria:.2f}")
        
    else:
        respuesta,tiempo=retorno
        tabla=[["codigo actividad economica","nombre actividad economica","codigo subsector economico",
                "nombre subsector economico","saldo a pagar","saldo a favor","total costos gastos","total ingresos netos"],
                [respuesta["codigo actividad economica"],respuesta["nombre actividad economica"],
                respuesta["codigo subsector economico"], respuesta["nombre subsector economico"],
                respuesta["saldo a pagar"], respuesta["saldo a favor"],respuesta["total costos gastos"], respuesta["total ingresos netos"]]]
    
        print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
        print("Tiempo [ms]: ", f"{tiempo:.2f}","Memoria [kB]: ", f"{memoria:.2f}")

def print_req_2(control,año,codigose,memory):
    retorno=controller.req_2(control,año,codigose,memory)
    if len(retorno)==3:
        respuesta,tiempo,memoria=retorno
        tabla=[["codigo actividad economica","nombre actividad economica","codigo subsector economico",
                "nombre subsector economico","saldo a pagar","saldo a favor","total costos gastos","total ingresos netos"],
                [respuesta["codigo actividad economica"],respuesta["nombre actividad economica"],
                respuesta["codigo subsector economico"], respuesta["nombre subsector economico"],
                respuesta["saldo a pagar"], respuesta["saldo a favor"],respuesta["total costos gastos"], respuesta["total ingresos netos"]]]
    
        print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
        
        print("Tiempo [ms]: ", f"{tiempo:.2f}","Memoria [kB]: ", f"{memoria:.2f}")
    
    else:   
        respuesta,tiempo=retorno
        tabla=[["codigo actividad economica","nombre actividad economica","codigo subsector economico",
                "nombre subsector economico","saldo a pagar","saldo a favor","total costos gastos","total ingresos netos"],
                [respuesta["codigo actividad economica"],respuesta["nombre actividad economica"],
                respuesta["codigo subsector economico"], respuesta["nombre subsector economico"],
                respuesta["saldo a pagar"], respuesta["saldo a favor"],respuesta["total costos gastos"], respuesta["total ingresos netos"]]]
    
        print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
        
        print("Tiempo [ms]: ", f"{tiempo:.2f}")

def print_req_3(control,año,memory):
    retorno=controller.req_3(control,año,memory)    
    Req3=retorno[0]
    SubSec=Req3[0]
    ActEcoMa=Req3[1]
    ActEcoMe=Req3[2]
    Time=retorno[1]
    Memo=None
    print("Subsector económico con el menor total de retenciones en ", año,"\n")
    print(tb.tabulate(lt.iterator(SubSec),headers="keys",maxcolwidths=10,maxheadercolwidths=10, tablefmt="double_grid"))
    if len(retorno)==3:
        Memo=retorno[2]
        if ActEcoMe:
            print("3 actividades económicas que más aportaron: ")
            print(tb.tabulate(lt.iterator(ActEcoMa),headers="keys",maxcolwidths=10, maxheadercolwidths=10, tablefmt="double_grid"))
            print("3 actividades que menos aportaron: ")
            print(tb.tabulate(lt.iterator(ActEcoMe),headers="keys",maxcolwidths=10, maxheadercolwidths=10, tablefmt="double_grid"))
        else:
            Tam=lt.size(ActEcoMa)
            print("Hay solamente ",Tam," actividades económicas en este subsector")
            print(tb.tabulate(lt.iterator(ActEcoMa),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        print("Tiempo [ms]: ", f"{Time:.2f}","Memoria [kB]: ", f"{Memo:.2f}")
    else:
        if ActEcoMe:
            print("3 actividades económicas que más aportaron: ")
            print(tb.tabulate(lt.iterator(ActEcoMa),headers="keys",maxcolwidths=10, maxheadercolwidths=10, tablefmt="double_grid"))
            print("3 actividades que menos aportaron: ")
            print(tb.tabulate(lt.iterator(ActEcoMe),headers="keys",maxcolwidths=10, maxheadercolwidths=10, tablefmt="double_grid"))
        else:
            Tam=lt.size(ActEcoMa)
            print("Hay solamente ",Tam," actividades económicas en este subsector")
            print(tb.tabulate(lt.iterator(ActEcoMa),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        print("Tiempo [ms]: ", f"{Time:.2f}")

def print_req_4(control,año,memory):
    retorno=controller.req_4(control,año,memory)
    if len(retorno)==3:
        respuesta,tiempo,memoria=retorno
        if len(respuesta)==3:
            
            subsector,actividadmaxima,actividadminima=respuesta
            tabla=["codigo sector economico","nombre sector economico","codigo subsector economico","nombre subsector economico","total costos y gastos nomina",
                "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor"],[subsector["codigo sector economico"],subsector["nombre sector economico"],
                    subsector["codigo subsector economico"],subsector["nombre subsector economico"],subsector["suma costos y gastos nomina"],
                    subsector["suma ingresos netos"], subsector["suma costos y gastos"],subsector["suma saldo por pagar"],
                    subsector["suma saldo a favor"]]
        
    
            print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            print("las tres actividades economicas que menos aportaron son: ")
            print(tb.tabulate(lt.iterator(actividadmaxima),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            print("las tres actividades economicas que más aportaron son: ")
            print(tb.tabulate(lt.iterator(actividadminima),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            
            print("Tiempo [ms]: ", f"{tiempo:.2f}","Memoria [kB]: ", f"{memoria:.2f}")
        else:
           subsector,actividades=respuesta 
           tabla=["codigo sector economico","nombre sector economico","codigo subsector economico","nombre subsector economico","total costos y gastos nomina",
                "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor"],[subsector["codigo sector economico"],subsector["nombre sector economico"],
                    subsector["codigo subsector economico"],subsector["nombre subsector economico"],subsector["suma costos y gastos nomina"],
                    subsector["suma ingresos netos"], subsector["suma costos y gastos"],subsector["suma saldo por pagar"],
                    subsector["suma saldo a favor"]]
           print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
           print("las actividades economicas de este subsector son:")
           print(tb.tabulate(lt.iterator(actividadminima),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            
           print("Tiempo [ms]: ", f"{tiempo:.2f}","Memoria [kB]: ", f"{memoria:.2f}")
               
    else:
        respuesta,tiempo=retorno
        if len(respuesta)==3:
            subsector,actividadmaxima,actividadminima=respuesta
            tabla=["codigo sector economico","nombre sector economico","codigo subsector economico","nombre subsector economico","total costos y gastos nomina",
                "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor"],[subsector["codigo sector economico"],subsector["nombre sector economico"],
                    subsector["codigo subsector economico"],subsector["nombre subsector economico"],subsector["suma costos y gastos nomina"],
                    subsector["suma ingresos netos"], subsector["suma costos y gastos"],subsector["suma saldo por pagar"],
                    subsector["suma saldo a favor"]]
            
        
            print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            print("Las tres actividades económicas que menos aportaron al subsector son:")
            print(tb.tabulate(lt.iterator(actividadmaxima),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            print("Las tres actividades económicas que más aportaron al subsector son:")
            print(tb.tabulate(lt.iterator(actividadminima),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            print("Tiempo [ms]: ", f"{tiempo:.2f}")
        else:
            subsector,actividades=respuesta 
            tabla=["codigo sector economico","nombre sector economico","codigo subsector economico","nombre subsector economico","total costos y gastos nomina",
                "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor"],[subsector["codigo sector economico"],subsector["nombre sector economico"],
                    subsector["codigo subsector economico"],subsector["nombre subsector economico"],subsector["suma costos y gastos nomina"],
                    subsector["suma ingresos netos"], subsector["suma costos y gastos"],subsector["suma saldo por pagar"],
                    subsector["suma saldo a favor"]]
            print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            print("las actividades económicas de este subsector son:")
            print(tb.tabulate(lt.iterator(actividades),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
            print("Tiempo [ms]: ", f"{tiempo:.2f}")

def print_req_5(control,año,memoria):
    retorno=controller.req_5(control, año, memoria)
    if len(retorno)==3:
        respuesta, tiempo,memoria=retorno
        subsector,mayores,menores=respuesta
        print("Subsector económico con mayor descuentos tributarios en ", año,"\n")
        print(tb.tabulate(lt.iterator(subsector),headers="keys",maxcolwidths=10,maxheadercolwidths=10, tablefmt="double_grid"))
    
        if menores:
            print("3 actividades económicas que más aportaron: ")
            print(tb.tabulate(lt.iterator(mayores),headers="keys",maxcolwidths=10, maxheadercolwidths=10, tablefmt="double_grid"))
            print("3 actividades que menos aportaron: ")
            print(tb.tabulate(lt.iterator(menores),headers="keys",maxcolwidths=10, maxheadercolwidths=10, tablefmt="double_grid"))
   
        else:
            print("Hay menos de 6 actividades económicas en este subsector")
            print(tb.tabulate(lt.iterator(mayores),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        print("Tiempo [ms]: ", f"{tiempo:.2f}", "| Memoria [kB]: ", memoria)
        
    else:
        respuesta, tiempo=retorno
        subsector,mayores,menores=respuesta
        print("Subsector económico con mayor descuentos tributarios en ", año,"\n")
        print(tb.tabulate(lt.iterator(subsector),headers="keys",maxcolwidths=10,maxheadercolwidths=10, tablefmt="double_grid"))
    
        if menores:
            print("3 actividades económicas que más aportaron: ")
            print(tb.tabulate(lt.iterator(mayores),headers="keys",maxcolwidths=10, maxheadercolwidths=10, tablefmt="double_grid"))
            print("3 actividades que menos aportaron: ")
            print(tb.tabulate(lt.iterator(menores),headers="keys",maxcolwidths=10, maxheadercolwidths=10, tablefmt="double_grid"))
   
        else:
            print("Hay menos de 6 actividades económicas en este subsector")
            print(tb.tabulate(lt.iterator(mayores),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        
        print("Tiempo [ms]: ", f"{tiempo:.2f}") 
    
def print_req_6(control,año,memoria):
    retorno=controller.req_6(control,año,memoria)
    if len(retorno)==3:
        respuesta,tiempo,memoria=controller.req_6(control,año,memoria)
        sector,subsectormayor,subsectormenor,actividadmasaporte, actividadmenosaporte, actividadesmasaporte1,actividadesmenosaporte1=respuesta
        tabla=["codigo sector economico","nombre sector economico",
            "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor",
            "subsector que mas aportó","subsector que menos aportó"],[sector["codigo sector economico"],sector["nombre sector economico"],
                sector["suma ingresos netos"], sector["suma costos y gastos"],sector["suma saldo por pagar"],
                sector["suma saldo a favor"],sector["subsector que más aporto"],sector["subsector que menos aporto"]]
        
        print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        
        print("subsector que más aportó")
        tabla1=["codigo subsector economico","nombre subsector economico",
            "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor"],[subsectormayor["codigo subsector economico"],subsectormayor["nombre subsector economico"],
                subsectormayor["suma ingresos netos"], subsectormayor["suma costos gastos"],subsectormayor["suma saldo por pagar"],
                subsectormayor["suma saldo a favor"]]
            
        print(tb.tabulate(tabla1,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        tabla1_1=["codigo actividad economica",
                     "nombre actividad economica",
                     "total ingresos netos",
                     "total costos y gastos",
                     "total saldo a favor",
                     "total saldo a pagar"],[
                     actividadmenosaporte["codigo actividad economica"],
                     actividadmenosaporte["nombre actividad economica"],
                     actividadmenosaporte["total ingresos netos"],
                     actividadmenosaporte["total costos y gastos"],
                     actividadmenosaporte["total saldo a favor"],
                     actividadmenosaporte["total saldo a pagar"]]
        
        tabla1_2=["codigo actividad economica",
                     "nombre actividad economica",
                     "total ingresos netos",
                     "total costos y gastos",
                     "total saldo a favor",
                     "total saldo a pagar"],[
                     actividadmasaporte["codigo actividad economica"],
                     actividadmasaporte["nombre actividad economica"],
                     actividadmasaporte["total ingresos netos"],
                     actividadmasaporte["total costos y gastos"],
                     actividadmasaporte["total saldo a favor"],
                     actividadmasaporte["total saldo a pagar"]]
        
        print("actividades que menos y mas aportaron al subsector mayor")
        
        print(tb.tabulate(tabla1_1,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))
        print(tb.tabulate(tabla1_2,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))

        print("subsector que menos aporto")
        
        tabla2=["codigo subsector economico","nombre subsector economico",
            "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor"],[subsectormenor["codigo subsector economico"],subsectormenor["nombre subsector economico"],
                subsectormenor["suma ingresos netos"], subsectormenor["suma costos gastos"],subsectormenor["suma saldo por pagar"],
                subsectormenor["suma saldo a favor"]]
        
        print(tb.tabulate(tabla2,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))
        tabla2_1=["codigo actividad economica",
                     "nombre actividad economica",
                     "total ingresos netos",
                     "total costos y gastos",
                     "total saldo a favor",
                     "total saldo a pagar"],[actividadesmenosaporte1["codigo actividad economica"],
                     actividadesmenosaporte1["nombre actividad economica"],
                     actividadesmenosaporte1["total ingresos netos"],
                     actividadesmenosaporte1["total costos y gastos"],
                     actividadesmenosaporte1["total saldo a favor"],
                     actividadesmenosaporte1["total saldo a pagar"]]
        
        tabla2_2=["codigo actividad economica",
                     "nombre actividad economica",
                     "total ingresos netos",
                     "total costos y gastos",
                     "total saldo a favor",
                     "total saldo a pagar"],[
                    actividadesmasaporte1["codigo actividad economica"],
                     actividadesmasaporte1["nombre actividad economica"],
                     actividadesmasaporte1["total ingresos netos"],
                     actividadesmasaporte1["total costos y gastos"],
                     actividadesmasaporte1["total saldo a favor"],
                     actividadesmasaporte1["total saldo a pagar"]]
        

        print("actividades que menos y mas aportaron al subsector menor")
        print(tb.tabulate(tabla2_1,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))
        print(tb.tabulate(tabla2_2,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))
    
        print("Tiempo [ms]: ", f"{tiempo:.2f}","Memoria [kB]: ", f"{memoria:.2f}")
        
    else:
        respuesta,tiempo=controller.req_6(control,año,memoria)
        sector,subsectormayor,subsectormenor,actividadmasaporte, actividadmenosaporte, actividadesmasaporte1,actividadesmenosaporte1=respuesta
        tabla=["codigo sector economico","nombre sector economico",
            "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor",
            "subsector que mas aportó","subsector que menos aportó"],[sector["codigo sector economico"],sector["nombre sector economico"],
                sector["suma ingresos netos"], sector["suma costos y gastos"],sector["suma saldo por pagar"],
                sector["suma saldo a favor"],sector["subsector que más aporto"],sector["subsector que menos aporto"]]
        
        print(tb.tabulate(tabla,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        
        print("subsector que más aportó")
        tabla1=["codigo subsector economico","nombre subsector economico",
            "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor"],[subsectormayor["codigo subsector economico"],subsectormayor["nombre subsector economico"],
                subsectormayor["suma ingresos netos"], subsectormayor["suma costos gastos"],subsectormayor["suma saldo por pagar"],
                subsectormayor["suma saldo a favor"]]
            
        print(tb.tabulate(tabla1,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        
        print("actividades que menos y mas aportaron al subsector mayor")
        
        tabla1_1=["codigo actividad economica",
                     "nombre actividad economica",
                     "total ingresos netos",
                     "total costos y gastos",
                     "total saldo a favor",
                     "total saldo a pagar"],[
                     actividadmenosaporte["codigo actividad economica"],
                     actividadmenosaporte["nombre actividad economica"],
                     actividadmenosaporte["total ingresos netos"],
                     actividadmenosaporte["total costos y gastos"],
                     actividadmenosaporte["total saldo a favor"],
                     actividadmenosaporte["total saldo a pagar"]]
        
        tabla1_2=["codigo actividad economica",
                     "nombre actividad economica",
                     "total ingresos netos",
                     "total costos y gastos",
                     "total saldo a favor",
                     "total saldo a pagar"], [
                     actividadmasaporte["codigo actividad economica"],
                     actividadmasaporte["nombre actividad economica"],
                     actividadmasaporte["total ingresos netos"],
                     actividadmasaporte["total costos y gastos"],
                     actividadmasaporte["total saldo a favor"],
                     actividadmasaporte["total saldo a pagar"]]
        
        print(tb.tabulate(tabla1_1,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))
        print(tb.tabulate(tabla1_2,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))
        

        print("subsector que menos aporto")
        
        tabla2=["codigo subsector economico","nombre subsector economico",
            "Total ingresos netos","Total costos y gastos","Total saldo por pagar","total saldo a favor"],[subsectormenor["codigo subsector economico"],subsectormenor["nombre subsector economico"],
                subsectormenor["suma ingresos netos"], subsectormenor["suma costos gastos"],subsectormenor["suma saldo por pagar"],
                subsectormenor["suma saldo a favor"],]
        
        print(tb.tabulate(tabla2,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
        
        tabla2_1=["codigo actividad economica",
                     "nombre actividad economica",
                     "total ingresos netos",
                     "total costos y gastos",
                     "total saldo a favor",
                     "total saldo a pagar"],[
                     actividadesmenosaporte1["codigo actividad economica"],
                     actividadesmenosaporte1["nombre actividad economica"],
                     actividadesmenosaporte1["total ingresos netos"],
                     actividadesmenosaporte1["total costos y gastos"],
                     actividadesmenosaporte1["total saldo a favor"],
                     actividadesmenosaporte1["total saldo a pagar"]]
        
        tabla2_2=["codigo actividad economica",
                     "nombre actividad economica",
                     "total ingresos netos",
                     "total costos y gastos",
                     "total saldo a favor",
                     "total saldo a pagar"],[
                     actividadesmasaporte1["codigo actividad economica"],
                     actividadesmasaporte1["nombre actividad economica"],
                     actividadesmasaporte1["total ingresos netos"],
                     actividadesmasaporte1["total costos y gastos"],
                     actividadesmasaporte1["total saldo a favor"],
                     actividadesmasaporte1["total saldo a pagar"]]

        print("actividades que menos y mas aportaron al subsector menor")
        print(tb.tabulate(tabla2_1,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))
        print(tb.tabulate(tabla2_2,headers="firstrow",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid",showindex=False))
    
        print("Tiempo [ms]: ", f"{tiempo:.2f}")
    
def print_req_7(control,año,codigose,Topn,memory):
    respuesta=controller.req_7(control,año,codigose,Topn,memory)
    if len(respuesta)==3:
            lista,tiempo,memoria=respuesta  
            if lista==None:
                print("opcion no valida digite otro numero porfavor")  
            else:            
                print(tb.tabulate(lt.iterator(lista),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid"))
             
                print("Tiempo [ms]: ", f"{tiempo:.2f}","Memoria [kB]: ", f"{memoria:.2f}")  
    else:   
        lista,tiempo=respuesta   
        if lista==None:    
            print("opcion no valida digite otro numero porfavor")
        else:        
            print(tb.tabulate(lt.iterator(lista),headers="keys",maxcolwidths=10,maxheadercolwidths=10,tablefmt="double_grid")) 
            print("Tiempo [ms]: ", f"{tiempo:.2f}")

def print_req_8(control,año,Topn,memoria):
    retorno=controller.req_8(control,año,Topn,memoria)
    if len(retorno)==3:
            listas,tiempo,memoria=retorno
            listasubsectores,listactividades=listas
            print(tb.tabulate(lt.iterator(listasubsectores),headers="keys",maxcolwidths=5,maxheadercolwidths=8,tablefmt="double_grid"))
            print(tb.tabulate(lt.iterator(listactividades),headers="keys",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
            print("Tiempo [ms]: ", f"{tiempo:.2f}","Memoria [kB]: ", f"{memoria:.2f}")  
    else:
        listas,tiempo=retorno
        listasubsectores,listactividades=listas
        
        print(tb.tabulate(lt.iterator(listasubsectores),headers="keys",maxcolwidths=5,maxheadercolwidths=8,tablefmt="double_grid"))
        tabla=tb.tabulate(lt.iterator(listactividades),headers="keys",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid")
        print(tabla)
        print("Tiempo [ms]: ", f"{tiempo:.2f}")
 
# Booleneador 3000
        
def castBoolean(value):
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False

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
               
                print("¿Quiere medir memoria? True/False")
                memoria= castBoolean(input("Respuesta: "))
                                
                print("Ingrese el archivo que quiere cargar")
                print("1- Small")
                print("2- 5%")
                print("3- 10%")
                print("4- 20%")
                print("5- 30%")
                print("6- 50%")
                print("7- 80%")
                print("8- 100%")
                file=int(input("Ingrese el número correspondiente\n"))
                control=new_controller()
                print("Cargando información de los archivos ....\n")
                data = load_data(control,file, memoria)
                
                print_data(data)
                
                
            elif int(inputs) == 2:
                año=input("ingrese año de interes:\n")
                codigose=input("ingrese codigo de sector economico:\n")
                print("¿Quiere medir memoria? True/False")
                memoria= castBoolean(input("Respuesta: "))
                print_req_1(control,año,codigose,memoria)

            elif int(inputs) == 3:
                año=input("ingrese año de interes:\n")
                codigose=input("ingrese codigo de sector economico:\n")
                print("¿Quiere medir memoria? True/False")
                memoria= castBoolean(input("Respuesta: "))
                print_req_2(control,año,codigose,memoria)
                

            elif int(inputs) == 4:
                año=input("ingrese año de interes:\n")
                print("¿Quiere medir memoria? True/False")
                memoria= castBoolean(input("Respuesta: "))
                print_req_3(control,año,memoria)
                

            elif int(inputs) == 5:
                print("¿Quiere medir memoria? True/False")
                memoria= castBoolean(input("Respuesta: "))
                año=input("ingrese año de interes:\n")
                print_req_4(control,año,memoria)
                
            elif int(inputs) == 6:
                año=input("Ingrese el año a buscar:\n")
                print("¿Quiere medir memoria? T/F")
                memoria=castBoolean(input("Respuesta: "))
                print_req_5(control,año,memoria)

            elif int(inputs) == 7:
                año=input("ingrese año de interes:\n")
                print("¿Quiere medir memoria? True/False")
                memoria= castBoolean(input("Respuesta: "))
                print_req_6(control,año,memoria)

            elif int(inputs) == 8:
                
                año=input("ingrese año de interes:\n")
                Topn=input("ingrese numero Top N:\n")
                codigose=input("ingrese el codigo del subsector que desea revisar:\n")
                print("¿Quiere medir memoria? True/False")
                memoria= castBoolean(input("Respuesta: "))
                print_req_7(control,año,codigose,Topn,memoria)

            elif int(inputs) == 9:
                año=input("ingrese año de interes:\n")
                Topn=input("ingrese numero Top N:\n")
                print("¿Quiere medir memoria? True/False")
                memoria= castBoolean(input("Respuesta: "))
                print_req_8(control,año,Topn,memoria)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)