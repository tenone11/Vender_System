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
gametype_lb = ttk.Label(win, text='游戏类型')
gametype_txt = tk.Entry(win, width=20)
area_lb = ttk.Label(win, text='供应商地区')
area_txt = tk.Entry(win, width=20)
sv = ttk.Label(win, text='---------------------------------')
sv2 = ttk.Label(win, text='---------------------------------')


def add_admin():
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


def show_user_info():
    tk.messagebox.showinfo('用户信息', user_json.show_admin())


def add_gametype():
    if gametype_txt.get() == "":
        tkinter.messagebox.showwarning('警告', '用户名不能为空')
    else:
        user_json.add_item('Game_Type', gametype_txt.get())
        tkinter.messagebox.showinfo('提示', '添加游戏类型成功\n%s' % (gametype_txt.get()))
        win.destroy()


def del_one_gametype():
    _account = user_json.gametype()
    for i in range(len(_account)):
        if _account[i] == cmb_gametype_list.get():
            user_json.del_item('Game_Type', i)
            tkinter.messagebox.showinfo('提示', '成功删除类型\n%s' % (cmb_gametype_list.get()))
            win.destroy()


def add_area():
    if area_txt.get() == "":
        tkinter.messagebox.showwarning('警告', '地区不能为空')
    else:
        user_json.add_item('Area', area_txt.get())
        tkinter.messagebox.showinfo('提示', '地区添加成功\n%s' % (area_txt.get()))
        win.destroy()


def del_one_area():
    _account = user_json.area()
    for i in range(len(_account)):
        if _account[i] == cmb_area_list.get():
            user_json.del_item('Area', i)
            tkinter.messagebox.showinfo('提示', '成功删除地区\n%s' % (cmb_area_list.get()))
            win.destroy()


ok_button = ttk.Button(win, text='OK', command=add_admin)
cmb_list = ttk.Combobox(win)
cmb_list['value'] = user_json.accounts()
del_button = ttk.Button(win, text='Delete', command=delete_item)
info_button = ttk.Button(win, text='详细信息', command=show_user_info)
add_gametype_button = ttk.Button(win, text='增加', command=add_gametype)
cmb_gametype_list = ttk.Combobox(win)
cmb_gametype_list['value'] = user_json.gametype()
del_gametype_button = ttk.Button(win, text='删除此类型', command=del_one_gametype)
add_area_button = ttk.Button(win, text='增加', command=add_area)
cmb_area_list = ttk.Combobox(win)
cmb_area_list['value'] = user_json.area()
del_area_button = ttk.Button(win, text='删除此地区', command=del_one_area)

account_lb.pack()
account_txt.pack()
password_lb.pack()
password_txt.pack()
ok_button.pack()
cmb_list.pack()
del_button.pack()
info_button.pack()
sv.pack()
gametype_lb.pack()
gametype_txt.pack()
add_gametype_button.pack()
cmb_gametype_list.pack()
del_gametype_button.pack()
sv2.pack()
area_lb.pack()
area_txt.pack()
add_area_button.pack()
cmb_area_list.pack()
del_area_button.pack()
win.mainloop()
