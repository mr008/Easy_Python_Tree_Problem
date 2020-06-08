import unittest
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode


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


        self.assertEqual(tree1.height, 3)
        self.assertEqual(tree2.height, -1)
        self.assertEqual(tree3.height, 1)

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
        pass

    def test_get_node(self):
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

        self.assertEqual()

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

        self.assertEqual()

    def remove_value(self):
        pass


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
