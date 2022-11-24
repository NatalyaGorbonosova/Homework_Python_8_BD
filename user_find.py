import tkinter as tk
from tkinter import ttk
import sqlite3
import user_delete as ud
import user_upgrade as uu
def user_find():
                                    #Изменений данных ученика, связь с user_upgrade
    def user_update():
        find_students.destroy()
        uu.upgrade_user()
                                    #Удаление ученика, связь с  user_delete
    def user_delete():
        find_students.destroy()
        ud.user_delete()

    def full_row(list, r):
        frm_data = tk.Frame(master=find_students, width=12, height=2)
        frm_data.pack()
        c = 0
        for item in list:
            tk.Label(master = frm_data, text = item, width=12, height=1).grid(row=r, column=c)
            c += 1

    def full_row_data(list, r):
        
        frm_data = tk.Frame(master=find_students, width=12, height=2)
        frm_data.pack()
        c = 0
        for item in list:
            tk.Label(master = frm_data, text = item, width=12, height=1).grid(row=r, column=c)
            c += 1
                                        # Находит ученника по введенному критерию
    def find_data(name_col, data):
        title = ['id', 'Фамилия', 'Имя', 'Класс','Родители','Телефон']
        frm_label = tk.Frame(master=find_students, relief=tk.FLAT)
        frm_label.pack()
        full_row(title, 0)
        try:
            sqlite_connection = sqlite3.connect('students_table.db')
            cursor = sqlite_connection.cursor()
           
            if name_col == 'id': 
                split_select_query = """SELECT * from students_table where id = ?"""
                cursor.execute(split_select_query, (data, ))
            elif name_col == 'surename': cursor.execute("SELECT * from students_table   WHERE surename = '"+  data +"'")
            elif name_col == 'name': cursor.execute("SELECT * from students_table   WHERE name = '"+  data +"'")
            elif name_col == 'parents': cursor.execute("SELECT * from students_table   WHERE parents = '"+  data +"'")
            elif name_col == 'phone': cursor.execute("SELECT * from students_table   WHERE phone = '"+  data +"'")
            elif name_col == 'class': cursor.execute("SELECT * from students_table   WHERE class = '"+  data +"'")
            
            records = cursor.fetchall()
            r = 1
            for row in records:
                full_row_data(row, r)
                r +=1
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                                        #Получение данных об учениках, которых надо найти  
    def get_numbers():
        def get_name():
            name_what = ent_what.get()
            title = ['id', 'surename', 'name', 'class', 'parents', 'phone']
            find_data(title[index], name_what)
            
            btn_delete = tk.Button(master= find_students, width=25, text='Удалить ученика по id', relief=tk.RAISED, command=user_delete)
            btn_delete.pack(pady=5)

            btn_upgrade = tk.Button(master=find_students, width=30, text='Изменить данные ученика по id', relief=tk.RAISED, command=user_update)
            btn_upgrade.pack(pady=5)
        
        value = cmb_where.get()
        index = cmb_where.current()
        
        lbl_what = tk.Label(master=find_students, text=f'Введите {value}')
        lbl_what.pack()
        ent_what = tk.Entry(master=find_students, width=15)
        ent_what.pack()
        frm_button = tk.Frame(master=find_students, relief=tk.RAISED, border=2)
        frm_button.pack()
        btn_get_name = tk.Button(master=frm_button, text='Ввести значение', width=15, command=get_name)
        btn_get_name.pack()
                                        #Основная  часть, создание окна и его элементов      
    find_students = tk.Tk()
    find_students.title('Поиск данных')
    find_students.geometry('1000x400+100+20')
    find_students.rowconfigure(0, minsize=5, weight=1)
    find_students.columnconfigure(0, minsize=5, weight=1)
    
    lbl_where = tk.Label(master = find_students, text='Выберите критерий поиска из списка')
    lbl_where.pack()
    
    cmb_where = ttk.Combobox(
        master=find_students, 
        values=('id', 'Фамилия', 'Имя', 'Класс','Родители','Tелефон'),
        state='readonly')
    cmb_where.pack()
    
    frm_button = tk.Frame(master=find_students, relief=tk.RAISED, border=2)
    frm_button.pack()
    btn_get = tk.Button(master=frm_button, text='Выбрать', width=10, height=1, command=get_numbers)
    btn_get.pack()
  
    find_students.mainloop()