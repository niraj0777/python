# s = "Hello, World"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(s[6])
# print(s[7])
# print(s[8])
# print(s[9])
# print(s[10])
# print(s[11])

# var = "invalid escape sequence"
# count_e= var.count("e")
# print(count_e)

# var = "invalid escape sequence"
# count = 0
# for char in var:
#     if char == "e":
#         count += 1
# print(count)


# var = "invalid escape sequence absndfds"
# print(len(var))
# count = 0
# for x in range(len(var)):
#     if var[x] == "e":
#         count += 1
# print(count)

# var = "invalid escape sequence"
# a=0
# for x in var:
#     a= a + 1
#     print(x,a)
# print(var[0:7])    

# s = "Hello, World!"
# print(s[7:12])
# print(s[:7])
# print(s[7::2])
# print(s[0:5:2])
# print(s[6:11:2])
# print(s[::-1])
# print(s[6:0:-1])

# s= "Heello, world"

# for char in s:
#     if char.lower() == "h":
#         print("the charater is 'h' or "H".")
#     else:
#         print("the charater is 'h' or "H".")

# s= "Hello"
# # s[0]="h"
# s= "h" + s[1:]
# print(s)

# s = "Hello, World!"
# s = s.replace("World","Nepal")
# print(s)

# a = "hello, World"
# print(a.upper())

# b = "hello, World"
# print(b.lower())


# c =" hello, World"
# print(c.title())

# a ="##########hello world##########"
# print (a.lstrip("#"))
# print (a + "dsf")
# print (a.rstrip())

# c =" hello, World"
# print(c.split())

# c=" "
# words =[ "hy", " you", "boy "]
# print(c.join(words))

# a=int(input("enter the first value"))
# b=int(input("enter the second value"))
# s=f"the sum of {a} and {b} is {a+b}."
# print(s)

# s="hello"
# print(s.islower())

# s="hello,{}"
# print(s.format("Python"))

# name = "#######hello####world######"
# # print(name.strip("#"))
# print(name.replace ("#",""))

output = "#######hello####world######"
name ="hello world"
total_output_length = len(output)
removing_left_side_length = len(output.lstrip("#"))
left_side_value = total_output_length - removing_left_side_length
removing_right_side_length = len(output.rstrip("#"))
right_side_value = total_output_length - removing_right_side_length

left = left_side_value
right = right_side_value
a = "#"*left + "hello" + name.replace(" ", "####") + "#"*right
print(a)


