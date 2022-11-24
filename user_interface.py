import tkinter as tk
import user_show as us
import user_add as ua
import user_find as uf

def user_interface():
    def choice(x):
        if x == 'Список': us.user_show()
        if x == 'Найти': uf.user_find()
        if x == 'Добавить': ua.user_add()
        
    students = tk.Tk()
    students.title('Работа со студентами')
    students.geometry('600x400+200+100')
    students.rowconfigure(0, minsize=5, weight=1)
    students.columnconfigure(0, minsize=100, weight=1)
    lbl_text = tk.Label(master = students, text='Выберете действие', height=5)
    lbl_text.pack()
    frm_button = tk.Frame(master = students, relief=tk.RAISED, border=10, )
    frm_button.pack()
    btn_list = ['Список', 'Найти', 'Добавить']
    r = 3
    for i in btn_list:
        cmd = lambda x = i: choice(x)
        tk.Button(master = frm_button, text = i, command=cmd, width=30, height=2).grid(row=r, column=0)
        r +=1
    students.mainloop() 
user_interface()
