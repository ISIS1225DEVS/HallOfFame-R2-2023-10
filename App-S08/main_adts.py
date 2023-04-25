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
from tabulate import tabulate
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

class List:
    """
    A custom list class that can use different data structures and comparison functions.

    Attributes:
        list: The underlying list object from the lt module.
        datastructure: The type of data structure used for the list ("ARRAY_LIST" or "SINGLE_LINKED").
        cmpfunction: The comparison function used to sort or search the list elements.
        sorted: A boolean flag indicating whether the list is sorted or not.
        elements: A reference to the list elements (either an array or a node).
    """
    
    def __init__(self, datastructure="ARRAY_LIST", cmpfunction=None, adt=None, sorted=False):
        """
        Initializes a List object with the given parameters.

        Args:
            datastructure (str): A string indicating the type of data structure to use for the list ("ARRAY_LIST" or "SINGLE_LINKED"). Defaults to "ARRAY_LIST".
            cmpfunction (function): A function that takes two elements as arguments and returns a negative number if the first element is less than the second, zero if they are equal, or a positive number if the first element is greater than the second. Defaults to None.
            adt (object): An existing list object from the lt module to use as the underlying list. Defaults to None.
            sorted (bool): A boolean flag indicating whether the list is sorted or not. Defaults to False.
        """
        if adt is not None:
            self.list = adt
            self.datastructure = adt["type"]
            self.cmpfunction = adt["cmpfunction"]
            self.sorted = sorted
            if self.datastructure == "ARRAY_LIST":
                self.elements = adt["elements"]
            else:
                self.elements = adt["first"]
        else:
            self.list = lt.newList(datastructure, cmpfunction)
            self.datastructure = datastructure
            self.cmpfunction = cmpfunction
            self.sorted = sorted
            if self.datastructure == "ARRAY_LIST":
                self.elements = self.list["elements"]
            else:
                self.elements = self.list["first"]
    
    def __str__(self) -> str:
        """
        Returns a string representation of the list.

        Returns:
            A string containing the list elements.
        """
        if self.datastructure == "ARRAY_LIST":
            return str(self.elements)
        else:
            return str(self.list["first"])
    
    def __len__(self) -> int:
        """
        Returns the number of elements in the list.

        Returns:
            An integer representing the size of the list.
        """
        return lt.size(self.list)
    
    def __iter__(self):
        """
        Returns an iterator over the list elements.

        Returns:
            An iterator object that can be used in a for loop or with next().
        """
        return lt.iterator(self.list)
    
    def __type__(self):
        """
        Returns a string describing the type of the list.

        Returns:
            A string containing the ADT name and the data structure name.
        """
        return f"ADT : list , Datastructure: {self.datastructure}"
    
    def addFirst(self, element):
        """
        Adds an element at the beginning of the list.

        Args:
            element: The element to be added to the list.

        Raises:
            Exception: If there is no space left in the list (only for array lists).
        """
        lt.addFirst(self.list, element)
    
    def addLast(self, element):
        """
        Adds an element at the end of the list.

        Args:
            element: The element to be added to the list.

        Raises:
            Exception: If there is no space left in the list (only for array lists).
        """
        lt.addLast(self.list, element)
    
    def isEmpty(self) -> bool:
        """
        Checks if the list is empty or not.

        Returns:
            True if the list has no elements, False otherwise.
        """
        return lt.isEmpty(self.list)
    
    def size(self) -> int:
        """
        Returns the number of elements in the list.

        Returns:
            An integer representing the size of the list.
        """
        return lt.size(self.list)
    
    def firstElement(self):
        """
        Returns the first element of the list.

        Returns:
            The element at the first position of the list, or None if the list is empty.
        """
        return lt.firstElement(self.list)
    
    def lastElement(self):
        """
        Returns the last element of the list.

        Returns:
            The element at the last position of the list, or None if the list is empty.
        """
        return lt.lastElement(self.list)
    
    def getElement(self, pos):
        """
        Returns the element at a given position of the list.

        Args:
            pos (int): An integer between 1 and the size of the list, indicating the position of the element to be returned.

        Returns:
            The element at the specified position of the list.

        Raises:
            IndexError: If the position is out of range (less than 1 or greater than the size of the list).
        """
        return lt.getElement(self.list, pos)
    
    def deleteElement(self, pos):
        """
        Deletes and returns the element at a given position of the list.

        Args:
            pos (int): An integer between 1 and the size of the list, indicating the position of the element to be deleted.

        Returns:
            The element that was deleted from the list, or None if the position is invalid.

        Raises:
            IndexError: If the position is out of range (less than 1 or greater than the size of the list).
        """
        return lt.deleteElement(self.list, pos)
    
    def removeFirst(self):
        """
        Removes and returns the first element of the list.

        Returns:
            The element that was removed from the list, or None if the list is empty.
        """
        return lt.removeFirst(self.list)
    
    def removeLast(self):
        """
        Removes and returns the last element of the list.

        Returns:
            The element that was removed from the list, or None if the list is empty.
        """
        return lt.removeLast(self.list)
    
    def insertElement(self, element, pos):
        """
        Inserts an element at a given position of the list.

        Args:
            element: The element to be inserted.
            pos (int): An integer between 1 and the size of the list + 1, indicating the position where the element will be inserted.

        Returns:
            True if the element was inserted successfully, False otherwise.

        Raises:
            IndexError: If the position is out of range (less than 1 or greater than the size of the list + 1).
        """
        return lt.insertElement(self.list, element, pos)
    
    def isPresent(self, element):
        """
        Checks whether an element is present in the list.

        Args:
            element: The element to be searched for.

        Returns:
            True if the element is present in the list, False otherwise.
        """
        return lt.isPresent(self.list, element)
    
    def exchange(self, pos1, pos2):
        """
        Exchanges the elements at two positions in the list.

        Args:
            pos1 (int): The position of the first element to be exchanged.
            pos2 (int): The position of the second element to be exchanged.

        Raises:
            IndexError: If either position is out of range (less than 1 or greater than the size of the list).
        """
        return lt.exchange(self.list, pos1, pos2)
    
    def changeInfo(self, pos, element):
        """
        Changes the value of an element in the list.

        Args:
            pos (int): The position of the element to be changed.
            element: The new value of the element.

        Raises:
            IndexError: If the position is out of range (less than 1 or greater than the size of the list).
        """
        return
    
    def subList(self, pos1, numElements):
        """
        Returns a new list that contains a portion of the original list.
        Args:
            pos1: the initial position of the sublist.
            numElements: the number of elements of the sublist.
        Returns:
            A new List object representing the sublist.
        """
        sub_list = lt.subList(self.list, pos1, numElements)

        sub_list = List(adt=sub_list)

        return sub_list
    
    def iterator(self):
        """
        Return the iterator for the list.
        """
        return lt.iterator(self.list)
    
    def sort(self, sort_criteria = None):
        """
        Sort the list.
        Args:
            sort_criteria: the criteria used to sort the list
        Returns:
            The sorted list or an error message if no sort criteria is specified.
        """
        if sort_criteria is None:
            return "No se ha especificado un criterio de ordenamiento"

        sorted_list = merg.sort(self.list, sort_criteria)

        self.sorted = True

        return sorted_list

    def isSorted(func):
        """
        Decorator that checks if the list is sorted before running a search method.
        Args:
            func: the function being decorated
        Returns:
            The decorated function.
        """
        def decorator(self, *args):

            if self.sorted:

                return func(self, *args)

            else:

                return "La lista no esta ordenada"

        return decorator




    @isSorted
    def linealSearch(self,element):
        """
        Perform a linear search on the list.
        Args:
            element: the element to look for in the list.
        Returns:
            The index of the element if found, None otherwise.
        """
        pos = None
        while pos == None:
            for list_element in self.list:
                if lt.getElement(self.list, pos) == element:
                    pos = pos
                    break
            element += 1
        return pos

    @isSorted
    def binarySearch(self, element):
        """
        Perform a binary search on the list.
        Args:
            element: the element to look for in the list.
        Returns:
            The index of the element if found, -1 otherwise.
        """
        # inicializar i en el inicio de la lista
        i = 0
        # inicializar f en el final de la lista
        f = lt.size(self.list)
        # inicializar pos en -1 para indicar que no se ha encontrado el elemento
        pos = -1
        # inicializar found en False
        found = False
        # mientras i sea menor o igual que f y found sea False
        while i <= f and not found:
            # calcular la posicion de la mitad entre i y f
            m = (i + f) // 2
            # si el elemento en la posicion m es igual al elemento buscado
            if lt.getElement(self.list, m) == element:
                # asignar m a pos
                pos = m
                # asignar True a found
                found = True
            # si el elemento en la posicion m es mayor que el elemento buscado
            elif lt.getElement(self.list, m) > element:
                # asignar m - 1 a f
                f = m - 1
            # si el elemento en la posicion m es menor que el elemento buscado
            else:
                # asignar m + 1 a i
                i = m + 1
        # retornar pos
        return pos

    @isSorted
    def binarySearchMin(self, element):
        """
        Find the minimum index of an element in a sorted list using binary search.
        Args:
            element: the element to look for in the list.
        Returns:
            The index of the first element in the list if there are duplicates or the element itself if there are no duplicates.
        """
        # Initialize variables
        m = 0
        i = 0
        f = lt.size(self.list)
        pos = -1
        found = False
        # Loop until the element is found or the list is empty
        while i <= f and not found:
            # Calculate the middle index
            m = (i + f) // 2
            # If the element is found, set the position and return
            if lt.getElement(self.list, m) == element:
                pos = m
                found = True
            # If the element is greater than the middle element, change the lower bound
            elif lt.getElement(self.list, m) > element:
                f = m - 1
            # If the element is less than the middle element, change the upper bound
            else:
                i = m + 1
        # If the element is found, find the minimum position
        if found == True:
            while lt.getElement(self.list, pos - 1) == element:
                pos -= 1
        # If the element is not found, find the position where the element should be inserted
        elif lt.getElement(self.list, m) > element:
            pos = m
            while lt.getElement(self.list, pos - 1) > element:
                pos -= 1
        return pos

    @isSorted
    def binarySearchMax(self, element):
        """
        Find the maximum index of an element in a sorted list using binary search.
        Args:
            element: the element to look for in the list.
        Returns:
            The index of the last element in the list if there are duplicates or the element itself if there are no duplicates.
        """
        m = 0
        i = 0
        f = lt.size(self.list)
        pos = -1
        found = False
        while i <= f and not found:
            m = (i + f) // 2
            # Compare the middle element with the given element
            if lt.getElement(self.list, m) == element:
                pos = m
                found = True
            # If the middle element is greater than the given element, then the element can only be present in the left subarray
            elif lt.getElement(self.list, m) > element:
                f = m - 1
            # If the middle element is smaller than the given element, then the element can only be present in the right subarray
            else:
                i = m + 1
        # If the element is found in the list, then we search for the last element in the list
        if found == True:
            while lt.getElement(self.list, pos + 1) == element:
                pos += 1
        # If the element is not in the list, then the position of the element is the position of the last smaller element
        elif lt.getElement(self.list, m) < element:
            pos = m
            while lt.getElement(self.list, pos + 1) > element:
                pos += 1
        return pos

class Stack:
    
    def __init__(self, datastructure = "DOUBLE_LINKED") -> object:

        self.stack = st.newStack(datastructure)
        self.datastructure = datastructure
    

    def __str__(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.stack["elements"])
        else:
            return str(self.stack["first"])

    def __len__(self) -> int:

        return st.size(self.stack)

    def __type__(self) -> str:

        return f"ADT : stack , Datastructure: {self.datastructure}"

    def elements(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.stack["elements"])
        else:
            return str(self.stack["first"])

    def push(self, element):

        st.push(self.stack, element)

    def pop(self):

        return st.pop(self.stack)

    def isEmpty(self) -> bool:

        return st.isEmpty(self.stack)

    def top(self):

        return st.top(self.stack)

    def size(self) -> int:

        return st.size(self.stack)

class Queue:

    def __init__(self, datastructure)-> object:

        self.queue = qu.newQueue(datastructure)
        self.datastructure = datastructure
        

    def __str__(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.queue["elements"])
        else:
            return str(self.queue["first"])
    def __len__(self) -> int:

        return qu.size(self.queue)

    def __type__(self) -> str:

        return f"ADT : queue , Datastructure: {self.datastructure}"

    def elements(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.queue["elements"])
        else:
            return str(self.queue["first"])
    def enqueue(self, element):

        qu.enqueue(self.queue, element)

    def dequeue(self):

        return qu.dequeue(self.queue)
    def peek(self):

        return qu.peek(self.queue)

    def isEmpty(self) -> bool:

        return qu.isEmpty(self.queue)
    def size(self) -> int:

        return qu.size(self.queue)

class HashMap():

    def __init__(self, numelements=17, maptype = "CHAINING", loadfactor = 4.0, cmpfunction = None):

        self.map = mp.newMap(numelements=numelements, maptype=maptype, loadfactor=loadfactor, cmpfunction=cmpfunction)
        self.maptype = maptype
        self.loadfactor = loadfactor
        self.cmpfunction = cmpfunction
        

    def __str__(self) -> str:

        return str(mp.keySet(self.map))

    def __len__(self) -> int:

        return mp.size(self.map)

    def type(self) -> str:

        return f"ADT : map , Datastructure: {self.maptype}"

    def put(self, key, value):

        mp.put(self.map, key, value)

    def get(self, key):

        return mp.get(self.map, key)

    def remove(self, key):

        return mp.remove(self.map, key)

    def contains(self, key):
        """
        Returns True if the key is in the map, False otherwise.

        Parameters:
        key (str): The key to search for in the map.

        Returns:
        bool: True if the key is in the map, False otherwise.
        """
        return mp.contains(self.map, key)


    def isEmpty(self) -> bool:

        return mp.isEmpty(self.map)

    def size(self) -> int:

        return mp.size(self.map)

    def keySet(self):

        keySet = mp.keySet(self.map)

        return List(adt=keySet)

    def valueSet(self):

        valueSet = mp.valueSet(self.map)

        return List(adt=valueSet)
