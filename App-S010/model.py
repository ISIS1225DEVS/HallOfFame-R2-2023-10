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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """



import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Contrucción estructura de datos

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog={"todo":None, 
             "2012":None,
             "2013":None,
             "2014":None,
             "2015":None,
             "2016":None,
             "2017":None,
             "2018":None,
             "2019":None,
             "2020":None,
             "2021":None}
    catalog["todo"]=lt.newList(datastructure="ARRAY_LIST")
    
    catalog["2012"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2013"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2014"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2015"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2016"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2017"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2018"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2019"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2020"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)
    
    catalog["2021"]=mp.newMap(numelements=43,
                              maptype="PROBING",
                              loadfactor=0.5)

    return catalog

# Funciones para agregar informacion al modelo

def add_data(catalog, impuesto):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    impuestoformato2=formato2(impuesto)
    
    lt.addLast(catalog["todo"],formato1(impuesto))
    add_año(catalog,impuestoformato2)
    #TODO: Crear la función para agregar elementos a una lista
    
def formato1(linea):
    linea= {"año": linea["Año"],
            "codigo actividad economica": linea["Código actividad económica"],
            "nombre actividad economica": linea["Nombre actividad económica"],
            "codigo sector economico": linea["Código sector económico"],
            "nombre sector economico": linea["Nombre sector económico"],
            "codigo subsector economico":linea["Código subsector económico"],
            "nombre subsector economico": linea["Nombre subsector económico"],
            "saldo a pagar":linea["Total saldo a pagar"],
            "saldo a favor":linea["Total saldo a favor"],
            }
    return linea

def formato2(linea):
    linea= {"año": linea["Año"],
            "codigo actividad economica": linea["Código actividad económica"],
            "nombre actividad economica": linea["Nombre actividad económica"],
            "codigo sector economico": linea["Código sector económico"],
            "nombre sector economico": linea["Nombre sector económico"],
            "codigo subsector economico":linea["Código subsector económico"],
            "nombre subsector economico": linea["Nombre subsector económico"],
            "saldo a pagar":linea["Total saldo a pagar"],
            "saldo a favor":linea["Total saldo a favor"],
            "descuentos tributarios":linea["Descuentos tributarios"],
            "total costos gastos":linea["Total costos y gastos"],
            "total costos gastos nomina":linea["Costos y gastos nómina"],
            "total retenciones":linea["Total retenciones"],
            "total ingresos netos":linea["Total ingresos netos"],
            "impuestos a cargo":linea["Total Impuesto a cargo"]
            }
    return linea

def add_año(catalog,impuesto):
    año=impuesto["año"]
    codigo=impuesto["codigo subsector economico"]
    
    
    
    if mp.contains(catalog[año],codigo):
        
    #obtención del diccionario de cada sector
        parejallave=mp.get(catalog[año],codigo)
        entradacodigo= me.getValue(parejallave)
    
    #Sumatoria descuentos tributarios
        entradacodigo["suma descuentos tributarios"]+=int(impuesto["descuentos tributarios"])
            
    #Sumatoria costos y gastos para cada subsector
        entradacodigo["suma costos y gastos"]+=int(impuesto["total costos gastos"])
        
        entradacodigo["suma costos y gastos nomina"]+=int(impuesto["total costos gastos nomina"])
           
    #Sumatoria retenciones  
        entradacodigo["suma total retenciones"]+=int(impuesto["total retenciones"])
        
        entradacodigo["suma ingresos netos"]+=int(impuesto["total ingresos netos"])
        entradacodigo["suma saldo por pagar"]+=int(impuesto["saldo a pagar"])
        
        if int(impuesto["saldo a pagar"])>int(entradacodigo["maximo saldo por pagar"]):
            entradacodigo["maximo saldo por pagar"]=impuesto["saldo a pagar"]
            entradacodigo["actividad maxima saldo por pagar"]=impuesto 
       
        entradacodigo["suma saldo a favor"]+=int(impuesto["saldo a favor"])
        if int(impuesto["saldo a favor"])>int(entradacodigo["maximo saldo a favor"]):
            entradacodigo["maximo saldo a favor"]=impuesto["saldo a favor"]
            entradacodigo["actividad maxima saldo a favor"]=impuesto
            
            
            
        entradacodigo["suma impuestos a cargo"]+=int(impuesto["impuestos a cargo"])
        
        
        
    else:
       entradacodigo=newcodigo(impuesto)
       
       mp.put(catalog[año],codigo,entradacodigo)
       
    llavevalor=mp.get(catalog[año],codigo)
    diccionariosubsector=me.getValue(llavevalor)
    lt.addLast(diccionariosubsector["actividades"],impuesto)
    
def newcodigo(impuesto):
    diccionario={"codigo sector economico":impuesto["codigo sector economico"],
                 "nombre sector economico":impuesto["nombre sector economico"],
                 "codigo subsector economico":impuesto["codigo subsector economico"],
                 "nombre subsector economico":impuesto["nombre subsector economico"],
                 "suma descuentos tributarios":int(impuesto["descuentos tributarios"]),
                 "suma costos y gastos":int(impuesto["total costos gastos"]),
                 "suma costos y gastos nomina":int(impuesto["total costos gastos nomina"]),
                 "suma total retenciones":int(impuesto["total retenciones"]),
                 "suma ingresos netos":int(impuesto["total ingresos netos"]),
                 "suma saldo por pagar":int(impuesto["saldo a pagar"]),
                 "maximo saldo por pagar":int(impuesto["saldo a pagar"]),
                 "actividad maxima saldo por pagar":impuesto,
                 "suma saldo a favor":int(impuesto["saldo a favor"]),
                 "maximo saldo a favor":int(impuesto["saldo a favor"]),
                 "actividad maxima saldo a favor":impuesto,
                 "suma impuestos a cargo":int(impuesto["impuestos a cargo"]),
                 
                 "actividades":None}
    diccionario["actividades"]=lt.newList(datastructure="ARRAY_LIST")
    
    return diccionario

# Funciones ordenamiento de datos

def primerosyultimos(catalog):
   listaaorganizar=catalog["todo"]
   se.sort(listaaorganizar,cmpaño)
   
   posicion1=1
   posicion2=0
   contador=0
   
   año=lt.getElement(listaaorganizar,1)["año"]
   
   listamayoresultima=lt.newList(datastructure="ARRAY_LIST")
   listamenoresultima=lt.newList(datastructure="ARRAY_LIST")
   
   
   
   for impuestos in lt.iterator(listaaorganizar):
      if impuestos["año"]== año:
          
          contador+=1
          if contador==lt.size(listaaorganizar)-1:
            sublistamenores=lt.subList(listaaorganizar,posicion1,3)
            
            sublistamayor=lt.subList(listaaorganizar,lt.size(listaaorganizar)-2,3)
            
            for elementos in lt.iterator(sublistamenores):
                lt.addLast(listamenoresultima,elementos)
                
            for elementos in lt.iterator(sublistamayor):
                lt.addLast(listamayoresultima,elementos)  
             
            
      else:
          año=impuestos["año"]
          
          posicion2=contador
          sublistamenores=lt.subList(listaaorganizar,posicion1,3)
          
          sublistamayor=lt.subList(listaaorganizar,posicion2-2,3)
          contador+=1
          posicion1=contador
          
          for elementos in lt.iterator(sublistamenores):
                lt.addLast(listamenoresultima,elementos)
                
          for elementos in lt.iterator(sublistamayor):
                lt.addLast(listamayoresultima,elementos)  
                
   
   return   listamenoresultima,listamayoresultima
  
def cmpaño(impuesto1,impuesto2):
    dato1=impuesto1["año"]
    dato2=impuesto2["año"]
    
    dato1_1=impuesto1["codigo actividad economica"]
    dato1_2=impuesto2["codigo actividad economica"]
    
    condicion=True
    
    if dato1!=dato2:
     condicion=dato1<dato2
    else:
        if "/"in dato1_1:
            lista1=dato1_1.split(sep="/")
        else:
            lista1=dato1_1.split(sep=" ")
            
        if "/"in dato1_2:
            
            lista2=dato1_2.split(sep="/")
            
        else:
            
            lista2=dato1_2.split(sep=" ")
            
        valor1=int(lista1[0])
        valor2=int(lista2[0])
        
        condicion=valor1<valor2
        
    return condicion     
     
# Funciones de los Requerimientos

def req_1(catalogo,año,codigose):
    """
    Función que soluciona el requerimiento 1
    """
 
    valoresaño=catalogo[año]
    listacodigose=mp.keySet(valoresaño)
    
    
    maximo=0
    respuesta=None
    for subsector in lt.iterator(listacodigose):
        llavevalor=mp.get(valoresaño,subsector)
        dicatrabajar=me.getValue(llavevalor)
        
        if codigose == dicatrabajar["codigo sector economico"]:
            if int(dicatrabajar["maximo saldo por pagar"])>maximo:
                maximo= int(dicatrabajar["maximo saldo por pagar"])
                respuesta=dicatrabajar["actividad maxima saldo por pagar"]
                
    
    entrega=respuesta.copy()
    del entrega["año"]
    del entrega["codigo sector economico"]
    del entrega["total retenciones"]
    del entrega["impuestos a cargo"]
    
    return entrega
    
def req_2(catalogo,año,codigose):
    """
    Función que soluciona el requerimiento 2
    """
    valoresaño=catalogo[año]
    listacodigose=mp.keySet(valoresaño)
   
    maximo=0
    respuesta=None
    
    for subsector in lt.iterator(listacodigose):
        llavevalor=mp.get(valoresaño,subsector)
        dicatrabajar=me.getValue(llavevalor)
        
        if codigose == dicatrabajar["codigo sector economico"]:
            if int(dicatrabajar["maximo saldo a favor"])>maximo:
                maximo= int(dicatrabajar["maximo saldo a favor"])
                respuesta=dicatrabajar["actividad maxima saldo a favor"]
            
    
    
    entrega=respuesta.copy()
    
    del entrega["año"]
    del entrega["codigo sector economico"]
    del entrega["total retenciones"]
    del entrega["impuestos a cargo"]
    
    return entrega

def req_3(catalogo,año):
    AñoEsp=catalogo[año]
    CodSec=mp.keySet(AñoEsp)
    MinRet=None
    for RecCod in lt.iterator(CodSec):
        KeyVal=mp.get(AñoEsp,RecCod)
        Values=me.getValue(KeyVal)
        ImpIni={"codigo sector economico":Values["codigo sector economico"],
                "nombre sector economico":Values["nombre sector economico"],
                "codigo subsector economico":Values["codigo subsector economico"],
                "nombre subsector economico":Values["nombre subsector economico"],
                "total retenciones":Values["suma total retenciones"],
                "suma total ingresos netos":Values["suma ingresos netos"],
                "total costos y gastos":Values["suma costos y gastos"],
                "total saldo a pagar":Values["suma saldo por pagar"],
                "total saldo a favor":Values["suma saldo a favor"],
                "actividades":Values["actividades"]}
        if MinRet==None:
            MinRet=ImpIni["total retenciones"]
            ImpFin=ImpIni
        elif ImpIni["total retenciones"]<MinRet:
            MinRet=ImpIni["total retenciones"]
            ImpFin=ImpIni
        
    ActEco=ImpFin["actividades"]
    sa.sort(ActEco,cmpTotalRet)
    
    for Del in lt.iterator(ActEco):
        del Del["año"]
        del Del["total costos gastos nomina"]
        del Del["descuentos tributarios"]
        del Del["codigo sector economico"]
        del Del["nombre sector economico"]
        del Del["codigo subsector economico"]
        del Del["nombre subsector economico"]
    ActImp=None
    ActMen=None
    Tam=lt.size(ActEco)
    if Tam<6:
        ActImp=ActEco
    else:
        ActImp=lt.subList(ActEco,1,3)
        ActMen=lt.subList(ActEco,Tam-2,3)
    del ImpFin["actividades"]     
    Imp=lt.newList("ARRAY_LIST")
    lt.addLast(Imp,ImpFin)
    return Imp,ActImp,ActMen

def req_4(catalogo,año):
    """
    Función que soluciona el requerimiento 4
    """
    añoescogido=catalogo[año]
    listasubsectores=mp.keySet(añoescogido)
    valormaximo=0
    subsectormaximo=None
    
    for subsector in lt.iterator(listasubsectores):
        llavevalor=mp.get(añoescogido,subsector)
        
        diccionariosubsector=me.getValue(llavevalor)
        
        
        if valormaximo<int(diccionariosubsector["suma costos y gastos nomina"]):
            valormaximo=int(diccionariosubsector["suma costos y gastos nomina"])
            subsectormaximo=subsector
                 
    parejallavevalor=mp.get(añoescogido,subsectormaximo)
    diccionarioactividades=me.getValue(parejallavevalor)
    
    merg.sort(diccionarioactividades["actividades"],cmpcostosygastonomina)
    if lt.size(diccionarioactividades["actividades"])<6:
        list6=lt.newList(datastructure="ARRAY_LIST")
        for actividad in lt.iterator(diccionarioactividades["actividades"]):
        
            diccionario1={"codigo actividad economica":actividad["codigo actividad economica"],
                        "nombre actividad economica":actividad["nombre actividad economica"],
                        "total costos gastos nomina":actividad["total costos gastos nomina"],
                        "total ingresos netos":actividad["total ingresos netos"],
                        "total costos gastos":actividad["total costos gastos"],
                        "total saldo por pagar":actividad["saldo a pagar"],
                        "total saldo a favor":actividad["saldo a favor"]}
            lt.addLast(list6,diccionario1)
            
        copia=diccionarioactividades.copy()
        del copia["suma descuentos tributarios"]
        del copia["suma total retenciones"]
        del copia["actividades"]
    
        return copia, list6
    
    else:
        actividadesmas=lt.subList(diccionarioactividades["actividades"],1,3)
        actividadesmenos=lt.subList(diccionarioactividades["actividades"],(lt.size(diccionarioactividades["actividades"])-2),3)
        
        actividadesmasultimo=lt.newList(datastructure="ARRAY_LIST")
        actividadesmenossultimo=lt.newList(datastructure="ARRAY_LIST")
        for actividad in lt.iterator(actividadesmas):
            
            diccionario1={"codigo actividad economica":actividad["codigo actividad economica"],
                        "nombre actividad economica":actividad["nombre actividad economica"],
                        "total costos gastos nomina":actividad["total costos gastos nomina"],
                        "total ingresos netos":actividad["total ingresos netos"],
                        "total costos gastos":actividad["total costos gastos"],
                        "total saldo por pagar":actividad["saldo a pagar"],
                        "total saldo a favor":actividad["saldo a favor"]}
            
            lt.addLast(actividadesmasultimo,diccionario1)
            
        
        for actividad in lt.iterator(actividadesmenos):
            diccionario2={"codigo actividad economica":actividad["codigo actividad economica"],
                        "nombre actividad economica":actividad["nombre actividad economica"],
                        "total costos gastos nomina":actividad["total costos gastos nomina"],
                        "total ingresos netos":actividad["total ingresos netos"],
                        "total costos gastos":actividad["total costos gastos"],
                        "total saldo por pagar":actividad["saldo a pagar"],
                        "total saldo a favor":actividad["saldo a favor"]}
            
            lt.addLast(actividadesmenossultimo,diccionario2)
    
    copia=diccionarioactividades.copy()
    del copia["suma descuentos tributarios"]
    del copia["suma total retenciones"]
    del copia["actividades"]
    
    return  copia,actividadesmasultimo,actividadesmenossultimo

def req_5(data_structs,año):
    """
    Función que soluciona el requerimiento 5
    """
    catalog_año=data_structs[año]
    max=0
    subsector_max=0
    codigos=mp.keySet(catalog_año)
    for cod in lt.iterator(codigos):
        llave_valor=mp.get(catalog_año, cod)
        impuestos=me.getValue(llave_valor)
        impuestos=formato_5(impuestos)
        if impuestos["total descuentos tributarios"]>max:
            max=impuestos["total descuentos tributarios"]
            subsector_max=impuestos
        
    lst_actividades= subsector_max["actividades"]
    merg.sort(lst_actividades,cpm_descuentos_tributarios)
    
    for dic in lt.iterator(lst_actividades):
        
        del dic["año"]
        del dic["total costos gastos nomina"]
        del dic["total retenciones"]
        del dic["codigo sector economico"]
        del dic["nombre sector economico"]
        del dic["codigo subsector economico"]
        del dic["nombre subsector economico"]
    if lt.size(lst_actividades)<=6:
        mayores=lst_actividades
        menores=None
    else:
        mayores=lt.subList(lst_actividades,1,3)
        menores=lt.subList(lst_actividades,(lt.size(lst_actividades))-2,3)
    del subsector_max["actividades"]
    subsector=lt.newList("ARRAY_LIST")
    lt.addLast(subsector,subsector_max)
    
    return subsector,mayores,menores
      
def req_6(catalogo,año):
    """
    Función que soluciona el requerimiento 6
    """
    diccionariossectores=mp.newMap(numelements=23,
                                   maptype="PROBING",
                                   loadfactor=0.5)
    diccionarioaño=catalogo[año]
    llavesdicaño=mp.keySet(diccionarioaño)
    
    for subsectores in lt.iterator(llavesdicaño):
        diccionariosubsector=me.getValue(mp.get(diccionarioaño,subsectores))
        
        if mp.contains(diccionariossectores,diccionariosubsector["codigo sector economico"]):
            sector=me.getValue(mp.get(diccionariossectores,diccionariosubsector["codigo sector economico"]))
            sector["suma ingresos netos"]+=int(diccionariosubsector["suma ingresos netos"])
            sector["suma costos y gastos"]+=int(diccionariosubsector["suma costos y gastos"])
            sector["suma saldo por pagar"]+=int(diccionariosubsector["suma saldo por pagar"])
            sector["suma saldo a favor"]+=int(diccionariosubsector["suma saldo a favor"])
        
        else:
            nuevosector=newsector(diccionariosubsector)
            mp.put(diccionariossectores,diccionariosubsector["codigo sector economico"],nuevosector)
        
        formatoainsertar={"codigo subsector economico":diccionariosubsector["codigo subsector economico"],
                          "nombre subsector economico":diccionariosubsector["nombre subsector economico"],
                          "suma ingresos netos":diccionariosubsector["suma ingresos netos"],
                          "suma costos gastos":diccionariosubsector["suma costos y gastos"],
                          "suma saldo por pagar":diccionariosubsector["suma saldo por pagar"],
                          "suma saldo a favor":diccionariosubsector["suma saldo a favor"]}   
        lt.addLast(me.getValue(mp.get(diccionariossectores,diccionariosubsector["codigo sector economico"]))["subsectores"],formatoainsertar) 
    
    valoresdicsectores=mp.valueSet(diccionariossectores)
    
    merg.sort(valoresdicsectores,cmpingresosnetos)
    
    sectorescodigo=lt.lastElement(valoresdicsectores)
    
    merg.sort(sectorescodigo["subsectores"],cmpingresosnetos)
    
    subsectormax=lt.lastElement(sectorescodigo["subsectores"])
    subsectormin=lt.firstElement(sectorescodigo["subsectores"])
    
    #ahora a buscar las actividades
    diccompletossmax=me.getValue(mp.get(diccionarioaño,subsectormax["codigo subsector economico"]))
    merg.sort(diccompletossmax["actividades"],cmpingresosnetos2)
    
    actividadmasaporte=formatoactividadesreq6(lt.lastElement(diccompletossmax["actividades"]))
    actividadmenosaporte=formatoactividadesreq6(lt.firstElement(diccompletossmax["actividades"]))
            
    diccompletossmin=me.getValue(mp.get(diccionarioaño,subsectormin["codigo subsector economico"]))
    merg.sort(diccompletossmin["actividades"],cmpingresosnetos2)
    
    actividadesmasaporte1=formatoactividadesreq6(lt.lastElement(diccompletossmin["actividades"]))
    actividadesmenosaporte1=formatoactividadesreq6(lt.firstElement(diccompletossmin["actividades"]))
            
    del sectorescodigo["subsectores"]
    sectorescodigo["subsector que más aporto"]=subsectormax["codigo subsector economico"]
    sectorescodigo["subsector que menos aporto"]=subsectormin["codigo subsector economico"]
    
    return  sectorescodigo, subsectormax,subsectormin, actividadmasaporte, actividadmenosaporte, actividadesmasaporte1,actividadesmenosaporte1
 

def req_7(catalogo,año,codigo,topn):
    """
    Función que soluciona el requerimiento 7
    """

    llavevalor=mp.get(catalogo[año],codigo)
    diccionario_subsector=me.getValue(llavevalor)
    actividades=diccionario_subsector["actividades"]
    merg.sort(actividades,cmp_costos_gastos)
    
    final=lt.newList("ARRAY_LIST")
    if lt.size(actividades)>=int(topn):
        actividades=lt.subList(actividades,1,int(topn))
    
    for actividad in lt.iterator(actividades):
        respuesta=formato_7(actividad)
        lt.addLast(final,respuesta)
    
    return final

def req_8(catalog,año,topn):
    mapaaño=catalog[año]
    listallaves=mp.keySet(mapaaño)
    merg.sort(listallaves,codigosubsector)
    listasubsectores=lt.newList(datastructure="ARRAY_LIST")
    listaactividades=lt.newList(datastructure="ARRAY_LIST")
    
    if lt.size(listallaves)>12:
        lista3primeros=lt.subList(listallaves,1,3)
        lista3ultimos=lt.subList(listallaves,lt.size(listallaves)-2,3)
        
        for subsectores in lt.iterator(lista3primeros):
            diccionarioatrabajar=me.getValue(mp.get(mapaaño,subsectores))
            copia=diccionarioatrabajar.copy()
    
            del copia["actividades"]
            del copia["suma descuentos tributarios"]
            del copia["suma costos y gastos nomina"]
            del copia["suma total retenciones"]
            del copia["maximo saldo por pagar"]
            del copia["maximo saldo a favor"]
            del copia["actividad maxima saldo por pagar"]
            del copia["actividad maxima saldo a favor"]
            lt.addLast(listasubsectores,copia)
            
            merg.sort(diccionarioatrabajar["actividades"],cmpimpuestosacargo)
            
            if lt.size(diccionarioatrabajar["actividades"])<6:
                for actividades in lt.iterator(diccionarioatrabajar["actividades"]):
                    formato={"codigo sector economico":actividades["codigo sector economico"],
                            "nombre sector economico":actividades["nombre sector economico"],
                            "codigo subsector economico":actividades["codigo subsector economico"],
                            "nombre subsector economico":actividades["nombre subsector economico"],
                            "codigo actividad economica":actividades["codigo actividad economica"],
                            "nombre actividad economica":actividades["nombre actividad economica"],
                            "total impuestos a cargo":actividades["impuestos a cargo"],
                            "total costos y gastos":actividades["total costos gastos"],
                            "total saldo por pagar":actividades["saldo a pagar"],
                            "total saldo a favor":actividades["saldo a favor"]}   
                    lt.addLast(listaactividades,formato)
                        
            else:
                sublista=lt.subList(diccionarioatrabajar["actividades"],1,int(topn))
                for actividades in lt.iterator(sublista):
                    formato={"codigo sector economico":actividades["codigo sector economico"],
                            "nombre sector economico":actividades["nombre sector economico"],
                            "codigo subsector economico":actividades["codigo subsector economico"],
                            "nombre subsector economico":actividades["nombre subsector economico"],
                            "codigo actividad economica":actividades["codigo actividad economica"],
                            "nombre actividad economica":actividades["nombre actividad economica"],
                            "total impuestos a cargo":actividades["impuestos a cargo"],
                            "total costos y gastos":actividades["total costos gastos"],
                            "total saldo por pagar":actividades["saldo a pagar"],
                            "total saldo a favor":actividades["saldo a favor"]} 
                    
                    lt.addLast(listaactividades,formato)
        
        for subsectores in lt.iterator(lista3ultimos):
            diccionarioatrabajar=me.getValue(mp.get(mapaaño,subsectores))
            copia=diccionarioatrabajar.copy()
    
            del copia["actividades"]
            del copia["suma descuentos tributarios"]
            del copia["suma costos y gastos nomina"]
            del copia["suma total retenciones"]
            del copia["maximo saldo por pagar"]
            del copia["maximo saldo a favor"]
            del copia["actividad maxima saldo por pagar"]
            del copia["actividad maxima saldo a favor"]
            lt.addLast(listasubsectores,copia)
            
            merg.sort(diccionarioatrabajar["actividades"],cmpimpuestosacargo)
            
            if lt.size(diccionarioatrabajar["actividades"])<6:
                for actividades in lt.iterator(diccionarioatrabajar["actividades"]):
                    formato={"codigo sector economico":actividades["codigo sector economico"],
                            "nombre sector economico":actividades["nombre sector economico"],
                            "codigo subsector economico":actividades["codigo subsector economico"],
                            "nombre subsector economico":actividades["nombre subsector economico"],
                            "codigo actividad economica":actividades["codigo actividad economica"],
                            "nombre actividad economica":actividades["nombre actividad economica"],
                            "total impuestos a cargo":actividades["impuestos a cargo"],
                            "total costos y gastos":actividades["total costos gastos"],
                            "total saldo por pagar":actividades["saldo a pagar"],
                            "total saldo a favor":actividades["saldo a favor"]}   
                    lt.addLast(listaactividades,formato)
                        
            else:
                sublista=lt.subList(diccionarioatrabajar["actividades"],1,int(topn))
                for actividades in lt.iterator(sublista):
                    formato={"codigo sector economico":actividades["codigo sector economico"],
                            "nombre sector economico":actividades["nombre sector economico"],
                            "codigo subsector economico":actividades["codigo subsector economico"],
                            "nombre subsector economico":actividades["nombre subsector economico"],
                            "codigo actividad economica":actividades["codigo actividad economica"],
                            "nombre actividad economica":actividades["nombre actividad economica"],
                            "total impuestos a cargo":actividades["impuestos a cargo"],
                            "total costos y gastos":actividades["total costos gastos"],
                            "total saldo por pagar":actividades["saldo a pagar"],
                            "total saldo a favor":actividades["saldo a favor"]} 
                    
                    lt.addLast(listaactividades,formato)
                    
            
    else:
    
        for subsectores in lt.iterator(listallaves):
            diccionarioatrabajar=me.getValue(mp.get(mapaaño,subsectores))
            copia=diccionarioatrabajar.copy()
    
            del copia["actividades"]
            del copia["suma descuentos tributarios"]
            del copia["suma costos y gastos nomina"]
            del copia["suma total retenciones"]
            del copia["maximo saldo por pagar"]
            del copia["maximo saldo a favor"]
            del copia["actividad maxima saldo por pagar"]
            del copia["actividad maxima saldo a favor"]
            lt.addLast(listasubsectores,copia)
            
            merg.sort(diccionarioatrabajar["actividades"],cmpimpuestosacargo)
            
            if lt.size(diccionarioatrabajar["actividades"])<6:
                for actividades in lt.iterator(diccionarioatrabajar["actividades"]):
                    formato={"codigo sector economico":actividades["codigo sector economico"],
                            "nombre sector economico":actividades["nombre sector economico"],
                            "codigo subsector economico":actividades["codigo subsector economico"],
                            "nombre subsector economico":actividades["nombre subsector economico"],
                            "codigo actividad economica":actividades["codigo actividad economica"],
                            "nombre actividad economica":actividades["nombre actividad economica"],
                            "total impuestos a cargo":actividades["impuestos a cargo"],
                            "total costos y gastos":actividades["total costos gastos"],
                            "total saldo por pagar":actividades["saldo a pagar"],
                            "total saldo a favor":actividades["saldo a favor"]}   
                    lt.addLast(listaactividades,formato)
                        
            else:
                sublista=lt.subList(diccionarioatrabajar["actividades"],1,int(topn))
                for actividades in lt.iterator(sublista):
                    formato={"codigo sector economico":actividades["codigo sector economico"],
                            "nombre sector economico":actividades["nombre sector economico"],
                            "codigo subsector economico":actividades["codigo subsector economico"],
                            "nombre subsector economico":actividades["nombre subsector economico"],
                            "codigo actividad economica":actividades["codigo actividad economica"],
                            "nombre actividad economica":actividades["nombre actividad economica"],
                            "total impuestos a cargo":actividades["impuestos a cargo"],
                            "total costos y gastos":actividades["total costos gastos"],
                            "total saldo por pagar":actividades["saldo a pagar"],
                            "total saldo a favor":actividades["saldo a favor"]} 
                    
                    lt.addLast(listaactividades,formato)
                        
    return listasubsectores,listaactividades

# Funciones extras: Formatos

def formato_5(impuesto):
    formato={"codigo sector economico":impuesto["codigo sector economico"],
                "nombre sector economico":impuesto["nombre sector economico"],
                "codigo subsector economico":impuesto["codigo subsector economico"],
                "nombre subsector economico":impuesto["nombre subsector economico"],
                "total descuentos tributarios":impuesto["suma descuentos tributarios"],
                "suma total ingresos netos":impuesto["suma ingresos netos"],
                "total costos y gastos":impuesto["suma costos y gastos"],
                "total saldo a pagar":impuesto["suma saldo por pagar"],
                "total saldo a favor":impuesto["suma saldo a favor"],
                "actividades":impuesto["actividades"]}
    return formato

def newsector(dicatrabajar):
    diccionario={"codigo sector economico":dicatrabajar["codigo sector economico"],
                 "nombre sector economico":dicatrabajar["nombre sector economico"],
                 "suma ingresos netos":int(dicatrabajar["suma ingresos netos"]),
                 "suma costos y gastos":int(dicatrabajar["suma costos y gastos"]),
                 "suma saldo por pagar":int(dicatrabajar["suma saldo por pagar"]),
                 "suma saldo a favor":int(dicatrabajar["suma saldo a favor"]),
                 
                 "subsectores":None}
    diccionario["subsectores"]=lt.newList(datastructure="ARRAY_LIST")
    return diccionario       

def formatoactividadesreq6(actividad):
    formato={"codigo actividad economica":actividad["codigo actividad economica"],
                     "nombre actividad economica":actividad["nombre actividad economica"],
                     "total ingresos netos":actividad["total ingresos netos"],
                     "total costos y gastos":actividad["total costos gastos"],
                     "total saldo a favor":actividad["saldo a favor"],
                     "total saldo a pagar":actividad["saldo a pagar"]}
    return formato

def formato_7(actividad):
    
    formato={"codigo actividad economica":actividad["codigo actividad economica"],
                     "nombre actividad economica":actividad["nombre actividad economica"],
                     "codigo sector economico": actividad["codigo sector economico"],
                     "nombre sector economico":actividad["nombre sector economico"],
                     "total ingresos netos":actividad["total ingresos netos"],
                     "total costos y gastos":actividad["total costos gastos"],
                     "total saldo a pagar":actividad["saldo a pagar"],
                     "total saldo a favor":actividad["saldo a favor"]}
    
    return formato

# Funciones extras: Comparaciones

def codigosubsector(codigo1,codigo2):
    dato1=int(codigo1)
    dato2=int(codigo2)
    condicion=True
    if dato1!=dato2:
        condicion=dato1<dato2
    return condicion
                
def cmpimpuestosacargo(elemento1,elemento2):
    dato1=int(elemento1["impuestos a cargo"])
    dato2=int(elemento2["impuestos a cargo"])
    condicion=True
    if dato1!=dato2:
        condicion=dato1>dato2
    return condicion

def cmpsaldoafavor(impuesto1,impuesto2):
    dato1=int(impuesto1["saldo a favor"])
    dato2=int(impuesto2["saldo a favor"])
    condicion=True
    if dato1!= dato2:
        condicion=dato1<dato2
    return condicion

def cmpTotalRet(data1, data2):
    descuento1=int(data1["total retenciones"])
    descuento2=int(data2["total retenciones"])
    condicion=False
    if descuento1!=descuento2:
        condicion=descuento1<descuento2
    return condicion

def cmpcostosygastonomina(actividad1,actividad2):
    dato1=int(actividad1["total costos gastos nomina"])
    dato2=int(actividad2["total costos gastos nomina"])
    condicion=True
    if dato1!= dato2:
        condicion=dato1<dato2
    return condicion

def cpm_descuentos_tributarios(data1, data2):
    descuento1=int(data1["descuentos tributarios"])
    descuento2=int(data2["descuentos tributarios"])
    condicion=False
    if descuento1!=descuento2:
        condicion=descuento1<descuento2
    return condicion

def cmpingresosnetos(sector1,sector2):
    dato1=int(sector1["suma ingresos netos"] )
    dato2=int(sector2["suma ingresos netos"] ) 
    condicion=True
    if dato1!=dato2:
        condicion=dato1<dato2 
    return condicion  

def cmpingresosnetos2(actividad1,actividad2):
    dato1=int(actividad1["total ingresos netos"] )
    dato2=int(actividad2["total ingresos netos"] ) 
    condicion=True
    if dato1!=dato2:
        condicion=dato1<dato2 
    return condicion  

def cmp_costos_gastos(data1,data2):
    data1=int(data1["total costos gastos"])
    data2=int(data2["total costos gastos"])
    condicion=False
    if data2!=data1:
        condicion=data1<data2
    return condicion

