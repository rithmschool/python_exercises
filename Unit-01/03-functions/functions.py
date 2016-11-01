def difference(num1,num2):
	return num1-num2

difference(2,2)
difference(0,2)

def product(num1,num2):
	return num1*num2

product(2,2)
product(0,2)

def print_day(day_number):
	if day_number == 1:
		return "Sunday"
	elif day_number== 2:
		return "Monday"
	elif day_number==3:
		return "Tuesday"
	elif day_number==4:
		return "Wednesday"
	elif day_number==5:
		return "Thursday"
	elif day_number==6:
		return "Friday"
	elif day_number==7:
		return "Saturday"
	
	return None

print_day(4)
print_day(41)


def last_element(num_list):
	if len(num_list)==0:
		return None
	else:
		return num_list[-1]

last_element([1,2,3,4,5])


def number_compare(num1,num2):
	if num1>num2:
		return "First is greater"
	elif num1<num2:
		return "Second is greater"
	else:
		return "Numbers are equal"

number_compare(1,1)
number_compare(1,2)
number_compare(2,1)


def single_letter_count(string1, string2):
	counter=0
	for letter in string1.lower():
		if letter == string2.lower():
			counter+=1
	return counter

single_letter_count('Crazy Amazing','A')



def multiple_letter_count(string):
	dictionary = {}
	for letter in string:
		if dictionary.get(letter) == None:
			dictionary[letter]=1
		else:
			dictionary[letter] +=1
	return dictionary

multiple_letter_count("hello")
multiple_letter_count("person")


def list_manipulation(list1,command,location,*value):
	if len(value)>0:
		value = value[0]

	if command == "remove":
		if location == "beginning":
			return list1.pop(0)
		else:
			return list1[-1]
	else:
		if location == "beginning":
			list1.insert(0,value)
			return list1
		else:
			list1.insert(-1,value)
			return list1


list_manipulation([1,2,3], "remove", "end")
list_manipulation([1,2,3], "remove", "beginning")
list_manipulation([1,2,3], "add", "beginning", 20)
list_manipulation([1,2,3], "add", "end", 30)


def is_palindrome(string):
	return string.replace(" ","").lower() == string.replace(" ","").lower()[::-1]

is_palindrome('testing')
is_palindrome('tacocat')
is_palindrome('hannah')
is_palindrome('robert')


def frequency(list1,search_term):
	return list1.count(search_term)

frequency([1,2,3,4,4,4], 4)
frequency([True, False, True, True], False)


def flip_case(word, letter_to_flip):
	results = ""
	for letter in word:
		if letter.lower()==letter_to_flip.lower():
			if letter.islower():
				results+=letter.upper()
			else:
				results+=letter.lower()
		else:
			results+=letter
	return results

flip_case("Hardy har har", "h") # "hardy Har Har"


def multiply_even_numbers(num_list):
	results=1;
	for num in num_list:
		if num%2==0:
			results=results*num
	return results

multiply_even_numbers([2,3,4,5,6])


def mode(num_list):
	counted = {}
	for num in num_list:
		if counted.get(num)==None:
			counted[num]=1
		else:
			counted[num]+=1
	largest = None
	for key in counted:
		if counted[key]>largest:
			largest = key 

	return largest

mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4



def capitalize(string):
	return string.capitalize()

capitalize("tim") # "Tim"
capitalize("matt") # "Matt"




