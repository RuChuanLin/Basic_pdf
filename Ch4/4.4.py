# 4.4======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
# 4.4.1======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #從第0號開始，一直到第3號以前(不含第3號)，把元素印出來。
# ---------------------------------------------------------------------------------------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4]) #從第1號開始，一直到第4號以前(不含第4號)，把元素印出來。
# ---------------------------------------------------------------------------------------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) #從「最前面」開始，一直到第4號以前(不含第4號)，把元素印出來。
# ---------------------------------------------------------------------------------------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) #從第2號開始(含第2號)，一直到最後一個(☆含最後一個)，把元素印出來。
# ---------------------------------------------------------------------------------------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) #從倒數第3個一直到最後一個，把元素印出來，也就是「最後3個」。
# 4.4.2======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
players = ['charels', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]: #迴圈也可以分段，從最一開始一直到第3號元素以前(不含第3號)
    print(player)
# ★
#分段很好用，假設他每一次得到的分數都不一樣，如果要統計他最高的3個分數，可以先用sort按照最高排到最低排序list的元素(就是他的所有得分)，然後再抓出最高的3個分數(最一開始到4號之前不含4號)

# 4.4.3======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
# ★
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #把My_foods的元素，從第一個一直到最後一個，全部指定進去friend_foods中，
# 其實在這裡「不能」直接打「friend_foods = my_foods」，意思不一樣，這樣會變成把那兩個變數進行關聯，修改任何一個的話那另外一個也會跟著被更動。
#上面單純就複製的意思
print("My favorite foods are:")
print(my_foods)

print("\nMy friens's favorite foods are:")
print(friend_foods)
# ---------------------------------------------------------------------------------------------------------------------
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #把my_foods從第一個元素複製到最後一個，複製給friend_foods

my_foods.append('cannoli') #新增跟另外一個list不同的元素
friend_foods.append('ice cream') #新增跟另外一個list不同的元素

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# ---------------------------------------------------------------------------------------------------------------------
# ★
my_foods = ['pizza', 'falafel', 'carrot cake']
# 這行不通
friend_foods = my_foods #把friend_foods關聯到my_foods，這兩個變數都指向同一個list

my_foods.append('cannoli') #把cannoli加入至my_foods的list裡面，但是friend_foods這個list也會更動到
friend_foods.append('ice cream') #把ice cream加入到friend_foods的list裡面，但是my_food這個list也會更動到

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# ---------------------------------------------------------------------------------------------------------------------










