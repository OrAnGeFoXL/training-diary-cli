from simple_term_menu import TerminalMenu
from datetime import datetime, date

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
calendar_colours = {
        'plan':         #blue text 
        'succes_plan':  #green bg
        'fail_plan'     #red bg
        'unplanned':    #yellow bg
        }

import calendar
from calendar import monthrange

def calendar_t():    
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024,1)

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


def print_month(weeks, colorlist):
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    header = '' 
    delimeter = ' '

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

            if day in colorlist:
                if day < 10:
                    day = ' ' + str(day)
                else:
                    day = str(day)

                week_str = week_str + delimeter + colors['red'] + day + colors['end'] + delimeter

            elif day ==0:
                week_str = week_str + ' '*4

            else:
                if day < 10:
                    day = ' ' + str(day)
                else:
                    day = str(day)
                week_str = week_str + delimeter + day +delimeter
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
a = month_str()
print_month(a, [10, 21, 1])
