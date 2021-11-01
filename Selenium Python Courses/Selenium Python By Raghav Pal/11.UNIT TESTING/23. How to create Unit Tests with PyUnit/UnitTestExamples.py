import unittest

from Examples import Example

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")

    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
        print("This will run after every method")

    def test_add(self):
        result1 = Example.Addition(self, 30, 20)
        print("Addition is ", result1)
        self.assertEqual(result1, 50)
        self.assertEqual(result1, 50)
        # self.assertEqual(Example.Addition(self, 30, 20), 50)
        # self.assertEqual(Example.Addition(self, 0, 0), 0)
        # self.assertEqual(Example.Addition(self, 30, 10), 40)

    def test_sub(self):
        result2 = Example.Subtraction(self, 50, 10)
        print("Subtraction is ", result2)
        self.assertEqual(result2, 40)


if __name__ == '__main__':
    unittest.main()
