#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from Admin.Sources import user_json

win = tk.Tk()
win.title('管理员录入系统')
account_lb = ttk.Label(win, text='用户名')
account_txt = tk.Entry(win, width=20)
password_lb = ttk.Label(win, text='密码')
password_txt = tk.Entry(win, width=20)


def go():
    if account_txt.get() == "":
        tkinter.messagebox.showwarning('警告', '用户名不能为空')
    elif password_txt.get() == "":
        tkinter.messagebox.showwarning('警告', '密码不能为空')
    else:
        user_json.add_account(account_txt.get(), password_txt.get())
        tkinter.messagebox.showinfo('提示', '用户录入成功\n用户名:%s\n密码:%s' % (account_txt.get(), password_txt.get()))
        win.destroy()


def delete_item():
    _account = user_json.accounts()
    for i in range(len(_account)):
        if _account[i] == cmb_list.get():
            user_json.del_account(i)
            tkinter.messagebox.showinfo('提示', '成功删除\n用户名:%s' % (cmb_list.get()))
            win.destroy()


ok_button = ttk.Button(win, text='OK', command=go)
cmb_list = ttk.Combobox(win)
cmb_list['value'] = user_json.accounts()
del_button = ttk.Button(win, text='Delete', command=delete_item)

account_lb.pack()
account_txt.pack()
password_lb.pack()
password_txt.pack()
ok_button.pack()
cmb_list.pack()
del_button.pack()
win.mainloop()
