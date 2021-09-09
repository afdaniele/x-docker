import unittest


class TestABC(unittest.TestCase):

    def setUp(self):
        self.my_var = None

    def test_A(self):
        self.assertTrue(True)

    def test_B(self):
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
