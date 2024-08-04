import os


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



def main():
    print_row('12.01.23', 30, 10)
    print_row('13.01.23', 20, 40)


#if __name__ ==__main__:
main()
