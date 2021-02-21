#!/usr/bin/env python3

import sys
import time
from argparse import ArgumentParser

from adb import *
from ui import *

# TODO help
print('Убедитесь, что отладка по usb включена.')
time.sleep(2)
print('Подтверите подключение на устройстве ...')
device = Adb.connect()
apps = Adb.load_apps(device)

parser = ArgumentParser()
parser.add_argument("-f", dest="file",
                    help="remove packages listed in file")
args = parser.parse_args()
if args.file:
    file = args.file
    if (os.path.isdir(file)):
        print('Не правильный путь к файлу')
        sys.exit(0)
    with open(file) as f:
        lines = f.read().splitlines()
        file_apps = map(str.strip, lines)
        exist_apps = list(set(apps) & set(file_apps))
        if (exist_apps):
            confirmed_apps = Ui.confirm_to_delete(exist_apps, pre_selected=True)
            if confirmed_apps:
                Adb.try_remove_packages(device, confirmed_apps)
        else:
            print("Ничего из списка не найдено")
else:
    selected_apps = Ui.select_apps(apps)
    if selected_apps:
        confirmed_apps = Ui.confirm_to_delete(selected_apps)
        if (confirmed_apps):
            Adb.try_remove_packages(device, confirmed_apps)
    else:
        print("Ничего не выбрано")

input("Нажмите Ввод для выхода...")
