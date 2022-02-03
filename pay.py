import pandas as pd


import pyfiglet

ascii_banner = pyfiglet.figlet_format("Welcome to Payroll Reports!", font="digital")
print(ascii_banner)

employee_count = 1

while employee_count <= 10:
    overtime = 0
    employee_name = input(f"\nEnter Employee {employee_count}'s Name: ")
    pay_rate = float(input("Enter Pay Rate: $"))
    hours_worked = float(input("Enter Hours: "))

    regular_pay = hours_worked * pay_rate

    if hours_worked > 40:
        overtime = (hours_worked-40) * (1.5*pay_rate)
        gross_pay = regular_pay + overtime
    else:
        gross_pay = regular_pay

    fed_tax = gross_pay * 0.1
    state_tax = gross_pay * 0.06
    fica = gross_pay * 0.03
    net_pay = gross_pay - (fed_tax + state_tax + fica)

    df = pd.DataFrame.from_dict({"Employee Name": [employee_name], "Hours Worked": [hours_worked], "Pay Rate": [pay_rate], "Regular Pay": [regular_pay], "OT Pay": [overtime], "Gross Pay": [gross_pay], "Fed Tax": [fed_tax], "State Tax": [state_tax], "FICA": [fica], "Net Pay": [net_pay]})

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)

    employee_count += 1
