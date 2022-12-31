from db import selects, update_data

class Helper:
    def __init__(self):
        
        self.cmd_list = {
            'exit': {'func': self.func_exit, 'params': []},
            'help': {'func':self.print_help, 'params': []},
            '1': {'func': selects.select_1, 'params': []},
            '2': {'func': selects.select_2, 'params': ['id subject: ']},
            '3': {'func': selects.select_3, 'params': ['id subject: ']},
            '4': {'func': selects.select_4, 'params': []},
            '5': {'func': selects.select_5, 'params': ['id teacher: ']},
            '6': {'func': selects.select_6, 'params': ['id group: ']},
            '7': {'func': selects.select_7, 'params': ['id group: ', 'id subject: ']},
            '8': {'func': selects.select_8, 'params': ['id teacher: ']},
            '9': {'func': selects.select_9, 'params': ['id student: ']},
            '10': {'func': selects.select_10, 'params': ['id student: ', 'id teacher: ']},
            '11': {'func': selects.select_11, 'params': ['id student: ', 'id teacher: ']},
            '12': {'func': selects.select_12, 'params': ['id group: ', 'id subject: ']},
            'i-teacher': {'func': update_data.insert_teacher, 'params': ['Name teacher: ']},
            'U-teacher': {'func': update_data.update_teacher, 'params': ['id teacher: ', 'New name teacher: ']}
        }

    def func_exit(self):
        print('Goodby')
        quit()

    def print_help(self):
        print(' 1) 5 студентів з найбільшим середнім балом з усіх предметів')
        print(' 2) Студенти з найвищим середнім балом з певного предмету')
        print(' 3) Середній бал у групах з певного предмету')
        print(' 4) Середній бал на потоці (по всіх)')
        print(' 5) Курси певного викладача ')
        print(' 6) Список студентів певної групи ')
        print(' 7) Оцінки студентів у окремій группі з певного предмету ')
        print(' 8) Середній бал, який ставив певний викладач зі своїх предметів ')
        print(' 9) Список курсів, які відвідував студент (параметри: id студента)')
        print(' 10) Список курсів, які певний викладач читає певному студенту ')
        print(' 11) Середній бал, який певний викладач ставить певному студенту ')
        print(' 12) Оцінки студентів у певній групі з певного предмету на останньому занятті ')
        print(' i-teacher (u-teacher, d-teacher) - Додати (Змінити, Видалити) викладача ')
        print(' i-group (u-group, d-group) - Додати (Змінити, Видалити) групу ')
        print(' i-student (u-student, d-student) - Додати (Змінити, Видалити) студента ')
        print(' i-subject (u-subject, d-subject) - Додати (Змінити, Видалити) предмет ')
        print('i-grade (u-grade, d-grade) - Додати (Змінити, Видалити) оцінку ')
        print('help - Список команд')
        print(' exit - Вихід')

    def cmd(self, cmd):
        if cmd not in self.cmd_list:
            print('Wrong command.')
            return
        args = []
        for el in self.cmd_list[cmd]['params']: 
            while True:
                param = input(el)
                if param:
                    args.append(param)
                    break
        self.cmd_list[cmd]['func'](*args)
