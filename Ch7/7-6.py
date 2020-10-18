# 7-4===================================================================
# ----------------------------------------------------------------------
# 原版本(就已經是條件測試囉^^)
message = "\n請在每一次的詢問中加入一種比薩配料： "
message += "\n如果配料規劃完成了，請輸入'quit'來結束。"

pizza = ""

while pizza != 'quit':
    pizza = input(message)
    if pizza != 'quit':
        print("我們將會為您加入" + pizza + "於比薩中！")
# ----------------------------------------------------------------------
message = "\n請在每一次的詢問中加入一種比薩配料： "
message += "\n如果配料規劃完成了，請輸入'quit'來結束。"

active = True

while active:
    pizza = input(message)
    if pizza == 'quit':
        active = False
    else:
        print("我們將會為您加入" + pizza + "於比薩中！")
# ----------------------------------------------------------------------
message = "\n請在每一次的詢問中加入一種比薩配料： "
message += "\n如果配料規劃完成了，請輸入'quit'來結束。"

while True:
    pizza = input(message)
    if pizza == 'quit':
        break
    else:
        print("我們將會為您加入" + pizza + "於比薩中！")
# 7-5===================================================================
# ----------------------------------------------------------------------
# 原版本(就已經是條件測試囉^^)
message = "\n請問您幾歲呢?"
message += "\n想離開請輸入'q'"

age = 1

while age != 'q':
    age = input(message)
    if age != 'q':
        if int(age) < 3:
            print("您免費入場，歡迎您！")
        elif int(age) <= 12:
            print("10美元")
        elif int(age) > 12:
            print("15美元")
# ----------------------------------------------------------------------
message = "\n請問您幾歲呢?"
message += "\n想離開請輸入'q'"

active = True

while active:
    age = input(message)
    if age == 'q':
        active = False
    else:
        if int(age) < 3:
            print("您免費入場，歡迎您！")
        elif int(age) <= 12:
            print("10美元")
        elif int(age) > 12:
            print("15美元")
# ----------------------------------------------------------------------
message = "\n請問您幾歲呢?"
message += "\n想離開請輸入'q'"

while True:
    age = input(message)
    if age == 'q':
        break
    else:
        if int(age) < 3:
            print("您免費入場，歡迎您！")
        elif int(age) <= 12:
            print("10美元")
        elif int(age) > 12:
            print("15美元")




