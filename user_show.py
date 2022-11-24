import tkinter as tk
from tkinter import *
import sqlite3
def user_show():
    
    def full_row(list, r):
        c = 0
        for item in list:
            tk.Label(master = frm_label, text = item, width=15, height=1).grid(row=r, column=c)
            c += 1

    def full_data(list, r): #Заполняет текстовое поле данными из БД
        str_list = []
        for el in list: str_list.append(str(el))
        for i in range(len(str_list)):
            txt_list.insert(END, str_list[i].center(15, ' '))
        txt_list.insert(END, '\n')
    
    all_students = tk.Tk()
    all_students.title('Список студентов')
    all_students.geometry('900x600+200+100')
    all_students.rowconfigure(0, minsize=5, weight=1)
    all_students.columnconfigure(0, minsize=5, weight=1)
    title = ['id', 'Фамилия', 'Имя', 'Класс','Родители','Телефон']
    frm_label = tk.Frame(master=all_students, relief=tk.FLAT)
    frm_label.pack()
    full_row(title, 0)
    txt_list = tk.Text(master=all_students, width=90, height=40)
    txt_list.pack(pady=5)
    scroll = Scrollbar(command=txt_list.yview)
    scroll.pack(side=LEFT, fill=Y)
 
    txt_list.config(yscrollcommand=scroll.set)
                                                # Обращется к БД за данными
    try:
        sqlite_connection = sqlite3.connect('students_table.db')
        cursor = sqlite_connection.cursor()
        split_select_query = """SELECT * from students_table"""   #Сам запрос к БД
        cursor.execute(split_select_query)
        records = cursor.fetchall()
        r = 1
        for row in records:
            full_data(row, r)
            r +=1
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    all_students.mainloop()
