import unittest
from decimal import *
from copy import deepcopy

class PotterKata(unittest.TestCase):
	
	def testCanRunTestHarness(self):
		self.assertEqual(2, 2)

	def testNewShoppingBasketHasPriceZero(self):
		basket = Basket()
		self.assertEqual(0, basket.checkout())
	
	def testAddingOneBookHasPrice7(self):
		basket = Basket()
		basket.add(PHILOSOPHERS_STONE)
		self.assertEqual(700, basket.checkout())
	
	def testAddingTwoDifferentBooksHasPrice13_30(self):
		basket = Basket()
		basket.add(PHILOSOPHERS_STONE)
		basket.add(CHAMBER_OF_SECRETS)
		self.assertEqual(1330, basket.checkout())
	
	def testAddingTwoSameBooksHasPrice14(self):
		basket = Basket()
		basket.add(PHILOSOPHERS_STONE)
		basket.add(PHILOSOPHERS_STONE)
		self.assertEqual(1400, basket.checkout())
	
	def testAddingTwoSameBooksAndOneDifferentBookHasPrice20_30(self):
		basket = Basket()
		basket.add(PHILOSOPHERS_STONE)
		basket.add(PHILOSOPHERS_STONE)
		basket.add(CHAMBER_OF_SECRETS)
		self.assertEqual(2030, basket.checkout())
	
	def testAddingTwoPairsOfBooksHasPrice26_60(self):
		basket = Basket()
		basket.add(PHILOSOPHERS_STONE)
		basket.add(PHILOSOPHERS_STONE)
		basket.add(CHAMBER_OF_SECRETS)
		basket.add(CHAMBER_OF_SECRETS)
		self.assertEqual(2660, basket.checkout())	
	
	def testAddingThreeDifferentBooksHasPrice18_90(self):
		basket = Basket()
		basket.add(PHILOSOPHERS_STONE)
		basket.add(CHAMBER_OF_SECRETS)
		basket.add(PRISONER_OF_AZKABAN)	
		self.assertEqual(1890, basket.checkout())

PHILOSOPHERS_STONE = 1
CHAMBER_OF_SECRETS = 2
PRISONER_OF_AZKABAN = 3

class Basket:
	
	def __init__(self):
		self.book_list = {}
		self.book_list[PHILOSOPHERS_STONE] = 0
		self.book_list[CHAMBER_OF_SECRETS] = 0
		self.book_list[PRISONER_OF_AZKABAN] = 0
		self.book_count = 0
		self.total_price = 0
	
	def add(self, book_number):
		self.book_list[book_number] += 1
		self.book_count += 1
		self.total_price += 700	
	
	def checkout(self):
		if (self.book_count == 0):
			return 0
		else:
			return (self.groupbooks()[0] * 700) + (self.groupbooks()[1] * 1330) + (self.groupbooks()[2] * 1890)
			
	
	def groupbooks(self):
		group_counts = [0, 0, 0]
		temp_book_list = deepcopy(self.book_list)
		group_counts[2] = self.calculate_triples(temp_book_list)
		group_counts[1] = self.calculate_doubles(temp_book_list)
		group_counts[0] = self.calculate_singles(temp_book_list)
		return group_counts	

	def calculate_triples(self, temp_book_list):
		triples_count = 0
		while(True):
			if (temp_book_list[PHILOSOPHERS_STONE] >= 1 and temp_book_list[CHAMBER_OF_SECRETS] >= 1 and temp_book_list[PRISONER_OF_AZKABAN] >= 1):
				triples_count += 1
				temp_book_list[PHILOSOPHERS_STONE] -= 1
				temp_book_list[CHAMBER_OF_SECRETS] -= 1
				temp_book_list[PRISONER_OF_AZKABAN] -= 1
			else:
				break	
		return triples_count
	
	def calculate_doubles(self, temp_book_list):
		doubles_count = 0
		while(True):
			if (temp_book_list[PHILOSOPHERS_STONE] >= 1 and temp_book_list[CHAMBER_OF_SECRETS] >= 1):
				doubles_count += 1
				temp_book_list[PHILOSOPHERS_STONE] -= 1
				temp_book_list[CHAMBER_OF_SECRETS] -= 1
			elif (temp_book_list[CHAMBER_OF_SECRETS] >= 1 and temp_book_list[PRISONER_OF_AZKABAN] >= 1):
				doubles_count += 1
				temp_book_list[CHAMBER_OF_SECRETS] -= 1
 				temp_book_list[PRISONER_OF_AZKABAN] -= 1
			elif (temp_book_list[PHILOSOPHERS_STONE] >= 1 and temp_book_list[PRISONER_OF_AZKABAN] >= 1):
				doubles_count += 1
				temp_book_list[PHILOSOPHERS_STONE] -= 1
 				temp_book_list[PRISONER_OF_AZKABAN] -= 1
			else:
				break
		return doubles_count

	def calculate_singles(self, temp_book_list):
		return sum(temp_book_list.values())
	
if __name__ == '__main__':
	unittest.main()
