#!/usr/bin/python3

"""
Singly linked list implementation
"""

class Node:
    """
    Singly linked list implementation

    """
    
    def __init__(self, data, next_node=None):
        self.__data = None
        self.__next_node = None
        if type(data) == int:
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if next_node == None or type(next_node) == Node:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")


    @property
    def data(self):
        """
        retrieve node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set value of data of current node
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        return next node that this node links to
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node

        """
        if (value == None or type(value) == type(Node(1))):
            self.__next_node = value
            return 
        raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    SinglyLinked List implementatiion
    """

    def __init__(self):
        """
        
        initialize the linked list


        """
        self.__head = None
        self.temp = None

    def __str__(self):
        """
        print nodes
        """
        temp = self.__head
        results = ""
        while (temp != None):
            results += str(temp.data)+"\n"
            temp = temp.next_node
        return results
    
    def sorted_insert(self, value):
        """
        insert node into the node
        """
        self.temp = self.__head
        if (self.temp == None):
            print("1: ", value)
            self.__head = Node(value)
        elif (self.temp.data < value):
            print("2: ", value)
            self.__head = Node(value)
            print('xsd')
            print(self.temp.data)
            self.__head.next_node = self.temp
            print(self.__head.data)
        else:
            while (self.temp.next_node != None):
                if self.temp.next_node > value:
                    self.temp = self.temp.next_node
                else:
                    temp2= Node(value)
                    temp2.next_node(self.temp.next_node)
                    self.temp.next_node(temp2)
                    return
            temp2 = Node(value)
            temp2.next_node(self.temp.next_node)
            self.temp.next_node(temp2)
            return 

