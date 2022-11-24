import tkinter as tk
import sqlite3
import user_show as us
def user_add():

    def full_row(list, r):
        c = 0
        for item in list:
            tk.Label(master = frm_label, text = item, width=12, height=1).grid(row=r, column=c)
            c += 1
                                #Находит последний индекс в БД
    def get_id():
        try:
            sqlite_connection = sqlite3.connect('students_table.db')
            cursor = sqlite_connection.cursor()
            split_select_query = """SELECT id from students_table"""
            cursor.execute(split_select_query)
            records = cursor.fetchall()
            id = records[len(records)-1][0]
            cursor.close()
            return id + 1 
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                                                #Запрос на добавление данных в БД
    def sqlite_insert_data(list):               
        try:
            sqlite_connection = sqlite3.connect('students_table.db')
            cursor = sqlite_connection.cursor()
            sqlite_insert_query = """INSERT INTO students_table
                                 (id, surename, name, class, parents, phone)
                                 VALUES (?, ?, ?, ?, ?, ?);"""
            cursor.execute(sqlite_insert_query, list)
            sqlite_connection.commit()
            tk.Label(master=add_students, text='Данные внесены').pack()
            
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                        #Закрывает окно
    def exit():
        add_students.destroy()
        us.user_show()
                                #Добавляет данные об ученике
    def add_student():
        list_data = []
        list_data.append(get_id())

        list_data.append(ent_surname.get())
        list_data.append(ent_name.get())
        list_data.append(int(ent_class.get()))
        list_data.append(ent_parents.get())
        list_data.append(ent_phone.get())

        sqlite_insert_data(list_data)
        tk.Button(master=add_students, text='Закрыть', command= exit).pack()
                                            #Создается окно и поля для ввода данных
    add_students = tk.Tk()
    add_students.title('Добавить студента')
    add_students.geometry('600x400+200+100')
    add_students.rowconfigure(0, minsize=5, weight=1)
    add_students.columnconfigure(0, minsize=5, weight=1)

    title = ['id', 'Фамилия', 'Имя', 'Класс','Родители','Телефон']
    frm_label = tk.Frame(master=add_students, relief=tk.FLAT)
    frm_label.pack(padx=1, pady=15)
    full_row(title, 0)

    frm_entry = tk.Frame(master=add_students, width=12, relief=tk.SUNKEN)
    frm_entry.pack(padx=1, pady=10)

    lbl_id = tk.Label(master=frm_entry, width=12, text=get_id())
    lbl_id.grid(row=1, column=0)

    ent_surname = tk.Entry(master=frm_entry, width=12)
    ent_surname.grid(row=1, column=1)

    ent_name = tk.Entry(master=frm_entry, width=12)
    ent_name.grid(row=1, column=2)

    ent_class = tk.Entry(master=frm_entry, width=12)
    ent_class.grid(row=1, column=3)

    ent_parents = tk.Entry(master=frm_entry, width=12)
    ent_parents.grid(row=1, column=4)

    ent_phone = tk.Entry(master=frm_entry, width=12)
    ent_phone.grid(row=1, column=5)

    frm_button = tk.Frame(master=add_students, width=12, relief=tk.SUNKEN)
    frm_button.pack(padx=1, pady=5)

    btn_add = tk.Button(master=frm_button, width=12, text='Добавить', command=add_student)
    btn_add.pack()

    add_students.mainloop()