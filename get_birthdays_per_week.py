from collections import defaultdict
from datetime import datetime, timedelta


def birthday_date(users_birthday: datetime):
    return users_birthday.replace(year=datetime.now().year)


def get_report_date():
    '''Find nearest Monday'''
    date = (datetime.now())
    while date.weekday() != 0:
        date += timedelta(days=1)
    return date

#main func
def get_birthdays_per_week(users) -> dict:
    result_dict = defaultdict(list)
    report_date = get_report_date()
    for user in users:
        if timedelta(days=-3) < (birthday_date(user['birthday']) - report_date) < timedelta(days=4):
            weekday = birthday_date(user['birthday']).strftime('%A')
            if weekday in ('Saturday', 'Sunday'):
                weekday = "Monday"
            result_dict[weekday].append(user['name'])
    return result_dict


def create_report(dict):
    report_date = get_report_date()
    introducion = f"Report was created on {report_date.strftime('%d.%m.%Y')}, because it is the nearest Monday\n"
    print(introducion + '*' * len(introducion))
    if not len(dict):
        print('For this week, noone has birthday')
    for k, v in dict.items():
        v = ', '.join(v)
        print(f'{k:<10}: {v}')

if __name__ == '__main__':
    
    users1 = [{'name':'Constantine', 'birthday':datetime(year=1995, month=1, day=22)},
         {'name':'Oleg', 'birthday':datetime(year=2000, month=1, day=22)},
         {'name':'Taisa', 'birthday':datetime(year=2005, month=1, day=24)},
         {'name':'Alex', 'birthday':datetime(year=1995, month=1, day=25)},
         {'name':'Dana', 'birthday':datetime(year=1995, month=10, day=21)}]
    users2 = []
    create_report(get_birthdays_per_week(users1))
    create_report(get_birthdays_per_week(users2))