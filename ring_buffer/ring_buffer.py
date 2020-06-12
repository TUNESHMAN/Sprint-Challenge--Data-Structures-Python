from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        # It is important to state that from the illustration given, the Ring_Buffer operates on a FIFO principle. Hence, it is a queue.
        self.capacity = capacity
        self.current = None
        self.size = 0  # We may also want to keep track of the size of the linked list
        self.storage = DoublyLinkedList()

    # This method will enqueue the new item into the list
    def append(self, item):
        if self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
            self.size += 1  # after an item is added to the list, it will increase by 1
        else:
            current_node = None
            node = self.storage.head
        while current_node is None and node is not None:
            if node.value == self.current:
                current_node = node
            node = node.next
        # It is also possible that the node is at the tail
            if current_node is self.storage.tail:
                self.storage.delete(self.storage.head)
                self.storage.add_to_head(item)
            else:
                current_node.insert_after(item)
                self.storage.delete(current_node)
        self.current = item

    def get(self):
        list_buffer_contents = []
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents
