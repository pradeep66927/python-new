# revese list without using built in function or wihout taking another list
a=[1,2,3,4,5]
i=0
j=len(a)-1
while i<j:
	t=a[i]
	a[i]=a[j]
	a[j]=t
	i+=1
	j-=1
print("revese of a= ",a)

##  or

a=a[len(a)-1::-1]
print(a)

##############################################################
### reverse list taking aother list using swapping # need to right

# a=[1,2,3,4,5]
# b=[]
# i=len(a)-1
# j=0
# while i>=0:
# 	b[j]=a[i]
# 	j+=1
# 	i-=1
# print("revese of a= ",b)

##########################################
# a=[1,2,3,4,5]
# b=[]
# i=0
# j=len(a)-1
# while i>=0:
# 	t=a[i]
# 	b[j]=a[i]
# 	a[j]=t
# 	i+=1
# 	j-=1
# print("revese of a= ",b)


##shifting each element one step left or right in list


#############################################################

# string can be directly converted into list by using string
#string method 'splilt'
# a='pradeep'
# b=a.split() 
# print(b)
#print(type(a))

##############################################################

# or using list we can do same

# a='pradeep'
# b=list(a)
# print(b)

##################### or  #################################
# import ast
# color ="['Red', 'Green', 'White']"
# print(ast.literal_eval(color))


##########################################################

#revese list without using built in function i have to do

# size=int(input('enter the size of list: '))
# a=[]
# for i in range(size):
# 	num=int(input('enter the number: '))
# 	a.append(num)
# print(a)
# i=0
# j=size-1
# for i in range(len(a)):
# 	t=a[i]

# a='pradeep'
# b=list(a)
# print(b)
######################################################
###########################################
## USING REMOVE method in list IN A DIFFERENT WAY
# a=[1,2,3,4,5]
# b=a
# for i in b:
# 	b.remove(i)
# print(a)
# print(b)

## OUTPUT:-
#[2,4]

###########################################

# a=[1,2,3,4,5]
# b=a
# #b=a.copy()
# for i in a:
# 	a.remove(i)
# print(a)
# print(b)
# a=12_1.2
# b=1.56
# print(a+b)

## OUTPUT:-122.76

##################################################################

## without using print after input we need add list with input 

# a=['pradeep','vikas','roshan']
# # # b=a
# # b=a.copy()
# # b=a
# for i in a:
# 	print(i,end='')
# 	age=input(' age is:')

####################################################################
####################################################################
##SLICE ASSIGNMENT IN LIST

# l=[10,2,4,7,3,8,910,20]
# l[1:3]=[100,100]
# print(l)

##OUTPUT:-[10, 100, 100, 7, 3, 8, 910, 20]


##REMOVE MORE THAN ONE ELEMENT IN ONCE by using slice assignment

# l=[10,20,30,40,50] 
# l[1:3]=[]
# print(l)

##replace more than one element at once

# l=[10,2,4,7,3,8,910,20]
# l[1:3]=[100,100]
# print(l)

##output:-[10, 100, 100, 7, 3, 8, 910, 20]

#################################################################
################################################################
##COPY OR DEEP COPY OF LIST
# c=[1,2,3]
# d=list(c)
# c[0]=[30]
# print(c)

# a=[[1,2,3],[21,23]

###########################################################

#BUBBLE SORT

# a=[10,5,8,20,9,7,34,22]
# for i in range(len(a)):
# 	for j in range((len(a)-i-1)):
# 		if a[j]>a[j+1]:
# 			t=a[j]
# 			a[j]=a[j
# 			a[j+1]=t
# print(a)
#######################################################
# UNIVERSAL CODE / dynamic code for BUBBLE SORT

# size=int(input('enter the size of the list:'))
# a=[]
# #a=[10,5,8,20,9,7]
# for i in range(size):
# 	val=int(input('enter number: '))
# 	a.append(val)
# for i in range(len(a)):
# 	for j in range(0,(len(a)-i-1)):
# 		if a[j]>a[j+1]:
# 			t=a[j]
# 			a[j]=a[j+1]
# 			a[j+1]=t
# print('sorted list:',a)

########################################################
# how to take nested list as input

# t=[]
# n=int(input('enter size :'))
# for i in range (n):
# 	ta=[]
# 	for j in range(n):
# 		val=int(input('value :'))
# 		ta.append(val)
# 	t.append(ta)
# print(t)

#########################################################

# # ATM USING LIST

# password=12345
# bal=20000
# language_option=['1.ENGLISH\n','2.HINDI\n']
# #choose_transaction=['1.balance inquiry\n','2.cash withdrawl\n','3.cash deposit\n','4.exit transaction\n']
# choose_transaction=['1.balane inquiry\n,2.cash withdrwl\n,3.cash deposit\n,4.exit transaction\n']
# select_option2=[1,2] 
# select_option=[1,2,3,4]
# print('WELCOME TO THE ATM MACHINE\nplease swipe your card')
# print('please choose your lenguage option\n1.ENGLISH\n2.HINDI\n')
# count=0
# iput=int(input('choose your language_option :'))
# if iput==select_option2[0]: 
# 	while True:
# 			#print('WELCOME TO THE ATM MACHINE\nplease swipe your card')
# 	#		print('please choose your lenguage option\n1.ENGLISH\n2.HINDI\n')
# 		print('1.balane inquiry\n,2.cash withdrwl\n,3.cash deposit\n,4.exit transaction\n')
	#	if count==0:
		# iput=int(input('choose your language_option :'))
		# if iput==select_option2[0]:
			# print('1.balane inquiry\n2.cash withdrwl\n3.cash deposit\n4.exit transaction\n')
		#	print(for i in ['1.balane inquiry\n,2.cash withdrwl\n,3.cash deposit\n,4.exit transaction\n'])
			#for i in (choose_transaction):
			#print(choose_transaction[i])
		#		print(['1.balane inquiry\n,2.cash withdrwl\n,3.cash deposit\n,4.exit transaction\n'])
		#	#print(['1.balance inquiry\n2.cash withdrawl\n3.cash deposit\n4.exit transaction\n'])
		#		iput=int(input('please enter your transaction: '))
# 		iput=int(input('chose your transaction: '))
# 		if iput==1:
# 			pas=int(input('enter your password:'))
# 			if password == pas:
# 				print('your current balance is',bal)
# 				another_tran=input('do want to another transaction YES/NO press y or n: ')
# 				if another_tran == 'y':
# 					continue
# 				else:
# 					print('exited from the transaction\n  thanks for using atm')
# 					break						
# 			else:
# 				print('wrong password')
# 		elif iput==2:
# 			pas=int(input('enter your password:'))
# 			if pas==password:
# 				amout=int(input('enter amount to withdrawl: '))
# 				if amout<=bal:
# 					print('collect your cash\nyour remaining balance is',bal-amout)
# 				else:
# 					print('insufficient balance in your account')
# 					another_tran=input('do want to another transaction YES/NO press y or n: ')
# 					if another_tran == 'y':
# 						continue
					
# 					else:
# 						print('you exited from the transaction\n thanks for using atm')
# 						break		
# 			else:
# 				print('wrong password')
# 		elif iput==3:
# 			pas=int(input('enter your password:'))
# 			if pas==password:
# 				dipos=int(input('enter amount to deposit: '))
# 				print('cash is diposited\nyour new balance is',bal+dipos)
# 				another_tran=input('do want to another transaction YES/NO press y or n: ')
# 				if another_tran == 'y':
# 					continue
# 				else:
# 					print('you exited from the transaction\n thanks for using atm')
# 					break		
# 			else:
# 				print('wrong password')
# 		elif iput==4:
# 			print('successfully exited from the transaction\n thanks for using atm')
# 			#pas=int(input('enter your password:')
# 			#if pas==password:
# 				#dipos=int(input('enter amount to deposit: '))
# 				#print('cash is diposited\nyour new balane is',bal+dipos)
# 		else:
# 			print('please enter correct option')
# else:
# 	print('sorry, this language is not available.')
				

####################################################################################################

#this is from ,meraki more questions series


# Python mein hum ek loop ke andar loop bhi chala sakte hain.
#Sochiye humare paas ek list hai jisme aur list hain jinme integers hain. Kuch aise:

# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]


# #Iss list se agar humne saare numbers ko ek ek kar ke print karna hai. 
#toh hum kuch aisa code likh sakte hain:

# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# count1 = 0
# while count1 < len(big_list): #3
	
#     small_list_length = len(big_list[counter1])
#     count2 = 0
#     while count2 < small_list_length: #6
    	
#         print (big_list[counter1][counter2])
#         count2 = count2 + 1
#     count1 = count1 + 1
#     print ('-----')

## print( len(big_list))
# #print( small_list_length)
# #print(len(big_list[counter1]))

# it is iterating each item below questions

# a = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# count1 =0
# while count1 < len(a): #3
# 	b = len(a[count1])
# 	count2 = 0
# 	while count2 < b:  #6
# 		print (a[count1][count2]) # count1=0 01 02 03,count1=1 10 11 13 
# 		count2 = count2 + 1       # count1=3 30 31 32 33 34 35
# 	count1 = count1 + 1
# 	print ('------')


###################################################
# #USING FOR LOOP 

# a = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# count1 = 0
# for i in range (len(a)):
# 	b = len(a[count1])
# 	count2 = 0
# 	for j in range(count2,b):
# 		print (a[count1][count2]) # count1=0 01 02 03,count1=1 10 11 13 
# 		count2 = count2 + 1       # count1=3 30 31 32 33 34 35
# 	count1 = count1 + 1
# 	print ('------')

##########################################################
#code dope 11
#remove dublicate item without using other list

# a = [1,2,3,2,1,3,12,12,32]
# i = 0
# while i < len(a):
# 	j = i+1
# 	while j < len(a):
# 		if a[i] == a[j]:
# 			del(a[j])
# 		j=j+1
# 	i = i+1
# print(a)

##python way
# a = [1,2,3,2,1,3,12,12,32]
# a = list(set(a))
# print a

# ########################################################

# a=[[1,2,3],[4,5,6]]
# i = 0
# while i<len(a):
# 	j = 0
# 	while j < len(a[i]):
# 		print(a[i][j])
# 		j = j+1
# 	i = i+1

##############################################################

# for i in range (len(a)):
# 	for j in range (len(a[i])):
# 		print(a[i][j])


################################################################

# #W3RESOUrces

# Write a Python program to count the number of strings. 
# where the string length is 2 or more and the first and last character are same from a given list of strings.

# words=['abc', 'xyz', 'aba', '1221']
# ctr = 0

# for word in words:
# 	if len(word) > 1 and word[0] == word[-1]:
# 		ctr += 1

# print(ctr)


#################################################################

##QN- TABLE IN NESTED LIST ACCORDING TO USER

#a=int(input('enter no upto u want table'))
# # nested list input how to take
# t=[]
# n=int(input('enter no upto u want table:'))

# for i in range (1,n+1):
# 	ta=[]
# 	b=1
# 	for j in range(1,11):
# 		c=i*j
			
# 		ta.append(c)
		
# 	t.append(ta)
# print(t)

## HOW TO CONVERT NESTED LIST TO FLATTERN LIST
# a=[6,[4,3,[2,1,[49]]]]	# have to do this
# b=[]
# for i in a:
# 	b.append(i)
# print(b)


###################################################

## FIND HCF OF a list or a value

# a=int(input('enter first num: '))
# b=int(input('enter second num: '))
# if a>b:
# 	mn=b
# else:
# 	mn=a
# for i in range(1,mn+1):
# 	if a%i==0 and b%i==0:
# 		HCF=i
# print(f'hcf of 1st and 2nd is {HCF}')	

############################################
# # #LCM OF NUMBER

# a=int(input('enter first num: '))
# b=int(input('enter second num:'))
# if a>b:
# 	maxn=a
# else:
# 	maxn=b
# value=maxn

# while (True):
# 	if maxn%a==0 and maxn%b==0:
# 		break
# 	else:
# 		maxn=maxn+value
	
# print(f'lcm of {a} and {b} is {maxn}')

###############################################

#THIRD MAX FROM THE LIST

# a=[2,3,34,50,100,21,10,23,49]
# for i in range (len(a)):
# 	for j in range(len(a)-i-1):
# 		if a[j]>a[j+1]:
# 			t=a[j]
# 			a[j]=a[j+1]
# 			a[j+1]=t
# print(a)
# print(f'third highest is {a[-3]}')

#####################################################

##FLATTEN LIST FROM NESTED
# multiple levels of nesting allowed.
  
# input list
# l = [1 k=[]
# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# for i in range (len(l)):

# 	for j in range (len(l[i])):
# 		for k in range (len[i][j]):
# 			k.append(k[i][j][k])
# print(f'originonal list is {l}')
# print(f'flatten list is {k}')
# 	if type(i)==list:
# 		for j in i:
# 			k.append(j)
# 	else:		
# 		k.append(i)

##############################################################

# a=[1,2,4,56,3,[3,[3,44],4,53,2,[3,5,[2,5,67,8],23]]]
# main_list = []
# while True:
#     c = True
#     for i in a:
#         if type(i) == list:
#             main_list.extend(i)
#             c = False
#         else:
#             main_list.append(i)
#     if c:
#         break 
#     else:
#         a = main_list
#         main_list = []
# print(main_list)

##################################################################

# nested_list = [[1,[2, [2, 3, 4], [5, [6,11,12,13], 7], [8, 9, 10]]]]
# #nested_list=[[1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]],34]]
# nested_list=[1, 2, [3, 4, [5, 6]],0,[9],8, [9, [10]]]
# flat=[]
# le=len(nested_list)
# print(le)
# s=0
# while le>s:
# 	for i in nested_list:
# 		if type(i)==list:
# 			flat.extend(i)
# 		else:
# 			flat.append(i)
# 			s+=1
# 			#print(flat)
# #print(flat)			
# 	if le>s:
# 		nested_list=flat
# 		flat=[]
# 		#print(flat)
# print(flat)

##########################################

# a=9
# v=a
# a=0
# print(v)
#output:v=9

############################################################
##2nd SECOND METHOD TO FLATTEN LIST

# nested_list=[1,[2,[3,[4,[5,[6,[7,8,9,10]]]]]]]
# emptyList=[]
# while nested_list:
# 	copyItem=nested_list.pop()
# 	#print(copyItem)
# 	if type(copyItem)==list:
# 		nested_list.extend(copyItem)
# 	else:
# 		emptyList.append(copyItem)
# emptyList.reverse()
# print(emptyList) 


# #HANGMAN GAME 1 ###############################################


# import random 

# hangman_f=[' +--------------+------\n |		|\n |		|\n |		|\n |		O\n |\n |\n |\n |\n |\n |',' +--------------+------\n |		|\n |		|\n |		|\n |		O\n |		|\n |		|\n |\n |\n |\n |',' +--------------+------\n |		|\n |		|\n |		|\n |		O\n |		|\n |		|\n |	       / \\\n |\n |\n |',' +--------------+------\n |		|\n |		|\n |		|\n |		O\n |		|\n |	       / \\\n |              |\n |              |\n |\n |\n |',' +--------------+------\n |		|\n |		|\n |		|\n |		O\n |		|\n |	       / \\\n |              |\n |              |\n |             / \\\n |\n |']

# i=0
# while i<=5:
# 	x=random.randint(1,10)
# 	guess=input('enter your guessing no between 1 to 10.: ')
# 	if guess == x:
# 		print('you are the WINNNER!')
# 		break
# 	else:
# 		#for i in hangman_f:
# 		if i==1:
# 			print(hangman_f[0])
# 		elif i==2:
# 			print(hangman_f[1])
# 		elif i==3:
# 			print(hangman_f[2])
# 		elif i==4:
# 			print(hangman_f[3])
# 		elif i==4:
# 			print(hangman_f[4])					
# 	i+=1		

##second method is by vikash for figure part only

# while len(hangman_f)>i:
# 	x=random.randint(1,11)
# 	inp=int(input('Guess any num between 1 to 10: '))
# 	if inp==x:
# 		print('congratulation, you won the game!!')
# 		break
# 	else:
# 		print(hangman_f[i])
# 		i+=1

#############################################################

