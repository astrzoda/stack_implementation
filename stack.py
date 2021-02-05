from collections import Iterable
import pytest


class Node:
    def __init__(self, value, parent: "Node" = None):
        self.value = value
        self.parent = parent


class Stack:
    def __init__(self, new_element):
        self._node = Node(new_element)

    @property
    def depth(self):
        counter = 0
        node = self._node
        while node is not None:
            counter += 1
            node = node.parent
        return counter

    def push(self, new_element):
        self._node = Node(new_element, parent=self._node)

    def pop(self):
        if self.depth == 0:
            raise ValueError("Cannot use pop for empty stack")
        self._node = self._node.value


if __name__ == "__main__":
    stack = Stack("abc")

    # print("depth", stack.depth)
    stack.push("abc")
    # print("depth", stack.depth)
    stack.pop()
    print(stack.depth)

    # print(stack.top)
    # stack = Stack()
    # print(stack.depth)



