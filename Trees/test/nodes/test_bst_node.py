import unittest

from Trees.src.nodes.bst_node import BSTNode


class TestBSTNode(unittest.TestCase):
    def test_create_childless_node(self):
        node1 = BSTNode(5)
        self.assertEqual(node1.left, None)
        self.assertEqual(node1.right, None)
        self.assertEqual(node1.children, None)
        node2 = BSTNode("hello")
        self.assertEqual(node2.left, None)
        self.assertEqual(node2.right, None)
        self.assertEqual(node2.children, None)

    def test_create_node(self):
        node1 = BSTNode(25)
        node3 = BSTNode(30)
        node4 = BSTNode(15)
        node2 = BSTNode(20, [node4, node3], node1 )
        self.assertEqual(node2.parent, node1)
        self.assertEqual(node2.left.value, 15)
        self.assertEqual(node2.right.value, 30)
        self.assertEqual(node2.children, [node4, node3])
        self.assertEqual(node2.left, node4)
        self.assertEqual(node2.right, node3)

    def test_remove_child(self):
        node1 = BSTNode(25)
        node3 = BSTNode(30)
        node4 = BSTNode(15)
        node2 = BSTNode(20, [node4, node3], node1)
        node2.remove_child(node3)
        self.assertEqual(node2.left, node4)
        self.assertEqual(node2.right, None)
        self.assertEqual(node2.num_children, 1)

    def test_replace_child(self):
        node1 = BSTNode(25)
        node3 = BSTNode(30)
        node4 = BSTNode(15)
        node2 = BSTNode(20, [node4, node3], node1)
        node5 = BSTNode(45)
        node2.replace_child(node3, node5)
        self.assertEqual(node2.left, node4)
        self.assertEqual(node2.right, node5)
        node6 = BSTNode(13)
        node2.replace_child(node4, node6)
        self.assertEqual(node2.left, node6)
        self.assertEqual(node2.right, node5)




if __name__ == '__main__':
    unittest.main()
