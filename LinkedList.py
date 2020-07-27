### Node definition
class Node:
    # Class constructor
    def __init__(self, value):
        self.value = value
        self.next = None
    # Used for pretty-printing the linked list
    def __repr__(self):
        curr = self
        str = ""
        while curr:
            str += curr.value
            curr = curr.next
            if curr:
                str += " -> "
        return str
