

class Node:
    def __init__(self, value, parent: "Node" = None):
        self.value = value
        self.parent = parent


class Stack:
    def __init__(self, *items):
        self._depth = 0
        self._last_node = None
        for item in items:
            self.push(item)

    def push(self, new_element):
        self._last_node = Node(new_element, parent=self._last_node)
        self._depth += 1

    @property
    def top(self):
        if self._last_node is None:
            raise ValueError("Empty stack has no top")
        else:
            return self._last_node.value

    def pop(self):
        if self._last_node is None:
            raise ValueError("Empty stack cannot be popped")
        else:
            popped_element = self._last_node.value
            self._last_node = self._last_node.parent
            self._depth -= 1
            return popped_element


if __name__ == '__main__':
    stack = Stack(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    print(stack.top)
