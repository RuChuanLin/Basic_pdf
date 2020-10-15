# 6.4===================================================================
# ----------------------------------------------------------------------
""""""
# 6.4.1=================================================================
# ----------------------------------------------------------------------
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
# ----------------------------------------------------------------------
# 建立一個用來儲存外星人的空列表
aliens = []

#創造30個綠色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


# 印出前面5個外星人
for alien in aliens[:5]:
    print(alien)

print("。。。")
# 顯示創造了幾個外星人
print("Total number of aliens: " + str(len(aliens)))
# ----------------------------------------------------------------------
# 建立一個用來儲存外星人的空列表
aliens = []

#創造30個綠色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0: 3]: # 修改前面3個外星人的資訊
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 顯示前面5個外星人
for alien in aliens[0: 5]:
    print(alien)
print("。。。")
# ----------------------------------------------------------------------
# 建立一個用來儲存外星人的空列表
aliens = []

#創造30個綠色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0: 3]: # 修改前面3個外星人的資訊
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0: 5]: # 修改前面5個外星人的資訊 (擴展這個迴圈)
    if alien['color'] == 'green': # 把綠色便成黃色
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':# 把黃色便成紅色
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 顯示前面10個外星人
for alien in aliens[0: 10]:
    print(alien)
print("。。。")


# 6.4.2=================================================================
# ----------------------------------------------------------------------
# 儲存所點比薩的資訊
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'], # 把一個key關連到多個value的方法
    # 把一個key關連到一個list -> 嵌套
    }

# 概述所點的比薩
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']: # pizza['toppings']將會回傳一個list
    print("\t" + topping)
# ----------------------------------------------------------------------
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    } # 在這裡每個value都是一個list

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    # 最後印出來，在sarah那邊文法會不對，因為她只喜歡一個語言
    for language in languages:
        print("\t" + language.title())

# 6.4.3=================================================================
# ----------------------------------------------------------------------



















































































