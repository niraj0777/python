# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def great(self):
#         print(f"hello my name is {self.name} and my age is {self.age}")

# p1 = person ("ram ", 20)

# p2 = person ("sita", 21)            

# p3 = person ("ritaa", 18)                        

# p3.great()

# class rect_area:
#     def __init__(self, length, breath):
#         self.length = length
#         self.breath = breath
#     def area(self):
#         print("area:",self.length*self.breath)
# rect_box = rect_area(4,6)            
# rect_window = rect_area(5,6)            
# rect_door = rect_area(4,8) 
# rect_box.area()   
# rect_window.area() 
# rect_door.area()      

'''without parameter'''
# class rect_area:
#     def area(self,length,breath):
#         print("area:",length*breath)
# rect_box = rect_area()            
# rect_window = rect_area()            
# rect_door = rect_area() 
# rect_box.area(2,3)   
# rect_window.area(4,6) 
# rect_door.area(6,7)   

'''return'''

# class rect_area:
#     def __init__(self, length, breath):
#         self.length = length
#         self.breath = breath
#     def area(self):
#         result = self.length*self.breath
#         return result
    
# rect_box = rect_area(4,6)            
# rect_window = rect_area(5,6)            
# rect_door = rect_area(4,8) 
# result_rect_box =rect_box.area()   
# result_rect_window =rect_box.area()   
# result_rect_door =rect_box.area()   


'''Inheritance'''
# class Animal:
#     def speak(self):
#         return "Animal speaks"
# class dog(Animal):
#     def bark(self):
#         return "dog barks"

# my_dog = dog()
# print(my_dog.speak())
# print(my_dog.bark())

# class A:
#     def method_A(self):
#         return "method A"
# class B:
#     def method_B(self):
#         return "Method B"

# class C(A, B):
#     def method_C(self):
#         return "Method C"

# obj_C = C()
# print(obj_C.method_A())
# print(obj_C.method_B())
# print(obj_C.method_C())

# class A:
#     def method_A(self):
#         return "method A"
# class B(A):
#     def method_B(self):
#         return "Method B"

# class C(B):
#     def method_C(self):
#         return "Method C"

# obj_C = C()
# # print(obj_C.method_A())
# # print(obj_C.method_B())
# print(obj_C.method_C())

# class rectangle:
#     def _init_ (self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth
# class square(rectangle):
#     def _init_ (self, length):
#         super()._init_(length,length)

# square = square(5)

# print("Area of square ", square.area()) 

'''try execpt'''

# def divide():
#     try:
#         x =int(input("enter the number for x"))
#         y =int(input("enter the number for y"))
#         result = x/y
#         print("result",result)
#     except ZeroDivisionError as e:
#         print("you have enter the zero number for y")
#         x =int(input("enter the number for x"))
#         y =int(input("enter the number for y"))
#         result = x/y
#         print("result",result)
#     except ValueError:
#         print("you have enter the charater")
#         x =int(input("enter the number for x"))
#         y =int(input("enter the number for y"))
#         result = x/y
#         print("result",result)
# divide()       


# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("something else went is wrong")        


# x = -1
# try: 
#    if x < 0 :
#       raise Exception("Sorry, no numbers is below zero")
# except Exception as e:
#     print(e)
#     x=int(input("enter the number"))  

# x = input("enter the name")
# try:
#     x = input("enter the name")
#     if x == int: raise Exception ("sorry, only charater")
# except Exception as e:
#     print(e)
#     x = input("enter the name")

'''create custom execption to hanlde diffeent cases'''

# class negative_error(Exception):
#     def __init__(self,message):
#         super().__init__(message)


# class zero_error(Exception):
#     def __init__(self,message):
#         super().__init__(message)        

# x = int(input("enter the age"))

# try:
#     if x<0:
#         raise negative_error("sorry,no number is below zero")
#     elif x==0:
#         raise zero_error("sorry, age cannot be zero")
# except negative_error as e:
#     print(f"Error:{e}")
#     x = int(input("enter the age"))        
#     print("the age is:")
# except zero_error as e:
#     print(f"Error:{e}")
#     x = int(input("enter the age"))        
#     print("the age is:")


'''Raise Custom Exception to handle different cases with the same execpt block'''
# x= int (input ("enter the age"))
# try:
#   if x<0:
#     raise Exception("sorry, no number below zero")
#   elif x==0:
#     raise Exception("sorry, age is zero")
# except Exception as e:
#   print(e)
#   print('you have entered negative number')
#   x= int (input("Re-enter the age"))



'''Raise inbuilt Exception to handle different cases with same except block'''
# try:
#     x =int(input("enter the number for x"))
#     y =int(input("enter the number for y"))
#     result = x/y
#     print("result",result)
# except ZeroDivisionError as e:
#     print("you have enter the zero number for y")
#     x =int(input("enter the number for x"))
#     y =int(input("enter the number for y"))
#     result = x/y
#     print("result",result)
# except TypeError as e:
#     print("you have enter zero")
#     x=int(input("enter the number for x"))
#     y=int(input("enter the number for y"))
#     result=x/y
#     print("result", result)

import traceback
# def divide():
#   print("hello before try except")
#   try:
#     x= int(input("enter the number for x"))
#     y= int (input("enter the number for y"))
#     result=x/y
#     print(z)
#     print("result",result)
#   except Exception as e:
#     traceback.print_exc()
#     print(f"handle all exception{e}")
# divide()

'''trackback'''
# import traceback

# def divide():
#     try:    
#       print("hello before try execpt")
#       x =int(input("enter the number for x"))
#       y =int(input("enter the number for y"))
#       result = x/y
#       print("result",result)
    
#     except Exception as e:
#       traceback.print_exc()
#       print (f"handle all exception {e}")    
# divide()


