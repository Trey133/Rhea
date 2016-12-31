#!/usr/bin/python

import os

while True:
    os.system("curl wttr.in/42220")
    os.system('awk -F= "/^(psk|id)/{print $2}" /etc/NetworkManager/system-connections/"$(iwgetid -r)" ')
    os.system("date --rfc-3339=ns")
