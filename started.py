=
# print ('Hello World')
name="Addy"
# age=40
# new_patient="she is a new patient"
# #exemple de output print 
# print(name+ new_patient+str(age) )
# print(name, new_patient,age )
# print(f"{name} {new_patient} {age} ")

# sunt foarte importante spatiile in pytho , aceasta inseamna ierarhia

# raspunsul = input("esti tu "+name )
# print("hello",bool(int(raspunsul))) 
# #bool din "0" tot e true  de aceea era acel bug

# birth_year=input("care e ziua ta de nastere")
# age= 2026-int(birth_year)
# print(" ziua ta este pe ",age)

# de conversie functiile
# int()
# float()
# bool()
# str()

# try:
#     price1= int(input("cat costa serviciile tale de programing "))
#     print("\n")
#     price2= int(input("cat costa serviciile tale de hosting "))
#     print("\n")
#     price3= int(input("cat costa serviciile tale de analiza "))
#     print("\n")
#     price4= int(input("cat costa serviciile tale de strategie "))
#     print("\n")
#     #le convertim de la inceput
#     #la sum sunt mai mult de 2 argumente de aceea utilizam []
#     #try and cacth ca except exception as e : raise e
#     print("total e ", sum([price1,price2,price3,price4]))
# except Exception as e:
#     raise e
    
# course="my dear friend"
# print(course.upper())
# print(course.find("r")) #returneaza indexul
# # a doua metoda
# print("my" in course)
# print(course.replace("ear",'ead'))

#substract and so online
#division   cu impartirea
# print(1/9)
# print(1//9) #impartirea ca la float
# print(1%9)
# print(10**9) # la puterea a 9
  
# a=9
# a+=5
# print(a)
# #ordinea operatiilor ca la matematica
# #incrementarea
# #compararea < > == !+ <= >=
# x= 3==2
# print(x)
# logical operato and or and not && || and !=

#if else
# a=9
# if a>10:
#     print("este adevarat my dear")
#     print("este adevarat my dear")
# elif a<10:
#     print("nooooo")
# else: print("done finanally")

#exemple cu conversiile
# weight= int(input(" introduce you weight "))
# unnit= input("K or L")
# if(unnit.upper()=="K") :
#     converted=weight/0.45
#     print("weight in lbs is ",converted)
# else:
#     converted= weight*0.45
#     print("weight in kg is ",converted)

#while loops
# a=7
# while a>1:
#     print(a-1)
#     print("\n")
#     a-=1

#list
# names=["addy","elly","tommy","sam"]
# print(names)
# for name in names:
#     print(name,"\n")
#     print(names[0:3])
#list method 
number=["love","bronnies"]
print(number)
number.append("elly")
print(number)
number.remove("bronnies")
print(number)
print("pp " in number)
print(len(number))

#range functionun nr la intamplare

range(5) 
range(5,10) #5...9
range(5,10,2) #5 7 9 ,,,, 2 este ca un step

#tuples , change after they are creating doesnt change , imunable







