

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self._diagram(self)

    def _diagram(self, node, top='', root='', bottom=''):
        if node is None:
            return f'{root} null\n'

        if node.left is None and node.right is None:
            return f'{root} {node.data}\n'

        a = self._diagram(
            node.right,
            f'{top} ',
            f'{top}┌──',
            f'{top}│ ',
        )

        b = f'{root}{node.data}\n'

        c = self._diagram(
            node.left,
            f'{bottom}│ ',
            f'{bottom}└──',
            f'{bottom} ',
        )
        return f'{a}{b}{c}'


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data=data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data=data)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data=data)
                        break
                    current = current.right

    def remove(self, data):
        '''
        find data in tree by get_node_with_parent function
        parent, node

        if there is 0 children:
            - at root
            - at leaf
        else if there is one child:
            -

        :param data:
        :return:
        '''

        parent, node = self.get_node_with_parent(data)
        if node is None:
            print("Not found")
            return False
        if parent is None and node is None:
            return False

        children_count = 0

        if node.left and node.right:
            children_count = 2
        elif node.left is None and node.right is None:
            children_count = 0
        else:
            children_count = 1

        print(f'parent: \n{parent}, node:\n {node}')
        print(f'children count: {children_count}')


        if children_count == 0:
            if parent:
                # at leaf
                if parent.right is node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                # at root
                self.root = None
        elif children_count == 1:
            if node.left:
                next_node = node.left
            else:
                next_node = node.right
                
            if parent:
                if parent.left is node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.root = next_node
        else:
            parent_leftmost_node, leftmost_node = self.find_in_order_successor(node.right)
            print(f'parent_leftmost_node\n{parent_leftmost_node}')
            print(f'leftmost_node\n{leftmost_node}')
            node.data = leftmost_node.data
            parent_leftmost_node.left = None
            if parent_leftmost_node is leftmost_node:
                node.right = None

            # check if leftmost_node is a direct child of the node
            if parent_leftmost_node is node:
                node.data = leftmost_node.data
                node.right = leftmost_node.right
            else:
                node.data = leftmost_node.data
                parent_leftmost_node.left = leftmost_node.right

            return True


    def find_in_order_successor(self, node):
        current = node
        parent = node
        while current.left:
            parent = current
            current = current.left
        return parent, current



    def get_node_with_parent(self, data):
        parent = None
        current = self.root
        while current:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        return parent, None


    def search(self, data):
        current = self.root
        while True:
            if current is None:
                return None
            elif current.data == data:
                return current
            elif data > current.data:
                current = current.right
            else:
                current = current.left


    def find_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    def find_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current

    def inorder(self, node):
        current = node
        if current is None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

    def preorder(self,node):
        current = node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left)
        self.preorder(current.right)

    def postorder(self, node):
        current = node
        if current is None:
            return
        self.postorder(current.left)
        self.postorder(current.right)
        print(current.data)

    def __str__(self):
        return f'{self.root}'

# BIG-CASE: found node have 2 children
# # CASE: found node is root
# tree = BinaryTree()
# tree.insert(8)
# tree.insert(10)
# tree.insert(4)
# tree.insert(5)
# tree.insert(3)
# tree.insert(1)
# print(tree)
# tree.remove(8)
# print(tree)
#
# print('--- remove 4 ---')
# tree.remove(4)
# print(tree)


# CASE: Found node is a normal node
print('CASE: Found node is a normal node')
tree = BinaryTree()
tree.insert(5)
tree.insert(8)
tree.insert(7)
tree.insert(6)
tree.insert(4)
tree.insert(3)
tree.insert(1)
tree.insert(10)
tree.insert(9)
print(tree)
print('remove')
tree.remove(8)
print(tree)


# CASE: found node h


# print('remove 2')
# tree.remove(2)
# print(tree)
#
#
# print('--- remove 4 ---')
# tree.remove(4)
# print(tree)





