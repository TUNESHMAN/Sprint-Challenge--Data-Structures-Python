# We have to make an implementation of linked list here


class List_Node:
    def __init__(self, value, next=None, prev=None):
        # Here, I initialize the node
        self.value = value
        self.next = next
        self.prev = prev
# We need to wrap the value we are given in a node and place it next to this first node. It is possible the first node has a node next to it already

    def insert_after(self, value):
        # We store the node that is already beside the first node in a container
        current_next = self.next
        # The new next node will be the freshly created node
        self.next = List_Node(value, self, current_next)
        if current_next:
            current_next.prev = self.next
            
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev
    
    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
