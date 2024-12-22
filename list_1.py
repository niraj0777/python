# numbers=[1,2,3,4,5]
# fruits=['apple','banana','cheery']
# mixed_type=[10,'hello', True, 3.34]
# print(fruits[1])
# print(numbers[-3])
# print(mixed_type[2])

# # slicing

# print(numbers[1:4])
# print(fruits[:2])
# print(mixed_type[1:3])

# replacing

# fruits=["apple", "banana", "cheery"]
# fruits[1] = "blackcurrant"
# print(fruits)

# fruits=["apple", "banana", "cheery", "orange", "kiwi", "mango"]
# fruits[2:5] = ["blackcurrant", "watermelon", "pineapple"]
# print(fruits)

# # insert
# fruits=["apple", "banana", "cheery"]
# fruits.insert(2, "mango")
# print(fruits[2])

# # append : puts value at last
# fruits=["apple", "banana", "cheery"]
# fruits.append("mango")
# print(fruits)

# extend
# fruits=["apple", "banana", "cheery"]
# tropical=["mango", "pineapple", "kiwi"]
# fruits.extend(tropical)
# print(fruits)

# mixed = [1, "apple", "banana",2,5,7,"cheery",True,4,9,10]

# even=[x for x in mixed if type(x)== int and x % 2 == 0]
# odd=[x for x in mixed if type(x) == int and x % 2 != 0]
   
# print("even numbers",even)
# print("odd numbers",odd)

# mixed = [1, "apple", "banana",2,5,7,"cheery",True,4,9,10]

# even_list = []
# odd_list = []
# for i in range (11):
#     print (mixed[i])
#     if type (mixed[i]) == int and mixed[i] % 2 == 0:
#         even_list.append(mixed[i])
#     elif type (mixed[i]) == int and mixed[i] % 2 != 0:
#         odd_list.append(mixed[i])

# print("odd list",odd_list)
# print("even list",even_list)  

# even_list = []
# odd_list = []
# for a in range(mixed[a]):
#     if type(mixed[a]) == str and len[a] % 2 == 0:
#         even_list.append(mixed[a])
#     elif type (mixed[i]) == str and len[a] % 2 != 0:
#         odd_list.append(mixed[a]) 
# print("odd list",odd_list)
# print("even list",even_list)          

# mixed = [1, 'apple', 'banana', 2, 3, 7, 'cherry', True, 4, 9, 6]

# odd_numbers = []
# even_numbers = []
# odd_strings=[]
# even_strings=[]

# for a in range(len(mixed)):
#     if type(mixed[a])==int:
#         if mixed[a] % 2 == 0:
#             print(a, "is even")
#             even_numbers.append(mixed[a])
#         else:
#             print(mixed[a], "is odds")
#             odd_numbers.append(mixed[a])

#     elif type(mixed[a])==str: 
#         if (len(mixed[a]) % 2) == 0:
#             print(mixed[a], "is even string")
#             even_strings.append(mixed[a])
#         else:
#             print(mixed[a], "is odd string")
#             odd_strings.append(mixed[a])       

# print("Odd numbers:", odd_numbers)
# print("Even numbers:", even_numbers)
# print("Odd strings:", odd_strings)
# print("Even strings:", even_strings)

# mixed = [1, 'apple', 'banana', 2, 3, 7, 'cherry', True, 4, 9, 6]



# mixed = [1, 'apple', 'banana', 2, 3, 7, 'cherry', True, 4, 9, 6]

# vowels = 'aeiou'

# for item in mixed:
#     if type(item) == str:
#         for char in item:
#             if char.lower() in vowels:
#                 print(char, end=' ')

# fruits=['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)                


# len()

# fruits=['apple', 'banana', 'cherry']
# print(len(fruits))


# fruits=['apple', 'banana', 'cherry']
# index = 0 
# while index < len(fruits):
#     print(fruits[index])
#     index += 1

# # remove
# fruits=['apple', 'banana', 'pineapple', 'cherry']
# fruits.remove('pineapple')
# print(fruits)    

# pop() : remove the specified index

# fruits=['apple', 'banana', 'cherry']
# fruits.pop(1)
# print(fruits)

# del : to remove specfied index
# fruits=['apple', 'banana', 'cherry']
# del fruits[0]
# print(fruits)

# clear: empties the list
# fruits=['apple', 'banana', 'cherry']
# fruits.clear()
# print(fruits)

# thislist = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]
# output 1: thislist = ["cheery", grapes]
# output 2: thislist = ["apple", "banana", "cherry", "grapes"]
# output 3: "apple" - count-2


# thislist = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]
# thislist.remove("banana")
# thislist.remove("banana")
# thislist.remove("banana")
# thislist.remove("apple")
# thislist.remove("apple")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]
# newlist= []
# for x in thislist:
#     if thislist.count(x) ==1:
#         newlist.append(x)
# print(newlist)        


# # thislist = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]
# seen=[]
# for x in thislist:
#     if x not in seen:
#         seen.append(x)
# print(seen)        

# # thislist = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]
# count = 0
# for x in thislist:
#     if x == 'apple':
#         count +=1
# print ("the number",count)        

# fruits = ["apple", "banana", "cherry", "banana", "banana", "apple", "grapes"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)  

# fruits = ["apple", "banana", "cherry", "pineapple", "kiwi", "mango", "grapes"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "pineapple", "kiwi", "mango", "grapes"]
# newlist = [x for x in fruits if "b" in x]
# print(newlist)

# numbers = [1,2,3,4,5,6,7,8,9]
# even_list=[]
# for x in numbers:
#     if x%2 == 0:
#         even_list.append(x**2)

# print(even_list)  


# numbers = [1,2,3,4,5,6,7,8,9]
# numbers = [x**2 for x in numbers if x%2 == 0]
# print(numbers)

# numbers = [1,2,3,4,5,6,7,8,9]
# newlist= [x if x%2 == 0 else "false" for x in numbers]
# print(newlist)

# newlist = [x if x%2 != 0 else "false" for x in numbers]
# print(newlist)



# matrix
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix)
# x = matrix[0]
# print(x)
# print(type(x))
# print(x[1])

# print(matrix[0][0])
# print(matrix[1][2])        



# for x in matrix:
#     print(x)
#     break

# add all number of matrix in loop

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# total = 0
# for row in matrix:
#     for numbers in row: 
#         total += numbers
# print("The total sum is:", total)       


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total = sum(num for row in matrix for num in row)

# print("The total sum is:", total)


# .sort
# thislist=["apple", "banana", "cheery", "mango", "orange", "kiwi", "monkey"]
# thislist.sort(reverse=True)
# print(thislist)

# new_list= sorted(thislist)
# print(new_list)

# copy
# thislist=[1,2,3]
# list2 = thislist.copy()
# list2.append(4)

# print("list2",list2)
# print ("thislist",thislist)

# thislist=["apple", "banana", "cheery"]
# mylist=list(thislist)
# print(thislist)


# slice operator
# thislist=["apple", "banana", "cheery"]
# mylist=thislist[:]
# print(mylist)


# join twolist
# list1=["a", "b", "c"]
# list2=[1,2,3]
# list3= list1 + list2
# print(list3)

# # TUPLE 
# fruits=("apple", "banana", "cheery")
# print(fruits[1])

# convert tuple into list 
# x=("apple", "banana", "cheery")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# fruits=("apple", "banana", "kiwi")
# (green, yellow, red) = fruits
# print(green)
# print(red)
# print(yellow) 

# unpacking tuples
# fruits=("apple", "banana", "kiwi", "strawberry", "mango")
# (*green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red) 

'''set'''
# a={}
# print(type(a))

# a=set()
# print(a)

# my_set={"a","b","c","d"}
# print(my_set)

# thisset={'apple','banana','kiwi','pineapple','pineapple','apple'}
# print(thisset)

'''add set'''
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

'''update()'''
# thisset = {"apple", "banana", "cherry"}
# fruits = {"pineapple", "mango", "papaya"}
# thisset.update(fruits)
# print(thisset)

'''remove() and discard'''
# thisset={"apple", "banana", "cherry","grapes"}
# thisset.remove("banana")
# thisset.discard("grapes")
# print(thisset)

'''pop()'''
# thisset={"apple", "banana", "cherry","grapes"}
# x=thisset.pop()
# print(x)
# print(thisset)

'''Loop set'''
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

'''Union'''
# set1={"a","b","c","d"}
# set2={1,2,3,4}
# set3={"Josh","Niruta","Ishant"}
# set4={"apple", "banana", "cherry"}
# set5=set1.union(set2,set2,set3,set4)
# print(set5)

'''use | to join two set'''
# set1={"a","b","c","d"}
# set2={1,2,3,4}
# set3={"Josh","Niruta","Ishant"}
# set4={"apple", "banana", "cherry"}
# set5=set1|set2|set3|set4
# print(set5)

'''intersection()'''
# set3={"Josh","Niruta","Ishant","apple","banana",5}
# set4={"apple", "banana", "cherry","Ishant"}
# set1={1,2,3,4,5}
# set2=set3.intersection(set4)
# print(set2)

'''You can use the & operator instead of the intersection() method'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)

'''intersection_update()'''
# set1 = {"apple", "banana", "cherry","a"}
# set2 = {"google", "microsoft", "apple","a"}
# set3={"a","b","c","d"}
# set4={1,2,3,4,"a"}
# set1.intersection_update(set2,set3,set4)
# print(set1)

'''The values True and 1 are considered the same value. The same goes for False and 0'''
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

'''Difference()'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set={"Josh","Niruta","Ishant","apple"}
# set3=set1.difference(set2,set)
# print(set3)

'''-'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = {"apple", "cherry"}
# set4 = { "microsoft", "apple"}
# set5=set1-set2-set3-set4
# print(set5)

'''difference_update'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

'''symmetric_difference()'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

'''symmetric_difference for more than 2 sets==we use '^' this symbol'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = {"apple", "cherry"}
# set4 = { "microsoft", "apple"}
# set = set1^set2^set3^set4
# print(set)

'''disjoint'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set=set1.isdisjoint(set2)
# print(set)

'''subset'''
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# w=y.issuperset(x)
# z = x.issubset(y)
# print(z)
# print(w)

'''x = ((1, 2), (2, 3), (4, 5), (6, 7), (0, 2), (3, 2))'''

# Initialize variables to store the tuple with the highest sum and the highest sum value
# max_sum = 0
# max_tuple = ()

# # Iterate through each tuple
# for tup in x:
#     tup_sum = sum(tup)  # Calculate the sum of the current tuple
#     if tup_sum > max_sum:
#         max_sum = tup_sum  # Update the highest sum
#         max_tuple = tup  # Update the tuple with the highest sum

# print("The tuple with the highest sum is {max_tuple} and the sum is {max_sum}",max_tuple, max_sum)


