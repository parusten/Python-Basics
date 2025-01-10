# type casting: int(str,num), float(), str(), bool()
# age = int([]) # type error
age = input("Enter the age between 0 to 100:>> ")
print(age, type(age))
# help(input)

# Branching/Selection and Iteration/Looping
'''
if condition:          if conditions{      }
    statement
    statement
elif condition:
    statements
    statements
else:
    other codes
'''

'''
while condition:
    statements
    # break and continue
    break: terminates the loop  on trigger
    continue: bypass the code below it but continues the loop
'''
"""
condition: expression that returns either True or False
False in Python:
    0,0.0, False, None
    Collection: [], (), {},""
Others are always True
"""

try:
    age = int(age)
    # logical operators: and, or, not
    if (age >= 0) and (age <= 100):  # age == 0 and 100
        new_age = int(age) - 10
        print("My new age is", new_age)
    else:
        print("The age should be between 0 to 100!")
except ValueError as error:
    print("The age should be number")
    print(error)

# a = True and 1
# b = 1 and True
# c= 0 or "Sandip"

# print(a,b,c)

'''
for i in range(n):   for (int i=0;i<n;i++)
    stements
    
i: iteration variable
in: membership operator
    if statements, checks
    for statements, iterate
    always needs collection/iterables
range(n): generates number from 0 to n-1, gives n numbers starting from 0
range(start, stop, step)
'''

# for i in range(3):
#     if i == 2:
#         # pass  # this section handles the condition for something
#         break
#     print(i)
