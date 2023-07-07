from Node import Node

class BST:

    def __init__(self, head_node_value):
        self.head_node = Node(head_node_value)
        
    def add_node(self, value, node = None):
        new_node = Node(value)
        if not node:
            node = self.head_node
        if value > node.value:
            if not node.right:
                node.right = new_node
            else:
                self.add_node(value, node.right)
        else:
            if not node.left:
                node.left = new_node
            else:
                self.add_node(value, node.left)

    def get_min(self, node_p=None):
        if not node_p:
            node_p = self.head_node
        if node_p.left:
            return self.get_min(node_p.left)
        else:
            return node_p

    def get_max(self):
        node_p = self.head_node
        while node_p.right:
            node_p = node_p.right
        return node_p

    def search_node(self, value, node_p=None):
        if not node_p:
            node_p = self.head_node
        if value == node_p.value:
            return True
        elif value > node_p.value:
            return self.search_node(value, node_p.right) if node_p.right else False
        else:
            return self.search_node(value, node_p.left) if node_p.left else False


    def print_in_order(self, node=None):
        if not node:
            node = self.head_node
        if node.left:
            self.print_in_order(node.left)
        print(node.value)
        if node.right:
            self.print_in_order(node.right)

bst = BST(100)

print(bst)

bst.add_node(105)
bst.add_node(130)
bst.add_node(115)

bst.add_node(75)
bst.add_node(50)
bst.add_node(60)

print(bst.head_node.right.right.left)
print(bst.head_node.left, 75)
print(bst.head_node.left.left)
print(bst.head_node.left.left.right)

print(bst.get_min())
print(bst.get_max())

print(bst.search_node(105))
bst.print_in_order()