import unittest
from plutoRover import userInput
from plutoRover import calculate_direction
from plutoRover import current_direction

class plutoRoverTests(unittest.TestCase):

	def test_user_input_validation_accepted(self):

		self.assertTrue(userInput("FBFF") == "Accepted")
		self.assertTrue(userInput("FBLR") == "Accepted")


	def test_user_input_validation_rejected(self):
 
		self.assertTrue(userInput("FRSD") == "Rejected") # Invalid characters
		self.assertTrue(userInput("S QA /") == "Rejected") # No symbols or spaces allowed

	def test_calculate_direction_left(self):
		from plutoRover import calculate_direction
		calculate_direction("L")
		from plutoRover import current_direction
		self.assertEqual(current_direction, "W")

	def test_calculate_direction_right(self):
		from plutoRover import calculate_direction
		calculate_direction("R")
		from plutoRover import current_direction
		self.assertEqual(current_direction, "E")


    # Tests to Move forwards and backwards

if __name__=='__main__':
	unittest.main()

