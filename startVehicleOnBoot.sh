#!/bin/bash
python3 `${$1}main.py` &
sleep 20
hciconfig hci0 up
hciconfig hci0 sspmode 1
hciconfig hci0 piscan
