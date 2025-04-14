import unittest

class TestEsPalindromo(unittest.TestCase):
    def test_palindromos(self):
        self.assertTrue(is_palindrome('radar'))  
        self.assertTrue(is_palindrome('anilina')) 
        self.assertTrue(is_palindrome('reconocer'))
        self.assertTrue(is_palindrome('oso'))
        self.assertTrue(is_palindrome('aibofobia'))


if __name__ == '__main__':
    unittest.main()

    