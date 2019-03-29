import unittest
from pairassignment import *

class Testpair(unittest.TestCase):
	"""Test tax"""
	def test_tax(self):
		self.assertEqual(4795,final_tax(360000,200000))

	def test1_tax(self):
		self.assertEqual(0,final_tax(50000,0))

	def test2_tax(self):
		self.assertEqual(0,final_tax(100000,50000))

	def test3_tax(self):
		self.assertEqual(0,final_tax(150000,100000))

	def test4_tax(self):
		self.assertEqual(422,final_tax(200000,150000))

	def test5_tax(self):
		self.assertEqual(4391,final_tax(350000,200000))

	def test6_tax(self):
		self.assertEqual(10146,final_tax(400000,350000))

	def test7_tax(self):
		self.assertEqual(19125,final_tax(450000,400000))

	def test8_tax(self):
		self.assertEqual(34500,final_tax(500000,450000))

	def test9_tax(self):
		self.assertEqual(51500,final_tax(550000,500000))

	def test10_tax(self):
		self.assertEqual(68500,final_tax(600000,550000))

	def test11_tax(self):
		self.assertEqual(1507,final_tax(250000,200000))

	def test12_tax(self):
		self.assertEqual(3492,final_tax(300000,250000))

	def test13_tax(self):
		self.assertEqual(586400,final_tax(2040000,2172000))

	def test14_tax(self):
		self.assertEqual(15210,final_tax(500000,100000))

if __name__ == '__main__':
	unittest.main()