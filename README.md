# pyadbgui

### Описание

Простая программа под linux для удаления приложений через adb. Не требует установленного adb.

![screen1](https://github.com/zella/pyadbgui/blob/main/screenshots/1.png)

![screen2](https://github.com/zella/pyadbgui/blob/main/screenshots/2.png)

### Как пользоваться

1. Скачать исполняемый файл https://github.com/zella/pyadbgui/releases
2. Включите режим разработчика и отладку по usb на android устройстве
3. Подключите устройство по шнуру и выберите "передачу файлов"
4. Запустите программу и следуйте инструкциям


### Как собрать из исходников

**Linux**
```
cd ../pyadbgui
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
pyinstaller --onefile pyadbgui.py
```
**Windows**  

Для запуска требуется `libusb-1.0.dll`
```
TODO должно собираться стандартым методом
```

### TODO
* Сборка для mac
