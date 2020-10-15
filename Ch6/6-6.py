favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

visited_people = ['jen', 'erin', 'sarah', 'edward', 'phil', 'eric']

for name in visited_people:
    if name in favorite_language.keys():
        print("Thank you, " + name.title() + " !")
    elif name not in favorite_language.keys():
        print(name.title() + ", please take our poll!")






