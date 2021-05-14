import datetime
from application import *
from application.db import *
if __name__ == '__main__':
    print(datetime.datetime.today())
    print('this is main start')
    salary.calculate_salary()
    people.get_employees()
    print('this is main end')
