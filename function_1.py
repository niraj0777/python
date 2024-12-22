# def addition(a,b):
#     sum= a +b 
#     return sum

# result = addition(5,3)
# print(result)

'''using tuple'''
# def values(number):
#     min_value = min(number)
#     max_value = max(number)
#     sum_value = sum(number)
#     return min_value, max_value, sum_value
# numbers = [1,2,3,4,5]
# result = values(numbers)
# print(result)
# print(result[0])

# def values(numbers):
#     return{
#         'min' : min(numbers),
#         'max' : max(numbers),
#         'sum' : sum(numbers)
#     }
# numbers = [1,2,3,4,5]
# result = values(numbers)
# print(result.get("min")) 
# print(result.get("max")) 
# print(result.get("sum"))

'''with parameter'''
# def subtraction(a,b):
#     result=(a-b)
#     return result
# x = subtraction(1,2)
# print (x)


'''without parameter'''
# def subtraction():
#     c = 2
#     d = 5
#     result = c - d
#     return result
# x = subtraction()
# print(x)

'''with parametr and without return'''
# def subtraction (c,d):
#     result= c - d
#     print("result",result)
# subtraction(4,2)    

'''without parameter and without return'''
# def subtraction():
#     c = 4
#     d = 1
#     result = c - d 
#     print ("result",result)

# subtraction()    


# def addition(a,b = 0):
#     sum= a +b 
#     return sum

# result = addition(5,3)
# print(result)


# def my_function():
'''local variable'''
#     x = 10 
#     print("inside function :", x)
# my_function()
# x = 15
# print("outside function:", x)  

'''gobal variable'''
# y = 20
# def my_function():
#     x = 10 
#     print("inside function :", x)
# my_function()
# print("outside function:", y)     

'''using gobal key'''
# z = 30
# def gobal():
#     z = 1 + 5
#     print("inside function :", z)
# gobal()
# print("outside function:", z)     

'''create function to find the number is odd or even'''
# def is_even_or_odd(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# number1 = 10
# print(f"{number1} is {is_even_or_odd(number1)}")

    
 
'''create function to check palindrome'''
# def is_palindrome(num):
#     original = num
#     reversed_num = 0
#     if num < 0:
#         return False
#     while num != 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     return original == reversed_num
# number = int(input("Enter a number: "))
# if is_palindrome(number):
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")


'''create function to check armstrong'''
# def is_armstrong(number):
#     digits = str(number)
#     n = len(digits)
#     total = sum(int(digit) ** n for digit in digits)
#     return total == number

# number1 = 153
# number2 = 123

# print(f"{number1} is an Armstrong number: {is_armstrong(number1)}")
# print(f"{number2} is an Armstrong number: {is_armstrong(number2)}")


'''arbitrary arguments, *args'''
# def my_function(*kids):
#     print("The youngest child is : " +kids[2])
# my_function("emil", "tom", "bob")    

'''arbitrary krywords arguments, **kwargs'''
# def my_function(**kids):
#     print("his last name is " +kids["lname"])
# my_function(fname="ram", lname="sita")    

'''lambda'''
# x = lambda a,b : a+b
# print(x(4,5))

# x = lambda a,b : a*b
# print(x(5,6))

# x= lambda a,b,c : a+b-c
# print(x(10,4,6))

'''1 1 2 3 5 . . . . . . . .'''
