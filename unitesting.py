import unittest
from methods import lahya


class test_lahya(unittest.TestCase):
    def test_lower(self):
        obj = lahya('lahya','sri')
        self.assertEqual(obj.lower,'lahyasri')
    def test_islower(self):
        obj1 = lahya('lahya','sri')
        self.assertTrue(obj1.islower,'lahyasri')




