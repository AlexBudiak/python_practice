def salary():
    n = []
    emp_num = int(input('Number of employees: '))
    for i_emp in range(emp_num):
        n.append(int(input(f'Salary of {i_emp + 1} employee: ')))
    for i_list in n:
        if i_list == 0:
            n.remove(i_list)

    print(f'Employees left {len(n)}')
    print(f'Salaries: {n}')

salary()