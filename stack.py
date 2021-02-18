from collections import Iterable


class Node:
    def __init__(self, value, parent: "Node" = None):
        self.value = value
        self.parent = parent


class Stack:
    def __init__(self, *args):
        self._last_node = None  # sentry
        if len(args) == 0:
            pass
        elif isinstance(args[0], Iterable):
            for i, value in enumerate(args[0]):
                if i == 0:
                    self._last_node = Node(value)
                else:
                    parent = self._last_node
                    self._last_node = Node(value, parent)

        else:
            self._last_node = Node(args[0])

    @property
    def top(self):
        if self._last_node is None:
            raise ValueError
        else:
            return self._last_node.value

    def pop(self):
        if self._last_node is None:
            raise ValueError
        else:
            popped_element = self._last_node.value
            self._last_node = self._last_node.parent
            self.depth -= 1
            return popped_element

    def push(self, new_element):
        self._last_node = Node(new_element, parent=self._last_node)

    @property
    def depth(self):
        counter = 0
        node = self._last_node
        while node is not None:
            counter += 1
            node = node.parent
        return counter

    @depth.setter
    def depth(self, value):
        self._depth = value  # why self._depth is underlined here?


if __name__ == "__main__":
    try:
        stack = Stack([1, 2, 3])
        stack.pop()
        stack.pop()
        print(stack.depth)
        print(stack.top)
    except ValueError:
        print("")




