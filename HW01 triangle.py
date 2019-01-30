import unittest, math

def classifyTriangle(a,b,c):
    
    if (a == b == c):
        return 'This is an equilateral triangle.'
    elif ((a + b < c) or (a + c < b) or (b + c < a)):
        return 'This is not a valid triangle.'
    elif (((a**2 + b**2 == round(c**2)) or (b**2 + round(c**2) == a**2) or (a**2 + round(c**2) == b**2)) and ((a == b) or (b == c) or (a == c))):
        return 'This is an isoceles right triangle.'
    elif ((a == b) or (b == c) or (a == c)):
        return 'This is an isoceles triangle.'
    elif ((a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2)) and ((a != b) and (a != c) and (b != c)):
        return 'This is a scalene right triangle.'
    elif ((a != b) and (a != c) and (b != c)):
        return 'This is a scalene triangle.'

class TriangleTest(unittest.TestCase):

    def testEquilateral(self):
        self.assertEqual(classifyTriangle(1,1,1), 'This is an equilateral triangle.')
    
    def testInvalid(self):
        self.assertEqual(classifyTriangle(1,1,3), 'This is not a valid triangle.')
    
    def testIsoRight(self):
        self.assertEqual(classifyTriangle(1,1,math.sqrt(2)), 'This is an isoceles right triangle.')
        
    def testIsoceles(self):
        self.assertEqual(classifyTriangle(2,2,3), 'This is an isoceles triangle.')
    
    def testScaRight(self):
        self.assertEqual(classifyTriangle(3,4,5), 'This is a scalene right triangle.')
        
    def testScalene(self):
        self.assertEqual(classifyTriangle(2,3,4), 'This is a scalene triangle.')
        
if __name__ == '__main__':
    unittest.main()