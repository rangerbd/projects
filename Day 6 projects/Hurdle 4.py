def jump():
    turn_left()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while at_goal()==False:
    if front_is_clear():
        move()
        if wall_on_right()== False:
            turn_right()
       
            
            
    else:
        turn_left()
        
  
        
    

    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
