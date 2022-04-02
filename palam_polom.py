import random
options=["🤚","✋"]
computer1_score=0
computer2_score=0
user_score=0
scores=[]
for i in range(5):
    computer1_choice=random.choice(options)
    computer2_choice=random.choice(options)
    user_choice=input("Choose between 🤚 , ✋:")

    if(user_choice==options[0] and  computer1_choice==options[0] and computer2_choice==options[0]):
       computer1_score+=1
       computer2_score+=1
       user_score+=1

    elif(user_choice==options[0] and  computer1_choice==options[0] and computer2_choice==options[1]):
        user_score+=1
        computer1_score+=1

    elif(user_choice==options[0] and  computer1_choice==options[1] and computer2_choice==options[1]):
        computer1_score+=1
        computer2_score+=1

    elif(user_choice==options[0] and  computer1_choice==options[1] and computer2_choice==options[0]):
        computer2_score+=1
        user_score+=1

    elif(user_choice==options[1] and  computer1_choice==options[1] and computer2_choice==options[1]):
        computer1_score+=1
        computer2_score+=1
        user_score+=1

    elif(user_choice==options[1] and  computer1_choice==options[0] and computer2_choice==options[0]):
        computer1_score+=1
        computer2_score+=1

    elif(user_choice==options[1] and  computer1_choice==options[1] and computer2_choice==options[0]):
        computer1_score+=1
        user_score+=1

    elif(user_choice==options[1] and  computer1_choice==options[0] and computer2_choice==options[1]):
        computer2_score+=1
        user_score+=1

scores.append(user_score)
scores.append(computer1_score)
scores.append(computer2_score)

print("User Score:",user_score)
print("Computer1 Score:",computer1_score)
print("Computer2 Score:",computer2_score)

if(scores[0]>scores[1] and scores[0]>scores[2]):
    print("User won!")

elif(scores[1]>scores[0] and scores[1]>scores[2]):
    print("Computer1 won!")

elif(scores[2]>scores[0] and scores[2]>scores[1]):
    print("Computer2 won!")

else:
    print("Game has not winner")
