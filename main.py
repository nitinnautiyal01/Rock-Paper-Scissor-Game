import random

match = 0
hum_won = 0 # hum = human
comp_won = 0 # comp = computer
draw = 0

# To select option from Rock Paper Scissor, Choose number between 1,2,3

print("For Rock, Press 1")
print("For Paper, Press 2")
print("For Scissor, Press 3")


while match < 5:
    hum = int(input("Enter your input : "))
    comp = random.randint(1,3)
    match = match + 1

    print(f"Round : {match}")
    
    # if Match will Draw

    if comp == hum:
        if comp == 1:
            print("comp = rock")
            print("you = rock")

        if comp == 2:
            print("comp = paper")
            print("you = paper")
        
        if comp ==3:
            print("comp = scissor")
            print("you = scissor")
 

        print("Draw")
        draw += 1
    
    # If human wins

    elif (comp == 1 and hum == 2):
        print("comp = rock")
        print("you = paper")
        print("you win!")
        hum_won += 1

    elif (comp == 2 and hum == 3):
        print("comp = paper")
        print("you = scissor")
        print("you win!")
        hum_won += 1 

    elif (comp == 3 and hum == 1):
        print("comp = scissor")
        print("you = rock")
        print("you win!")
        hum_won += 1 
    
    # If computer wins

    elif (comp == 1 and hum == 3):
        print("comp = rock")
        print("you = scissor")
        print("you lose!")
        comp_won += 1 
        
    elif (comp == 2 and hum == 1):
        print("comp = paper")
        print("you = rock")
        print("comp win!")
        comp_won += 1   
       
    elif (comp == 3 and hum == 2):
        print("comp = scissor")
        print("you = paper")
        print("comp win!")
        comp_won += 1 
        
    # If human choose other number than 1,2,3

    else:
        print("Invalid Entry! Play Again")
        match -= 1


# Final Result

print(f"Total number of matches : {match}")
print(f"You won : {hum_won}")
print(f"Comp won : {comp_won}")
print(f"Draw : {draw}")
