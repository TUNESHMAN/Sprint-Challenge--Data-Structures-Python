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
        if self.capacity > len(self.storage):
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            self.size += 1  # after an item is added to the list, it will increase by 1
        else:
            removed_node = self.storage.head
            self.size -=1
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            if removed_node == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        list_buffer_contents.append(self.current.value)

        if self.current == self.storage.tail:
            node = self.storage.head
        else:
            node = self.current.next

        while node is not self.current:
            list_buffer_contents.append(node.value)
            node = node.next if node.next else self.storage.head

        return list_buffer_contents
