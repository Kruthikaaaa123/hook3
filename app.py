import unittest
def add(a,b):
  return a + b
def subtract(a,b):
  return a - b
def multiply(a,b):
  return a * b
class TestCalculator  
  
 def test_add(self):
  self.assertEqual(add(20,40),60)
 def test_subtract(self):
  self.assertEqual(subtract(20,15),5)
 def test_multiply(self):
  self.assertEqual(multiply(6,4),24)
if__name__=="__main__":
  print("student calculator application")
  print("addition:",add(20,20))
  print("subtraction:",subtract(20,10))
  print("multiplication:",multiply(5,4))
  print("\nExceuting automated tests.\n")
  unittest.main(argc=['first-arg-is-ignored'],exit=False)
