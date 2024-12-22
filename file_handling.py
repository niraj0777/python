# f = open("filehandling.txt", "r")
# value = f.read()
# print(type(value))

'''readline()'''
# f= open("filehandling.txt", "r")
# print(f.readline())
# print(f.readable())

''''''
# f= open("filehandling.txt", "r")
# for x in f:
#     print(x)

'''close'''    
# f= open("filehandling.txt", "r")
# print(f.readline())
# f.close()

# f= open("filehandling.txt", "r")
# print(f.readlines())

# f= open("filehandling.txt", "r")
# values = f.readlines()
# print("values",values)
# a= ["hello\n", "testing\n"]
# f.writelines(a)






# f= open("filehandling.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# f= open("filehandling.txt", "r")
# print(f.read())

# f= open("filehandling.txt", "w")
# f.write("Now the file has more content!")
# f.close()

# f= open("filehandling.txt", "r")
# print(f.read())

''''''
# file_path = 'filehandling.txt'
# with open(file_path, 'r') as file:
#     content = file.read()
#     print(content)


''''''
# import os 
# os.remove("filehandling.txt")

''''''
# import os 
# if os.path.exists("filehandling.txt"):
#     os.remove("filehandling.txt")
# else:
#     print("this file doesnot exist")    

''' name,age,science,maths,english,total marks
ram,13,57,60,70,...
hari,10,47,90,49,...
shyam,11,,66,50,30,...
gita,12,27,61,72,...
sita,13,51,36,76,... '''

# file_path = "filehandling.txt"
# with open(file_path, "r") as file:
#         f = file.readlines()
# for x in f [1:]:
#         data = x.strip().split(',')
#         name = data[0]
#         age = int(data[1])
#         science = int(data[2]) 
#         maths = int(data[3])
#         english = int(data[4])
#         total = science + maths + english
        # print(f"Name: {name}, Age: {age}, Science: {science}, Maths: {maths}, English: {english}, Total Marks: {total}")

# import csv


# data =[
#     ['Alice', 30, 'London'],
#     ['Bob', 25, 'Paris'],
#     ['Charlie', 35, 'Berlin']
# ]

# file_path = 'output.csv'
# with open(file_path, mode='w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name', 'age', 'city'])
#     for row in data:
#         csv_writer.writerow(row)

# import csv


# data =[
#     ['Alice', 30, 'London'],
#     ['Bob', 25, 'Paris'],
#     ['Charlie', 35, 'Berlin']
# ]
 
# with open("input.csv", mode='w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name', 'age', 'city'])
#     while True:
#         if input("enter 1 for exit else any key")=='1':\
#         break
#         name = input("enter the name:")
#         age = int(input("enter the age"))
#         city = input("enter the city")

#         ra = [name, age, city]
#         csv_writer.writerow(ra)

# print("Data has been written to 'input.csv'")
        



# while True:
#     name = input("Enter the name: ")
#     age = int(input("Enter the age: "))
#     city = input("Enter the city: ")
#     data.append([name, age, city])
#     continue_input = input("Do you want to add another entry? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

# print("the Data is :")
# for entry in data:
#     print(entry)


# import csv
# file_path = 'data.csv'
# with open(file_path, mode ='r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#      print(row)


# import csv
# file_path = 'data.csv'
# with open(file_path, mode ='r') as file:
#     csv_reader = csv.DictReader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#      print(row['Name'], row['age'], row['city'])

# import csv

# data =[
#     {'Name': 'Alice', 'Age': 30, 'City': 'London'},
#     {'Name': 'Bob', 'Age': 20, 'City': 'Paris'},
#     {'Name': 'Ali', 'Age': 25, 'City': 'KTM'}
# ]

# file_path = 'output.csv'
# fieldnames = ['Name', 'Age', 'City'] 

# with open(file_path, mode='w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,3,5,7,11]

x1 = [6,7,8,9,10]
y1 = [2,3,5,7,11]

plt.plot(x,y, marker= 'o', linestyle= '--', color ='b', label='prime_numbers')
plt.plot(x1,y1, marker = 'o',linestyle = '-' ,color = 'r',label = ' Numbers' )

plt. xlabel('x Axis')
plt. ylabel('y Axis')
plt.title('Prime numbers plot')

plt.legend()
plt.show()


