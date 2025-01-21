import random

options = ['R','P','S']
user_score = 0
py_score = 0
draw = 0

print('--------------------------------------INTRODUCTION----------------------------------')
print('Hi!, I am Saksham . I have made this game for fun and moreover to implement the things that i learnt so far in python , I hope you enjoy this :) ')

print('---------------------------------------------------------------------------------------')

print('--------------------------------------RULES----------------------------------')
print('Firstly choose how many rounds you want to play , After that enter your choice . Which are R(ROCK),P(PAPER),S(SISSOR), after you have entered your choice , IF you win you get 1 point if Python Wins He gets 1 point. THANK YOU')

print('-------------------------------------------------------------------------------------')

print('--------------------------------------ALL THE BEST ----------------------------------')






i = input("--------------------How many times you want to play ? : ")
i = int(i) # type: ignore
a = 0
for a in range(i):
 

 computer = random.choice(options)
 user = input('------------------------Enter Your Choice : ')
 user = user.upper()

 if computer == user :
  print("Tie!","Python Choosed " + computer,'and You choosed '+ user)
  draw += 1

 elif computer == 'R' and user == 'P':
  print("You Won!","Python Choosed " + computer,'and You choosed '+ user)  
  user_score += 1
 
 elif computer == 'P' and user == 'S':
  print("You Won!","Python Choosed " + computer,'and You choosed '+ user)
  user_score += 1

 elif computer == 'S' and user == 'R':
  print("You Won!","Python Choosed " + computer,'and You choosed '+ user)
  user_score += 1

 else:
  print("Python Won !","Python Choosed " + computer,'and You choosed '+ user)  
  py_score += 1

  print("--------------------Next Round----------------")



 a += 1


if user_score > py_score :
 print('---------------------------------Congratulations You Won !--------------------------------------')
 print('Your Score : '+ str(user_score))
 print('Python Score : ' + str(py_score))
 print('Times Drawed : ' + str(draw)) #concatination only works in strings


elif user_score < py_score :
 print('-----------------------------------------Soory! You Lost---------------------------------------')
 print('Your Score : '+ str(user_score))
 print('Python Score : ' + str(py_score))
 print('Times Drawed : ' + str(draw))

else:
 print("------------------------------------------IT'S A TIE !!------------------------------------")
 print('Your Score : '+ str(user_score))
 print('Python Score : ' + str(py_score))
 print('Times Drawed : ' + str(draw))



print("--------------------------------THANK YOU FOR PLAYNG :)---------------------------")