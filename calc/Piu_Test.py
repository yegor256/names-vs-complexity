import unittest
from Piu import Piu

class Piu_Test(unittest.TestCase):
    def test_tree(self):
        piu = Piu('clones_test/OneStatement.java')
        self.assertEqual(piu.tree(), 1)
