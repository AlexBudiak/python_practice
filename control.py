employee_id_list = []
employee_num = int(input('Input number of employees on work: '))
for _ in range(employee_num):
    employee_id = int(input('Input employee ID: '))
    employee_id_list.append(employee_id)

find_employee_id = int(input('Input ID to find in list: '))

flag = 0
for id in employee_id_list:
    if find_employee_id == id:
        flag += 1
    else:
        flag += 0
if flag > 0:
    print('Employee on work')
else:
    print('Employee not on work')