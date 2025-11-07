import unittest
import time
def Boss(Str: str) -> str:
    """
    Check if Boss Baby follows revenge rules: no shooting first, all shots avenged.
    Returns "Good boy" if rules followed, "Bad boy" otherwise.
    """
    n = len(Str)
    if n == 1 or Str[0] == 'R':  # Single char or Boss shoots first -> Bad boy
        return "Bad boy"
    
    counter = 0  # Track unavenged shots
    for char in Str:
        if char == 'S': 
            counter += 1  # Shot fired at Boss
        else:  # char == 'R'
            if counter > 0:  # Only count revenge if there are unavenged shots
                counter -= 1
    
    return "Good boy" if counter == 0 else "Bad boy"
    
#    Time Complexity: O(n) where n is the length of the string
#    Space Complexity: O(1) - only uses a single counter variable

class TestBossFunction(unittest.TestCase):
    def test_single_char(self):
        self.assertEqual(Boss("S"), "Bad boy")
        self.assertEqual(Boss("R"), "Bad boy")
        
    def test_form_tc(self):
        self.assertEqual(Boss("SRSSRRR"), "Good boy")
        self.assertEqual(Boss("RSSRR"), "Bad boy")
        self.assertEqual(Boss("SSSRRRRS"), "Bad boy")
        self.assertEqual(Boss("SRRSSR"), "Bad boy")
        self.assertEqual(Boss("SSRSRR"), "Good boy")
        

    def test_one_round(self):
        self.assertEqual(Boss("SSRR"), "Good boy")
        self.assertEqual(Boss("SR"), "Good boy")
        self.assertEqual(Boss("SSSRRR"), "Good boy")
        self.assertEqual(Boss("SSRRRRR"), "Good boy")
        self.assertEqual(Boss("SRRRRRRRRRR"), "Good boy")
        self.assertEqual(Boss("RSSSSS"), "Bad boy")
        self.assertEqual(Boss("SSSSSRR"), "Bad boy")

    def test_multiple_round(self):
        self.assertEqual(Boss("SSRRRSS"), "Bad boy")
        self.assertEqual(Boss("SRRRRRRRRRRSSSS"), "Bad boy")
        self.assertEqual(Boss("RSRSRRRSSS"), "Bad boy")
        self.assertEqual(Boss("SSSSRRRRS"), "Bad boy")
        self.assertEqual(Boss("SSRRSSRSRR"), "Good boy")
        self.assertEqual(Boss("SSRRSSRRRRRRR"), "Good boy")
        self.assertEqual(Boss("SSSSSRSSSSSSSSRSRSRSSSRRRR"), "Bad boy")
        
    def test_edge_cases(self):
        self.assertEqual(Boss("S" * 500000 + "R" * 499999), "Bad boy")
        self.assertEqual(Boss("S" * 500000 + "R" * 500000), "Good boy")
        large_balanced = "SR" * 500000
        self.assertEqual(Boss(large_balanced), "Good boy")
    
    def test_performance(self):
        large_input = "S" * 500000 + "R" * 500000 # Test with maximum size input
        start = time.time()
        result = Boss(large_input)
        end = time.time()
        
        self.assertEqual(result, "Good boy")
        print(f"Performance test completed in {end - start} seconds")
        self.assertLess(end - start, 1.0) 

        

if __name__ == '__main__':
    unittest.main()
