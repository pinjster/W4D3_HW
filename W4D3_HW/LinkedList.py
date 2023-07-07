from Node import Node
class LinkedList():

    def __init__(self, value):
        self.head = Node(value)

    def __repr__(self):
        str_output = f'Linked List:'
        node_p = self.head
        while node_p.right:
            str_output += f' {node_p.value} ->'
            node_p = node_p.right
        str_output += f' {node_p.value}'
        return str_output
    
    def __iter__(self):
        current_n = self.head
        while current_n:
            yield current_n
            current_n = current_n.right

    def add_node(self, val):
        new_node = Node(val)
        for n in self:
            if n.right == None:
                n.right = new_node
                return
            
    def remove_node(self, val):
        if self.head.value == val:
            self.head = self.head.right
            return
        node_p = self.head
        while node_p.right:
            if node_p.right.value == val:
                node_p.right = node_p.right.right
                return
            else:
                node_p = node_p.right
        print(f'ERROR: {val} not found')

    def display_nodes(self):
        print(self)

    def insert_node(self, val):
        new_node = Node(val)
        if val < self.head.value:
            new_node.right = self.head
            self.head = new_node
            return
        node_p = self.head
        while node_p.right:
            if node_p.value < val < node_p.right.value:
                new_node.right = node_p.right
                node_p.right = new_node
                return
            node_p = node_p.right
        node_p.right = new_node
            

if __name__ == '__main__':
    new_list = LinkedList('N1')
    new_list.add_node('N5')
    new_list.add_node('N3')
    new_list.add_node('N2')
    new_list.add_node('N4')
    new_list.display_nodes()

    new_list.remove_node('N6')
    new_list.remove_node('N5')
    new_list.display_nodes()
    new_list.remove_node('N3')
    new_list.display_nodes()