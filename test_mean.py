import unittest
import mean

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(mean.avg([3.5,2,10,5,7.5]),5.6)
	def test2(self):
		self.assertEqual(mean.avg([]),-1)
	def test3(self):
		self.assertEqual(mean.avg([5,'r',10]),-1)
if __name__ == '__main__':
	unittest.main()

