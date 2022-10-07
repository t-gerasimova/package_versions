#!/usr/bin/python3

import glob, json
from os import path
from pandas import DataFrame
from openpyxl import load_workbook

raw_list = open('package_list.txt', 'r').readlines()                      # читаем файл с перечнем ПО
soft_list = [line.rstrip('\n') for line in raw_list]                      # создаем список из перечня ПО

DataFrame({'Name': [], 'Packages': []}).to_excel('results.xlsx', index=False)  # создаем файл excel

wb = load_workbook('results.xlsx')                                         # загружаем книгу excel
ws = wb.active                                                             # активируем лист excel

files = glob.glob('/tmp/*.json')                                           # находим все файлы json

for file in files:

    name = path.basename(file).split('.')[0]                               # извлекаем имя файла (оно же имя сервера)

    with open(file, 'r') as jf:
        data = json.load(jf)                                               # выгружаем данные json в словарь

    pack = [f"{data[key][0]['name']} {data[key][0]['version']}" for key in data if key in soft_list]  # генерируем список пакетов из словаря

    ws.append([name, str(pack)])                                           # добавляем строку данных в excel

wb.save('results.xlsx')                                                    # сохраняем данные в excel


