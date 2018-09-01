import unittest
from triangles import classify_triangle

__SCALENE__ = "scalene"
__EQUILATERAL__ = "equilateral"
__RIGHT__ = "right"
__ISOSOLESE__ = "isosolese"
__NONE__ = None

class TestTriangles(unittest.TestCase) :
  """test cases for classify_triangles function
  """

  def test_scalene(self):
    """test scalene triangles
    """
    self.assertEqual(__SCALENE__, classify_triangle(4, 5, 6))
    self.assertEqual(__SCALENE__, classify_triangle(0.4, 0.5, 0.6))

  def test_equilateral(self):
    """test equilateral triangles
    """
    self.assertEqual(__EQUILATERAL__, classify_triangle(4, 4, 4))
    self.assertEqual(__EQUILATERAL__, classify_triangle(0.1, 0.1, 0.1))

  def test_right(self):
    """test right triangles
    """
    self.assertEqual(__RIGHT__, classify_triangle(3, 4, 5))
    self.assertEqual(__RIGHT__, classify_triangle(0.25, 0.4, 0.47))
  
  def test_isosolese(self):
    """test isosolese triangles
    """
    self.assertEqual(__ISOSOLESE__, classify_triangle(3, 4, 4))
    self.assertEqual(__ISOSOLESE__, classify_triangle(0.25, 0.4, 0.4))
  
  def test_precision_right(self):
    """ensure code is precise to only 2 decimal places for right triangles
    """
    self.assertEqual(__RIGHT__, classify_triangle(0.25001111, 0.400111, 0.47111111))
  
  def test_precision_isosolese(self):
    """ensure code is precise to only 2 decimal places for isosolese triangles
    """
    self.assertEqual(__ISOSOLESE__, classify_triangle(0.25, 0.405, 0.41))

  def test_precision_equilateral(self):
    """ensure code is precise to only 2 decimal places for equilateral triangles
    """
    self.assertEqual(__EQUILATERAL__, classify_triangle(4.001, 4.002, 4.003))

  def test_precision_scalene(self):
    """ensure code is precise to only 2 decimal places for scalene triangles
    """
    self.assertEqual(__SCALENE__, classify_triangle(0.44444, 0.555555, 0.666666))

  def test_bad_inputs(self):
    """testing invalid inputs, all these should return None
    """
    self.assertEqual(__NONE__, classify_triangle(-1, 4, 4))
    self.assertEqual(__NONE__, classify_triangle(4, -1, 4))
    self.assertEqual(__NONE__, classify_triangle(4, 4, -1))
    #BUG: this will fail on purpose
    self.assertEqual(__NONE__, classify_triangle(4, 0, 4))

if __name__ == '__main__':
    unittest.main()