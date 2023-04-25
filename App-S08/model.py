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
import main_adts as adt
import datetime
from tabulate import tabulate
from types import FunctionType
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

#OPTIMIZE Objects

class DataStructs:

    def __init__(self):

        self.all_data = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)
        self.map_by_year = adt.HashMap(numelements=10, maptype="PROBING", loadfactor=0.5)
class EconomicActivity():

    def __init__(self, data: dict):
        """
        This class represents an economic activity.

        Attributes:
        year (int): The year of the data.
        code_activity (int): The code of the economic activity.
        name_activity (str): The name of the economic activity.
        code_subsector (int): The code of the subsector.
        name_subsector (str): The name of the subsector.
        code_sector (int): The code of the sector.
        name_sector (str): The name of the sector.
        total_net_incomes (int): The total net incomes.
        total_favorable_balance (int): The total favorable balance.
        total_payable_balance (int): The total payable balance.
        total_retencions (int): The total retentions.
        total_cost_and_expenses (int): The total cost and expenses.
        costs (int): The costs.
        costs_and_payroll_expenses (int): The costs and payroll expenses.
        tax_discounts (int): The tax discounts.
        """
        self.dict_data = {}
        self.year = int(data["Año"])
        self.dict_data["Año"] = self.year
        self.code_activity = (data["Código actividad económica"])
        self.dict_data["Código actividad económica"] = self.code_activity
        self.name_activity = data["Nombre actividad económica"]
        self.dict_data["Nombre actividad económica"] = self.name_activity
        self.code_subsector = (data["Código subsector económico"])
        self.dict_data["Código subsector económico"] = self.code_subsector
        self.name_subsector = data["Nombre subsector económico"]
        self.dict_data["Nombre subsector económico"] = self.name_subsector
        self.code_sector = (data["Código sector económico"])
        self.dict_data["Código sector económico"] = self.code_sector
        self.name_sector = data["Nombre sector económico"]
        self.dict_data["Nombre sector económico"] = self.name_sector
        self.total_net_incomes = int(data["Total ingresos netos"])
        self.dict_data["Total ingresos netos"] = self.total_net_incomes
        self.total_favorable_balance = int(data["Total saldo a favor"])
        self.dict_data["Total saldo a favor"] = self.total_favorable_balance
        self.total_payable_balance = int(data["Total saldo a pagar"])
        self.dict_data["Total saldo a pagar"] = self.total_payable_balance
        self.total_retencions = int(data["Total retenciones"])
        self.dict_data["Total retenciones"] = self.total_retencions
        self.total_cost_and_expenses = int(data["Total costos y gastos"])
        self.dict_data["Total costos y gastos"] = self.total_cost_and_expenses
        self.costs = int(data["Costos"])
        self.dict_data["Costos"] = self.costs
        self.costs_and_payroll_expenses = int(data["Costos y gastos nómina"])
        self.dict_data["Costos y gastos nómina"] = self.costs_and_payroll_expenses
        self.tax_discounts = int(data["Descuentos tributarios"])
        self.dict_data["Descuentos tributarios"] = self.tax_discounts
        self.total_tax_liability = int(data["Total Impuesto a cargo"])
        self.dict_data["Total Impuesto a cargo"] = self.total_tax_liability

    def create_table(self, columns, maxwidht=20):
        tabulate_list = []
        tabulate_list.append(self.create_list(columns))
        print(tabulate(tabular_data = tabulate_list, headers = columns, tablefmt = "grid", maxheadercolwidths=maxwidht, maxcolwidths=maxwidht))
        return tabulate_list

    def create_vertical_table(self, columns, maxwidth=40):

        tabular_list = []
        tabular_list.append(self.create_list(columns))

        tabulate_list = []

        for column in columns:

            row = [column, tabular_list[0][columns.index(column)]]
            tabulate_list.append(row)

        visual_table = tabulate(tabular_data = tabulate_list, headers = ["Attribute", "Value"], tablefmt = "grid", maxheadercolwidths=maxwidth, maxcolwidths=maxwidth)
        return visual_table

    def create_list(self, columns):
        tabulate_list = []
        for data in columns:
            attribute = self._match_columns(data)
            tabulate_list.append(attribute)
        return tabulate_list

    def _match_columns(self, column):
        attribute = self.dict_data[column]
        return attribute
class Year(DataStructs):

    def __init__(self):

        self.all_data = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)
        self.map_by_sector = adt.HashMap(numelements=15, maptype="PROBING", loadfactor=0.5)
        self.map_by_subsectors = adt.HashMap(numelements=21, maptype="PROBING", loadfactor=0.5)
        self.subsector_max = None
        self.subsector_min = None
        #HACK Bonus
        self.list_subsectors = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)

    def search_min_max_subsector(self, sort_criteria):
        all_sectors = self.map_by_sector.valueSet()
        for sector in all_sectors:
            max, min = sector.obtain_max_and_min_subsector(sort_criteria)
            if self.subsector_max is None:
                self.subsector_max = max
            elif sort_criteria(max, self.subsector_max):
                self.subsector_max = max
            if self.subsector_min is None:
                self.subsector_min = min
            elif sort_criteria(min, self.subsector_min) == False:
                self.subsector_min = min
        return self.subsector_max, self.subsector_min

    def search_min_max_sector(self, sort_criteria):
        all_sectors = self.map_by_sector.valueSet()
        for sector in all_sectors:
            if self.subsector_max is None:
                self.subsector_max = sector
            elif sort_criteria(sector, self.subsector_max):
                self.subsector_max = sector
            if self.subsector_min is None:
                self.subsector_min = sector
            elif sort_criteria(sector, self.subsector_min) == False:
                self.subsector_min = sector
        return self.subsector_max, self.subsector_min



    def create_table(self, columns, attribute, maxim, maxwidth=20):

        list_top = getattr(self, attribute)


        if list_top.size() <= maxim:

            return self._create_table_data(list_top, columns)

        elif list_top.size() > maxim:
            new_list = adt.List()

            for element in list_top.subList(1, (maxim//2)):

                new_list.addLast(element)

            for element in list_top.subList(list_top.size() - (maxim//2)-1, maxim//2):

                new_list.addLast(element)

            return self._create_table_data(new_list, columns)


    def _create_table_data(self, list: adt.List, columns, maxwidth = 20):

        tabular = []

        for element in list:
            element_list = element.create_list(columns)
            tabular.append(element_list)

        table = tabulate(tabular, headers=columns, tablefmt="grid", maxheadercolwidths=maxwidth, maxcolwidths=maxwidth)

        return table


    def _reformatColumns(self, columns: list):

        new_columns = []

        for data in columns:

            if data.startswith("Total"):

                data = f"{data} del subsector económico"
                new_columns.append(data)
            else:
                new_columns.append(data)

        return new_columns

    def create_list(self, columns: list):

        tabular = []

        for data in columns:

            element_list = self._match_columns(data)
            tabular.append(element_list)

        return tabular

    def _match_columns(self, column):

        attribute = self.dict_data[column]

        return attribute
class Sector():

    def __init__(self):

        self.all_data = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)
        self.map_by_subsector = adt.HashMap(numelements=21, maptype="PROBING", loadfactor=0.5)
        #NOTE: Atributos para el requerimiento 1
        self.max_total_payable_balance = None #NOTE: EconomicActivity
        self.min_total_payable_balance = None #NOTE: EconomicActivity
        #NOTE: Atributos para el requerimiento 2
        self.max_total_favorable_balance = None #NOTE: EconomicActivity
        self.min_total_favorable_balance = None #NOTE: EconomicActivity
        #NOTE: Atributos para el requerimiento 4, 5, 6
        self.dict_data = {}
        self.total_all_net_incomes = 0
        self.total_all_costs_and_expenses = 0
        self.total_all_payable_balance = 0
        self.total_all_favorable_balance = 0
        self.less_apport_subsector = None #NOTE: Subsector
        self.more_apport_subsector = None #NOTE: Subsector
        #OPTIMIZE: Atributos propios del sector
        self.name_sector = None
        self.code_sector = None

    def give_attributes(self, data : EconomicActivity):
        self.name_sector = data.name_sector
        self.code_sector = data.code_sector
        self.dict_data["Nombre sector económico"] = self.name_sector
        self.dict_data["Código sector económico"] = self.code_sector

    def actualize(self, data : EconomicActivity):
        self.sum_values(data)
        self.actualize_dict()

    def actualize_dict(self):
        self.dict_data["Total ingresos netos"] = self.total_all_net_incomes
        self.dict_data["Total costos y gastos"] = self.total_all_costs_and_expenses
        self.dict_data["Total saldo a pagar"] = self.total_all_payable_balance
        self.dict_data["Total saldo a favor"] = self.total_all_favorable_balance

        if self.less_apport_subsector is not None and self.more_apport_subsector is not None:
            self.dict_data["Subsector económico que más aportó"] = self.less_apport_subsector.code_subsector
            self.dict_data["Subsector económico que menos aportó"] = self.more_apport_subsector.code_subsector

    def sum_values(self, data : EconomicActivity):
        """
        This method takes an instance of the EconomicActivity class as an argument and updates four attributes of the current object in the following way:
        - self.total_all_net_incomes: The value of this attribute is increased by the total_net_incomes value of the EconomicActivity instance.
        - self.total_all_costs_and_expenses: The value of this attribute is increased by the total_cost_and_expenses value of the EconomicActivity instance.
        - self.total_all_payable_balance: The value of this attribute is increased by the total_payable_balance value of the EconomicActivity instance.
        - self.total_all_favorable_balance: The value of this attribute is increased by the total_favorable_balance value of the EconomicActivity instance.

        Parameters:
        data (EconomicActivity): An instance of the EconomicActivity class.

        Returns:
        None
        """
        self.total_all_net_incomes += data.total_net_incomes
        self.total_all_costs_and_expenses += data.total_cost_and_expenses
        self.total_all_payable_balance += data.total_payable_balance
        self.total_all_favorable_balance += data.total_favorable_balance

    def obtain_max_and_min_economic_activity(self, sort_criteria, attribute):
        """
        Función encargada de obtener el máximo y el mínimo de algun parametro de alguna actividad economica
        """
        sector_all_data = self.all_data
        sector_all_data.sort(sort_criteria)
        max = sector_all_data.firstElement()
        min = sector_all_data.lastElement()
        if attribute == "total_payable_balance":
            self.max_total_payable_balance = max
            self.min_total_payable_balance = min
        elif attribute == "total_favorable_balance":
            self.max_total_favorable_balance = max
            self.min_total_favorable_balance = min

        return max, min

    def obtain_max_and_min_subsector(self, sort_criteria):
        subsector_all_data = self.map_by_subsector.valueSet()
        subsector_all_data.sort(sort_criteria)
        max = subsector_all_data.firstElement()
        min = subsector_all_data.lastElement()
        self.less_apport_subsector = min
        self.more_apport_subsector = max
        self.actualize_dict()
        return max, min

    def create_table_sector(self, columns: list, maxwidht = 20):
        tabular = []
        tabular.append(self.create_list(columns))
        columns = self._reformatColumns(columns)
        return tabulate(tabular, headers=columns, tablefmt="grid", maxcolwidths=maxwidht, maxheadercolwidths=maxwidht)

    def _reformatColumns(self, columns: list):

        new_columns = []

        for data in columns:

            if data.startswith("Total"):

                data = f"{data} del sector económico"
                new_columns.append(data)
            else:
                new_columns.append(data)

        return new_columns

    def create_list(self, columns: list):

        tabular = []

        for data in columns:

            element_list = self._match_columns(data)
            tabular.append(element_list)

        return tabular


    def _match_columns(self, column):
        attribute = self.dict_data[column]

        return attribute
class Subsector():

    def __init__(self):


        self.all_data = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)
        #NOTE: Atributos para el requerimiento 3
        self.total_retencions = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id) #NOTE: List of EconomicActivity
        #NOTE: Atributos para el requerimiento 4
        self.total_costs_and_payroll_expenses = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id) #NOTE: List of EconomicActivity
        #NOTE: Atributos para el requerimiento 5
        self.tax_discounts = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id) #NOTE: List of EconomicActivity
        #NOTE: Atributos para el requerimiento 6
        self.total_net_incomes = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id) #NOTE: List of EconomicActivity
        #NOTE: Atributos para el requerimiento 7
        self.total_costs_and_expenses = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id) #NOTE: List of EconomicActivity
        #HACK: Bonus
        self.total_tax_liability = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id) #NOTE: List of EconomicActivity

        self.min_activity = None
        self.max_activity = None

        self.dict_data = {}
        self.total_all_retencions = 0
        self.total_all_costs_and_payroll_expenses = 0
        self.total_all_tax_discounts = 0
        self.total_all_net_incomes = 0
        self.total_all_costs_and_expenses = 0
        self.total_all_payable_balance = 0
        self.total_all_favorable_balance = 0
        self.total_all_tax_liability = 0

        self.name_subsector = None
        self.code_subsector = None
        self.name_sector = None
        self.code_sector = None

    def give_attributes(self, data : EconomicActivity):

        self.name_subsector = data.name_subsector
        self.code_subsector = data.code_subsector
        self.name_sector = data.name_sector
        self.code_sector = data.code_sector
        self.dict_data["Nombre subsector económico"] = self.name_subsector
        self.dict_data["Código subsector económico"] = self.code_subsector
        self.dict_data["Nombre sector económico"] = self.name_sector
        self.dict_data["Código sector económico"] = self.code_sector

    def actualize(self, data : EconomicActivity):
        self.sum_values(data)
        self.actualize_dict()

    def sum_values(self, data: EconomicActivity):

        self.total_all_retencions += data.total_retencions
        self.total_all_costs_and_payroll_expenses += data.costs_and_payroll_expenses
        self.total_all_tax_discounts += data.tax_discounts
        self.total_all_net_incomes += data.total_net_incomes
        self.total_all_costs_and_expenses += data.total_cost_and_expenses
        self.total_all_payable_balance += data.total_payable_balance
        self.total_all_favorable_balance += data.total_favorable_balance
        self.total_all_tax_liability += data.total_tax_liability

    def actualize_dict(self):
        self.dict_data["Total de retenciones"] = self.total_all_retencions
        self.dict_data["Total de costos y gastos de nómina"] = self.total_all_costs_and_payroll_expenses
        self.dict_data["Total de descuentos tributarios"] = self.total_all_tax_discounts
        self.dict_data["Total ingresos netos"] = self.total_all_net_incomes
        self.dict_data["Total costos y gastos"] = self.total_all_costs_and_expenses
        self.dict_data["Total saldo a pagar"] = self.total_all_payable_balance
        self.dict_data["Total saldo a favor"] = self.total_all_favorable_balance
        self.dict_data["Total de Impuestos a cargo"] = self.total_all_tax_liability

        if self.min_activity is not None and self.max_activity is not None:

            columns = ["Código actividad económica",
                       "Nombre actividad económica",
                       "Total ingresos netos",
                       "Total costos y gastos",
                       "Total saldo a pagar",
                       "Total saldo a favor"]
            self.min_activity = self.min_activity.create_vertical_table(columns)
            self.max_activity = self.max_activity.create_vertical_table(columns)

            self.dict_data["Actividad económica que menos aportó"] = self.min_activity
            self.dict_data["Actividad económica que más aportó"] = self.max_activity

    def sort_data_subsector(self, sort_criteria: FunctionType, attribute: str):
        """
        Funcion encargada de ordenar la lista de las actividades economicas
        """
        subsector_all_data = self.all_data
        subsector_all_data.sort(sort_criteria)

        if attribute == "total_retencions":
            self.total_retencions = subsector_all_data
        elif attribute == "total_costs_and_payroll_expenses":
            self.total_costs_and_payroll_expenses = subsector_all_data
        elif attribute == "tax_discounts":
            self.tax_discounts = subsector_all_data
        elif attribute == "total_net_incomes":
            self.min_activity = subsector_all_data.lastElement()
            self.max_activity = subsector_all_data.firstElement()
            self.actualize_dict()
        elif attribute == "total_costs_and_expenses":
            self.total_costs_and_expenses = subsector_all_data
        elif attribute == "total_tax_liability":
            self.total_tax_liability = subsector_all_data

    def is_list_created(func: FunctionType):
        def decorator(self, *args, **kwargs):
            if self.total_retencions.isEmpty() and self.total_costs_and_payroll_expenses.isEmpty() and self.tax_discounts.isEmpty() and self.total_costs_and_expenses:
                print("La lista no ha sido creada")
            else:
                return func(self , *args, **kwargs)
        return decorator

    @is_list_created
    def create_tables_min_max(self, attribute: str, columns: list):
        """
        Funcion encargada de crear las tablas de minimo y maximo de las actividades economicas
        """

        if attribute == "total_retencions":
            return self._create_table_min_max(self.total_retencions, columns)
        elif attribute == "total_costs_and_payroll_expenses":
            return self._create_table_min_max(self.total_costs_and_payroll_expenses, columns)
        elif attribute == "tax_discounts":
            return self._create_table_min_max(self.tax_discounts, columns)

    def create_table_top(self, columns, top: int, attribute, maxwidth = 20):

        list_top = getattr(self, attribute)

        if list_top.size() <= top:

            return self._create_table_data(list_top, columns)

        elif list_top.size() > top and top <= 12:

            return self._create_table_data(list_top.subList(1, top), columns)

        elif top > 12:
            list_top = list_top.subList(1, top)
            new_list = adt.List()

            for element in list_top.subList(1, 6):

                new_list.addLast(element)

            for element in list_top.subList(list_top.size() - 5, 6):

                new_list.addLast(element)

            return self._create_table_data(new_list, columns)

    def _create_table_data(self, list: adt.List, columns, maxwidth = 20):

        tabular = []

        for element in list:
            element_list = element.create_list(columns)
            tabular.append(element_list)

        table = tabulate(tabular, headers=columns, tablefmt="grid", maxheadercolwidths=maxwidth, maxcolwidths=maxwidth)

        return table

    def _create_table_min_max(self, list: adt.List, columns: list, maxwidth = 20):
        """
        Funcion encargada de crear las tablas de minimo y maximo de las actividades economicas
        """

        if list.size() < 6:

            table = self._create_table_data(list, columns, maxwidth)

            return table

        else:

            min_list = list.subList(1, 3)
            max_list = list.subList(list.size() - 2, 3)

            table_min = self._create_table_data(min_list, columns, maxwidth)
            table_max = self._create_table_data(max_list, columns, maxwidth)

            return table_min, table_max

    def create_table_subsector(self, columns: list, maxwidth = 20):
        tabular = []
        tabular.append(self.create_list(columns))
        columns = self._reformatColumns(columns)
        return tabulate(tabular, headers=columns, tablefmt="grid", maxcolwidths=maxwidth, maxheadercolwidths=maxwidth)

    def _reformatColumns(self, columns: list):

        new_columns = []

        for data in columns:

            if data.startswith("Total"):

                data = f"{data} del subsector económico"
                new_columns.append(data)
            else:
                new_columns.append(data)

        return new_columns

    def create_list(self, columns: list):

        tabular = []

        for data in columns:

            element_list = self._match_columns(data)
            tabular.append(element_list)

        return tabular

    def _match_columns(self, column):

        attribute = self.dict_data[column]

        return attribute
# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #CHECK: Inicializar las estructuras de datos

    data_structs = DataStructs()

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs : DataStructs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    d = new_data(data)
    columns_activity = ["Código actividad económica",
                        "Nombre actividad económica",
                        "Descuentos tributarios",
                        "Total ingresos netos",
                        "Total costos y gastos",
                        "Total saldo a pagar",
                        "Total saldo a favor"]

    data_structs.all_data.addLast(d)

    add_register_by_year(data_structs, d)

    return data_structs

def add_register_by_year(data_structs : DataStructs, data : EconomicActivity):

    map_by_year = data_structs.map_by_year

    year = data.year

    exist = map_by_year.contains(year)

    if not exist:

        value = Year()
        value.code = data.year
        map_by_year.put(year, value)
        entry = map_by_year.get(year)
        year_data = me.getValue(entry)
        year_data.all_data.addLast(data)
        add_register_by_sector(year_data, data)
    else:
        entry = map_by_year.get(year)
        year_data = me.getValue(entry)
        year_data.all_data.addLast(data)
        add_register_by_sector(year_data, data)

    return data_structs


def add_register_by_sector(year : Year, data : EconomicActivity):

    map_by_sector = year.map_by_sector

    sector = data.code_sector

    exist = map_by_sector.contains(sector)

    if not exist:
        value = Sector()
        map_by_sector.put(sector, value)
        entry = map_by_sector.get(sector)
        sector_data = me.getValue(entry)
        sector_data.all_data.addLast(data)
        sector_data.give_attributes(data)
        sector_data.actualize(data)
        add_register_by_subsector(sector_data,year, data)

    else:
        entry = map_by_sector.get(sector)
        sector_data = me.getValue(entry)
        sector_data.all_data.addLast(data)
        sector_data.sum_values(data)
        sector_data.actualize(data)
        add_register_by_subsector(sector_data,year, data)

    return year

def add_register_by_subsector(sector : Sector, year: Year, data : EconomicActivity):

    map_by_subsector = sector.map_by_subsector
    year_map_by_subsector = year.map_by_subsectors

    subsector = data.code_subsector

    exist = map_by_subsector.contains(subsector)
    exist_year = year_map_by_subsector.contains(subsector)

    if not exist:
        value = Subsector()
        map_by_subsector.put(subsector, value)
        entry = map_by_subsector.get(subsector)
        subsector_data = me.getValue(entry)
        subsector_data.give_attributes(data)
        subsector_data.actualize(data)
        subsector_data.all_data.addLast(data)
    else:
        entry = map_by_subsector.get(subsector)
        subsector_data = me.getValue(entry)
        subsector_data.actualize(data)
        subsector_data.all_data.addLast(data)

    if not exist_year:
        value = Subsector()
        year_map_by_subsector.put(subsector, value)
        entry = year_map_by_subsector.get(subsector)
        year.list_subsectors.addLast(subsector_data)
        subsector_data = me.getValue(entry)
        subsector_data.give_attributes(data)
        subsector_data.actualize(data)
        subsector_data.all_data.addLast(data)
    else:
        entry = year_map_by_subsector.get(subsector)
        subsector_data = me.getValue(entry)
        subsector_data.actualize(data)
        subsector_data.all_data.addLast(data)

    return sector

# Funciones para creacion de datos

def new_data(info):
    """
    Crea una nueva estructura para modelar los datos
    """

    data = EconomicActivity(info)

    try:
        data.id = int(data.year + data.code_activity)
    except:
        i = 0

        for char in data.code_activity:
            if char in [" ","/"]:
                data.code_activity = data.code_activity[0:i]
                break
            else:
                i += 1
        data.id = int(data.year + int(data.code_activity))

    return data


# Funciones de consulta


def req_1(data_structs: DataStructs, code_year: int, code_sector: str):
    """
    Función que soluciona el requerimiento 1
    """
    # CHECK: Realizar el requerimiento 1

    map_year = data_structs.map_by_year
    # map_year.get(code_year) -> entry = {"key": code_year, "value": year_data} year_data = Year()

    if not map_year.contains(code_year):
        return False

    year_data = me.getValue(map_year.get(code_year))
    map_sector = year_data.map_by_sector

    if not map_sector.contains(code_sector):
        return False

    sector_data = me.getValue(map_sector.get(code_sector))
    max, min = sector_data.obtain_max_and_min_economic_activity(compare_by_rq1, "total_payable_balance")

    return max


def req_2(data_structs: DataStructs, code_year: int, code_sector: str):
    """
    Función que soluciona el requerimiento 1
    """
    # CHECK: Realizar el requerimiento 1

    map_year = data_structs.map_by_year

    if not map_year.contains(code_year):
        return False

    year_data = me.getValue(map_year.get(code_year))
    map_sector = year_data.map_by_sector

    if not map_sector.contains(code_sector):
        return False

    sector_data = me.getValue(map_sector.get(code_sector))
    max, min = sector_data.obtain_max_and_min_economic_activity(compare_by_rq2, "total_favorable_balance")

    return max


def req_3(data_structs, code_year):
    """
    Función que soluciona el requerimiento 3
    """
    # CHECK: Realizar el requerimiento 3

    map_year = data_structs.map_by_year
    if not map_year.contains(code_year):
        return False
    year_data = me.getValue(map_year.get(code_year))
    max_subsector, min_subsector =  year_data.search_min_max_subsector(compare_by_rq3)
    min_subsector.sort_data_subsector(compare_by_retencions, "total_retencions")

    return min_subsector


def req_4(data_structs, code_year):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4

    map_year = data_structs.map_by_year
    if not map_year.contains(code_year):
        return False
    year_data = me.getValue(map_year.get(code_year))
    max_subsector, min_subsector =  year_data.search_min_max_subsector(compare_by_rq4)
    max_subsector.sort_data_subsector(compare_by_payroll_expenses, "total_costs_and_payroll_expenses")

    return max_subsector

def req_5(data_structs, code_year):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    map_year = data_structs.map_by_year
    if not map_year.contains(code_year):
        return False
    year_data = me.getValue(map_year.get(code_year))
    max_subsector, min_subsector =  year_data.search_min_max_subsector(compare_by_rq5)
    max_subsector.sort_data_subsector(compare_by_tax_discounts, "tax_discounts")

    return max_subsector


def req_6(data_structs, code_year):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    map_year = data_structs.map_by_year
    if not map_year.contains(code_year):
        return False
    year_data = me.getValue(map_year.get(code_year))
    max_sector, min_sector = year_data.search_min_max_sector(compare_by_sector_rq6)
    max_subsector, min_subsector =  max_sector.obtain_max_and_min_subsector(compare_by_subsector_rq6)
    max_subsector.sort_data_subsector(compare_by_net_income, "total_net_incomes")
    min_subsector.sort_data_subsector(compare_by_net_income, "total_net_incomes")

    return max_sector, max_subsector, min_subsector


def req_7(data_structs: DataStructs, code_year: int, code_sector: str):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    map_years = data_structs.map_by_year
    if not map_years.contains(code_year):
        return False
    year = me.getValue(map_years.get(code_year))
    map_subsectors = year.map_by_subsectors
    if not map_subsectors.contains(code_sector):
        return False
    subsector = me.getValue(map_subsectors.get(code_sector))
    subsector.sort_data_subsector(compare_by_total_costs_and_expenses, "total_costs_and_expenses")

    return subsector


def req_8(data_structs, code_year, top):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    map_years = data_structs.map_by_year
    if not map_years.contains(code_year):
        return False
    year = me.getValue(map_years.get(code_year))
    year.list_subsectors.sort(compare_subsectors_by_total_tax_liability)

    tables_subsector = adt.List()

    for subsector in year.list_subsectors:
        subsector.sort_data_subsector(compare_by_tax_liability, "total_tax_liability")
        tables_subsector.addLast(subsector)

    return year, tables_subsector


#NOTE Funciones utilizadas para comparar elementos dentro de una lista

def compare_by_id(data_1 : EconomicActivity, data_2: EconomicActivity):
    """
    Función encargada de comparar dos datos
    """
    id_1 = data_1.id
    id_2 = data_2.id
    name1 = data_1.name_activity
    name2 = data_2.name_activity
    return compare(id_1, id_2, name1, name2)

def compare_by_rq1(data_1 : EconomicActivity, data_2: EconomicActivity):
    """
    Función encargada de comparar dos datos
    """
    id_1 = data_1.total_payable_balance
    id_2 = data_2.total_payable_balance
    name1 = data_1.name_activity
    name2 = data_2.name_activity
    return compare(id_1, id_2, name1, name2)

def compare_by_rq2(data_1 : EconomicActivity, data_2: EconomicActivity):
    """
    Función encargada de comparar dos datos
    """
    id_1 = data_1.total_favorable_balance
    id_2 = data_2.total_favorable_balance
    name1 = data_1.name_activity
    name2 = data_2.name_activity
    return compare(id_1, id_2, name1, name2)

def compare_by_rq3(data1 : Subsector, data2: Subsector):
    id1 = data1.total_all_retencions
    id2 = data2.total_all_retencions
    name1 = data1.name_subsector
    name2 = data2.name_subsector
    return compare(id1, id2, name1, name2)

def compare_by_rq4(data1: Subsector, data2: Subsector):
    id1 = data1.total_all_costs_and_payroll_expenses
    id2 = data2.total_all_costs_and_payroll_expenses
    name1 = data1.name_subsector
    name2 = data2.name_subsector
    return compare(id1, id2, name1, name2)

def compare_by_rq5(data1: Subsector, data2: Subsector):
    id1 = data1.total_all_tax_discounts
    id2 = data2.total_all_tax_discounts
    name1 = data1.name_subsector
    nam2 = data2.name_subsector
    return compare(id1, id2, name1, nam2)

def compare_by_sector_rq6(data1: Sector, data2: Sector):
    id1 = data1.total_all_net_incomes
    id2 = data2.total_all_net_incomes
    name1 = data1.name_sector
    name2 = data2.name_sector
    return compare(id1, id2, name1, name2)

def compare_by_subsector_rq6(data1: Subsector, data2: Subsector):
    id1 = data1.total_all_net_incomes
    id2 = data2.total_all_net_incomes
    name1 = data1.name_subsector
    name2 = data2.name_subsector
    return compare(id1, id2, name1, name2)

def compare_subsectors_by_total_tax_liability(data1: Subsector, data2: Subsector):
    id1 = data1.total_all_tax_liability
    id2 = data2.total_all_tax_liability
    name1 = data1.name_subsector
    name2 = data2.name_subsector
    return compare(id1, id2, name1, name2)

def compare_by_payroll_expenses(data1: EconomicActivity, data2: EconomicActivity):
    id1 = data1.costs_and_payroll_expenses
    id2 = data2.costs_and_payroll_expenses
    name1 = data1.name_activity
    name2 = data2.name_activity
    return compare(id1, id2, name1, name2)

def compare_by_retencions(data1 : EconomicActivity, data2: EconomicActivity):
    id1 = data1.total_retencions
    id2 = data2.total_retencions
    name1 = data1.name_activity
    name2 = data2.name_activity
    return compare(id1, id2, name1, name2)

def compare_by_tax_discounts(data1 : EconomicActivity, data2: EconomicActivity):
    id1 = data1.tax_discounts
    id2 = data2.tax_discounts
    name1 = data1.name_activity
    name2 = data2.name_activity
    return compare(id1, id2, name1, name2)

def compare_by_net_income(data1 : EconomicActivity, data2: EconomicActivity):
    id1 = data1.total_net_incomes
    id2 = data2.total_net_incomes
    name1 = data1.name_activity
    name2 = data2.name_activity
    return compare(id1, id2, name1, name2)

def compare_by_total_costs_and_expenses(data1 : EconomicActivity, data2: EconomicActivity):

    id1 = data1.total_cost_and_expenses
    id2 = data2.total_cost_and_expenses
    name1 = data1.name_activity
    name2 = data2.name_activity
    return reverse_compare(id1, id2, name1, name2)

def compare_by_tax_liability(data1 : EconomicActivity, data2: EconomicActivity):
    id1 = data1.total_tax_liability
    id2 = data2.total_tax_liability
    name1 = data1.name_activity
    name2 = data2.name_activity
    return compare(id1, id2, name1, name2)

def compare(id1, id2, name1, name2):
    if id1 == id2:
        if name1 < name2:
            return True
        else:
            return False
    elif id1 > id2:
        return True
    else:
        return False

def reverse_compare(id1, id2, name1, name2):
    if id1 == id2:
        if name1 < name2:
            return True
        else:
            return False
    elif id1 < id2:
        return True
    else:
        return False

#NOTE Funciones utilizadas para comparar las llaves dentro de un mapa


#NOTE Funciones de ordenamiento