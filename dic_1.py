# '''empty dictionary'''
# empty_dict={}

# '''dictionary with intital values'''
# my_dict={
#     "name" :"ram",
#     "age" : 20,
#     "city" : "ktm"
# }
# print(my_dict["name"])
# print(my_dict.get("address"))
# my_dict["age"]=31
# my_dict["gender"]= "male"
# print (my_dict)



# '''mixe key'''
# mixed_dic ={
#     1 : "one",
#     "2" : "two", 
#     (1,2) :"tuple"
# }


# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
# #     "year" : 1964
# #     }
# # x = car.keys()
# # print(x)
# # car["color"] = "white"
# # print(x)
# # x = car.values() 
# # # dict_values(['Ford', 'Mustang', 1964, 'white'])
# # print(x)

# students = {
#     "name" : "abc",
#     "rollno" : 12,
#     "address" : "ktm",
#     "id": 12
# }

# for k,v in students.items():
#     if k == "rollno" and v == 12:
#         students [k]= 1

# if students.get("phoneno.")== None:
#     students["Phoneno."] = 123456789

# print(students)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily)

# myfamily ={}
# n = int (input("enter the number of child : "))

# for x in range(n):
#     name = input("enter the name : ")
#     year = int(input("enter the year"))
#     myfamily[f"child{x}"] = {
#         "name" : name,
#         "year" : year
#     }

#     # add
#     myfamily["child1"]["address"] = "ktm"
#     print(myfamily)

# records = {
#     1: {
#         "name" : "ram",
#         "age": "11",
#         "marks" : {
#             "english" : 56,
#             "maths" : 23,
#             "science" : 45
#         }
#     },
    
#     2: {
#         "name" : "hari",
#         "age": "12",
#         "marks" : {
#             "english" : 54,
#             "maths" : 27,
#             "science" : 55 
#         }  
#     },
    
#     3: {
#         "name" : "ram",
#         "age": "11",
#         "marks" : {
#             "english" : 88,
#             "maths" : 90,
#             "science" : 99 
#         }  
#     } 
# }

# Initialize variables to store the highest total marks and the corresponding student details


# highest_total = 0
# top_student = {}

# Iterate through each student's records


# for student_id, student_info in records.items():
#     total_marks = sum(student_info["marks"].values())



#     # Compare and update if current student's total marks are higher
#     if total_marks > highest_total:
#         highest_total = total_marks
#         top_student = {
#             "student_id": student_id,
#             "name": student_info["name"],
#             "total_marks": highest_total
#         }

# print(f"Top student is {top_student['name']} (ID: {top_student['student_id']}) with total marks: {top_student['total_marks']}")

