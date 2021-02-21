import os
from os.path import expanduser

from adb_shell.adb_device import AdbDeviceUsb
from adb_shell.auth import keygen
from adb_shell.auth.sign_pythonrsa import PythonRSASigner


class Adb:

    @staticmethod
    def connect() -> AdbDeviceUsb:
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

    @staticmethod
    def load_apps(device) -> list:
        response = device.shell('pm list packages')
        packages = list(map(lambda x: x.replace("package:", ""), response.splitlines()))
        packages.sort()
        return packages

    @staticmethod
    def try_remove_package(device, app) -> bool:
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

    @staticmethod
    def try_remove_packages(device, apps):
        idx = 0
        ok = 0
        total = len(apps)
        for app in apps:
            idx = idx + 1
            print("Удаляем {} из {}: {} ...".format(idx, total, app), end=" ")
            if Adb.try_remove_package(device, app):
                ok = ok + 1
                print("Успех")
            else:
                print("Неудача")
        print("Удалено {} из {} приложений".format(ok, total))
