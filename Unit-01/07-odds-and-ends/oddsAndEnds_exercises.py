def get_next_multiple(num):
	for value in range(num, 1000):
		if value%num==0:
			yield value


genMultipleOfTwo = get_next_multiple(2)
next(genMultipleOfTwo)
next(genMultipleOfTwo)
next(genMultipleOfTwo)
next(genMultipleOfTwo)

genMultipleofThirteen = get_next_multiple(13)

next(genMultipleofThirteen)
next(genMultipleofThirteen)
next(genMultipleofThirteen)
next(genMultipleofThirteen)

print("--- is_prime ---------------------------------------------")

def is_prime(num):
	for value in range(2,num):
		if num%value==0:
			return False

	return True
	

is_prime(500)

print(is_prime(11)) # True
print(is_prime(122)) # False
print(is_prime(35))
print(is_prime(89))


print("--- get_next_prime ---------------------------------------------")
import itertools
def get_next_prime():
	for value in itertools.count(2):
		if is_prime(value):
			yield value

# 	for value in range(1,1001):
# 		if value%2!=0 and value%3!=0:
# 			yield value

gen = get_next_prime()
print(next(gen))


print("---------------------------------------------")

def double_result(func):
	def wrapper(*args):
		return func(*args)*2

	return wrapper


def add(a,b):
    return a+b

add(5,5) # 10

@double_result
def add(a,b):
    return a+b

print(add(10,5))


print("---------------------------------------------")


def only_even_parameters(func):
	def wrapper(*args):
		for value in args:
			if value%2==0:
				return func(*args)
			else:
				return "Please add even numbers!"

	return wrapper


@only_even_parameters
def add(a,b):
    return a+b

print(add(5,5)) # "Please add even numbers!"
print(add(4,4)) # 8
print(add(7,6))
print(add(10,6))

@only_even_parameters
def multiply(a,b,c,d,e):
    return a*b*c*d*e

print(multiply(2,3,4,5,6))
print(multiply(4,4,4,4,4))


print("---------------------------------------------")

def sum_index(collection):
	results=0
	for k,v in enumerate(collection):
		results+=k
	return results


print(sum_index([1,2,3,4])) # 6
print(sum_index((1,2,3,4,5,5,5,5,5,5,5))) # 6


print("---------------------------------------------")
import re

def remove_vowels(string):
	newString = re.sub("(?i)[aeiouy]", "", string)
	return newString

print(remove_vowels("awesome")) # wsm
print(remove_vowels("MAtt")) # Mtt
print(remove_vowels("aEeiOouHH")) 



print("---------------------------------------------")
def collect_email(string):
	split_char = '@'
	newString = re.split(split_char, string)
	return newString[0]

print(collect_email('elie@rithmschool.com')) # elie
print(collect_email('tom@gmail.com')) # tom



print("---------------------------------------------")
def collect_domain_name(string):
	split_char = '@'
	newString = re.split(split_char, string)
	return newString[1]

print(collect_domain_name('elie@rithmschool.com')) # rithmschool.com
print(collect_domain_name('tom@gmail.com')) # gmail.com


print("---------------------------------------------")
def valid_phone_number(string):
	newString = re.search("(\d-)?\d\d\d-\d\d\d-\d\d\d\d", string)
	if newString==None:
		return False
	else:
		return True

print(valid_phone_number("1-567-425-1234")) # True
print(valid_phone_number("123-456-7894")) # True
print(valid_phone_number("173-495-1234")) # True
print(valid_phone_number("1-973-495-124")) # False
print(valid_phone_number("173-49-1234")) # False




