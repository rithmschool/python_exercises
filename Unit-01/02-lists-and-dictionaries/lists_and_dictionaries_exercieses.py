#############################################
# List Comprehension

###############
# 1. 
[print(value) for value in [1,2,3,4]]

###############
# 2.
[print(value*20) for value in [1,2,3,4]]

###############
# 3.
print([value[0] for value in ["Elie", "Tim", "Matt"]])

###############
# 4.
print([value for value in [1,2,3,4,5,6] if value%2==0])

###############
# 5.
print([value1 for value1 in [1,2,3,4] for value2 in [3,4,5,6] if value1==value2])

###############
# 6.
print([value.lower()[::-1] for value in ["Elie", "Tim", "Matt"]])

###############
# 7.
print("".join([letter1 for letter1 in "first" for letter2 in "third" if letter1==letter2]))

###############
# 8.
print([number for number in range(1,100) if number%12==0])

###############
# 9.
print([letter for letter in "amazing" if letter not in ["a","e","i","o","u"]])

###############
# 10.
print([[number for number in range(0,3)] for value in range(0,3)])

###############
# 11.
print([[number for number in range(0,10)] for value in range(0,10)])



print("#############################################")
#############################################
# Dictionary Comprehension

###############
# 1. 
print({k:v for k,v in [("name", "Elie"), ("job", "Instructor")]})

###############
# 2. 
states_full = ["California", "New Jersey", "Rhode Island"]
states_abbr = ["CA", "NJ", "RI"]
print({k:v for k,v in list(zip(states_abbr,states_full))})

###############
# 3. 
print({k:0 for k in ["a","e","i","o","u"]})

###############
# 4. 
print({num-64:chr(num) for num in range(65,91)})

###############
# Super Bonus
# print({k:v for k,v in "awesome sauce" if })



