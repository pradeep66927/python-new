## W3RESOURCES question 
##Write a Python program to invert a dictionary with unique hashable values.
 
# students = {
#   'Theodore': 10,
#   'Mathew': 11,
#   'Roxanne': 9,
# }

# new_dicts={}
# for pair in students.items():
# 	new_dicts[pair[1]]=pair[0]
# print(new_dicts)

# new_dicts={}
# for i in students.items():
# 	new_dicts[i[1]]=i[0]
# print(new_dicts)

#############################################################

## not done
##Write a Python program to count the frequency in a given dictionary.
# dictt = {
#  'V': 10,
#  'VI': 10,
#  'VII': 40,
#  'VIII': 20,
#  'IX': 70,
#  'X': 80,
#  'XI': 40,
#  'XII': 20, 
#  }
# from collections import counter
# result = Counter(dictt.values())
# print(dictt)		

###########################################################################

# #Q-9 Write a Python program to iterate over dictionaries using for loops  

# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for color_key, value in d.items():
# 	print(color_key, 'corresponds to ', d[color_key]) 

# output:-
# Red corresponds to  1
# Green corresponds to  2
# Blue corresponds to  3
########################################################################

##Q-10 Write a Python program to sum all the items in a dictionary.

# my_dict = {'data1':100,'data2':-54,'data3':247}
# print(sum(my_dict.values()))

# Sample Output:
# 293 
###################################################################3

## Q-11 Write a Python program to multiply all the items in a dictionary.

# my_dict = {'data1':100,'data2':-54,'data3':247}
# result=1
# for key in my_dict:    
#     result=result * my_dict[key]

# print(result)
# Sample Output:
# -1333800 
########################################################################

## Q-12 Write a Python program to remove a key from a dictionary.

# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'a' in myDict: 
#     del myDict['a']
# print(myDict)

# Sample Output:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# {'b': 2, 'c': 3, 'd': 4}
####################################################################

## Q-13 Write a Python program to sort a given dictionary by key
# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}

# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))
	
# Sample Output:
# black: #000000                                                                                                
# green: #008000                                                                                                
# red: #FF0000                                                                                                  
# white: #FFFFFF 
###################################################################################3

##Q-15 Write a Python program to get the maximum and minimum value in a dictionary.
# my_dict = {'x':500, 'y':5874, 'z': 560}

# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])

# Sample Output:

# Maximum Value:  5874                                                                                          
# Minimum Value:  500
######################################################################
## Q-16 Write a Python program to remove duplicates from Dictionary.
# student_data = {'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    }
# }

# result = {}

# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value

# print(result)

# Sample Output:

# {'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4': {'subje
# ct_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 'id1': {'subject_integration'
# : ['english, math, science'], 'class': ['V'], 'name': ['Sara']}}  
#######################################################################

## Q-18 Write a Python program to check a dictionary is empty or not.
# my_dict = {}

# if not bool(my_dict):
#     print("Dictionary is empty")
	
# Sample Output:
# Dictionary is empty 

####################################################################
## Q-19 Write a Python program to combine two dictionary adding values for common keys.
# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)

# Sample Output:

# Counter({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 

#################################################################
## Q-20 Write a Python program to print all unique values in a dictionary.
# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

# Sample Output:

# Original List:  [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'},
#  {'VIII': 'S007'}]                                                                                            
# Unique Values:  {'S009', 'S002', 'S007', 'S005', 'S001'} 

#####################################################################################
## Q-23 Write a Python program to combine values in python list of dictionaries.

# from collections import Counter
# item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result = Counter()
# for d in item_list:
#     result[d['item']] += d['amount']
# print(result) 
 
## Sample Output:

##Counter({'item1': 1150, 'item2': 300})

###################################################################################

# ## Q-24 Write a Python program to create a dictionary from a string.
# from collections import defaultdict, Counter
# str1 = 'w3resource' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)
  
# #Sample Output:

# #{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

## Q- 25  ########################################################################
    #need to asked mentor
# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)
 
# Sample Output:
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

## Q-27 ############################################
## Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# new_dict = current = {}
# for name in num_list:
#     current[name] = {}
#     current = current[name]
# print(new_dict)
 
# Sample Output:
# {1: {2: {3: {4: {}}}}}

## Q-28 #####################################################
##Write a Python program to sort a list alphabetically in a dictionary.
# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# sorted_dict = {x: sorted(y) for x, y in num.items()}
# print(sorted_dict)

## Sample Output:
##{'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

## Q-29 #############################################################
# need to asked mantor 
## Write a Python program to remove spaces from dictionary keys.

# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# print("Original dictionary: ",student_list)
# student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
# print("New dictionary: ",student_dict)

# Sample Output:
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}

## Q-30 ##################################################################

## Write a Python program to get the top three items in a shop.

# from heapq import nlargest
# from operator import itemgetter
# items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for name, value in nlargest(3, items.items(), key=itemgetter(1)):
#     print(name, value)
	
# Sample Output:
# item4 55                                                                                                      
# item1 45.5                                                                                                    
# item3 41.3 

########################################################################### 

## Q-31 Write a Python program to get the key, value and item in a dictionary.
  # have to asked mantor 
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key  value  count")
# for count, (key, value) in enumerate(dict_num.items(), 1):
#     print(key,'   ',value,'    ', count)

##key  value  count                                                                                             
# 1     10      1                                                                                               
# 2     20      2                                                                                               
# 3     30      3                                                                                               
# 4     40      4                                                                                               
# 5     50      5                                                                                               
# 6     60      6

## Q-32 #########################################################

## Write a Python program to print a dictionary line by line.

# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print (b,':',students[a][b])
		
# ##Sample Output:
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3

## Qn-34 ################################################################

##Write a Python program to count number of items in a dictionary value that is a list
# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# ctr = sum(map(len, dict.values()))
# print(ctr)

# ##Sample Output:
# 5

##Q-35  ############################################################
## Write a Python program to sort Counter by value.

from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(x.most_common())

# Sample Output:
# [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
