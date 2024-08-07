from simple_term_menu import TerminalMenu

ex_list = [
        "Отжимания",
        "Приседания",
        "Подтягивание"
        ]

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


main_menu()
