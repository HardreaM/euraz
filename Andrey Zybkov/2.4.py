class Tree:

    nodes = []
    depth = 1

    def __init__ (self):
        pass

    def get_all_in_level(self, level):
        for node in self.nodes:
            if node.get_level() == level:
                print(node.get_number(), node.get_value(), node.get_level())

    def set_node (self, node):
        node.set_number(len(self.nodes))
        if node.get_level() > self.depth:
            self.depth = node.get_level()
        self.nodes.append(node)

    def get_depth (self):
        print(self.depth)

    def nodes_in_level (self, level):
        count = 0
        for node in self.nodes:
            if node.get_level() == level:
                count += 1
        print(count)

    def get_node (self, number):
        for node in self.nodes:
            if node.get_number() == number:
                return node

    def get_nodes (self):
        return self.nodes

class Node:

    def __init__ (self, value, level, parent):
        if len(Tree.get_nodes(tree)) == 0:
            self.__root = True
        else:
            self.__root = False
        self.__value = value
        self.__level = level
        self.__parent = parent

    def set_number (self, number):
        self.__number = number

    def get_level (self):
        return self.__level

    def get_number (self):
        return self.__number
    
    def get_value (self):
        return self.__value

    def get_parents (self):
        pass

tree = Tree()
node1 = Node(5, 1, None)
node2 = Node(9, 2, [node1])
node3 = Node(12, 2, [node2])
tree.set_node(node1)
tree.set_node(node2)
tree.set_node(node3)
tree.get_all_in_level(2)
tree.get_depth()
tree.nodes_in_level(2)