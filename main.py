import datetime
from application import salary
from application.db import people
if __name__ == '__main__':
    print(datetime.datetime.today())
    print('this is main start')
    salary.calculate_salary()
    people.get_employees()
    print('this is main end')
