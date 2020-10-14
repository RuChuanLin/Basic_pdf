# 4-7===================================================================
# ----------------------------------------------------------------------
three_numbers = list(range(3, 31, 3))
#從3開始，到31以前(不含31)，每個元素依序+3

for number in three_numbers:
    print(number)


# 4-12開始===============================================================
# ----------------------------------------------------------------------
# 4.4.3=================================================================
# ----------------------------------------------------------------------
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #把My_foods的元素，從第一個一直到最後一個
# ，全部指定進去friend_foods中，
# 其實在這裡「不能」直接打「friend_foods = my_foods」，意思不一樣！
# 這樣會變成把那兩個變數進行關聯，修改任何一個的話那另外一個也會跟著被更動。
# 上面單純就複製的意思
print("My favorite foods are:")
for my_pizza in my_foods: #原本這裡是直接印整個list，現在用for迴圈來印
    print(my_pizza)

print("\nMy friens's favorite foods are:")
for friend_pizza in friend_foods: #原本這裡是直接印整個list，現在用for迴圈來印
    print(friend_pizza)
# ----------------------------------------------------------------------
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #把my_foods從第一個元素複製到最後一個，
# 複製給friend_foods

my_foods.append('cannoli') #新增跟另外一個list不同的元素
friend_foods.append('ice cream') #新增跟另外一個list不同的元素

print("My favorite foods are:")
for my_pizza in my_foods: #原本這裡是直接印整個list，現在用for迴圈來印
    print(my_pizza)

print("\nMy friend's favorite foods are:")
for friend_pizza in friend_foods: #原本這裡是直接印整個list，現在用for迴圈來印
    print(friend_pizza)
# ----------------------------------------------------------------------
my_foods = ['pizza', 'falafel', 'carrot cake']
# 這行不通
friend_foods = my_foods #把friend_foods關聯到my_foods，
# 這兩個變數都指向同一個list

my_foods.append('cannoli') #把cannoli加入至my_foods的list裡面，
# 但是friend_foods這個list也會更動到

friend_foods.append('ice cream') #把ice cream加入到friend_foods的list裡面，
# 但是my_food這個list也會更動到

print("My favorite foods are:")
for my_pizza in my_foods: #原本這裡是直接印整個list，現在用for迴圈來印
    print(my_pizza)

print("\nMy friend's favorite foods are:")
for friend_pizza in friend_foods: #原本這裡是直接印整個list，現在用for迴圈來印
    print(friend_pizza)
# ----------------------------------------------------------------------
# 4-12結束===============================================================