from LinkedList import Node

# Accespts a linked list and reverses it in-place
def reverse(head):
    if not head:  # Handle empty linked list case
        return head

    curr = head  # Current link, used for iteration
    prev = None  # Keeps track of the previous link
    while curr:
        next = curr.next  # First, save a pointer to the next link
        curr.next = prev  # Update the current link to poin to the previous link
        prev = curr       # Shift the previous pointer forward
        curr = next       # Shift the current pointer forward (curr = curr.next)
    head = prev  # The last link is now the first link!
    return head  # Return the new head

# Constructs a linked list and reverses it using the reverse method aboce
items = ['B', 'C', 'D']
head = Node('A')
node = head  # ALWAYS make a copy of the head
for item in items:
    node.next = Node(item)
    node = node.next

print("The original linked list: ", head)
print("The reversed linked list: ", reverse(head))

# Output
# The original linked list:  A -> B -> C -> D
# The reversed linked list:  D -> C -> B -> A
