# 5.4===================================================================
# ----------------------------------------------------------------------
""""""
# 5.4.1=================================================================
# ----------------------------------------------------------------------
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
# ----------------------------------------------------------------------
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
# 5.4.2=================================================================
# ----------------------------------------------------------------------
# ★
requested_toppings = [] # 建立一個空的list
if requested_toppings: # 空list 跟 False是相同的意思，都會使if的判斷不符合條件
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# 5.4.3=================================================================
# ----------------------------------------------------------------------
# ★
available_toppings = ['mushrooms', 'olivers', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] # 如果這邊固定的話其實甚至能用Tuple
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings: # 從另外一個list判斷這個list裡面的元素可否使用
        print("Adding " + requested_topping + ".")

    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")























































