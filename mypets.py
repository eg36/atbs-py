myPets = ['maru', 'ryju', 'kiju']
print('Enter pet name: ')
name = input()
if name not in myPets:
    print(name + ' is not my pet name :( ')
else:
    print(name + ' is my pet name')