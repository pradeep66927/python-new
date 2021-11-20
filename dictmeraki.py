
#A=1.w3school QUESTIONS
#B=2.MERAKI DICTIONARY QUESTIONS


#dict1={'brand':'suzuki','model':'desire','year':2020}
# x=dict1.copy()
# print(x)
# x.clear()
# dict1.setdefault('place','new delhi')
# print(x)
# print(dict1)
#print(dict1)

##nested dictionary 

# myfamily = {"child1" : { "name" : "Emil","year" : 2004},
#             "child2" : {"name" : "Tobias","year" : 2007},
#             "child3" : { "name" : "Linus", "year" : 2011 }}
# print(myfamily['child3'])           



# #Output:-
# #{“brand”:”suzuki”,”model”:”desire”,”year”:2020}

##MERAKI QUESTIONS 

## before this w3school questions 
## Exercise:
##Qn-1
## Use the get method to print the value of the "model" key of the car dictionary.

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.get('model'))

##output:-mustang

###############################################################
## qn-2
##Change the "year" value from 1964 to 2020.


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car['year'] =2020 
# print(car)

##########################################################
## qn-3
###Add the key/value pair "color" : "red" to the car dictionary.

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car['color']='red'
# print(car)

## or or or or or or or or or or or or 

##Add a color item to the dictionary by using the update() method:

# car= {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.update({"color": "red"})
# print(car)

################################################################### 
##qn-4
## DELETED RELATED ALL METHOD OF DICTIONARY #######################

##Use the pop method to remove "model" from the car dictionary.

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.pop('model')
# #print(x)
# print(car)

##The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.popitem()
# print(car)


##The del keyword removes the item with the specified key name:

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del car["model"]
# print(car)
# ##Use the clear method to empty the car dictionary.

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)

# ##The del keyword can also delete the dictionary existances completely:

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del car
# print(car)  #this will cause an error because "thisdict" no longer exists.

################################################################################
#B=2.MERAKI DICTIONARY questions

#Qn-1    done now have to do try more way 

# dict1={1:10, 2:20}
# dict2={3:30,2:40}
# dict3={5:50,2:60}
# dict4={}
# for key in dict1 :
#     if key in dict2:
#     	dict1[key] = dict1[key] + dict2[key] 
#     if key in dict3:#or key in dict2:
#     	dict1[key] = dict1[key] + dict3[key]
# dict4 = {**dict3, **dict2,**dict1}
# #dict4 = so({**dict3, **dict2,**dict1})
# import operator
# # print('original= ',b)
# asce=dict(sorted(dict4.items(),key=operator.itemgetter(0)))
# # print('ascending=',asce)
# print(asce)

# dict1={1:10, 2:20}
# dict2={3:30,2:40}
# dict3={5:50,6:60}
# dict4={}

# d4 = d1.copy()d4.update(d2)print(d4)Output: ...
# d5 = {**d1, **d2}print(d5) ...
# {**dict1, **dict2, **dict3}
# print(dict1.update(dict2.update(dict3)))



## BASE OR HINTS FORE  QUESTIONS 1

# for key in b:
#     if key in a:
#         b[key] = b[key] + a[key]

# c = {**a, **b}
# print(c)

###################################################################################
## Qn no-2   done

##check either input word is present in dictionary or not 

# dict={'name':'Raju', 'marks':56}
# exists=input('enter word to check existances :')
# if exists in dict:
# 	print('exist')
# else:
# 	print('not exist')


#############################################################################
## QN no-3    done 

##find sum of values of a dictionary 
# y_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#         }
#sum=0
# for x in y_dict.values():
# 	sum=sum+x
# print(sum)

## or or or or or or or or or or or or or or or or or or ##############

# sum=0
# for y in y_dict:
# 	sum=sum+y_dict[y]
# print(sum)

### or or or or or or or or or or ################

# sum=0
# for x,y in y_dict.items():
# 	sum=sum+y
# print(sum)
# 	

###########################################################################

## Qn no-4 done but i have to do with another method 

## Write a program remove the first key value pair from a nested dictionary
# dic= {
#       1: 'NAVGURUKUL',
#       2: 'IN',  
#       3:{    
#          'A' : 'WELCOME',
#           'B' : 'To',
#            'C' : 'DHARAMSALA'
#         }
#       }
# del dic[3]['A']
# print(dic)


# dic.pop([3]['A'])
# print(dic)
# for i in dic:
# 	for j in dic[i]:
# 		print(j)
# 		if dic[i][1]=='A':
# 			dic[i].pop('A')
# print(dic)
 
#####################################################################################

## QN no-5   done

##convert two list into a dictionary

# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5,]

#list3=dict(zip (list1, list2))
# print(list3)

###### 2nd method or ## or ## or ## or  ## or 2nd method

# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5]

# list1_list2_dict={}
# for i in range (len(list1)):
# 	list1_list2_dict[list1[i]]=list2[i]
# print(list1_list2_dict)


############################################################################
##  done

##Qn no-6  remove duplicate key from dictionary     ##  done this questions 

dic={
    'ball':'red',
    'bat':4,
    'wickets':8,
    'ball':'green',
    'bat':3
    }

dict1 = {}
for key,value in dic.items():
    if value not in dict1.values():
        dict1[key] = value
print(dict1)


# dict1={}
# for i in dic:

# 	if i not in dict1:
# 		dict1.update(i) 
# print(dict1)


########################################################################
###          done this questions
##QN no-7
## Take a list having dictionary elements as shown below (Sample Data) 
# and then store all the unique values into a list and print.


# list=[
# 	{"first":"1"}, 
# 	{"second": "2"}, 
# 	{"third": "1"}, 
# 	{"four": "5"}, 
# 	{"five":"5"}, 
# 	{"six":"9"},
# 	{"seven":"7"}
# 	]
# a=[]
# for i in list:
# 	for j in i.values():
# 		if j not in a:
# 			a.append(j)
# print(a)

########################################################################
##QN no-8   done

## Take input of name and marks of 10 students and store to a dictionary.
# {
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 
# size=int(input('enter size of dictionary :'))
# name_marks={}
# for i in range(size):
# 	k=input('enter the key :')
# 	v=int(input('enter the values: '))
# 	name_marks.update({k:v})
# print(name_marks)

###########################################################

## QN- self ******* how to multiply the vlue of ditionary

# size=int(input('enter size of dictionary :'))
# name_marks={}
# s=1
# for i in range(size):
# 	k=input('enter the key :')
# 	v=int(input('enter the values: '))
# 	name_marks.update({k:v})
# 	s=s*v
# print(name_marks)
# print(s)

######################################################################
##Qn-9   done but have to find easy or 2nd method for this qestions 

##Store the unique letters and their frequency of the letters from 
##the word "MISSISSIPPI" to a dictionary, were the letters are the keys and 
##their frequencies are the values.

#a="MISSISSIPPI"
# #m=i=s=p=0
# s=list(a)
# emp={}
# for i in s:
# 	count=s.count(i)
# 	if count >1:
# 		for j in range(count-1):
# 			emp[i]=count
# 			s.remove(i)
# 	else:
# 		emp[i]=count
# print(emp)

## 2nd method  Qn-9##########################################

# a="MISSISSIPPI"
# from collections import defaultdict, Counter
# a = "MISSISSIPPI" 
# my_dict = {}
# for letter in a:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

############################################################
## 2nd method  Qn-9 

##string = input()
# a="MISSISSIPPI"
# f = {}
# for i in a :#string:
#   f[i] = f.get(i,0) + 1
# print(f)



# from collections import Counter
# counts=Counter(word) # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
# for i in word:
#     print(i,counts[i])

# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))




######################################################################

## QN no-10     done

##Count the total number of items from the values of the dictionary 
## which are in the form of a list.

# dict =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# sum=0
# for i in list(dict.values()):
# 	if type(i)==list:
# 		for j in i:
# 			sum+=1
# 	else:
# 		sum+=1
# print(sum)	


###################################################################

##QN no-11     done but we getting key not value so i have to try it later

## Write a program to print the top 3 highest values of a given dictionary.
my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
# from heapq import nlargest
# three_largest=nlargest(3,my_dict,key=my_dict.get)
# print(three_largest)
a=[]
for i in my_dict.values():
	a.append(i)

	from heapq import nlargest
	three_largest=nlargest(1,a)
print(three_largest)


## heapq is module in above (like---nlargest, nsmallest etc)
#####################################################################

##QN no-12   done

##Write a program to create a dictionary with all numbers from 1 to 15 
##as the keys and their squares as the corresponding values.

# size=int(input('enter size of dic: '))   #solved
# dict1={}
# for i in range(1,size+1):
# 	dict1.update({i:i*i})
# print('dictionary of num and their square',dict1)

#####################################################################

##QN no-13   done

## Write a program to print the top 3 highest values of a given dictionary.

# my_dict = {
#     'a':50, 
#     'b':58,
#     'c':56,
#     'd':40,
#     'e':100, 
#     'f':20
#     }
# a=[]    
# for x in my_dict.values():
# 	#print(x)
# 	a.append(x)
# 	from heapq import nlargest
# 	three_largest=nlargest(3,a)
# print(three_largest)

#######################################################
## three smallest from dictionary  (my self questions)

# a=[]    
# for x in my_dict.values():
# 	#print(x)
# 	a.append(x)
# 	from heapq import nsmallest
# 	three_smallest=nsmallest(3,a)
# print(three_smallest)

	
#########################################################################

##QN no-14    1st method    in questions    done

## Write a program to sort a dictionary in ascending or descending according to its values .

#dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

#b={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# import operator
# print('original= ',b)
# asce=dict(sorted(b.items(),key=operator.itemgetter(1)))
# print('ascending=',asce)
# dece=dict(sorted(b.items(),key=operator.itemgetter(1),reverse=True))
# print('discending =',dece)


####### 2d method ##### 2d method ######  

# b={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print('original= ',b)
# c=sorted(b.items(),key=lambda x:x[1])
# d = dict(c)
# print('ascending=',d)
# dd=sorted(b.items(),key=lambda x:x[1],reverse=True)
# e = dict(dd)
# print('discending =',e)

############################################################################

######    CODE OUTPUT {meraki}     ###################################################

# ## qn qn-1
# a = {(1,2):1,(2,3):2}
# print(a[1,2])

# Options :-

# A. Key Error
# B. 1  this is correct
# C. {(2,3):2}
# D. {(1,2):1}

################################################

## QN no-2
# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])

# Options :- 
# A. Key Error  (right this)
# B. [1,2]
# C. {‘a’:1,’b’:2}
# D. (1,2)

#####################################################
##QN no-3
# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
        
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print (len(fruit))
# print(fruit)

##output- 3
##        {'Apple': 2, 'Banana': 1, 'apple': 1}

###########################################################

##QN no-4
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

#print (len(Details["Student"]))

## output:-1

############################################################

## QN no-5
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict)

## output:-30
##         {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}

################################################################

## QN no-6
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

## typeerror  unhashable type

#################################################################

## QN no-7

#rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)

## output:-True

############### DEBUGE CODE  #################
## QN no-1   done 

# details={
# 	"name":"Shanti",
# 	"lastname":"kumari",
# 	"age":12,
# 	"email":"shanti@navgurukul.org",
# 	}

# print(details["name"])
# print(details["lastname"])
# print(details["age"])

## debug lastname was missing and "" in age was missing 

#########################################################################################

##QN no-2  done

##You have been given a dictionary in which you have to find the sum of all the keys.
## You have to debug this code and find out how you can get the output as 14.
# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum)

## me replace 1 with i that was error 

####################################################################
# ## QN no-3   done

# c=dict()
# for i in range(1,16):
#     c.update({i:i*i})
# print(c)

## me debuge c=(i*i)replace with c.update({i:i*i})
####################################################################

## QN no-4    done

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
# 	c.update(i)
# print(c)

## me update update(i) with c.update(i) this was bug in this questions

##  2nd method   ## 3rd method using {**,**}

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}

# s.update(a)
# print(s)

# c={**s,**a}
# print(c)



