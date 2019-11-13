
def main():
	print("Hello FundApps!")

acceptedCommands = ["F", "B", "L", "R"]

def userInput(input):
	for input in list(input):
		if input not in acceptedCommands:
			return "Rejected"
		else:
			continue
	return "Accepted"

directions = { "N", "E", "S", "W"} # Calculate direction to identify which way user is facing.
current_direction = "N"

def calculate_direction(direction_command):
    global current_direction

   	# Left Rotation
    if direction_command == "L":
        if current_direction == "N":
        	current_direction = "W"
        elif current_direction == "E":
        	current_direction = "N"
        elif current_direction == "S":
        	current_direction = "E"
        elif current_direction == "W":
        	current_direction = "S"
    # Right Rotation    	
    elif direction_command == "R":
        if current_direction == "N":
        	current_direction = "E"
        elif current_direction == "E":
        	current_direction = "S"
        elif current_direction == "S":
        	current_direction = "W"
        elif current_direction == "W":
        	current_direction = "N"
    # Invalid Input sets position to default    	
    else:
    	current_direction = "N"
    return current_direction

x = 0
y = 0

def calculate_movement_forward(movement_command, direction, x, y):
	pass



# Move forward and backward

if __name__ == "__main__":
    main()