#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json

open_json = open('./Admin/Sources/user.json', 'r+', encoding='utf-8')
json_data = open_json.read()
json_data = json.loads(json_data)

def accounts():
    return json_data['User']

def passwords():
    return json_data['Password']

def add_account(account,password):
    json_data['User'].append(account)
    json_data['Password'].append(password)
    new=json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open('./Admin/Sources/user.json', 'w', encoding='utf-8') as f:
        f.write(new)
    return json_data

def del_account(val):
    del json_data['User'][val]
    del json_data['Password'][val]
    new=json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open('./Admin/Sources/user.json', 'w', encoding='utf-8') as f:
        f.write(new)
    return json_data
