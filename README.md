# pyadbgui

### Описание

Простая программа под linux для удаления приложений через adb. Не требует установленного adb.

![screen1](https://github.com/zella/pyadbgui/blob/main/screenshots/1.png)

![screen2](https://github.com/zella/pyadbgui/blob/main/screenshots/2.png)

### Как пользоваться

1. Включите режим разработчика и отладку по usb на android устройстве
2. Подключите устройство по шнуру и выберите "передачу файлов"
3. Запустите программу и следуйте инструкциям


### Как собрать из исходников

```
cd ../pyadbgui
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
pyinstaller --onefile pyadbgui.py
```


### TODO
* Сборка для windows. (проблемы с libusb, ругается антивирус)
