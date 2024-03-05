import sqlite3
from os import system as command
from prettytable import PrettyTable


class DataManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()


    def __execute_query(self, query: str, values=None) -> None:
        try:
            if values:
                print(f"Запрос: {query}")
                print(f"Значения: {values}")
                self.cursor.execute(query, values)
                print("Запрос выполнен")
                input()
            else:
                print(f"Запрос: {query}")
                self.cursor.execute(query)
                print("Запрос выполнен")
                input()
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")


    def insert_data(self, table_name: str, columns: list, values: list) -> None:
        columns = ", ".join(_ for _ in columns)
        question_marks = ", ".join("?" for _ in values)
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({question_marks})"
        self.__execute_query(query, tuple(values))
        self.conn.commit()


    def update_table(self, table_name: str, columns: list, values: list, id: str) -> None:
        value = ", ".join([f"{elem1} = {elem2}" for elem1, elem2 in zip(columns, values)])
        query = f"UPDATE {table_name} SET {value} WHERE {id}"
        self.__execute_query(query)
        self.conn.commit()


    def _select_table(self) -> list:
        command("cls")
        tables_list = []
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = self.cursor.fetchall()
        for table in tables:
            tables_list.append(table[0])

        return tables_list


    def select_data(self, table_name: str) -> list:
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


    def print_table(self, table_name: str) -> None:
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if not result:
            print("Нет данных для отображения.")
            return

        columns = [description[0] for description in self.cursor.description]
        table = PrettyTable(columns)
        table.align = 'l'

        for row in result:
            table.add_row(row)

        print(table)


    def select_columns(self, table_name: str) -> list:
        query = f'PRAGMA table_info({table_name})'
        self.cursor.execute(query)
        columns = self.cursor.fetchall()
        columns_list = []
        for column in columns:
            columns_list.append(column[1])

        return columns_list


    def delete_data(self, table_name: str, id_column: str) -> None:
        query = f"DELETE FROM {table_name} WHERE {id_column}"
        self.__execute_query(query)
        self.conn.commit()


    def close_connection(self) -> None:
        self.conn.close()