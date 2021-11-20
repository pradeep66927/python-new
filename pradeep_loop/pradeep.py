#pattern printing
#pattern triangle pattern 
# print("hi pradeep")
#Qn-1 ************************************************************
"""I=1                        #OUTPUT
while i<=5:                        #*
	j=1                            #**
	while j<=i:                    #***
		print("*",end=" ")         #****
		j=j+1                      #*****
	print()
	i=i+1
	"""
"""for i in range (1,6):
	for j in range(0,i):
		print("*",end="")
	print()	
"""

#Qn-2 ******************************************************
"""i=1                        #OUTPUT
while i<=5:                        #1
	j=1                            #22
	while j<=i:                    #333
		print(i,end=" ")           #4444
		j=j+1                      #55555
	print()
	i=i+1
	"""
"""for i in range (1,6):
	for j in range(0,i):
		print(i,end="")
	print()
	"""
#Qn-3	
"""i=1                        #OUTPUT
while i<=5:                        #1
	j=1                            #12
	while j<=i:                    #123
		print(j,end=" ")           #1234
		j=j+1                      #12345
	print()
	i=i+1
	"""
'''for i in range (0,7):
	for j in range(1,i):
		print(j,end="")
	print()
	'''
# i=1
# while i<=5:
# 	b=1
# 	while b<=5-i:
# 		print(" ",end="")       
# 		b=b+1                  
# 	j=1	
# 	while j<=i:
# 		print("*",end="")
# 		j=j+1
# 	print()
# 	i=i+1
		

# print('pradeep')


#Qn-4 *******************************************
# k=1
# i=1
# while i<=5:
# 	b=1
# 	while b<=5-i:
# 		print(" ",end="")   #not working
# 		b=b+1
# 	j=1	
# 	while j<=k:
# 		print("*",end="")
# 		j=j+1
# 	print()
# 	k=k+1
# 	#print()
# 	i=i+1	
# 	#print()


#Qn-5 *****************************************
# strl = input("enter string :")
# length=len(strl)
# for i in range (length):
#  	for j in range (length-i-1):
#  		print(" ",end=" ")
#  	for j in range (i+1):
#  		print(strl[j],end=" ")
#  	print()


 #output		
#           p 
#         p y 
#       p y t 
#     p y t h 
#   p y t h o 
# p y t h o n 

# strl = input("enter string :")
# length=len(strl)
# for i in range (length):
#  	for j in range (length-i-1):
#  		print(" ",end=" ")
#  	for j in range (i+1):
#  		print(strl[i],end=" ")  #we take i in
#  	print()                     #place of j

#output
#          p 
#         y y 
#       t t t 
#     h h h h 
#   o o o o o 
# n n n n n n

# strl = input("enter string :")
# length=len(strl)
# for i in range (length):
#  	for j in range (length-i-1):
#  		print(" ",end="")       #we remove space
#  	for j in range (i+1):       #from(" ") to ("")
#  		print(strl[i],end=" ")  
#  	print()	                    
#      p 
#     y y 
#    t t t 
#   h h h h 
#  o o o o o 
# n n n n n n 

# for row in range(7):
# 	for col in range(6):
# 		if col==0 or (col==4 and (row!=1 and row!=2)) or (row==0 or row==6) and (col>0 and col<4)) or(row==3 and (col==3 or col==5)):
# 			print("*",end="")
# 		else:
# 			print(end=" ")
# 	print()

#Qn-       **************************************
# for row in range(7):
# 	for col in range(5):
# 		if (row in {0,6}) and (col in {1,2,3}):
# 			print("*",end=" ")
# 		elif (row in {1,4,5}) and (col in {0,4}):
# 			print("*",end=" ")
# 		elif (row==2) and (col==0):
# 			print("*",end=" ")
# 		elif (row==3) and (col!=1):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()		

#OUTPUT			
#   * * *   
# *       * 
# *         
# *   * * * 
# *       * 
# *       * 
#   * * *  

# 2nd method *******************************
#n=5
#for i in range(n):

#Qn-  ***************************************
# s=7
# for r in range(s):
# 	for c in range(s):
# 		if (r==c) or (r+c==s-1):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()	
# #output
# *           * 
#   *       *   
#     *   *     
#       *       
#     *   *     
#   *       *   
# *           * 

#Qn-print z pattern*******************************
# i=1
# j=4
# for row in range(0,6):
# 	for col in range(0,6):
# 		if row==0 or row==5:
# 			print("*",end="")
# 		elif row==i and col==j:
# 			print("*",end="")
# 			i=i+1
# 			j=j-1
# 		else:
# 			print(end=" ")
# 	print()		
# output
# ******
#     * 
#    *  
#   *   
#  *    
# ******

#2nd method *************************************

# for row in range(0,6):
# 	for col in range(0,6):
# 		if (row==0 or row==5) or (row+col==5):
# 			print("*",end=" ")
# 		else:
# 			print(end="  ")
# 	print()

# 3rd metod **************************************		
# s=6
# for row in range(s):
# 	for col in range(s):
# 		if (row==0 or row==s-1) or (row+col==s-1):
# 			print("*",end=" ")
# 		else:
# 			print(end="  ")
# 	print()		
# k=1
# i=1
# while i<=5:
# 	b=1
# 	while b<=5-i:    #remaind 
# 		print(" ",end="")
# 		b=b+1
# 	j=1
# 	while j<=k:
# 		print("*",end=" ")
# 		j=j+1
# 	k=k+1
# 	print()
# 	i=i+1	
# #output
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# k=1
# i=1
# while i<=5:
# 	b=1
# 	while b<=5-i:    #remaind 
# 		print(" ",end="")
# 		b=b+1
# 	j=1
# 	while j<=k:
# 		print("A",end=" ")
# 		j=j+1
# 	k=k+1
# 	print()
# 	i=i+1	
#     A 
#    A A 
#   A A A 
#  A A A A 
# A A A A A 
#UNIVERSAL CODE FOR PYRAMID
# n=int(input("enter your number"))
# k=1
# i=1
# while i<=n:
# 	b=1
# 	while b<=n-i:    #remaind           
# 		print(" ",end="")
# 		b=b+1
# 	j=1
# 	while j<=k:
# 		print("A",end=" ")
# 		j=j+1
# 	k=k+1
# 	print()
# 	i=i+1	

 #***********************************************

 #ALPHABET BY USING ROW COLUMN METHOD

# for r in range(4):
# 	for c in range(4):
# 		if (r==0 and (c==0 or c==1 or c==2 or c==3)) or(r==1 and c==2) or (r==2 and c==1) or (r==3 and (c==0 or c==1 or c==2 or c==3)):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()		
# * * * * 
#     *   
#   *     
# * * * * 

# for r in range(3):
# 	for c in range(4):
# 		if (r==0 and (c==0 or c==2)) or (r==c) or (r==2 and (c==0 or c==2)):
# 			print("*",end=" ")
# 		else:
# 			print(" ", end=" ")
# 	print( )
#print(ord("A"))



# PRINT ALPHABET PATTERN BY USING ASCCI VALUE
# n=int(input("enter your number :"))
# for i in range(n):
# 	for z in range(1,n-i):
# 		print(' ',end='')
# 	for j in range(i+1):
# 		print(chr(65+i),end=" ")
# 	print(" ")	

# n=int(input("enter your number"))
# k=1
# i=0
# while i<=n:
# 	b=1
# 	while b<=n-i:    #remaind           
# 		print(" ",end="")
# 		b=b+1
# 	j=1
# 	while j<=k:
# 		print(chr(65+i),end=" ")
# 		j=j+1
# 	k=k+1
# 	print()
# 	i=i+1	

#SNACK PATTERN *****************************
#n=int(input("enter your number"))
for i in range(0,15,-1):
	for j in range(i+1):
		print(i,end=" ")
	print()	


# PALINDROME NUMBER(153=1^2+5^2+3^2=153 THAT IS PALI) 

# i=int(input("enter number"))
# orgi=i
# sum=0
# while i>0:
# 	sum=sum+(i%10)*(i%10)*(i%10)
# 	i=i//10
# if sum==orgi:
# 	print(orgi,"it is armstrong no")
# else:
# 	print(orgi,"it is not a armstrong no")
	
    
	