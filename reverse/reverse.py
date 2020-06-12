class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Initialize previous to none
        prev = None
        # Our current node will be the starting node
        current_node = self.head
        # Our current node will have a next which will be the previous node. So we need to traverse the list
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = prev
            # Our previous node becomes current node
            current_node = prev
            # Our current node becomes next_node
            current_node = next_node
        self.head = prev
