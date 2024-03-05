from class_human import *


class Admin(Human):
    def update_data(self):
        selected_table = chooce_table(self.database_manager, "Вы можете обновить данные в следующих таблицах: ")
        command("cls")

        self.database_manager.print_table(selected_table)
        columns = self.database_manager.select_columns(selected_table)
        coast_id_column = input_validation(request_text="Выберите строчку которую хотите изменить:\n")
        id_column = f"{columns[0]} = {coast_id_column}"
        columns.pop(0)
        command("cls")

        print("Выберите столбец который хотите обновить:")
        type_data(columns)
        selected_columns = choose_columns(columns)
        command("cls")

        values = choose_values(selected_columns)

        self.database_manager.update_table(selected_table, selected_columns, values, id_column)
        command("cls")


    def insert_data(self):
        selected_table = chooce_table(self.database_manager, "Вы можете внести данные в следующие таблицы: ")
        command("cls")
        if selected_table == False:
            print("Неправильный вывод данных")
            input()
            return

        print("Вы должны заполнить следующие столбцы: ")
        columns = self.database_manager.select_columns(selected_table)
        columns.pop(0)
        type_data(columns)
        command("cls")

        values = choose_values(columns)

        self.database_manager.insert_data(selected_table, columns, values)
        command("cls")


    def delete_data(self):
        selected_table = chooce_table(self.database_manager, "Вы можете удалять данные в следующих таблицах: ")
        command("cls")

        self.database_manager.print_table(selected_table)
        columns = self.database_manager.select_columns(selected_table)
        coast_id_column = input_validation(request_text="Выберите строчку которую хотите изменить:\n")
        id_column = f"{columns[0]} = {coast_id_column}"
        columns.pop(0)
        command("cls")

        self.database_manager.delete_data(selected_table, id_column)
        command("cls")


    def run_actions(self) -> int:
        try:
            while True:
                command("cls")
                actions = input_validation(request_text="""Вам доступны слудеющие действия:
1. Вывести данные в бухгалтерии
2. Добавить данные в бухгалетрию
3. Обновить данные из бухгалтерии
4. Удалить данные в бухгалтерии
5. Выход
""")
                command("cls")

                match actions:
                    case 1:
                        self.select_table()
                    case 2:
                        self.insert_data()
                    case 3:
                        self.update_data()
                    case 4:
                        self.delete_data()
                    case 5:
                        print("Пока пока)")
                        return 15
        finally:
            self.database_manager.close_connection()