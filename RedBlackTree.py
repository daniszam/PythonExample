class Node:

    def __init__(self, parent, key = None):
        self.parent = parent
        self.isRed = True
        self.key = key
        self.left = None
        self.right = None

    def checkParent(self):
        if self.parent.isRed:
            grandparent = self.parent.parent
            if grandparent.left is self.parent:
                if grandparent.right.isRed:
                    grandparent.isRed = True
                    grandparent.left.isRed = False
                    grandparent.right.isRed = False

    def __str__(self):
        return str(self.key)


class BlackRedTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(None, key)
        if self.root is None:
            self.root = node
        else:
            parentnode = self.root
            while parentnode is not None:
                a = parentnode
                if parentnode.key < node.key:
                    parentnode = parentnode.right
                else:
                    parentnode = parentnode.left
            node.parent = a
            if a.key < node.key:
                a.right = node
            else:
                a.left = node
        self.__fix_insertion(node)

    def __fix_insertion(self, node):
        if node is self.root:
            node.isRed = False
            return
        while node.parent is not None and node.parent.isRed:
            parent = node.parent
            grand_parent = parent.parent
            if parent is grand_parent.left:
                if grand_parent.right is not None:
                    if grand_parent.right.isRed:
                        parent.isRed = False
                        grand_parent.right.isRed = False
                        grand_parent.isRed = True
                        node = grand_parent
                else:
                    if node is parent.right:
                        node = parent
                        self.__left_rotate(node)
                    parent.isRed = False
                    grand_parent.isRed = True
                    self.__right_rotate(grand_parent)
            else:
                if grand_parent.left is not None:
                    if grand_parent.left.isRed:
                        parent.isRed = False
                        grand_parent.left.isRed = False
                        grand_parent.isRed = True
                        node = grand_parent
                else:
                    if node is parent.left:
                        node = parent
                        self.__right_rotate(node)
                    parent.isRed = False
                    grand_parent.isRed = True
                    self.__left_rotate(grand_parent)
        self.root.isRed = False

    def delete(self, key):
        node = self.root
        while node.key != key:
            if node.key < key:
                node = node.right
            else:
                node = node.left
        if node.left is None and node.right is None:
            if node is self.root:
                self.root = None
            else:
                if node is node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            return
        if node.left is None or node.right is None:
            if node.left is not None:
                if node.parent.left is node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.right
            else:
                if node.parent.left is node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.right
        else:
            y = node.right
            right = node.right
            while right is not None:
                right = right.left
                if right is not None:
                    y = right
            if y.right is not None:
                y.right.parent = y.parent
                y.parent.left = y.right
            if y is self.root:
                self.root = y.right
            else:
                if y.right is not None:
                    y.parent.left = y.right
                    y.right.parent = y.parent
            if y is node.right:
                node.right = None
            else:
                y.parent.left = None
        if y is not node:
            rotate = node.isRed
            node.isRed = y.isRed
            node.key = y.key
        if not rotate:
            if node.right is not None:
                self.__fix_deleting(node.right)
            else:
                self.__fix_deleting(node.left)

    def __fix_deleting(self, node):
        while node.parent.isRed is False and node is not self.root:
            if node is node.parent.left:
                brother = node.parent.right
                if brother.isRed:
                    brother.isRed = False
                    node.parent.isRed = True
                    self.__left_rotate(node.parent)
                if brother.right.isRed and brother.left.isRed:
                    brother.isRed = True
                else:
                    if not brother.right.isRed:
                        brother.left.isRed = False
                        brother.isRed = True
                        self.__right_rotate(brother)
                    parent = node.parent
                    brother.isRed = parent.isRed
                    parent.isRed = False
                    brother.right.isRed = False
                    self.__left_rotate(parent)
                    node = self.root
            else:
                brother = node.parent.left
                if brother.isRed:
                    brother.isRed = False
                    node.parent.isRed = True
                    self.__right_rotate(node.parent)
                if brother.right.isRed and brother.left.isRed:
                    brother.isRed = True
                else:
                    if not brother.left.isRed:
                        brother.right.isRed = False
                        brother.isRed = True
                        self.__left_rotate(brother)
                    parent = node.parent
                    brother = parent
                    parent.isRed = False
                    brother.left.isRed = False
                    self.__right_rotate(parent)
                    node = self.root
        node.isRed = False
        self.root.isRed = False

    def __left_rotate(self, node):
        y = node.right
        node.right = y.left
        y.parent = node.parent
        if y.left is not None:
            y.left.parent = node
        if node.parent is None:
            self.root = y
        else:
            if node is node.parent.left:
                node.parent.left = y
            else:
                node.parent.right = y
        y.left = node
        node.parent = y

    def __right_rotate(self, node):
        y = node.left
        node.left = y.right
        y.parent = node.parent
        if y.right:
            y.right.parent = node
        if node.parent is None:
            self.root = y
        else:
            if node is node.parent.left:
                node.parent.left = y
            else:
                node.parent.right = y
        y.right = node
        node.parent = y

    def max(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key

    def min(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key

    def breadth_first_search(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while (len(queue) > 0):
            print(queue[0])
            print("right" + str(queue[0].right))
            print("left" + str(queue[0].left))
            print("is red : " + str(queue[0].isRed))
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


tree = BlackRedTree()
tree.insert(8)
tree.insert(5)
tree.insert(1)
tree.insert(6)
tree.insert(0)
tree.insert(4)
tree.insert(2)
tree.delete(5)
print(tree.max())
print(tree.min())
tree.breadth_first_search()
