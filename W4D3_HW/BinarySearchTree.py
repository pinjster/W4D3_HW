from Node import Node
from LinkedList import LinkedList

class BST():

    def __init__(self, linked_list):
        self.linked_list = linked_list
        self.sorted_list = LinkedList(linked_list.head.value)
        self.head = Node(linked_list.head.value)
        self.add_list(linked_list)
        self.in_order_traversal()
        self.sorted_list.remove_node(self.sorted_list.head.value)

    def add_node(self, val):
        new_node = Node(val)
        node_p = self.head
        while node_p:
            if val < node_p.value:
                if node_p.left == None:
                    node_p.left = new_node
                    return
                node_p = node_p.left
            elif val > node_p.value:
                if node_p.right == None:
                    node_p.right = new_node
                    return
                node_p = node_p.right
            else:
                print(f'{val} already in Tree: Removed')
                return

    def add_list(self, list):
        for n in list:
            self.add_node(n.value)

    def in_order_traversal(self, n=None):
        if not n:
            n = self.head
        if n.left:
            self.in_order_traversal(n.left)
        self.sorted_list.add_node(n.value)
        if n.right:
            self.in_order_traversal(n.right)


if __name__ == '__main__':

    unsorted_linked_list = LinkedList(15)
    unsorted_linked_list.add_node(3)
    unsorted_linked_list.add_node(9)
    unsorted_linked_list.add_node(18)
    unsorted_linked_list.add_node(24)
    unsorted_linked_list.add_node(6)
    unsorted_linked_list.add_node(27)
    unsorted_linked_list.add_node(12)
    unsorted_linked_list.add_node(15)
    unsorted_linked_list.add_node(21)
    unsorted_linked_list.add_node(30)
    unsorted_linked_list.display_nodes()

    new_tree = BST(unsorted_linked_list)
    new_tree.sorted_list.display_nodes()