first_name = "John"
last_name = "Doe"
full_name = first_name + ' ' + last_name  #String concatenation
address = "123 Main Street"
address += ", Appartment 4B"
age = 28
employee_info = full_name + ' is ' + str(age) + " years old"   #Changed age type to string

position = "Data Analyst"
salary = 75000
employee_card = f'Name: {full_name} | Age: {age} | Position: {position} | Salary: ${salary}'  #used f-string
print(employee_card)

employee_code = "DEV-2026-JD-001"
department = employee_code[0:3]  #Slicing
print(department)
year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)
last_three = employee_code[-3:]  #Negative indexing
print(last_three)
