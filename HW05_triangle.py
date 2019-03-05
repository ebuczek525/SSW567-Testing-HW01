"""This module is a triangle function"""

def classify_triangle(a, b, c):

    """This function's docstring"""

    if a == b == c:
        return 'This is an equilateral triangle.'
    if ((a + b < c) or (a + c < b) or (b + c < a)):
        return 'This is not a valid triangle.'
    if ((a**2 + b**2 == round(c**2)) and ((a == b) or (b == c) or (a == c))):
        return 'This is an isoceles right triangle.'
    if ((a == b) or (b == c) or (a == c)):
        return 'This is an isoceles triangle.'
    if ((a**2 + b**2 == round(c**2)) and ((a != b) and (a != c) and (b != c))):
        return 'This is a scalene right triangle.'
    if ((a != b) and (a != c) and (b != c)):
        return 'This is a scalene triangle.'
