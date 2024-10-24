def start():
    move()
    turn_left()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
at_goal() == True

while at_goal()!=True:
    start()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
