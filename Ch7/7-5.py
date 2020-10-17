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