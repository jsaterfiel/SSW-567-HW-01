"""Classify Triangle
Takes in your the lengths of your sides of your triangle and returns to you in a
string what type of triangle you have.  precise to 2 decimal places.
@author: John Saterfiel
"""

def classify_triangle(side_a, side_b, side_c): # pylint: disable=R0911
    """Classify Triangle
    Takes in your the lengths of your sides of your triangle and returns to you in a
    string what type of triangle you have.  precise to 2 decimal places.
    Returns a string with the values "equilateral", "isosolese", "scalene", "right"
    or None if there were invalid inputs
    Args:
        side_a (integer): length of a side of the triangle
        side_b (integer): length of another side of the triangle
        side_c (integer): length of yet another side of the triangle
    Return:
        String, None
    """
    # check if we got inputs
    if side_a is None or side_b is None or side_c is None:
        return None

    #type checks allowing for polymorphism
    try:
        side_a + 1 # pylint: disable=W0104
        side_b + 1 # pylint: disable=W0104
        side_c + 1 # pylint: disable=W0104
    except TypeError:
        return None

    # checks for false/true as they extend int in python but won't work here
    if side_a is False or side_b is False or side_c is False:
        return None
    if side_a is True or side_b is True or side_c is True:
        return None

    # BUG: should of checked that none of the inputs were zero oops!

    # check that the inputs are greater than zero
    if side_a < 0 or side_b < 0 or side_c < 0:
        return None

    #sanitize inputs to ensure consistent precision
    rnd_side_a = round(side_a, 2)
    rnd_side_b = round(side_b, 2)
    rnd_side_c = round(side_c, 2)
    #print(rnd_side_a, rnd_side_b, rnd_side_c)≈

    #classify the triangles
    if round((side_a + side_b) / 2, 2) == rnd_side_a:
        return "equilateral"

    if round(side_a ** 2 + side_b ** 2, 2) == round(side_c ** 2, 2):
        return "right"

    if rnd_side_a == rnd_side_b or rnd_side_b == rnd_side_c or rnd_side_c == rnd_side_a:
        return "isosolese"

    #all other options have been exhausted so it must be a scalene
    return "scalene"

if __name__ == '__main__': # pragma: no cover
    print('4, 5, 6 (scalene):', classify_triangle(4, 5, 6))
    print('4, 4, 4 (equilateral):', classify_triangle(4, 4, 4))
    print('3, 4, 5 (right):', classify_triangle(3, 4, 5))
    print('3, 4, 4 (isosolese):', classify_triangle(3, 4, 4))
    print('0.25, 0.4, 0.1 (isosolese):', classify_triangle(0.25, 0.4, 0.1))
    print('0.25, 0.4, 0.47 (right):', classify_triangle(0.25, 0.4, 0.47))
    print('0.25001111, 0.400111, 0.47111111 (right):', \
        classify_triangle(0.25001111, 0.400111, 0.47111111))
    print('-1, 4, 4 (None):', classify_triangle(-1, 4, 4))
