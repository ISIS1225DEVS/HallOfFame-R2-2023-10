import controller
import model
from tabulate import tabulate
import main_adts as adt
from random import *

def new_controller(maptype, loadfactor):
    """
        Se crea una instancia del controlador
    """
    #CHECK: Llamar la función del controlador donde se crean las estructuras de datos

    control = controller.new_controller(maptype,loadfactor)

    return control

def memory_and_time():
    """
    Retorna el tiempo y la memoria utilizada por el programa
    """


    table_probing = []
    table_chaining = []
    loadfactor_probing = [0.1,0.5, 0.7, 0.9]
    loadfactor_chaining = [2,4,6,8]


    for i in loadfactor_probing:

        control = new_controller("PROBING", i)
        analyze = controller.load_data(control, "-large.csv", True)
        time = controller.load_data(control, "-large.csv", False)
        row = [i, time, analyze[1]]
        table_probing.append(row)

    for i in loadfactor_chaining:

        control = new_controller("CHAINING", i)
        analyze = controller.load_data(control, "-large.csv", True)
        time = controller.load_data(control, "-large.csv", False)
        row = [i, time, analyze[1]]
        table_chaining.append(row)

    return table_probing, table_chaining

def print_results(table_probing, table_chaining):
    print("Tabla de tiempos y memoria para el tipo de tabla Hashing: Probing")
    print(tabulate(table_probing, headers=["Load Factor", "Tiempo", "Memoria"], tablefmt="fancy_grid"))
    print("Tabla de tiempos y memoria para el tipo de tabla Hashing: Chaining")
    print(tabulate(table_chaining, headers=["Load Factor", "Tiempo", "Memoria"], tablefmt="fancy_grid"))

def cmpNormal(data1, data2):

    if data1 > data2:
        return False
    else:
        return True

def search_number(list: adt.List):

    a = randint(0,100)
    if list.isPresent(a) != 0:
        print(f"The number is : {a}")
        return a
    else:
        return search_number(list)



def test_search_algorithms():

    my_list = adt.List("ARRAY_LIST")

    for i in range(200):

        my_list.addLast(randint(0, 100))

    my_list.sort(cmpNormal)

    number = search_number(my_list)

    pos = my_list.binarySearch(number)

    print(f"The pos of the element is: {pos}")
    print(f"The element must be: {my_list.getElement(pos)}")

    return my_list.elements

def test_search_algorithms_erro():

    my_list = adt.List("ARRAY_LIST")

    for i in range(200):

        my_list.addLast(randint(0, 100))

    number = search_number(my_list)

    pos = my_list.binarySearch(number)

    return pos













                



