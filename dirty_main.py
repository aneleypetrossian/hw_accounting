import datetime

from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    current_date = datetime.date.today()
    print(f"Дата запуска (dirty): {current_date}")

    get_employees()
    calculate_salary()