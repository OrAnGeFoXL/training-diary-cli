from simple_term_menu import TerminalMenu
from datetime import datetime, date
import csv
ex_list = [
        "Отжимания",
        "Приседания",
        "Подтягивание"
        ]

colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'end': '\033[0m'
    }

#https://habr.com/ru/companies/macloud/articles/558316/ 
calendar_colours = {
        'plan': '\033[0;34m' ,         #blue text 
        'success_plan': '\033[0;30;42m' , #green bg
        'fail_plan': '\033[0;30;41m',     #red bg
        'unplanned': '\033[0;30;43m'      #yellow bg
        }

train_data_sample = {
        'plan': [15, 25] ,      
        'success_plan': [5, 10] ,
        'fail_plan': [1, 3],    
        'unplanned': [6, 7]      
        }

import calendar
from calendar import monthrange

def get_train_days():

    with open('user_data/main_diary.csv', 'r') as f:
        data = csv.DictReader(f)
        
        train_days = [int(row['DATE'][:2]) for row in data]
        print(train_days) 
        
    return train_days    


def calendar_t():    
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024,1)

def day_formater(day, colour):

    if day < 10:
        day = ' ' + str(day)
    else:
        day = str(day)

    if colour == 'default':
        f_day = day
    else:
        f_day = calendar_colours[colour]+day+colors['end']

    return f_day

def month_str(year=2024,month=8):

    date = datetime.now()

    weekday = date.weekday()
    day = date.today().day
    print(day)
    days = monthrange(year, month)[1]

    space_day_num = weekday -day%7 + 1
    space_list = [0]*space_day_num
    print(space_list)

    print(f'Пустые дни: {space_day_num}')

    print(weekday)
    
    days_list = list(range(1, days+1))

    print(days_list)
    
    calendar_list = space_list + days_list
    print(calendar_list)

    weeks = [calendar_list[i:i+7] for i in range(0, len(calendar_list),7)]
    
    last_week = weeks[-1]
    while len(last_week) < 7:
        last_week.append(0)

    return weeks


def print_month(weeks, train_data):
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    header = '' 
    delimeter = ' ' #пробел

    for day in days:
        header =header + delimeter + day + delimeter

    name = calendar.month_name[date.today().month]
    b = ' '*(round(len(header)/2))
    print(b + name + b)
    print(header)
    print('='*len(header))

    for week in weeks:
        week_str = ''
        for day in week:

            if day in train_data['plan']:
                day = day_formater(day, 'plan')

            elif day in train_data['unplanned']:
                day = day_formater(day, 'unplanned')

            elif day in train_data['fail_plan']:
                day = day_formater(day, 'fail_plan')

            elif day in train_data['success_plan']:
                day = day_formater(day, 'success_plan')

            elif day ==0:
                day = '  ' #двойной пробел

            else:
                day = day_formater(day,'default')
            week_str = week_str + delimeter + day + delimeter
        print(week_str)



def train_menu():
    
    term_menu = TerminalMenu(ex_list).show()

def main_menu():
    list = ["Начать тренировку",
            "Дневник тренировок",
            "Программы тренировок",
            "Достижения",
            "Help"
            ]
    term_menu = TerminalMenu(list)
    
    match term_menu.show():
        case 0:
            train_menu()
        case 1:
            print(list[1])
        case 2:
            print('Программы тренировок')
        case 3:
            print("Ваши достижения")
        case 4:
            print('Вывод справки')

    return

#calendar_t()
#main_menu()
get_train_days()
a = month_str()
print_month(a, train_data_sample)
