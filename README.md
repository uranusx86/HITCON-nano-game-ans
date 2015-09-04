# HITCON-nano-game-ans
this repo is for HITCON 2015 nano game's answer<br/>
the Arduino nano's specification is
* MCU: ATmega328
* Digital I/O Pins: 14 (of which 6 provide PWM output)
* Analog InputPins: 8
* Flash: 32 KB,use 2 KB for bootloader
* SRAM: 2 KB
* EEPROM: 1 KB
* Clock Speed: 16 MHz
* USB To Serial: CH340G chip

## How to install Arduino nano
1. For Ubuntu <br/>
    ```
    driver & python is ready, nothing to do
    ```
2. For MAC <br/>
    ```
    Install Driver http://kiguino.moos.io/downloads/CH341SER_MAC.ZIP

    Install AVR Toolchain https://www.obdev.at/products/crosspack/download.html

    Install Arduino IDE https://www.arduino.cc/download_handler.php

    Install Python serial libary https://pypi.python.org/pypi/pyserial
        tar xfvz pyserial-?.?.tar.gz
        cd pyserial-?.?
        sudo python setup.py install
    ```

3. For Windows <br/>
    ```
    Install Driver http://www.wch.cn/download/CH341SER_EXE.html

    Install AVR Toolchain http://www.atmel.com/tools/ATMELAVRTOOLCHAINFORWINDOWS.aspx

    Install Arduino IDE https://www.arduino.cc/download_handler.php

    Install Python2.7.X https://www.python.org/downloads/

    Install Python serial libary https://pypi.python.org/pypi/pyserial
        uncompress pyserial-?.?.tar.gz to Python27/Lib/site-packages/
        cd pyserial-?.?
        python setup.py install
    ```

## Ubuntu Arduino nano install trouble fix
    https://hitcon.hackpad.com/IoT-nano--Fx9aehf98Y9

## Play HITCON nano game

question code is already inside, just use **ans.py** to write your answer or copy **/question-X/ans.py** to **/ans.py**, and run it to communicate with Arduino nano, if you are correct, it will give you a key