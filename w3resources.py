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
# 	for j in range(i+1):
# 		print("*",end=" ")
# 	print(" ")
	
# for i in range(n,0,-1):
# 	for j in range(i-1):
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

# fibonacci series  #############################

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
# for i in range(1,10):
# 	for j in range(i):
# 		print(i,end="")
# 	print()	
# #output
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# or##########################################

# i=1
# #k=1
# while i<10:
# 	print(str(i)*i)
# 	i=i+1
# 	#k+=1

#  or #############################################

# for i in range(1,10):
# 	print(str(i)*i)

    
# code dope qn ***************** not working
#for i in range(7,0,-2):
#	for z in range(0,7):
#		print(1,end=)

		
	##############################################
#revrse pyramid of code dope qn

# n=int(input("enter your number"))
# k=1
# i=1
# while (n>0):
# 	b=1
# 	while b<i:    #remaind   
# 		print("  ",end="")
# 		b=b+1
# 	j=1
# 	while (j<=(n*2)-1):
# 		print("1",end=" ")
# 		j=j+1
# 	print() 	
# 	n=n-1
# 	i=i+1
#output
#1 1 1 1 1 1 1 
 # 1 1 1 1 1 
  #  1 1 1 
   #   1	

# i tried it print as 1010101 but not got done

# n=int(input("enter your number"))
# k=1
# i=1
# while (n>0):
# 	b=1
# 	while b<i:    #remaind           
# 		print("  ",end="")
# 		b=b+1
# 		j=1
# 		while (j<=(n*2)-1):
# 			if j%2==0:
# 				print("0")
# 			else:
# 				print("1",end=" ")
# 			j=j+1
# 		print()
# 		n=n-1
# 		i=i+1	

#USING ROW COLUMN METHOD
# for i in range(4):
# 	for j in range(7):
# 		if i in {0} and j in {0,2,4,6}:
# 			print("1",end=" ")	
# 		elif i in {1} and j in {1,3,5}:
# 			print("1",end=" ")
# 		elif i in {2} and j in {2,4}:
# 			print("1",end=" ")
# 		elif {i==j}:	
# 	 		print("1",end=" ")
# 	 	elif i in {0} and j in {1,3,5}:
# 	 		print("0",end=" ")
# 	 	elif i in {1} and j in {2,4}:
# 	 		print("0",end=" ")
# 	 	elif i in {2} and j in {4}:
# 	 		print("0",end=" ")
#         else:
#         	print()
	 
# for i in range(4):
# 	for j in range(7):
# 		if i in {0} and j in {0,2,4,6}:
# 			print("1",end=" ")	
# 		elif i in {0} and j in {1,3,5}:
# 	 		print("0",end=" ")
# 	#print() 		
# 		elif i in {1} and j in {1,3,5}:
# 			print("1",end=" ")
# 		elif i in {1} and j in {2,4}:
# 	 		print("0",end=" ")
# 	#print() 		
# 		elif i in {2} and j in {2,4}:
# 			print("1",end=" ")
# 		elif i in {2} and j in {4}:
# 			print("0",end=" ")
# 	#print()			
# 		elif {i==j}:	
# 	 		print("1",end=" ")
# 	 	else:
#         	print(" ")
#     print() 

# above code is not working as down output      	
#1010101
# 10101
#  101
#   1

# cofusion about printing a or i

# a='pradeep'
# for i in a:
# 	print(a)

# #outpout ,it iterate equal to no of char of a 

# pradeep
# pradeep
# pradeep
# pradeep
# pradeep
# pradeep
# pradeep

###############################################
# a='pradeep'
# for i in a:
# 	print(i)

# #output
# p
# r
# a
# d
# e
# e
# p
############################################
#a=5
#for i in (a):
#	print(a)

#output
#for i in (a):
#TypeError: 'int' object is not iterable

##############################################
# a=5
# for i in (a):
# 	print(i)

#output
# for i in (a):
#TypeError: 'int' object is not iterable

############################################
# a=5
# for i in range (a):
# 	print(i)

# output
# 0
# 1
# 2
# 3
# 4
############################################
# a=5
# for i in range(a):
# 	print(a)
#output
# 5
# 5
# 5
# 5
# 5

# CHOCOLATE FEAST QN(CHOCALATE AND WRAPPING)

# c =int(input('enter your chocolate : ')
# r=c%3
# count=0
# i=1
# tt=0
# tr=0
# while (count>c):
# 	tt=tt+1
# 	i=i+1
	 

# t=n//3
# tt=tt+t

#  print('total chocolate you get=',tt)



# int chocolateFeast(int n, int c, int m) {
#     int choco=n/c,eat=0,wp=0;
#     while(choco>0){  //add until chocolate=0
#         eat+=choco;
#         wp+=choco;   //counting no. of chocolates as wrappers
#         choco=wp/m;  //No. of wrappers turned
#         wp=wp%m;     //left wrappers
#     }
#     return eat;
# }

# print("_\v|"*5)   #it print siddi
#print("sur\vaj"*5)

# sum=0
# rap=0
# rup=int(input('enter rupees'))
# count=1
# elif rup==rup:
# 	sum=sum+rup
# 	rap=rap+sum
# 	while count<=10:
# 		if rap>=3:
# 			rem=rap%3
# 			rap=sum+rem
# 			bhag=rap//3
# 			rap=rem
# 			sum=sum+bhag
# 			if rap <3:
# 				break
# 	count=count+1
# 	print('number of chocolates = ',sum)

# print


#





#




#



#




#




#



# HARSHAD NUMBER (sum of digit of number ,then )
# divide this sum with this number

# num=int(input('enter number to check it is harshad or not : '))
# h=num
# sum=0
# while (h!=0):
# 	rem=h%10
# 	sum=sum+rem
# 	h=(h//10)
# if num%sum==0:
# 	print(num,'is a harshad number')
# else:
# 	print(num,'is not a harshad number')


# STRONG NUMBER(find factorial of digit of number 
# then add them ,compare to origional no )
# if both ,number and sum fact are same then it 
# strong 145

#n=int(input('enter a number :'))

# STRONG=n
# sum=0
# while (n>0):
# 	r=n%10
# 	fac=1
# 	for i in range(1,r+1):
# 		fac=fac*i
# 	sum=sum+fac
# 	n=n//10
# if STRONG==sum:
# 	print(sum,'is a strong no ')
# else:
# 	print(sum ,'is not a strong no')


# n=int(input('enter a number :'))

# STRONG=n
# sum=0
# while (n>0):
# 	r=n%10
# 	fac=1
# 	i=1
# 	while (i<=r):
# 		fac=fac*i
# 		i=i+1
# 	sum=sum+fac
# 	n=n//10
# if STRONG==sum:
# 	print(sum,'is a strong no ')
# else:
# 	print(sum ,'is not a strong no')


n=int(input('enter a number :'))

STRONG=n
sum=0
while (n>0):
	r=n%10
	fac=1
	for i in range(1,r+1):
		fac=fac*i
	sum=sum+fac
	n=n//10
if STRONG==sum:
	print(sum,'is a strong no ')
else:
	print(sum ,'is not a strong no')

