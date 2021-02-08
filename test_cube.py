import unittest
import cube

class TestCase(unittest.TestCase):

	def test1(self):
		self.assertEqual(cube.volume(3.5),42.875)
	def test2(self):
		self.assertEqual(cube.volume(-2),-1)
	def test3(self):
		self.assertEqual(cube.volume('r'),-1)
if __name__ == '__main__':
	unittest.main()

