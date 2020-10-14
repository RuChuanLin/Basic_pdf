# 5.3===================================================================
# ----------------------------------------------------------------------
""""""
# 5.3.1=================================================================
# ----------------------------------------------------------------------
age = 19
if age >= 18:
    print("You are old enough to vote!")
# ----------------------------------------------------------------------
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# 5.3.2=================================================================
# ----------------------------------------------------------------------
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# 5.3.3=================================================================
# ----------------------------------------------------------------------
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
# ----------------------------------------------------------------------
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is " + str(price) + ".")
# 把上面那一塊的程式碼精簡化
# ----------------------------------------------------------------------
# 5.3.4=================================================================
# ----------------------------------------------------------------------
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age <65: # 多判斷是否為老人，如果是的話就半價(下面的else:5元)
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")
# 5.3.5=================================================================
# ----------------------------------------------------------------------
# 程式裡面可以沒有else沒關係
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: # 把上面的else換成elif可以讓條件變得更加清晰
    price = 5
print("You admission cost is $" + str(price) + ".")
# 5.3.6=================================================================
# ----------------------------------------------------------------------
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
# ----------------------------------------------------------------------
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings: # 因為最上面的if就True了所以後面都不判斷，
    # 也因為這裡沒判斷所以即使這裡為True也不會執行。所以這是錯誤示範！
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
















































































