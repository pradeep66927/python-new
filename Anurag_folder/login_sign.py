# aa=open("log_sign.txt","w+")
# dic={}
# print("1.  sign\n 2.  login")
# opti= input("chose the option ")
# if opti=="1" or "sign":
#     a=input("Enter the name")
#     if "@gmail.com" in a:
#         pas = input("Enter the password")
#         ss,dd,ff,gg,hh=0,0,0,0,0
#         if len(pas)>=8:
#             for i in pas:
#                 if  i.islower():
#                     dd+=1
#                 if i.isupper():
#                     ff+=1
#                 if i.isdigit():
#                     gg+=1
#                 if i.specialcharacter():
#                     hh+=1
#             print(dd,ff,gg,hh)
#             if (hh+gg+ff+dd)==len(pas):
#                 repas= input("Enter the Re_password")
#         else:
#             print("Enter the strong password")


       
# f=open("sample.txt","w")
# f.write("File handling in python")
# f.close()

a=open("/home/ng/Desktop/anurag/mangal_file.py","r")
print(a.read())