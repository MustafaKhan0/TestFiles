from unittest import TestCase
import exponent

class Test_Exp(TestCase):
    
    def test_exp(self):
        self.assertEqual(exponent.exp(3,3), 27)
