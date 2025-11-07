import unittest
import time
def Superman(n: int, k: int, pos: list[int]) -> int:
    """
    Find maximum chickens Superman can protect with roof of length k.
    Uses sliding window to find optimal roof placement covering range [start, start+k).
    """
    max_protection = 0
    right = 0  # Right pointer for sliding window
    
    for left in range(n):
        # Extend window to include all chickens within roof coverage
        while right < n and pos[right] < pos[left] + k:
            right += 1
        max_protection = max(max_protection, right - left)
    
    return max_protection

# Time Complexity: O(n) - each chicken is visited at most twice (once by left, once by right pointer)                                                    │ │
# Space Complexity: O(1) - only uses constant extra space 

class TestSupermanFunction(unittest.TestCase):
    def test_from_given_tc(self):
        self.assertEqual(Superman(5,5,[2,5,10,12,15]), 2)
        self.assertEqual(Superman(6,10,[1,11,30,34,35,37]), 4)
    
    def test_normal(self):
        self.assertEqual(Superman(0, 10, []), 0) # Zero chickens
        self.assertEqual(Superman(1, 10, [5]), 1) # Single chicken            
        self.assertEqual(Superman(5, 100, [1, 2, 3, 4, 5]), 5) # All chickens in range
        self.assertEqual(Superman(3, 5, [0, 10, 20]), 1) # Cover only one chicken at a time
        self.assertEqual(Superman(5, 1, [1, 2, 3, 4, 5]), 1) # Roof length of 1 (covers single point)
        self.assertEqual(Superman(5, 3, [1, 1, 1, 4, 5]), 3) # Multiple chickens at same position
        self.assertEqual(Superman(6, 5, [1, 2, 3, 20, 21, 22]), 3) # Two clusters of chickens
        self.assertEqual(Superman(0, 10, []), 0) # Zero chickens
        self.assertEqual(Superman(3, 0, [1, 2, 3]), 0) # Zero roof length
   
    def test_large_inputs(self):
        # Maximum size input
        large_positions = list(range(0, 1000000, 10))  # 100,000 chickens , [0,10,20,...999990]
        result = Superman(len(large_positions), 50, large_positions)
        self.assertEqual(result, 5)
        
        # All chickens in range of roof
        large_positions = list(range(1000000))  # 1,000,000 chickens
        result = Superman(len(large_positions), 1000001, large_positions)
        self.assertEqual(result, 1000000)  # All covered
        
    def test_performance(self):
        large_positions = list(range(0, 1000000, 10))  # 100,000 chickens , [0,10,20,...999990]
        start = time.time()
        result = Superman(len(large_positions), 50, large_positions)
        end = time.time()
        
        self.assertEqual(result, 5)
        print(f"Performance test completed in {end - start} seconds")
        self.assertLess(end - start, 1.0) 
        
        

if __name__ == '__main__':
    unittest.main()
