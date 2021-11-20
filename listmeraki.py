# # list quetions set-1
# #NOTE:- 1.string data can be change into list directly by using split(string method)
# a='pradee'
# b=a.split()
# print(b)    #output-[]

# # or 2nd method
# b=list(a)
# # qn count element ##############################

# # numbers=[50,40,23,70,56,12,5,10,7]
# # count=0
# # for i in numbers:
# # 	count+=1
# # print(count)

# # or 	

# # numbers=[50,40,23,70,56,12,5,10,7]
# # count=0
# # for i in range(len(numbers)):
# # 	count+=1
# # print(count)	

# #list iteration questions #######################

# # count=0
# # for i in range(20,41):
# # 	count+=1
# # print(count)

# # max element qn ###############################

# # numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# # print('max of numbers =',max(numbers))

# #numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# #numbers.sort()
# #print(numbers)
# # max=numbers[0]
# # for i in numbers:
# # 	if i>max:
# # 		max=i
# # print('the max number =',max)

# # other method:-  ###############################

# #numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# #numbers.sort()
# #print('max number is=',(len(numbers)[numbers]-1))

#      


# #submission_type:url ##############################
# # 2nd max number of list

# # numbers=[50,40,23,70,56,12,5,10,7]
# # numbers.sort()
# # print(numbers)
# # numbers.pop()
# # print(numbers)
# # max=numbers[0]
# # for i in numbers:
# # 	if i>max:
# # 		max=i
# # print('2nd max numbers =',max)

# #reverse order ####################################


# # places=['delhi','gujrat','rajasthan','punjab','kerala']

# # for i in range((len(places)-1),-1,-1):
# # 	print(places[i])




# #plindrome or note ################################

# #a=input('enter name to chek it is plindrome or not')

# # name=[ 'n', 'i', 't', 'i', 'n' ]
# # b=name
# # c=[]
# # for i in range((len(b)-1),-1,-1):
# # 	c.append(b[i])
# # print(c)	
# # if c==b:
# # 	print('it is a plindrome')
# # else:
# # 	print('it is not a plindrome')	


# #binary to decimal #############################

#  #binary_number = [1, 0, 0, 1, 1, 0, 1, 1]    #something is missing in this programe
# num=eval(input('enter binary no: '))          #i=0 but i was taking 1 now correct
# sum=0
# i=0
# while num!=0: 
# 	rem=num % 10
# 	sum=sum + rem *(2**i) #pow(2,i)
# 	num=int(num/10)
# 	i=i+1
# print('decimal number:',sum)
	


# ##decimal to binary have to make

# num=int(input('enter decimal no: '))        
# bnry=[]
# #final_value=0
# while num!=0:
# 	temp=num%2 
# 	bnry.append(temp)
# 	num=num//2
# bnry.reverse()	
# print(bnry)


# # nested list questios #######################

# #which number is not present in second list

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# #list3=list1+list2
# c=[]
# for i in list1:
# 	if i not in list2:
# 		c.append(i)
# print(c)		
			
		

# score card question

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# nmarks=marks[0]+marks[1]+marks[2]

# print(nmarks)
# sum=0
# for i in nmarks:
# 	sum=sum+i
# print(sum)

# #  or ########################################

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# sum=0
# for i in marks:
# 	for j in i:
# 		sum=sum+j
# print(sum)


# "or or or "###################################

# marks = [
#      [78, 76, 94, 86, 88],
#      [91, 71, 98, 65, 76],
#      [95, 45, 78, 52, 49]
#  ]
# c=[] 
# for i in marks:
# 	c.extend(i)
# print(c)
# sum=0
# for j in c:
# 	sum=sum+j
# print(sum)	



# # total sum #######################################
# #pair which are sum of 30 in nested list
# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# p=[]
# for i in n:
# 	for j in range(len(n)):
# 		if i+n[j]==30:
# 			print(i,n[j])
# 			p.append([i,n[j]])
# print(p)			
 # [i,n[j]] not in p and [n[j],i] not in p:


# #magic square ##################################
# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
#     ]

# print(magic_square)      have to do it

# t=[]
# n=int(input('enter size :'))
# for i in range (n):
# 	ta=[]
# 	for j in range(n):
# 		val=int(input('value :'))
# 		ta.append(val)
# 	t.append(ta)

#if (row==0 or(row==1 or row==2) or (column==1)











# # # iterating two list #############################

# students = ['Rishabh','Madhurima','Rahul','Abhishek','Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# for i in range(len(students)):
# 	print(students[i]+'='+str(marks[i]))





# # kitne aadmi the ######################################
# #count odd and even number
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=even=0
# for i in elements:
# 	if i%2==0:
# 		even+=1
	
# 	else:
# 		odd+=1
# print('even=',even,'odd=',odd)		

# #aoo jode ###############################################
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=even=0		
# for i in elements:
#  	if i%2==0:
#  		even+=i
	
#  	else:
#  		odd+=i
# print('sum of even=',even,'sum of odd=',odd)

# # averege kitna hai#######################################
# # average of odd and even.

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=even=n1=n2=0	
# for i in elements:
#  	if i%2==0:
#  		even+=i
#  		n1=n1+1

#  	else:
#  		odd+=i
#  		n2=n2+1
# print('average of even=',int(even/n1),'sum of odd=',int(odd/n2))		


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=even=n1=n2=al=0	
# for i in elements:
# 	al=al+1
# 	if i%2==0:
# 		even+=i
# 		n1=n1+1
# 	else:
# 		odd+=i
# 		n2+=1
# soae=even+odd
# print("count of odd numbers=",n2, "count of even numbers=",n1,"count of all the numbers=",al,"sum of odd numbers=",odd,"sum of even numbers=",even,"sum of all the numbers=",soae,"average of odd numbers=",int(odd/n2),"average of even numbers=",int(even/n1),"average of all the numbers ka=",int(soae/al))


#MULTIPLE LIST ################################################################################################

# KITNE CROREPATI HAI

# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]

# crorepati=lakhpati=dilwale=0
# for i in kitna_paisa_hai:
# 	if i>=10000000:
# 		crorepati+=1
# 	elif i>=100000:
# 		lakhpati+=1
# 	else:
# 		dilwale+=1
# print('list me ',crorepati,'crorepati hai',lakhpati,'lakhpati hai',dilwale,'dilwale hai')

#count occurences ################################################################


# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# a=n=t=x=u=g=0
# for i in char_list:
# 	if i=='a':
# 		a+=1
# 	elif i=='n':
# 		n+=1
# 	elif i=='t':
# 		t+=1
# 	elif i=='x':
# 		x+=1
# 	elif i=='u':
# 		u+=1
# 	else:
# 		g+=1
# print('a=',a,'time','n=',n,'time','t=',t,'time','x=',x,'time','u=',u,'time','g=',g,'time',)


#Duplicates submission_type: Duplicates #####################################################

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]							

# n1=[]
# for i in n:
# 	if i not in n1:
# 		n1.append(i)
# print(n1)

##or without taking other list remove dublicate  need to try #####################
# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# n.sort()
# print(n)
# for i in n:
# 	if n[i]



#substring nikalo ##########################################################################

# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = "over"
# for i in mainStr:
# 	mainStr.replace('over','on')
# 	print(mainStr)	



# i try crorepati in different way to solve  not in working #####################################

# question_list = [
#     "How many continents are there?",              # pehla question
#     "What is the capital of India?",            # doosra question
#     "NG mei kaun se course padhaya jaata hai?"    # teesra question
# ]

# options_list = [
#     #pehle question ke liye options
#     ["Four", "Nine", "Seven", "Eight"],
#     #second question ke liye options
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     #third question ke liye options
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]
# slution_list=[3,4,1]

# for i in question_list:
# 	print(question_list[i]+'\n'+options_list[i]+'\n'solution_list[i])
# 	#if question_list[i]==3:
# 	#	print('you are right')
# 	#else:
# 	#	print('sorry you are wrong\nwright answer is delhi')


		
#Kaun Banega Codepati (KBC) - Setup not in working condi##############################

# question_list = ["How many continents are there?\n","What is the capital of India?\n","NG mei kaun se course padhaya jaata hai?\n"]
# options_list = ["1.Four\n2.Nine\n3.Seven\n4.Eight\n","1.Chandigarh\n2.Bhopal\n3.Chennai\n4.Delhi\n","1.Software Engineering\n2.Counseling\n3.Tourism\n4.Agriculture\n"]
# solution_list=[3,4,1]
# fifty_fifty_list=[' 1.four\n     \n 3.seven\n     ','1.Chandigarh\n2.        \n3.      \n4.Delhi\n','1.Software Engineering\n2.             \n3.          \n4.Agriculture\n']
# cou=0
# for i in range(len(question_list)):
# 	print('apka sawal hai: ')
# 	print(question_list[i])
# 	print('apka vikalp  hai')
# 	print(options_list[i])
# 	print("if you don't know answer you can use 50-50\nfor using 50-50 press 50")
# 	#print(solution_list[i])
# 	iput=int(input('choose your correct option :'))
# 	if iput==solution_list[i]:
# 		#i+=1
# 		print ("Congrats! Aapka answer sahi hai\napka sawal hai: \n", question_list[i], '\napka jawab  hai')
# 		print(options_list[i])#,"\nif you don't know answer you can use 50-50","\nfor using 50-50 press 50")
# 		if question_list[2]==solution_list[2]:	
# 			print("apne sabhi sawalo ka sahi jawab diya\nyou are winner\n   THANKS")
# 			break
# 	elif iput==50:
# 		if cou==0:
# 			cou+=1

# 			print(fifty_fifty_list[i],'\nenter option 2 of them')

# 			iput2=int(input('choose 2 of them :'))
# 			if iput2==3:
# 				print('apka sawal hai: ')
# 				print(question_list[i])
# 				print('apka jawab  hai')
# 				print(options_list[i])
# 		else:
# 			print('allready you have taken 50 50')


		 
	# else:
	# 	print('sorry! galat jawab .\nyou are out of the game')
	# 	break
	# 	if iput==4:
	# 		i+=1
	# 		print ("Congrats! Aapka answer sahi hai\n")
	# 		print('apka sawal hai: ')
	# 		print(question_list[i])
	# 		print('apka jawab  hai')
	# 		print(options_list[i])

	# 	else:
	# 		print('sorry! galat jawab .\nyou are out of the game')
	# 		if iput==1:
	# 			i+=1
	# 			print ("Congrats! Aapka answer sahi hai\n")
	# 			print('apka sawal hai: ')
	# 			print(question_list[i])
	# 			print('apka jawab  hai')
	# 			print(options_list[i])

	#else:
	# 	print('sorry! galat jawab .\nyou are out of the game')
	#elif iput!=(solution_list[i]):
	#	print('')

	# else:
		# print('sorry! galat jawab .\nyou are out of the game but\nyou have a chance 50-50 do you want use?')
	
		


			
	





#slution_list=[3,4,1]

# while True:
# 	# question_list = [
#  #    "Aapka Sawaal hai:\nHow many continents are there?\n",              # pehla question
#  #    "Aapka Sawaal hai:\nWhat is the capital of India?\n",            # doosra question
#  #    "Aapka Sawaal hai:\nNG mei kaun se course padhaya jaata hai?\n"    # teesra question

# 	print(question_list[0])
# 	for i in options_list:
# 		print(options_list[0])
# 	# option=int(input('please enter your option :')
# 	# 	if option==3:
# 	# 		print(question_list[0])
# 	# 		print(options_list[0])
# 	# 	else:
# 	# 		print('you are out of the game')
# for i in question_list:
# 	for i in range(len(options_list)):
# 		print(str(question_list[i])+str(options_list[i][i]))




	
	#for j in range (len(options_list)):
	#print(options_list[0])
	# for j in (options_list):
	# 	print(question_list[i]+options_list[j])
	# #print(options_list[i])


# THIS KBC IS IN WORKING CONDITION ####################################################################

# question_list = ["Qn.1.How many continents are there?\n","Qn.2.What is the capital of India?\n","Qn.3.NG mei kaun se course padhaya jaata hai?\n"]
# options_list = ["1.Four\n2.Nine\n3.Seven\n4.Eight\n","1.Chandigarh\n2.Bhopal\n3.Chennai\n4.Delhi\n","1.Software Engineering\n2.Counseling\n3.Tourism\n4.Agriculture\n"]
# solution_list=[3,4,1]
# fifty_fifty_list=[' 1.four\n     \n 3.seven\n     ','1.Chandigarh\n2.        \n3.      \n4.Delhi\n','1.Software Engineering\n2.             \n3.          \n4.Agriculture\n']
# cou=0
# for i in range(len(question_list)):
# 	print('apka sawal hai: ')
# 	print(question_list[i])
# 	print('apka vikalp  hai')
# 	print(options_list[i])
# 	if cou==0:
# 		print("if you don't know answer you can use 50-50\nfor using 50-50 press 50")
# 	iput=int(input('choose your correct option :'))
# 	if iput==solution_list[i]:
# 		#i+=1
# 		print("Congrats! Aapka answer sahi hai")
# 		if (len(question_list)-1)== i:
# 			print("apne SABHI sawalo ka sahi jawab diya\n you are winner\n   THANKS")
# 	elif iput==50:
# 		if cou==0:
# 			cou+=1

# 			print(fifty_fifty_list[i],'\nEnter option 2 of them')

# 			iput2=int(input('choose 2 of them :'))
# 			if iput2==solution_list[i]:
# 				print("Congrats! Aapka JAWAB sahi hai")
# 				if iput2==solution_list[2]:
# 					print("apne SABHI sawalo ka sahi jawab diya\n   you are winner\n   THANKS")

# 			else:
# 				print('sorry! galat jawab .\nyou are out of the game')
# 				break

# 		else:
# 			print('allready you have taken 50 50\n')
# 			print('apka sawal hai: ')
# 			print(question_list[i])
# 			print('apka vikalp  hai')
# 			print(options_list[i])
# 			iput2=int(input('choose your correct option :'))
# 			if iput2==solution_list[i]:
# 				print("Congrats! Aapka JAWAB sahi hai")
# 			else:
# 				print('sorry! galat jawab .\nyou are out of the game')
# 				break
# 	else:
# 		print('sorry! galat jawab .\nyou are out of the game but\nyou have a chance 50-50 do you want use?')


######################################################################################################


# DEBUGING PART QUEstions			

# Qn-1 

# name = ["Savitri", "Phule", "26"]
# print(name[0]+name[1])             #print(name[1]+name[2]=print(name[0]+name[1]) for required part             #


####################################################################### 
                                                                   #we can't add int and string
## QN-2
# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]     #so i change each marks in int
# total_marks =0                                                     # and print part was missing so
# # counter = 0														# i add it at last
# # while counter<=(len(marks)-1):
# for i in range(len (marks)):
#     total_marks = total_marks +int(marks[i])
#     #counter = counter + 1
# print(total_marks)

# #############################################################################

# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks =0
# counter = 0
# while counter<=(len(marks)-1):
# #for i in range (len (marks)-1):
# 	total_marks = total_marks +int(marks[counter])
# 	counter = counter + 1
# print(total_marks)

##########################################################################

# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
#     total_marks = total_marks + int(marks[counter])
#     counter = counter + 1
# print(total_marks)
