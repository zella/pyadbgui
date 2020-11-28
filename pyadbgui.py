#!/usr/bin/env python3
from adb_shell.adb_device import AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from prompt_toolkit.shortcuts import checkboxlist_dialog
from adb_shell.auth import keygen
from os.path import expanduser
import os


def adb_connect():
    key_dir = os.path.join(expanduser("~"), '.pyadb')
    if not os.path.exists(key_dir):
        os.makedirs(key_dir)
    key_path = os.path.join(key_dir, 'adbkey')
    keygen.keygen(key_path)
    adbkey = str(key_path)
    with open(adbkey) as f:
        priv = f.read()
    with open(adbkey + '.pub') as f:
        pub = f.read()
    signer = PythonRSASigner(pub, priv)
    device = AdbDeviceUsb()
    device.connect(rsa_keys=[signer], auth_timeout_s=60)
    return device


def adb_load_apps(device):
    response = device.shell('pm list packages')
    packages = list(map(lambda x: x.replace("package:", ""), response.splitlines()))
    packages.sort()
    return packages


def adb_try_remove_package(device, app):
    r = device.shell("pm uninstall " + app)
    if r.startswith('Success'):
        return True
    else:
        r = device.shell("pm uninstall -k --user 0 " + app)
        if r.startswith('Success'):
            return True
        else:
            print("Не получилось удалить " + app + r.replace("Failure", " "))
            return False


def ui_select_apps(apps):
    results = checkboxlist_dialog(
        title="Выберите приложения для удаления",
        text="",
        values=list(map(lambda x: (x, x), apps))
    ).run()
    return results


def ui_confirm_to_delete(apps):
    results = checkboxlist_dialog(
        title="Для подтверждения удаления еще раз выберете приложения",
        text="Внимание! Данные приложений будут потеряны",
        values=list(map(lambda x: (x, x), apps))
    ).run()
    return results


device = adb_connect()
apps = adb_load_apps(device)
selected_apps = ui_select_apps(apps)

if selected_apps:
    confirmed_apps = ui_confirm_to_delete(selected_apps)
    idx = 0
    ok = 0
    total = len(confirmed_apps)
    for app in confirmed_apps:
        idx = idx + 1
        print("Удаляем {} ...".format(app))
        if adb_try_remove_package(device, app):
            ok = ok + 1
            print("Успех")
        print("Обработано {} из {}".format(idx, total))
    print("Удалено {} из {} приложений".format(ok, total))
else:
    print("Bye-bye")
