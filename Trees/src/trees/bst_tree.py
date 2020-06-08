import copy
from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')




class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
        """
        You must have at least one member named root

        :param root: The root node of the tree if there is one.
        If you are provided a root node don't forget to count how many nodes are in it
        :param key: The function to be applied to a node's value for comparison purposes.
        It serves the same role as the key function in the min, max, and sorted builtin
        functions
        """
        self.key = key
        self.root = root

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        return self.get_height(self.root)

    def get_height(self, node: BSTNode[T]) -> int:

        if node is None:
            return -1
        leftHeight = self.get_height(node.left)
        rightHeight = self.get_height(node.right)
        return 1 + max(leftHeight, rightHeight)


    def __len__(self) -> int:
        """
        :return: the number of nodes in the tree
        """
        if self.root == None:
            return 0
        else:
            return self.count_nodes(self.root)

    def count_nodes(self, my_node: BSTNode[T]):
        count = 1
        if my_node.left != None:
            count += self.count_nodes(my_node.left)
        if my_node.right != None:
            count += self.count_nodes(my_node.right)
        return count

    def add_value(self, value: T) -> None:
        """
        Add value to this BST
        Duplicate values should be placed on the right
        :param value:
        :return:
        """
        my_node = BSTNode(value)
        self.get_add(my_node)

    def get_add(self, node) -> None:
        if self.root is None:
            self.root = node
            node.left = None
            node.right = None
        else:
            cur = self.root
            while cur is not None:
                if self.key(node.value) < self.key(cur.value):
                    if cur.left is None:
                        cur.left = node
                        cur.left.parent = cur
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = node
                        cur.right.parent = cur
                        cur = None
                    else:
                        cur = cur.right
            node.left = None
            node.right = None




    def get_node(self, value: K) -> BSTNode[T]:
        """
        Get the node with the specified value
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        cur = self.root
        while cur is not None:
            if self.key(cur.value) == value:
                return cur
            elif value < self.key(cur.value):
                cur = cur.left
            else:
                cur = cur.right
        raise MissingValueError


    def rec_max(self, node : BSTNode[T]) -> BSTNode[T]:
        if node is None:
            raise EmptyTreeError
        else:
            if node.right is None:
                return node
            else:
                return self.rec_max(node.right)

    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        return(self.rec_max(self.root))

    def rec_min(self, node : BSTNode[T]) -> BSTNode[T]:
        if node is None:
            raise EmptyTreeError
        else:
            if node.left is None:
                return node
            else:
                return self.rec_min(node.left)

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """

        return self.rec_min(self.root)



    def remove_value(self, value: K) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
        if self.key(self.root.value) == value:
            if self.root.children == None:
                self.root = None
            else:
                self.bst_remove(self.root)
        else:
            node = self.get_node(value)
            self.bst_remove(node)


    def bst_remove(self, node_to_remove: BSTNode[T]) -> None:
        if node_to_remove.children == None:
            if node_to_remove.parent != None:
                node_to_remove.parent.remove_child(node_to_remove)
        elif node_to_remove.num_children == 1:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.left if node_to_remove.left is not None else node_to_remove.right)
        else:
            successor = self.rec_max(node_to_remove.left)
            self.bst_remove(successor)
            node_to_remove.value = successor.value



    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       BST(self.root.left) == BST(other.root.left) and \
                       BST(self.root.right) == BST(other.root.right)
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    def __deepcopy__(self, memodict) -> "BST[T,K]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        new_root = copy.deepcopy(self.root, memodict)
        new_key = copy.deepcopy(self.key, memodict)
        return BST(new_root, new_key)
