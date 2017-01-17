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

    
       
        
if __name__=='__main__':
    unittest.main()

    
