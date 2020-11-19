from datetime import datetime
TasksDict = {}
def append_value(dict_obj, key, value):
# Check if key exist in dict or not
	if key in dict_obj:
		# Key exist in dict.
		# Check if type of value of key is list or not
		if not isinstance(dict_obj[key], list):
			# If type is not list then make it list
			dict_obj[key] = [dict_obj[key]]
			# Append the value in list
			dict_obj[key].append(value)
	else:
		# As key is not in dict,
		# so, add key-value pair
		dict_obj[key] = value
dt = str(input("Enter date in correct format (dd.mm.yyyy): "))
try:
	datetime.strptime(dt, "%d.%m.%Y")
except ValueError:
	print("Incorrect date value!")
	exit()
else:
	print("You enter this date: {}".format(dt))
finally:
	pass
choose = int(input("For this date you can add new tasks (enter 1) or view a list of existing tasks (enter 2): "))
if choose == 1:
	task = str(input("Enter task for this day: "))
	append_value(TasksDict, dt, task)
	print(TasksDict)
elif choose == 2:
	print('View')
	print(TasksDict)
else:
    print('You select wrong action!')
