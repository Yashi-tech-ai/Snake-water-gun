"""snake - water = snake 
snake - gun = gun 
water - gun = water 
water - snake = snake 
gun - snake = gun 
gun - water = water
"""
import random 
game_dict = {"snake":1, "water" :-1 , "gun":0}
reverse_dict = {1: "snake", -1: "water", 0: "gun"}
print(game_dict)
yourstring = input(("Enter your choice : ")).lower()
you = game_dict[yourstring] # here it matches the string to the number from game_dict
computer = random.choice([-1,1,0])
print(f"You chose {yourstring} and computer chose {reverse_dict[computer]}")

# Approach - 1
# if(computer == -1 and you == 1):
#     print("You win !!")
# elif(computer == -1 and you == 0):
#     print("you lose")
# elif(computer == -1 and you == -1):
#     print("its a tie")   
# elif(computer == 1 and you == -1):
#     print("you lose")   
# elif(computer == 1 and you == 0):
#     print("you win!!")   
# elif(computer == 1 and you == 1):
#     print("its a tie") 
# elif(computer == 0 and you == 1):
#     print("you lose")  
# elif(computer == 0 and you == -1):
#     print("you win!!")    
# elif(computer == 0 and you == 0):
#     print("its a tie") 
# else:
#     print("oops wrong input ")


# by checking the pattern of subtracting computer - you 
if((computer - you) == -1 or (computer - you) == 2 ):
    print("You lose")
elif((computer - you) == 1 or (computer - you) == -2):
    print("You win !!")
else:
     print("oops wrong input ")