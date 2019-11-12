import unittest
from plutoRover import plutoRover

class plutoRoverTests(unittest.TestCase):

	def test_user_input_validation_accepted(self):

		self.assertTrue(plutoRover.userInput("FBFF") == "Accepted")
		self.assertTrue(plutoRover.userInput("FBLR") == "Accepted")


	def test_user_input_validation_rejected(self):
 
		self.assertTrue(plutoRover.userInput("FRSD") == "Rejected") # Invalid characters
		self.assertTrue(plutoRover.userInput("S QA /") == "Rejected") # No symbols or spaces allowed


		# Tests to ensure direction change works as expected.
       # "N","E","S","W"
       # pass in user input for direction change
       # if input == "L":
       # 	depending on userCurrent direction, change counter clockwise
       # elif input == "R":
       # 	depending on userCurrent direction, change clockwise
       # else: 
       # 	invalid

    # Tests to Move forwards and backwards

if __name__=='__main__':
	unittest.main()

