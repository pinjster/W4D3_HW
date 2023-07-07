from Node import Node

class LinkedList:

    def __init__(self, head_node_value):
        self.head = Node(head_node_value)

    def __repr__(self):
        nodes= []
        current_node = self.head
        while current_node:
            nodes.append(current_node.value)
            current_node = current_node.right
        return f'<LinkedList: {" -> ".join(nodes)}>'

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    def append_node(self, value):
        node = Node(value)
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        current_node.right = node
        pass

    def remove_node(self, value):
        if value  == self.head.value:
            self.head = self.head.right
        else:
            for node in self:
                if value == node.right.value:
                    node.right = node.right.right
                    return
            print(f"Value: {value} not found")

    def insert_node(self, value, prev_node):
        for n in self:
            if n.right and prev_node == n.value:
                new_node = Node(value)
                new_node.right = n.right
                n.right = new_node
                return
        print(f'{prev_node = } not valid')

    def get_tail(self):
        for n in self:
            if n.right == None:
                return n.value

    def remove_tail(self):
        for n in self:
            pass
        self.remove_node(n.value)

    def print_list(self):
        for n in self:
            print(n)

linked_list = LinkedList('monday')
linked_list.append_node('tuesday')
linked_list.append_node('wednesday')
linked_list.append_node('friday')

print(linked_list)

linked_list.insert_node('thursday', 'wednesday')
linked_list.insert_node('sunday', 'saturday')
print(linked_list.get_tail())
linked_list.print_list()
linked_list.remove_tail()

#for n in linked_list:
#    print(n)

#linked_list.remove_node('tuesday')

#print(f'{[node for node in linked_list]}')