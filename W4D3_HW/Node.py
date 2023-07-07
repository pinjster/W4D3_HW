class Node():

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
        
    def __repr__(self):
        return f"Node: {self.value}"

if __name__ == '__main__':
    new_node = Node('NewNode')
    print(new_node)