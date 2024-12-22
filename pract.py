# weather the number is even or odd
 
# a=int(input("Enter the number :"))
# if (a%2 ==0):
#     print ("the number is even ")
# else:
#     print("the number is odd ") 

# wheather the number is positive or negative or odd
# a=int(input ("Enter the number"))
# if(a>0):
#     print("the number is positive")
# elif(a<0):
#     print("the number is negative")
# else :
#     print ("the number is 0")   
   
# value=input("Enter the number:")
# if value.isdigit():
#     num=int(value)
#     print("convert into integer",num)
# elif "." in value:
#     num=float(value)
#     print("convert into float",num)  
# elif value.isalpha():
#     num=str(value)
#     print("convert into string",num)     
# else:
#     print("invalid number input")    

# x = int(input("Enter the number"))
# y = int(input("Enter the number"))

# if x>y:
#     print("x is greater")
# elif y>x:
#     print("y is greater")
# else:
#     print("equal")
             
# a = int(input("Enter the number"))
# b = int(input("Enter the number"))
# c = int(input("Enter the number"))
# if a>b and b>c :
#    print ("a is greater",a)
# elif a==b and c==0 :
#    print("{a}and{b} are equal when {c} is equal to zero")
# elif a==b and b==c and a!=0 :
#    print("{a},{b},{c} are not zero")   
# else:
#    print("invalid")    

# x=int(input("Enter the number"))
# if x>=0 and x<10:
#     print(f"{x} positive single-digit number")
# elif x>=10:
#     print(f"{x} positive number, but not single-digit number")
# else:
#     print(f"{x} is not positive")     

# How do you generate a list of even numbers from 0 to 20?  
# even_numbers = [x for x in range(21) if x % 2 == 0]  
# print(even_numbers)       
   

# name= [1,"abc",2,2.25,True,"apple","cheery","grapes"]
# for x in name: 
#   if x  == "apple":
#     print (x)

# for x in "cherry":
#     print(x)  

# evennumber = [ x for x in range (20) if x%2==0]
# print (evennumber)

# for x in range(1,21,2):
#   print (x)

# 1-20

# evennumber = [x for x in range(1,20) if x%2 ==0]
# print (evennumber)
# i=1
# evenc=0
# oddc=0
# for x in range(21):
#   if x%2 ==0:
#    print("evennumber",x)
#    evenc += 1
#   else:   
#    oddc += 1
#    print("Total Even Numbers: {evenc}",x)
#    print("Total Odd Numbers: {oddc}",x)    

# Initialize counters
# even_counter = 0
# odd_counter = 0

# for num in range(1,21):
#     if num % 2 == 0:  
#         even_counter += 1
#     else:  
#         odd_counter += 1

# print("Even numbers count:", even_counter)
# print("Odd numbers count:", odd_counter)
   
# even_product = 1
# odd_product = 1

# for num in range(1,11):
#     if num%2 ==0:
#         even_counter *= num
#     else:
#         odd_counter *= num
# print("the product of even num:",even_counter)  
# print("the product of even num:",odd_counter)    

# while True:
#     num = int(input("Enter the number"))
#     if num == 3:
#         print("the number is")
#         break
#     print("num",num)
# print("outside the loop")    

# num= int(input("Enter the number"))
# for num in range(10):
#   if num == 4:
#      break
#   print("num",num)
# print("outside the loop")  

# num = int (input("Enter th number"))
# for num in range(10):
#    if num<5:
#       break
#    print("num",num)
# print("outside the loop")   

# sum = 0
# for x in range(1,31):
#    if x == 10: 
#       continue
#    sum += x
# print("Total sum",sum)   

# for x in range(5):
#     print("x",x)

#     for y in range(5):
#         print("y",y)   


# x = 1
# y = 2
# print("before swap x is",x)
# print("before swap y is",y)

# x,y = y,x
# print("after swap x is",x)
# print("after swap y is",y)

# x= 5
# y= 9
# print("before swap x is",x)
# print("before swap y is",y)
# z=x
# x=y
# y=z
# print("before swap x is",x)
# print("before swap y is",y)

# x=5
# print("x",x)
# y=10
# print("y",y)
# x = x + y
# y = x - y
# x = x - y
# print("x",x)
# print("y",y)

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j,end=" ")
#     print("\n")

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print("\n")
#     i += 1


'''SQL'''


import sqlite3
'''function to intialize sqlite database and table'''
# conn = sqlite3.connect('data.db')
# c = conn.cursor() 
# c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email TEXT)')
# conn.commit()
# conn.close()  

'''function to create a new record (create operation)'''
# conn = sqlite3.connect('data.db')
# c = conn.cursor()
# name = input("Enter the name")
# age = int(input("Enter the age"))
# email= input("Enter the email")
# c.execute('INSERT INTO users (name, age, email) VALUES (?,?,?)', (name, age, email))
# conn.commit()
# conn.close()

''' function to read and dispaly all records (read operation) '''
# conn= sqlite3.connect('data.db')
# c = conn.cursor()
# c.execute('SELECT * FROM users')
# rows = c.fetchall()
# print(rows)
# conn.close()

# for row in rows:
#     print(row)

'''function to update a record (update operation)'''
# conn = sqlite3.connect('data.db')
# c = conn.cursor()
# name = input("Ente the name")
# user_id = int(input("Enter the user_id"))
# age = int(input("Enter the age"))
# email = input("enter the email")
# c.execute('UPDATE users SET name = ?, age = ?, email = ? WHERE id = ?', (name, age, email, user_id))
# conn.commit()
# conn.close()

'''Function to delete a record (Delete operation)'''
# conn = sqlite3.connect('data.db')
# c = conn.cursor()
# user_id = int(input("Enter the id"))
# c.execute('DELETE FROM users WHERE id = ?', (user_id,))
# conn.commit()
# conn.close()


'''create functtion to run the CLI interface'''
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks to show.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 0 < task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def run_cli():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
run_cli()

