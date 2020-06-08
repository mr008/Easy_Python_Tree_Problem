import copy
from typing import Generic, Iterable, TypeVar, Optional


T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: get the right child
    """
    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        self.value = value
        self.left = None
        self.right = None
        self.num_children = 0
        self.children = children
        if self.children is not None:
            for val in self.children:
                if val.value >= self.value:
                    self.right = val
                    self.num_children += 1
                if val.value < self.value:
                    self.left = val
                    self.num_children += 1
        self.parent = parent

    def remove_child(self, my_node : "BSTNode[T]") -> None:
        if self.left.value == my_node.value:
            self.left = None
            self.num_children -= 1
        if self.right.value == my_node.value:
            self.right = None
            self.num_children -= 1

    def replace_child(self, node1: "BSTNode[T]", node2: "BSTNode[T]") -> None:
        if self.left == node1:
            self.left = node2
        elif self.right == node1:
            self.right = node2

    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """

        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    def __deepcopy__(self, memodict) -> "BSTNode[T]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        copy_node = BSTNode(copy.deepcopy(self.value, memodict))
        copy_node.left = copy.deepcopy(self.left, memodict)
        copy_node.right = copy.deepcopy(self.right, memodict)
        return copy_node
