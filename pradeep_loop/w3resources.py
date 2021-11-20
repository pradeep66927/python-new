print("hello")
#Qn-1    ****************************************
# i=1500
# while i<=2700:
# 	if i%5==0 and i%7==0:
# 		print(i)
# 	i=i+1	

#Qn-2
# temp=input("enter temperature in celsius/fahrenheit")
# degree=int(temp[:-1])
# i_convention=temp[-1]

# if i_convention.upper()=="c":
# 	result=int(round((9*degree)/5+32))
# 	o_convention="fahrenheit"

# elif i_convention.upper()=="f":
# 	result=int(round((degree-32)*5/9))  #not working
# 	o_convention="celsius"
# else:
# 	print("input proper convention")
# 	quit()
# print("the temperature in",o_convention,"is",result,"degree")


#Qn-4
#for row in range(10):
#	for col in range(6):     # wrong
#		print("*",end="")
#			
#	print()

#***********************************************		
# n=5
# for i in range(n):
# 	for j in range(i):
# 		print("*",end=" ")
# 	print(" ")
	
# for i in range(n,0,-1):
# 	for j in range(i):
# 		print("*",end=" ")
# 	print(" ")	
#output 
# *  
# * *  
# * * *  
# * * * *  
# * * * * *  
# * * * *  
# * * *  
# * *  
# *
#Qn-5

#word=input("enter word to reverse : ")
#for char in range (len(word)-1,-1,-1):
#	print(word[char],end="")
#print("\n")

#Qn-7
# numbers=(1,2,3,4,5,6,7,8,9)
# count_odd=0
# count_even=0
# for x in numbers:
# 	if x%2==0:
# 		count_even+=1
# 	else:
# 		count_odd+=1
# print("number of even numbers :",count_even)
# print("numbers of odd numbers:",count_odd)		

#Qn-8 ****************************************
#datalist=[1452,11.23,1+2j,True,"w3resourse",(0,1),[5,12],{"class":"v","section":"A"}]
#for item in datalist:
#	print("type of ",item,"is",type(item))

#Qn-9 **********************************8*******
# for i in range(7):
# 	#print(i)
# 	if i==3 or i==6:
# 		continue
# 	print(i)
#
#Qn-9  *****************************************

# x=0
# y=1
# z=0
# while x<=21:
# 	print(z)
# 	x=y
# 	y=z
# 	z=x+y
# 	x=x+1


#qn 16*****************************************
# for i in range(100,401):
# 	if i%2==0:
# 		print(i,end=",")

# 		it print 100 to 400 with comma even number

#qn 32 ********************************
# l=input("enter alphabet letter : ")
# if ( "a" in l or "e" in l or "u" in l or "i" in l or "o" in l):
# 	print("vowels")
# elif l=='y' :
# 	print("somtimes it assume as vowels")
# else:
# 	print("consonant")

# qn ********************************************
# print("enter number to calulate")

# count = 0
# sum = 0.0
# number = 1

# while number != 0:
# 	number = int(input(""))
# 	sum = sum + number
# 	count += 1

# if count == 0:
# 	print("Input some numbers")
# else:
# 	print("Average =", sum / (count-1), sum)

#qn 43 *************************8***8****8*
#a=1
# for i in range(1,11):
# 	for j in range(1,11):
# 		print("table of ",i,i,"x",j,"=",(i*j) )

#qn 44 ***************************************
for i in range(1,10):
	for j in range(i):
		#if i==1:
			#print(1)
		#else:
			print(i,end="")
		#i=i+1
		#if i==1:
		#	print(1)
		#else:	
	print()	
