# PROGRESS TRACKING QN ON 07/09/2021, 7pm by pratik bhai

# iterable=[1,2]
# for word in iterable:
# 	print(word)
# 	iterable.append(word)

## or ###################################################

# a=[1,2]
# for i in a:
# 	print(i)
# 	a.append(i)

# output:-
# 1
# 2
# 1
# 2
# .
# .
# .
# #infinititely print 121212 in vertical	

# note:-infinite for loop it itraterate infinitely 12

# a=(1,2)
# for i in a:
# 	print(i)
# 	a.append(i)

# # output:-
# # 1
# # Traceback (most recent call last):
# #   File "protrac.py", line 30, in <module>
# #     a.append(i)
# # AttributeError: 'tuple' object has no attribute 'append'

###########################################################
# i=0
# while i>=(-20):
# 	i=i-1
# 	print(i)
 
# output:-
# -1
# -2
# -3
# -4
# -5
# -6
# -7
# -8
# -9
# -10
# -11
# -12
# -13
# -14
# -15
# -16
# -17
# -18
# -19
# -20
# -21


#Pro Track on 22/09/2021,wed #############################

#On list 
#Qn-1 find the total charactor sum in list excluding space

# s=['pradeep thakur','from ng']
# m=[]
# for i in s:
# 	c=0
# 	for j in i:
# 		if not j.isspace():
# 			c+=1
# 	m.append(c)
# print(m)	

####### 2nd method #######################################

# s=['pradeep thakur','from ng']
# m=[]
# for i in s:
# 	c=0
# 	for j in i:
# 		if j!=' ':
# 			c+=1
# 	m.append(c)
# print(m)	

# ##########################################################
## 2nd Qn given in protrac

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# print('max of numbers =',max(numbers))

#numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
#numbers.sort()
#print(numbers)
# max=numbers[0]
# for i in numbers:
# 	if i>max:
# 		max=i
# print('the max number =',max)

##################################################################
##################################################################

##PROTRACK ON 11/10/2021

## print 1 to 100 with loop without using increamen
## this is not of protrac qn it is given by rahul

# n1=int(input('enter number which was divisible:' ))
# n2=int(input('enter 2nd number which will be the index: '))
# # if z%n1==0 and z%(n2*n2)==0:
# #  	print(z)

# x=0
# y=1
# z=0
# d=0
# count=0
# while True:
# 	count+=1
# 	#print(z)
# 	x=y
# 	y=z
# 	z=x+y
# 	#a=a+1
# 	if d=z%n1==0:
# 		d+=1
# 	if 
# 		pass
# 		#print(z)
# print("index=",a)

# n=int(input('enter number which was divisible:' )

###############################################################

##print up  0 to 89 fabonacci series

# x=0
# y=1
# z=0
# while z<=89:
# 	print(z)
# 	x=y
# 	y=z
# 	z=x+y

# ################################################################	
## Enter index no of fabonacci series and get value 

# n=int(input('enter index  which value u want:' ))
# x=0
# y=1
# z=0
# count=1
# while count<=n:
# 	count+=1
# 	x=y
# 	y=z
# 	z=x+y
# 	if count<=n:
# 		continue
# 	else: 
# 		print(z)

## OR #############################################################

# n=int(input('enter index no '))
# x=0
# y=1
# z=0
# a=0
# while True:
# 	a+=1
# 	x=y
# 	y=z
# 	z=x+y
# 	if a==n:
# 		break
# print(z)


## check it is fabonacci series number or not 

# #################################################################

# n=int(input('enter number to check it is fabonacci or not:' ))
# x=0
# y=1
# z=0
# while z<n:
# 	x=y
# 	y=z
# 	z=x+y
# if z==n:
# 	print(n,'is fabonacci number')
# else:
# 	print(n,'is not a fabonacci number')


#################################################################

## given two integers n and k .find position the n\th multiple of k in the fibonacci serries.
##Qn-4

# x=0
# y=1
# z=0
# d=0
# count=0
# n=int(input('enter the number : '))
# k=int(input('enter the number: '))
# while True:
# 	count+=1
# 	x=y
# 	y=z
# 	z=x+y
# 	if z%n==0:
# 		d+=1
# 	if d==k:
# 		break
# print(count)

###################################################################################
###################################################################################
## PROTRACK ON 20/10/2021

# n=int(input('enter the number of list'))
# num = int(input("Enter the number: "))
# list1 = [] #an empty list.
# for i in range(num):
# list1.append([])
# list1[i].append(1)
# for j in range(1, i):
# list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
# #if(num != 0):

# n=int(input('enter the number upto u want passcal :'))
# l=[]
# if n==1:
# 	l.append(n)
# 	print(l)
# elif n==2:
# 	for i in range(1,3):
# 		l.append(n-1)
# 		print(l)
# elif n==3:
# 	for i in range(1,4):
# 		if i==1:
# 			l.append(n-2)
# 			print(l)
# 		if i==2:
# 			l.append(n-1)
# 			print(l)	
# 		if i==3:
# 			l.append(n-2)	
# 			print(l)
# elif n==4:
# 	for i in range(1,5):
# 		if i==1:
# 			l.append(n-3)
# 			#print(l)
# 		if i==2:
# 			l.append(n-3)
# 			#print(l)	
# 		if i==3:
# 			l.append(n-1+1)	
# 			#print(l)
# 		if i==4:
# 			l.append(1)	
# 			print(l)
# elif n==5:
# 	for i in range(1,6):
# 		if i==1:
# 			l.append(n-4)
# 			print(l)
# 		if i==2:
# 			l.append(n-4+3)
# 			print(l)	
# 		if i==3:
# 			l.append(i+i)	
# 			print(l)
# 		if i==4:
# 			l.append(1)	
# 			print(l)					
# elif n==5:
# 	for i in range(1,5):
# 		l.append(n-3)
# 		print(l)



# num = int(input("Enter the number: "))  
# list1 = []  
# for i in range(num):  
#   list1.append([])  
#   list1[i].append(1)  
#   for j in range(1, i):  
#     list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])  
#   if(num != 0):  
#     list1[i].append(1)  
# for i in range(num):  
#   print(" " * (num - i), end = " ", sep = " ")  
#   for j in range(0, i + 1):  
#     print('{0:6}'.format(list1[i][j]), end = " ", sep = " ")  
#   print() 



# n=int(input('enter the number upto u want passcal :'))
# list1=[]
# for i in range(n):
# 	tlist=[]
# 	for j in range(i+1):
# 		if j==0 or j==i:
# 			tlist.append(1)
# 		else:
# 			tlist.append(list1[i-1][j-1]+list1[i-1][j])

# 	list1.append(tlist)
# print(list1)
# for i in range(n):
# 	for j in range(n-i-1):
# 		print(' ',end='')
# 	for	j in range(i+1):
# 		print(list1[i][j],end=' ')
# 	print()	












## progress trac Qestion on 11/11/2021

# dict1={}
# a=[1,2,3,4,5,6,7,8,9,10]
# b=['i','ii','iii','iv','v','vi','vii','viii','ix','x']
# d=dict(zip(a,b))
# print(d)


l1=['name','age','salary']
l2=['pradeep','suraj']
l3=[24,20]
l4=[40000,35000]
ln=[]
b=dict(zip(l2,l3))
count=0
for i,j in b.items():
	ln.append({l1[0]:i,l2[1]:j,l2[2]:l4[count]})
	count+=1
print(ln)



