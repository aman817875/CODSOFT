'''Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
'''
#defined add function
def add(a , b):
    return (a + b)#Addition of two numbers

#defined subtract function
def subtract(a , b):
    return a - b #substraction of two numbers

#defined multiply function
def multiply(a , b):
    return(a * b)#multiplicaton of two numbers

#defined divide function
def divide(a ,b):
    if b != 0:
        return (a / b) #division of two numbers
    else:
        return ("Din't divided by 0")

print("Select arithmetic operations :")
print("1. add\n2. subtract\n3. multiply\n4. divide")

#Giving choice to the user
operation_choice = input("Please enter your choice (1/2/3/4): ")

#Taking input drom user 
num1 = float(input("Please enter first number : "))
num2 = float(input("Please enter second number : "))

if operation_choice == '1':
    print(num1,"+",num2,"=",add(num1 , num2),"\nAddition of two numbers is done....\nThanks....")
elif operation_choice == '2':
    print(num1,"-",num2,"=",subtract(num1 ,num2),"\nSubstraction of two numbers is done....\nThanks....")
elif operation_choice == '3':
    print(num1,"*",num2,multiply,"=",multiply(num1 , num2),"\nMultiplication of two numbers is done....\nThanks....")
elif operation_choice == '4':
    print(num1,"/",num2,"=",divide(num1 , num2),"\nDivision of two numbers is done....\nThanks....")
else:
    print("Your input is Invalid....\nPlease enter valid input....")

