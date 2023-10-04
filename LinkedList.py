from Node import Node


class LinkedList:
    __size = 0

    def __init__(self, element):
        self.root = Node(element)
        self._size = 1

    def add(self, element):
        self.__add(self.root, element)

    def __add(self, root, element):
        if not root.next:
            root.next = Node(element)
            self._size += 1
        else:
            self.__add(root.next, element)

    def print_list(self):
        self.__print(self.root)

    def __print(self, root):
        if root is not None:
            print(root.element)
            self.__print(root.next)
