import unittest
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode
from Trees.src.errors import EmptyTreeError
from Trees.src.errors import MissingValueError

class TestBST(unittest.TestCase):

    def test_create_empty_tree(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)

    def test_create_tree(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)

    def test_get_height(self):
        tree1 = BST()
        tree2 = BST()
        tree3 = BST()

        tree1.root = BSTNode(23)
        tree1.root.right = BSTNode(27)
        tree1.root.left = BSTNode(5)
        tree1.root.right.right = BSTNode(30)
        tree1.root.right.right.right = BSTNode(33)
        tree1.root.right.right.right.right = BSTNode(49)
        tree1.root.right.left = BSTNode(24)
        tree1.root.left.left = BSTNode(3)
        tree1.root.left.right = BSTNode(8)

        tree2.root = None

        tree3.root = BSTNode(8)
        tree3.root.right = BSTNode(34)
        tree3.root.left = BSTNode(4)
        tree3.root.left.left = BSTNode(3)

        #self.assertEqual(tree1.height, 3)
        self.assertEqual(tree2.height, -1)
        #self.assertEqual(tree3.height, 1)

    def test_len(self):
        tree1 = BST()
        tree2 = BST()
        tree3 = BST()

        tree1.root = BSTNode(23)
        tree1.root.right = BSTNode(27)
        tree1.root.left = BSTNode(5)
        tree1.root.right.right = BSTNode(30)
        tree1.root.right.right.right = BSTNode(33)
        tree1.root.right.right.right.right = BSTNode(49)
        tree1.root.right.left = BSTNode(24)
        tree1.root.left.left = BSTNode(3)
        tree1.root.left.right = BSTNode(8)

        tree2.root = None

        tree3.root = BSTNode(8)
        tree3.root.right = BSTNode(34)
        tree3.root.left = BSTNode(4)
        tree3.root.left.left = BSTNode(3)

        self.assertEqual(len(tree1),9)
        self.assertEqual(len(tree2), 0)
        self.assertEqual(len(tree3), 4)

    def test_add_value(self):
        tree1 = BST()
        tree2 = BST()
        tree3 = BST()
        tree4 = BST(key = len)

        tree1.root = BSTNode(23)
        tree1.root.right = BSTNode(27)
        tree1.root.left = BSTNode(5)
        tree1.root.right.right = BSTNode(30)
        tree1.root.right.right.right = BSTNode(33)
        tree1.root.right.right.right.right = BSTNode(49)
        tree1.root.right.left = BSTNode(24)
        tree1.root.left.left = BSTNode(3)
        tree1.root.left.right = BSTNode(8)

        tree2.root = None

        tree3.root = BSTNode(8)
        tree3.root.right = BSTNode(34)
        tree3.root.left = BSTNode(4)
        tree3.root.left.left = BSTNode(3)
        tree3.root.left.left.left = BSTNode(1)

        tree4.root = BSTNode("help")
        tree4.root.right = BSTNode("weirdo")
        tree4.root.left = BSTNode("no")
        tree4.root.right.right = BSTNode("friendly")
        tree4.root.right.right.right = BSTNode("friendless")
        tree4.root.right.right.right.right = BSTNode("supercilious")
        tree4.root.right.left = BSTNode("there")
        tree4.root.left.left = BSTNode('n')
        tree4.root.left.right = BSTNode('yes')

        tree1.add_value(2)
        tree2.add_value(4)
        tree3.add_value(42)
        tree4.add_value("hello")

        self.assertEqual(tree1.root.left.left.left.value, 2)
        self.assertEqual(tree2.root.value, 4)
        self.assertEqual(tree3.root.right.right.value, 42)
        self.assertEqual(tree4.root.right.left.right.value, "hello")

    def test_get_node(self):
        tree1 = BST()
        tree2 = BST()
        tree3 = BST()
        tree4 = BST(key = len)

        tree1.root = BSTNode(23)
        tree1.root.right = BSTNode(27)
        tree1.root.left = BSTNode(5)
        tree1.root.right.right = BSTNode(30)
        tree1.root.right.right.right = BSTNode(33)
        tree1.root.right.right.right.right = BSTNode(49)
        tree1.root.right.left = BSTNode(24)
        tree1.root.left.left = BSTNode(3)
        tree1.root.left.right = BSTNode(8)

        tree2.root = None

        tree3.root = BSTNode(8)
        tree3.root.right = BSTNode(34)
        tree3.root.left = BSTNode(4)
        tree3.root.left.left = BSTNode(3)

        tree4.root = BSTNode("help")
        tree4.root.right = BSTNode("weirdo")
        tree4.root.left = BSTNode("no")
        tree4.root.right.right = BSTNode("friendly")
        tree4.root.right.right.right = BSTNode("friendless")
        tree4.root.right.right.right.right = BSTNode("supercilious")
        tree4.root.right.left = BSTNode("there")
        tree4.root.left.left = BSTNode('n')
        tree4.root.left.right = BSTNode('yes')

        self.assertEqual(tree1.get_node(23), tree1.root)
        self.assertEqual(tree1.get_node(49), tree1.root.right.right.right.right)
        #self.assertRaises(MissingValueError, tree1.get_node(40))
        #self.assertRaises(MissingValueError, tree2.get_node(2))
        self.assertEqual(tree3.get_node(4), tree3.root.left)
        self.assertEqual(tree4.get_node(12), tree4.root.right.right.right.right)
        self.assertEqual(tree4.get_node(1), tree4.root.left.left)

    def test_get_max_node(self):
        tree1 = BST()
        tree2 = BST()
        tree3 = BST()

        tree1.root = BSTNode(23)
        tree1.root.right = BSTNode(27)
        tree1.root.left = BSTNode(5)
        tree1.root.right.right = BSTNode(30)
        tree1.root.right.right.right = BSTNode(33)
        tree1.root.right.right.right.right = BSTNode(49)
        tree1.root.right.left = BSTNode(24)
        tree1.root.left.left = BSTNode(3)
        tree1.root.left.right = BSTNode(8)

        tree2.root = None

        tree3.root = BSTNode(8)
        tree3.root.right = BSTNode(34)
        tree3.root.left = BSTNode(4)
        tree3.root.left.left = BSTNode(3)

        self.assertEqual(tree1.get_max_node(), tree1.root.right.right.right.right)
        #self.assertRaises(EmptyTreeError, tree2.get_max_node())
        self.assertEqual(tree3.get_max_node(), tree3.root.right)

    def test_get_min_node(self):
        tree1 = BST()
        tree2 = BST()
        tree3 = BST()

        tree1.root = BSTNode(23)
        tree1.root.right = BSTNode(27)
        tree1.root.left = BSTNode(5)
        tree1.root.right.right = BSTNode(30)
        tree1.root.right.right.right = BSTNode(33)
        tree1.root.right.right.right.right = BSTNode(49)
        tree1.root.right.left = BSTNode(24)
        tree1.root.left.left = BSTNode(3)
        tree1.root.left.right = BSTNode(8)

        tree2.root = None

        tree3.root = BSTNode(8)
        tree3.root.right = BSTNode(34)
        tree3.root.left = BSTNode(4)
        tree3.root.left.left = BSTNode(3)
        tree3.root.left.left.left = BSTNode(1)


        self.assertEqual(tree1.get_min_node(), tree1.root.left.left)
        #self.assertRaises(EmptyTreeError, tree2.get_min_node())
        self.assertEqual(tree3.get_min_node(), tree3.root.left.left.left)

    def remove_value(self):
        tree1 = BST()
        tree2 = BST()
        tree3 = BST()
        tree4 = BST(key = len)

        tree1.root = BSTNode(23)
        tree1.root.right = BSTNode(27)
        tree1.root.left = BSTNode(5)
        tree1.root.right.right = BSTNode(30)
        tree1.root.right.right.right = BSTNode(33)
        tree1.root.right.right.right.right = BSTNode(49)
        tree1.root.right.left = BSTNode(24)
        tree1.root.left.left = BSTNode(3)
        tree1.root.left.right = BSTNode(8)

        tree2.root = None

        tree3.root = BSTNode(8)
        tree3.root.right = BSTNode(34)
        tree3.root.left = BSTNode(4)
        tree3.root.left.left = BSTNode(3)
        tree3.root.left.left.left = BSTNode(1)

        tree4.root = BSTNode("help")
        tree4.root.right = BSTNode("weirdo")
        tree4.root.left = BSTNode("no")
        tree4.root.right.right = BSTNode("friendly")
        tree4.root.right.right.right = BSTNode("friendless")
        tree4.root.right.right.right.right = BSTNode("supercilious")
        tree4.root.right.left = BSTNode("there")
        tree4.root.left.left = BSTNode('n')
        tree4.root.left.right = BSTNode('yes')

        tree4.remove_value(12)
        tree3.remove_value(4)
        tree1.remove_value(23)

        self.assertEqual(tree4.root.right.right.right.right, None)
        self.assertEqual(tree3.root.left, BSTNode(3))
        self.assertEqual(tree1.root, BSTNode(5))


    def test_tree_not_eq(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(92)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertNotEqual(tree, cmp_tree)

if __name__ == '__main__':
    unittest.main()
