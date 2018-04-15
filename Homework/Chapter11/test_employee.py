import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.em = Employee('Wang', 'Ming', 10000)

    def test_give_default_raise(self):
        self.em.give_raise()
        self.assertEqual(self.em.salary, 15000)

    def test_give_custom_raise(self):
        """self.em的状态不会发生改变，和初始化状态一样"""
        self.em.give_raise(10000)
        self.assertEqual(self.em.salary, 20000)

if __name__ == '__main__':
    unittest.main()