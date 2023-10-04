from Node import Node


class LinkedList:
    __size = 0

    def __init__(self, element):
        self.__first = Node(element)
        self.__last = self.__first
        self.__size = 1

    def add(self, element):
        if self.__first is None:
            self.__first = Node(element)
            self.__last = self.__first
        else:
            self.__last.next = Node(element)
            self.__last = self.__last.next
        self.__size += 1

    def remove(self, element):
        if self.__first.element == element:
            self.__first = self.__first.next
            self.__size -= 1
        else:
            prev = self.__first
            current = self.__first.next
            while current is not None:
                if current.element == element:
                    if current.next is not None:
                        prev.next = current.next
                    else:
                        self.__last = prev
                        prev.next = None
                    self.__size -= 1
                prev = current
                current = current.next

    def print_list(self):
        self.__print(self.__first)

    def __print(self, root):
        if root is not None:
            print(root.element)
            self.__print(root.next)

    def get_size(self):
        return self.__size

    def get_first(self):
        return self.__first.element

    def get_last(self):
        return self.__last.element

    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.__first = None
        self.__last = None
        self.__size = 0
