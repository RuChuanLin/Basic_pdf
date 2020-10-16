# 6.3===================================================================
# ----------------------------------------------------------------------
""""""
# 6.3.1=================================================================
# ----------------------------------------------------------------------
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
# ----------------------------------------------------------------------
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items(): # for迴圈銜接字典的方式，
    # user_0.items()會回傳一個 key:value的list
    print("\nKey: " + key)
    print("Value " + value)
# ----------------------------------------------------------------------
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
# 6.3.2=================================================================
# ----------------------------------------------------------------------
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favorite_language.keys(): # 不需要value只需要key的時候可以用
    # 擷取favorite_language之中的所有key，然後按照順序賦值給name
    print(name.title())
# ----------------------------------------------------------------------
# ★可能要多看幾次下面的if了
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends: # 檢查name是否在list裡面
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_language[name].title() + "!") # [name] == ['key']
# ----------------------------------------------------------------------
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'erin' not in favorite_language.keys(): # keys()會回傳一個list
    print("Erin, please take our poll!")


# 6.3.3=================================================================
# ----------------------------------------------------------------------
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_language.keys()): # ★指定字典中key的順序，
    # 使其按照ABCDE排列
    print(name.title() + ", thank you for taking the poll.")


# 6.3.4=================================================================
# ----------------------------------------------------------------------
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:") # values()也會回傳一個list
for language in favorite_language.values():
    print(language.title())
# 在這裡會發現Python重複了！
# ----------------------------------------------------------------------
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_language.values()): # ★用集合(set)剔除重複項
    # set類似list，但是每個元素必須獨一無二
    # 運用set來找出list裡面獨一無二的元素
    print(language.title())















































