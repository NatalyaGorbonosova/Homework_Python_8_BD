import tkinter as tk
import sqlite3
from tkinter import messagebox

def upgrade_user():
                        # Находит все id
    def find_id():
        try:
            sqlite_connection = sqlite3.connect('students_table.db')
            cursor = sqlite_connection.cursor()
            split_select_query = """SELECT * from students_table"""
            cursor.execute(split_select_query)
            records = cursor.fetchall()
            list_id = []
            for row in records:
                list_id.append(row[0])
            cursor.close()
            return list_id
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                                # Выводит информацию об ученике в полях ввода для редакции
    def get_info(id):
        try:
            sqlite_connection = sqlite3.connect('students_table.db')
            cursor = sqlite_connection.cursor()
            cursor.execute("SELECT * from students_table   WHERE id = '"+  id +"'")
            records = cursor.fetchall()
            list_data = []
            for i in range(len(records[0])):
                list_data.append(records[0][i])
            return list_data
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                                                                #Меняет данные в БД
    def change_db(id, surname, name, class_st, parents, phone):
        try:
            sqlite_connection = sqlite3.connect('students_table.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(
                "Update students_table set surename =  '"+  surname +"', name =  '"+  name +"', class =  '"+  class_st +"', parents =  '"+  parents +"', phone =  '"+  phone +"' where id =   '"+  id +"'")
            sqlite_connection.commit()
            
            sqlite_connection.commit()
            cursor.close()
            upgrade_students.destroy()
            messagebox.showinfo("Изменение данных", "Данные изменены")
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                                        # Получает измененную информацию из полей ввода
    def get_id():
        def change(id):
            surname = ent_entry_surname.get()
            name = ent_entry_name.get()
            class_st = ent_entry_class.get()
            parents = ent_entry_parents.get()
            phone = ent_entry_phone.get()
            
            change_db(id, surname, name, class_st, parents, phone)
        
        id = ent_entry_id.get()
        list_id = find_id()
        if int(id) in list_id: print(list_id)
        else: messagebox.showerror("Ошибка", "Такого id нет")
        tk.Label(master=upgrade_students, text='Введите изменения').pack(pady=5)
        list_info = get_info(id)
        frm_data = tk.Frame(master=upgrade_students, width=12)
        frm_data.pack(pady=5)
        tk.Label(master=frm_data, text=list_info[0]).grid(row=0, column=0)

        ent_entry_surname = tk.Entry(master=frm_data, width=15)
        ent_entry_surname.insert(0, list_info[1])
        ent_entry_surname.grid(row=0, column=1)

        ent_entry_name = tk.Entry(master=frm_data, width=15)
        ent_entry_name.insert(0, list_info[2])
        ent_entry_name.grid(row=0, column=2)

        ent_entry_class = tk.Entry(master=frm_data, width=15)
        ent_entry_class.insert(0, list_info[3])
        ent_entry_class.grid(row=0, column=3)

        ent_entry_parents = tk.Entry(master=frm_data, width=15)
        ent_entry_parents.insert(0, list_info[4])
        ent_entry_parents.grid(row=0, column=4)

        ent_entry_phone = tk.Entry(master=frm_data, width=15)
        ent_entry_phone.insert(0, list_info[5])
        ent_entry_phone.grid(row=0, column=5)

        cmd = lambda x = id: change(x)

        btn_get_change = tk.Button(master=upgrade_students, width=20, text= 'Внести изменения', command=cmd)
        btn_get_change.pack(pady=5)
                                    #Создание окна и поля ввода для id
    upgrade_students = tk.Tk()
    upgrade_students.geometry('600x400+200+100')
    upgrade_students.rowconfigure(0, minsize=5, weight=1)
    upgrade_students.columnconfigure(0, minsize=100, weight=1)

    tk.Label(master=upgrade_students, text='Введите индекс ученика, данные которого надо обновить').pack(pady=7)
    ent_entry_id = tk.Entry(master=upgrade_students, width=5)
    ent_entry_id.pack(pady=5)
    btn_get_id = tk.Button(master=upgrade_students, text='Ввести индекс', relief=tk.RAISED, width=12, command=get_id)
    btn_get_id.pack(pady=5)

    upgrade_students.mainloop()

