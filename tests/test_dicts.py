import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({1: 'January', 2: 'February', 3: 'March'}, 1), 'January')
        self.assertEqual(dicts.get_val({1: 'January', 2: 'February', 3: 'March'}, 3), 'March')
        self.assertEqual(dicts.get_val({1: 'January', 2: 'February'}, 3), 'git')
