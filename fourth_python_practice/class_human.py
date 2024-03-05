from defs import *

class Human:
    def __init__(self):
        self.database_manager = DataManager('accounting.db')


    def select_table(self):
        print("Для выхода напишите \"False\" после выбора таблицы")
        input()
        #keyboard.hook(on_escape_pressed)
        while True:
            selected_table = chooce_table(self.database_manager)

            if selected_table == False:
                print("Неправильный вывод данных")
                input()
                continue
            self.database_manager.print_table(selected_table)

            chek = input()
            if chek == "False":
                break

    def run_actions(self):
        pass