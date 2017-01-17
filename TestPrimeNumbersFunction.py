import unittest
import primeNumbers

class KnownValues(unittest.TestCase):

    def test_primeNumbers(self):
        result = primeNumbers.is_Prime(1)
        expected = None

        self.assertEqual(expected,result)
    def test_type(self):
        result = primeNumbers.is_Prime("hf")
        expected = "TypeError"
        self.assertEqual(expected,result)
        

    def test_not_equal(self):
        self.assertNotEqual(primeNumbers.is_Prime(1),"TypeError")

    def test_false(self):
        self.assertFalse(primeNumbers.is_Prime(1)!=None)

    def test_isPrime(self):
        self.assertEqual(primeNumbers.is_Prime(-5),"TypeError")

    def test_instance_of_type(self):
        self.assertIsInstance(primeNumbers.is_Prime("H"),str)

    def test_not_a_prime_number(self):
        self.assertNotEqual(5, primeNumbers.is_Prime(5))

    def test_acceptzero(self):
        self.assertEqual(primeNumbers.is_Prime(0),"TypeError")

    def test_accept_other_charcters(self):
        self.assertEqual(primeNumbers.is_Prime("847_(%)"),"TypeError")

    def test_negative_number(self):
        self.assertEqual(primeNumbers.is_Prime(-1),"TypeError")

    
       
        
if __name__=='__main__':
    unittest.main()

    
