class plutoRover():
	
	def main():
		print("Hello FundApps!")

	def userInput(input):
		acceptedCommands = ["F", "B", "L", "R"]
		for input in list(input):
			if input not in acceptedCommands:
				return "Rejected"
			else:
				continue
		return "Accepted"

	directions = { "N", "E", "S", "W"} # Calculate direction to identify which way user is facing.

	def calculate_direction():
		current_direction = "N"

       # pass in user input for direction change
       # if input == "L":
       # 	depending on userCurrent direction, change counter clockwise
       # elif input == "R":
       # 	depending on userCurrent direction, change clockwise
       # else: 
       # 	invalid

    # Move forward and backward

	if __name__ == "__main__":
	    main()