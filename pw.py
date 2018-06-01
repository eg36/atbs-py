#! python3
# Password locking program.

PASSWORDS = {
    'email': 'fgfggfgfgf',
    'blog': 'dffdfddfdsdffdfd',
    'dupa': 'fdfdkjfdjfdjfdjfd'
}

import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy password.')
    sys.exit()
