#! python3
# Password locking program.

PASSWORDS = {
    'email': 'fgfggfgfgf',
    'blog': 'dffdfddfdsdffdfd',
    'dupa': 'fdfdkjfdjfdjfdjfd'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy password.')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied')
else:
    print('There is no account named ' + account)