import unittest
import name 

class TestCase(unittest.TestCase):

	def test1(self):
		self.assertEqual(name.first_last("David","Cronk"),"DavidCronk")
	def test2(self):
		self.assertEqual(name.first_last("Don232","P5"),-1)
	def test3(self):
		self.assertEqual(name.first_last('',''),-1)
if __name__ == '__main__':
	unittest.main()

