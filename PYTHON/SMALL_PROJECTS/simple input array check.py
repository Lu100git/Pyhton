
employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

		
print('')
print('advance fucntion:')
print('')
print('')

def search_emp(input):
	if input in developers:
		print(str(input) + ' is a developer')


for x in range (0, 8):
    print(employees[x])

print("from the employee list enter an employee name")

input_variable = str(raw_input())
search_emp(input_variable)




