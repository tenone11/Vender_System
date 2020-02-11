#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json

open_user_json = open('./Admin/Sources/user.json', 'r+', encoding='utf-8')
user_json_data = open_user_json.read()
user_json_data = json.loads(user_json_data)

open_data_json = open('./Main/Sources/data.json', 'r+', encoding='utf-8')
data_json = open_data_json.read()
data_json = json.loads(data_json)


def accounts():
    return user_json_data['User']


def passwords():
    return user_json_data['Password']


def show_admin():
    data = ''
    for i in range(len(user_json_data['User'])):
        data += '用户名：%s\n密码：%s\n' % (user_json_data['User'][i], user_json_data['Password'][i])
    return data


def add_account(account, password):
    user_json_data['User'].append(account)
    user_json_data['Password'].append(password)
    new = json.dumps(user_json_data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open('./Admin/Sources/user.json', 'w', encoding='utf-8') as f:
        f.write(new)
    return user_json_data


def del_account(val):
    del user_json_data['User'][val]
    del user_json_data['Password'][val]
    new = json.dumps(user_json_data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open('./Admin/Sources/user.json', 'w', encoding='utf-8') as f:
        f.write(new)
    return user_json_data

def gametype():
    return data_json['Game_Type']

def area():
    return data_json['Area']

def add_item(item_name, name):
    data_json[item_name].append(name)
    new = json.dumps(data_json, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open('./Main/Sources/data.json', 'w', encoding='utf-8') as f:
        f.write(new)
    return data_json


def del_item(item_name, val):
    del data_json[item_name][val]
    new = json.dumps(data_json, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open('./Main/Sources/data.json', 'w', encoding='utf-8') as f:
        f.write(new)
    return data_json
