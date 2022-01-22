#What you need to know
#The functions move() and turn_left().
#The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
#How to use a while loop and an if statement.

def turn_right():		#turn_right function was not available in the code.
	for i in range(3):
		turn_left()

def conditionalMove():		#This will help to meet the problem of variable heights.		
	turn_left()
	move()
	turn_right()
	
#Now we need to execute the commands such that we can complete the race.

while not at_goal():
	if wall_in_front():
	while wall_in_front():
		conditionalMove()
	move()
	turn_right()
	while front_is_clear():
		move()
	turn_left()
#The above commands will help to clear the hurdle of variable heights because, at first we climb the heights and then we have to move forward until we reach to x-axis
	elif front_is_clear():
		move()
#Here, we will keep moving forward until front we reach to the wall/at goal
