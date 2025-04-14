import unittest
from src.palindrome import is_palindrome

class TestEsPalindromo(unittest.TestCase):
    def test_palindromos(self):
        self.assertTrue(is_palindrome('radar'))  
        self.assertTrue(is_palindrome('anilina')) 
        self.assertTrue(is_palindrome('reconocer'))
        self.assertTrue(is_palindrome('oso'))
        self.assertTrue(is_palindrome('aibofobia'))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome('anita lava la tina'))
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))
        self.assertTrue(is_palindrome('a mama Roma le aviva el amor a mama'))
        self.assertTrue(is_palindrome('Madam, Im Adam'))
        self.assertTrue(is_palindrome('race a car'))
    
    def test_not_palindrome(self):
        self.assertTrue(is_palindrome('universidad'))
        self.assertTrue(is_palindrome('silla'))
        self.assertTrue(is_palindrome('computadora'))
        self.assertTrue(is_palindrome('trabajo'))
        self.assertTrue(is_palindrome('gato'))
       

if __name__ == '__main__':
    unittest.main()

