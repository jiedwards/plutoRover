import unittest
from plutoRover import userInput, calculate_direction, current_direction

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
		calculate_direction("R")
		from plutoRover import current_direction
		self.assertEqual(current_direction, "E")

	def test_calculate_direction_invalid_input(self):
		from plutoRover import calculate_direction
		calculate_direction("H")
		from plutoRover import current_direction
		self.assertEqual(current_direction, "N")

# The movement below is happening consecutively as though the rover was live.
	def test_calculate_movement_forward_facing_E(self):
		from plutoRover import calculate_movement
		calculate_movement("F", "E")
		from plutoRover import x, y
		self.assertEqual(x, 1)
		self.assertEqual(y, 0)

	def test_calculate_movement_forward_facing_N(self):
		from plutoRover import calculate_movement
		calculate_movement("F", "N")
		from plutoRover import x, y
		self.assertEqual(x, 1)
		self.assertEqual(y, 1)

	def test_calculate_movement_forward_facing_S(self):
		from plutoRover import calculate_movement
		calculate_movement("F", "S")
		from plutoRover import x, y
		self.assertEqual(x, 1)
		self.assertEqual(y, 0)

	def test_calculate_movement_forward_facing_W(self):
		from plutoRover import calculate_movement
		calculate_movement("F", "W")
		from plutoRover import x, y
		self.assertEqual(x, 0)
		self.assertEqual(y, 0)

	def test_calculate_movement_backward__facing_E(self):
		from plutoRover import calculate_movement
		calculate_movement("B", "E")
		from plutoRover import x, y
		self.assertEqual(x, -1)
		self.assertEqual(y, 0)

	def test_calculate_movement_backward__facing_N(self):
		from plutoRover import calculate_movement
		calculate_movement("B", "N")
		from plutoRover import x, y
		self.assertEqual(x, -1)
		self.assertEqual(y, -1)

	def test_calculate_movement_backward__facing_S(self):
		from plutoRover import calculate_movement
		calculate_movement("B", "S")
		from plutoRover import x, y
		self.assertEqual(x, -1)
		self.assertEqual(y, 0)

	def test_calculate_movement_backward__facing_W(self):
		from plutoRover import calculate_movement
		calculate_movement("B", "W")
		from plutoRover import x, y
		self.assertEqual(x, 0)
		self.assertEqual(y, 0)

if __name__=='__main__':
	unittest.main()

