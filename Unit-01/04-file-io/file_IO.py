##################################################
# Part 1 - Text Files

def add_student(first_name):
	with open('students.txt', 'a') as file:
		file.write(first_name+"\n")

# add_student("Raymond")
# add_student("Greg")

def find_student(first_name):
	with open('students.txt', 'r') as file:
		for row in file:
			if row.strip()==first_name:
				return "Found a student by that name: {}.".format(row.strip())
	return "Did not find a {}".format(first_name)


# find_student("Matt")


def update_student(first_name, new_name):
	with open('students.txt', 'r') as file:
		data = list(file)
		# new_data = [new_name for name2 in [name.strip() for name in data] if first_name==new_name else name2]
		# [name for name in new_data if first_name != new_name else new_name]
		new_data = []
		for idx,value in enumerate([name.strip() for name in data]):
			if value==first_name:
				new_data.append(new_name+"\n")
			else:
				new_data.append(value+"\n")
	
	with open('students.txt', 'w') as file2:
		file2.write("".join(new_data))

# update_student("Matt","Whiskey")


def remove_student(first_name):
	with open('students.txt', 'r') as file:
		data = list(file)
		new_data = []
		for idx,value in enumerate([name.strip() for name in data]):
			if value!=first_name:
				new_data.append(value+"\n")				
	
	with open('students.txt', 'w') as file2:
		file2.write("".join(new_data))


# remove_student("Whiskey")


###############
# Bonus







##################################################
# Part 2 - CSV
import csv

def print_names():
	with open("users.csv") as csvfile:
		reader = csv.reader(csvfile, delimiter=",")
		rows = list(reader)
		for row in rows:
			print(row[0], row[1])

# print_names()


def add_name():
	first_name = input("Enter first name: ")
	last_name = input("Enter last name: ")
	with open("users.csv", "a") as csvfile:
		data_writer = csv.writer(csvfile, delimiter="," , lineterminator="")
		csvfile.write('\n')
		data_writer.writerow([first_name,last_name])


add_name()









