#!/usr/bin/python3

import glob, json
from os import path
from pandas import DataFrame
from openpyxl import load_workbook

packages = './package_list.txt'
src = './tmp/*.json'
excel_file = 'results.xlsx'

raw_list = open(packages, 'r').readlines()                                 # читаем файл с перечнем ПО
soft_list = [line.rstrip('\n') for line in raw_list]                       # создаем список из перечня ПО


DataFrame({'Name': [], 'Packages': []}).to_excel(excel_file, index=False)  # создаем файл excel

wb = load_workbook(excel_file)                                             # загружаем книгу excel
ws = wb.active                                                             # активируем лист excel

files = glob.glob(src)                                                     # находим все файлы json


for file in files:

    name = path.basename(file).split('.')[0]                               # извлекаем имя файла (оно же имя сервера)

    with open(file, 'r') as jf:
        data = json.load(jf)                                               # выгружаем данные json в словарь

    pack = [f"{data[key][0]['name']} {data[key][0]['version']}" for key in data if key in soft_list]  # генерируем список пакетов из словаря

    ws.append([name, str(pack)])                                           # добавляем строку данных в excel

wb.save(excel_file)                                                        # сохраняем данные в excel
