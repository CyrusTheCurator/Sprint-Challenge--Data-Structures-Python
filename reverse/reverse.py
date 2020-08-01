class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        return value

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
        return node

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
        if not self.head:
            return False

        current = self.head

        new_list = LinkedList()
        while current:
            new_list.add_to_head(current.value) 
            current = current.get_next()

        self.head = new_list.head
        return new_list


classo = LinkedList()

classo.add_to_head(9)
classo.add_to_head(8)
classo.add_to_head(7)
classo.add_to_head(6)
classo.add_to_head(5)
classo.add_to_head(4)

print(classo.head.value)
classo.reverse_list(classo.head, None)
print(classo.head.value)