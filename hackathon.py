#Rolling the dice

#Similar to the “Guess the Number” game above, building a die roller can be used to play games. 
#Or you can make one similar to a Magic 6-Ball to answer your most profound questions! Skills used: 
# Random library, print, while loops.

# import random
# a=[1,2,3,4,5,6]
# #print(random.choice(a))

# =int(input('1st person turn',print(random.choice(a)))
# =int(input('2nd person turn',print(random.choice(a)))

# Generates a random number between
# a given positive range
#import random
#r1 = random.randint(1,7)
#print("Random number between 5 and 15 is % s" % (r1))
  
# Generates a random number between
# two given negative range
#r2 = random.randint(1,7)
#print("Random number between -10 and -2 is % d" % (r2))

#a=input('1st person tern:',r1)
#b=input('1st person tern:',r2)
# import random
# again=True
# while again:
# 	print(random.randint(1,6))
# 	another_roll=input('want to roll the dice again?(y/n)')
# 	if another_roll.lower()=='y':
# 		continue
# 	else:
# 		break
#Qn-1

#guessing game using random function
# import random
# for i in range(1,6):
#     rand = int(random.randint(1,10))
#     inp = int(input("your guess number is :"))
#     print('my guess is: ', rand)
#     if inp == rand:
#         print("guessed")
#         break
#     else:
#         print("you guessed wrong")
#         if rand < inp:
#             print("your guess is greater")
#         else:
#             print("your guess is lesser")

#Qn-2 ###################################################

## die roller..
import random
print('welcome to dice rolling game: ')
s1=s2=0
#s2=0
for i in range(1,7):
    if 1<i<=6:
        f=input('roll again? (y/n):')   
        if f=='y':
            pass
        else:
            break
    p1=input('roll dice player 1: ')
    c=random.randint(1,6)
    print(c)
    s1+=c
    p2=input('roll dice player 2: ')
    d=(random.randint(1,6))
    print(d)
    s2+=d
print('player 1: ',s1,'\n','player 2: ',s2)
if s1>s2:
    print('player 1 is winner: congrats: ')
elif s2>s1:
    print('player 2 is winner: congrats: ')
else:
    print("it's a Tie: ")

#QN-3.############################################################################                


# print("""my name is Roshan and i am 23 year old.i am form nagpur maharashtra.
# 	i have currentlly graduction. R.T.M.nagpur univrsity and i am ncc student and my best frinds chetan and my best teacther sonune sir in junior college.""")
# a=0
# p=0
# while a<=5:
# 	print("""1)what is your name?
# 		1)amit
# 		2)roshan
# 		3)akash
# 		4)pradeep""")
# 	b=input("enter your choice:--  ")
# 	if b=="2":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""2)how to old i am?
# 			1)20
# 			2)21
# 			3)22
# 			4)23""")
# 	c=input("enter your choice:--  ")
# 	if c=="4":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""3)what is your loction?
# 			1)bhandra
# 			2)tumsar
# 			3)nagpur
# 			4)dharmashala""")
# 	d=input("enter your choice:--  ")
# 	if d=="3":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""4)what is your  eduction?
# 			1)B.A
# 			2)graduction
# 			3)B.com
# 			4)engineering""")
# 	e=input("enter your choice:--  ")
# 	if e=="2":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""5)what is your univrsity name?
# 			1)nagpur
# 			2)bhandra
# 			3)chandrapur
# 			4)himachal pradesh""")
# 	f=input("enter your choice:--  ")
# 	if f=="1":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("your answer",p)
# 	break



# import random

# sumplayer1=sumplyersu0
# for i in range(5):
# 	print(random.randint(1,6))
# 	another_roll=('want to another roll ? (y/n)')print(random.randint(1,6)
# 	if another
# 	sumpoint+=(random.randint(1,6))
# print('sum of 1st player point',sumpoint)	
