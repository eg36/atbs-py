while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe! Enter the password')
    password = input()
    if password =='swordfish':
        break
print('access granted')