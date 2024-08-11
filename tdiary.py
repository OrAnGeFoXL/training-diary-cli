import os
import csv
from simple_term_menu import TerminalMenu
from datetime import datetime, timedelta


t_width, _ = os.get_terminal_size()

print(t_width)
print(type(t_width))


train_data = [
        ['07.08.24', 1, 23, 28, 21],
        ['09.08.24', 2, 25, 24, 18]
        ]

SHOW_DATE = True
FTICK = '█'
PTICK = '▒'

#Список цветов для CLI
c = ['\033[0m','\033[94m', '\033[92m', '\033[93m', '\033[91m', '\033[95m', '\033[96m', '\033[97m']

def print_row(date, fact, plan):

    if SHOW_DATE:
        date_ln = len(date)
    else:
        date_ln = 0

    f_color = c[4]
    
    label_ln = len(str(plan)) + len(str(fact)) + 4

    bar_ln = t_width - date_ln - label_ln

    if plan > fact:
        p_color = c[3]
     
        delta = plan - fact
        summ = plan + delta
        coef = delta/plan

        fact_ticks = round(coef*bar_ln)
        plan_ticks = bar_ln - fact_ticks

    else:
        p_color = c[2]
        delta = fact - plan
        summ = fact + delta
        coef = delta/fact

        fact_ticks = round(coef*bar_ln)
        plan_ticks = bar_ln - fact_ticks   

    label = f'{f_color}{fact}{c[0]}/{p_color}{plan}{c[0]}'
    plan_bar = f'{p_color}{PTICK*plan_ticks}{c[0]}'
    fact_bar = f'{f_color}{FTICK*fact_ticks}{c[0]}'

    print(f"{date} {fact_bar}{plan_bar} {label}")

def print_train(data):

    if SHOW_DATE:
        date_ln = len(data[0])
    else:
        date_ln = 0


def get_ex_list():

    ex_list = os.listdir('train_plans')
    ex_list = [i[:-4] for i in ex_list if '.csv' in i ]

    return ex_list

def add_train_data():

    print('Выберите упражнение:')
    ex = get_ex_list()
    menu = TerminalMenu(ex)   
    ex_data = ex[menu.show()]

    print('Введите уровень упражнения')
    lvl = input()

    print('Введите дату')
    last_date = [(datetime.today() - timedelta(days=i)).strftime('%d.%m.%Y') for i in range(7)]
    menu = TerminalMenu(last_date)
    date = last_date[menu.show()]
    
    #TODO Добавить автоматический подсчет количества подходов
    print('Введите количество повторений в первом подходе')
    reps =input()


def print_plan(csvdata):
    pass

def read_csv(path):
    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['LEVEL']} {c[3]}{row['NAME']}{c[0]}")

            levels = [
                    "Начальный уровень: ",
                    "Средний уровень  : ",
                    "Высокий уровень  : "
                    ]
            
            clmns = [row['LOW'], row['MED'], row['HIGH']]

            for i in clmns:
                ex, rep = str(i).split('x')
                rep1 = '\x1b[41m' + rep + '\x1b[0m '
                print(f"{levels[clmns.index(i)]} {rep1*int(ex)}") 

def main_menu():
    list = ["Отжимания",
            "Подтягивания",
            "Приседания"
            ]
    term_menu = TerminalMenu(list)
    menu_index = term_menu.show()
    
    return list[menu_index]

def main():
    #print_row('12.01.23', 30, 10)
    #print_row('13.01.23', 20, 40)
    main_menu()
    #read_csv("train_plans/pushups.csv")
    #read_csv("train_plans/squads.csv")
#if __name__ ==__main__:
main()
add_train_data()
