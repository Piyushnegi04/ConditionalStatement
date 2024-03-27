#print("AVI")
#to read the input from user
# name = input("Enter your name: ")
# print(name)

# age = input("Enter  your age: ")
# print(age)

#converting string to integer
#newdatatype(olddatatype value)
age = int(input("Enter your age: "))
print(age)

#conditional statement
# if condition  is true then enter in if condition
# if condition is false enter the outside if block
# if age >= 18:
#     print("You eligible  for govt exam.")
# else:
#     print("better luck next time.")

#multiple if else conditions
qualification  = input("enter your qualifications:")
# if age >=18 and qualification == 'gradute':
#     print("you are eligible for ssc exam:")
# elif age >-18 and  qualification == 'postgraduate':
#     print("you are eligible for civil exam:")
# elif age >=18 and qualification=='ssc':
#     print("you are eligible for D type job:")
# else:
#     print("Sabar karo.....")

#nested if else condition
if age >=18:
    if qualification == 'graduate':
        print("you are eligible for ssc exam:")
    elif qualification == 'postgraduate':
        print("you are eligible for civil exam:")
    elif qualification == 'ssc':
        print("you are eligible for D type job:")
    else:
        print("your qualification not fulfill the given criteria for job:")        
