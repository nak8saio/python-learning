# list demostration

# Create list
list_of_employees = ["Alexa","Jhon","Steven"]

for emp in list_of_employees:
    print(f"Name of employees in the list at {list_of_employees.index(emp)}  :{emp}")
    
# List concatenation Expression
list1 = [1,3,5]
list2 = [2,4,6]

list3 = list1+list2
print(f"concantenated list:{list3}")
# sort list
list3.sort()
print(f"concantenated list after sorting : {list3}")

# List concatenated multiple copy of the list using * operator

list4 = ["Hello!"] * 5

print(f"concantenated multiple copy of lists:{list4}")

# check contditional expression in list "in" and "not in"

list5 = [1,3,5]
if 3 in list5:
    print(f"Found")
elif 7 not in list5:
    print(f"not in the list")    
else:
    print(f"Not Found")    

# find unique number in list
l1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)
print(f"unique number:{l2}")  

# sum of all list items
total = 0
if l2 !=0:
 for i in l2:
    total +=i
 print(f"sum of all list elements:{total}")
 total_sum = sum(l2)
 print(f"Using method sum(): {total_sum}")

#  Python program to create a list of 5 random integers.
import random
l3 = []
for x in range(5):
    random_number = random.randint(0,100)
    l3.append(random_number)
print(f"Random numbers are : {l3}")    

    

    