# pyadbgui

### Описание

Простая программа для удаления(отключений) приложений по протоколу adb. Не требует установленного adb.

![screen1](https://github.com/zella/pyadbgui/blob/main/screenshots/1.png)

![screen2](https://github.com/zella/pyadbgui/blob/main/screenshots/2.png)

### Как пользоваться

1. Скачайте программу под вашу ос https://github.com/zella/pyadbgui/releases
2. Включите режим разработчика и отладку по usb на android устройстве
3. Подключите устройство по шнуру и выберите "передачу файлов"
4. Запустите программу и следуйте инструкциям

   **Дополнительно**
   
   Если у вас есть заготовленный список приложений для удаления, то запустите программу с ключем `-f`.  

    **Пример**
    
    `pyadbgui.exe -f /path/to/apps.txt`
    
    **apps.txt**
    ```
    com.facebook.system 
    com.facebook.appmanager
    com.facebook.services
    com.zhiliaoapp.musically.go
    com.zhiliaoapp.musically
    ```

   


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

Для запуска требуется `libusb-1.0.dll` https://github.com/libusb/libusb/releases
```
cd .\pyadbgui\
python.exe -m venv env
.\env\Scripts\activate.bat
pip3.exe install -r requirements.txt
pyinstaller.exe --onefile pyadbgui.py
```

### TODO
* Сборка для mac
