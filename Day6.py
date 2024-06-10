#reeborg's_world_code
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
    
turn_left()        
    
while not at_goal():      
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
#https://reeborg.ca/reeborg.html?  
#note: run the code in maze and hurdles.   
