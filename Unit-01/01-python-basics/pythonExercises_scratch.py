# adsfh

# if 1<2 and 4>2:
# 	print("Math is fun")


# number = int(input("Enter a number"))
# if number<0:
# 	print("That number is less than 0!")
# elif number>0:
# 	print("That number is greater than 0!")
# elif number == 0:
# 	print("You picked 0!")


# if "xylophone".find("y") != -1:
# 	print("present")

# str = "asldjfs"
# if str == str.lower():
# 	print("str is all lowercase")


# nums1 = [1,2,3]
# nums2 = [1,2,3]
# print(nums1 == nums2)
# print(nums1 is nums2) # false, not the same object

# if nums1 == nums2:
# 	print("they are the same")


# people = ["tim","ray","matt","janey","greg","elie"]
# first_letters = [name[0:1].upper() for name in people]
# print (first_letters)

# numbers = [10,30,-100,25,7,-12,60] # -50 to 50
# filtered_nums = [num for num in numbers if num<50 and num>-50]
# filtered_nums = [num for num in numbers if -50<num<50]
# print(filtered_nums)

# names = ["alice","bob","charlie","dwayne","ezekial"]
# short_names_dic = {names[i]:len(names[i]) for i in range(0,len(names)) if len(names[i])<7}
# short_names_dic = {shorty:len(shorty) for shorty in names if len(shorty)<7}
# print(short_names_dic);

def print_keywords(**kwargs):
	for keyword in kwargs:
		print(keyword)
	

print_keywords(a=1,b=2)


def keyword_check(**kwargs):
	for keyword in kwargs:
		if len(keyword)>10:
			return "long keyword"			
	return "no long keyword"

print(keyword_check(my_super_longUberLushousLongKeyword = "hi"))
print(keyword_check(my_super = "wuddup dog"))
print(keyword_check(a = "hi", b = "hi", c = "hi"))
print(keyword_check(a = "hi", b = "hi", my_super_longUberLushousLongKeyword = "hi"))











