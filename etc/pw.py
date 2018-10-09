#! python3
# pw.py - Программа для незащищенного хранения паролей

PASSWORDS = {'email' : 'F7minl',
             'blog': 'VmAlvQ',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Использование : pyhton pw.py [имя учетной записи] - копирование пароля учетной записи')
    sys.exit()

account = sys.argv[1]   # Имя учетной записи
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + account + ' скопирован в буфер обмена.')
else:
    print('Учетная запись ' + account + ' отсутсвует в списке.')