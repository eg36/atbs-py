#! python3
# Add bullets to text.

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes
    lines[i] = '* ' + lines[i] # add * to each string in lines.
text = '\n'.join(lines)

pyperclip.copy(text)