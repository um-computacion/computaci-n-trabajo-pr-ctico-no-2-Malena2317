import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.palindrome import is_palindrome

class TestEsPalindromo(unittest.TestCase):

    def test_simple_palindromes(self):
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
        self.assertFalse(is_palindrome('race a car')) # no es un palindromo por lo tanto es falso 
    
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome('universidad'))
        self.assertFalse(is_palindrome('silla'))
        self.assertFalse(is_palindrome('computadora'))
        self.assertFalse(is_palindrome('trabajo'))
        self.assertFalse(is_palindrome('gato'))

        #correcion ya que escribi mal la logica de los test , es false por que afirmo que estas palabras no son palindromos
       

    def test_edge_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('A'))
        self.assertTrue(is_palindrome('aa'))
        self.assertTrue(is_palindrome('7'))


if __name__ == '__main__':
    unittest.main()

