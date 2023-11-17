from turtle import Turtle  , Screen 
import random 
screen = Screen()
race_one  = False 
screen.setup (width= 500 ,height=  400 )


user_bet = screen.textinput ("welcome " , prompt= "who will win ")
colors = ["red" , "orange" , "yellow" , "green" ,"blue" , "purple"]
riders = []
# create a 6 riders with colors and setup their position 
for i in range (6) : 
    # create 6 turtles with 6 colors 
    rider = Turtle (shape= "turtle" )
    rider.color (colors[i])
    # setup the position in y axe 
    height = - 150 + (60  * i )
    rider.penup ()
    rider.goto (-240 , height )
    riders.append(rider)

if user_bet : 
    race_one = True 

while race_one : 
    for rider in riders : 
        if rider.xcor() > 230 : 
            race_one = False 
            winner = rider.pencolor ()
            if user_bet == winner : 
                print ("you win ")
            else : 
                print (f"you lose the winner is {winner}")
    
       
       
       
       
        rider.forward (random.randint (0 , 10))
        
    
          
    




    






screen.exitonclick ()








