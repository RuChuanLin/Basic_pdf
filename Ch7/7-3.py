number = input("請給我一個數字，我可以告訴你它到底是不是10的倍數 =D")
number = int(number)

if number % 10 ==0:
    print("嘿嘿! " + str(number) + " 是10的倍數喲！^^")
else:
    print("不是喲！ " + str(number) + " 不是10的倍數，因為它無法被10整除。")