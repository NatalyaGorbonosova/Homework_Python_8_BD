import tkinter as tk
import sqlite3
import user_show as us
def user_delete():
    def show_change():
        delete_students.destroy()
        us.user_show()

    def get_id():
        id = ent_entry_id.get()
        delete_student(id)
        tk.Button(master=delete_students, width=20, text='Показать изменения', command=show_change).pack(pady=5)

    def delete_student(id):
        try:
            sqlite_connection = sqlite3.connect('students_table.db')
            cursor = sqlite_connection.cursor()
            cursor.execute("DELETE from students_table   WHERE id = '"+  id +"'")
            sqlite_connection.commit()
            tk.Label(master=delete_students, text='Данные удалены').pack()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    delete_students = tk.Tk()
    delete_students.title('Удалить данные')
    delete_students.geometry('600x200+100+20')
    delete_students.rowconfigure(0, minsize=5, weight=1)
    delete_students.columnconfigure(0, minsize=5, weight=1)
    frm_button = tk.Frame(master=delete_students, width=15, relief=tk.SUNKEN)
    frm_button.pack()
    tk.Label(master=delete_students, text='Введите индекс студента, которго надо удалить').pack()
    ent_entry_id = tk.Entry(master=delete_students, width=10)
    ent_entry_id.pack(pady=5)
    btn_get_id = tk.Button(master=delete_students, width=10, text='Удалить', command=get_id)
    btn_get_id.pack(pady=5)
    delete_students.mainloop()

