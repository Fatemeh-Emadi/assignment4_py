import random

options=["Rock","Paper","Scissor"]
computer_score=0
user_score=0
for i in range(10):
    computer_choice=random.choice(options)
    user_choice=input("Choose 1.Rock 2.Paper 3.Scissor:")

    if user_choice=="Paper" and computer_choice=="Rock":
        user_score+=1
    elif user_choice=="Paper" and computer_choice=="Scissor":
        computer_score+=1
    elif user_choice=="Rock" and computer_choice=="Paper":
        computer_score+=1
    elif user_choice=="Rock" and computer_choice=="Scissor":
        user_score+=1
    elif user_choice=="Scissor" and computer_choice=="Paper":
        user_score+=1
    elif user_choice=="Scissor" and computer_choice=="Rock":
        computer_score+=1
    else:
        computer_score+=0
        user_score+=0

print("User:",user_score)
print("Computer:",computer_score)

if(user_score>computer_score):
    print("User Won")
elif(user_score<computer_score):
    print("Computer Won")
else:
    print("Draw")
