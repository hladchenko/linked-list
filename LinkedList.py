from Node import Node


class LinkedList:
    size = 0

    def __init__(self, element):
        self.root = Node(element)
        self.size = 1

    def add(self, element):
        self._add(self.root, element)

    def _add(self, root, element):
        if not root.next:
            root.next = Node(element)
        else:
            self._add(root.next, element)
        self.size += 1;

    def print(self):
        self._print(self.root)

    def print(self, root):
        print("TODO")
