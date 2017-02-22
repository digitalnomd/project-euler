import unittest
import first_10 as first

class TestLcs(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(first.problem1(), 233168)

    def test_problem2(self):
        self.assertEqual(first.problem2(), 4613732)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
