def classify_triangle(lengthA, lengthB, lengthC):
  """Classify Triangle
  Takes in your the lengths of your sides of your triangle and returns to you in a string what type of triangle you have.  precise to 2 decimal places.
  Args:
    lengthA (integer): length of a side of the triangle
    lengthB (integer): length of another side of the triangle
    lengthC (integer): length of yet another side of the triangle
  Return:
    String with the values "equilateral", "isosolese", "scalene", "right" or None if there were invalid inputs
  """
  # check if we got inputs
  if lengthA is None or lengthB is None or lengthC is None:
    return None

  #type checks allowing for polymorphism
  try:
    lengthA + 1
    lengthB + 1
    lengthC + 1
  except TypeError:
    return None

  # checks for false/true as they extend int in python but won't work here
  if lengthA is False or lengthB is False or lengthC is False:
    return None
  if lengthA is True or lengthB is True or lengthC is True:
    return None

  # BUG: should of checked that none of the inputs were zero oops!

  # check that the inputs are greater than zero
  if lengthA < 0 or lengthB < 0 or lengthC < 0:
    return None
  
  #sanitize inputs to ensure consistent precision
  roundedLengthA = round(lengthA, 2)
  roundedLengthB = round(lengthB, 2)
  roundedLengthC = round(lengthC, 2)
  #print(roundedLengthA, roundedLengthB, roundedLengthC)

  #classify the triangles
  if round( (lengthA + lengthB) / 2, 2) == roundedLengthA:
    return "equilateral"
  
  if round(lengthA ** 2 + lengthB ** 2, 2) == round(lengthC ** 2, 2):
    return "right"

  if roundedLengthA == roundedLengthB or roundedLengthB == roundedLengthC or roundedLengthC == roundedLengthA:
    return "isosolese"
  
  #all other options have been exhausted so it must be a scalene
  return "scalene"

if __name__ == '__main__':
  print('4, 5, 6 (scalene):', classify_triangle(4, 5, 6))
  print('4, 4, 4 (equilateral):', classify_triangle(4, 4, 4))
  print('3, 4, 5 (right):', classify_triangle(3, 4, 5))
  print('3, 4, 4 (isosolese):', classify_triangle(3, 4, 4))
  print('0.25, 0.4, 0.1 (isosolese):', classify_triangle(0.25, 0.4, 0.1))
  print('0.25, 0.4, 0.47 (right):', classify_triangle(0.25, 0.4, 0.47))
  print('0.25001111, 0.400111, 0.47111111 (right):', classify_triangle(0.25001111, 0.400111, 0.47111111))
  print('-1, 4, 4 (None):', classify_triangle(-1, 4, 4))
