# 7.2===================================================================
# ----------------------------------------------------------------------
# 7.2.1=================================================================
# ----------------------------------------------------------------------
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # 意思相當於 current_number = current_number + 1
# 7.2.2=================================================================
# ----------------------------------------------------------------------
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. " # 因為沒有在迴圈內所以只會+1次

message = "" # 先宣告message是空字串，★使Python首次執行while 程式時有可供檢查的東西。
# 如果沒有這樣做下面的while程式碼會無法執行，與for迴圈不同之處。
while message != 'quit':
    message = input(prompt) # 使用者的第一次輸入將會把初始設定的空字串蓋掉
    print(message) # 有個小缺點：輸入quit時也是會印出quit -> 可以加入一個判斷來解決
# ----------------------------------------------------------------------
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit': # 上面提到的，加入此判斷來解決輸出'quit'的問題
        print(message)
# 7.2.3=================================================================
# ----------------------------------------------------------------------
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True # while用來判斷的標誌，初始設定為True
while active:
    message = input(prompt)

    if message == 'quit': # 發生任何事情而必須停止程式時 -> 這邊只有一個，
        # 實際的產品可能會有很多個，總不可能把那一堆狀況全部向上一個那樣打在while判斷式裡面
        active = False # 把標誌設定為False來讓程式停止
    else: # 如果把else去掉，那就會把'quit'給印出來喔~
        print(message)
# 7.2.4=================================================================
# ----------------------------------------------------------------------
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: # 這個迴圈會一直執行，一直到遇到break
    city = input(prompt)

    if city == 'quit':
        break # 跳出這個迴圈的關鍵：只要執行到就會直接跳出
    else:
        print("I'd love to go to " + city.title() + "!")
# 7.2.5=================================================================
# ----------------------------------------------------------------------
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: # 當current_number是偶數的時候
        continue # 會跳到迴圈的一開始去執行，所以下面的print被略過
    print(current_number) # 導致只印出奇數
# 7.2.6=================================================================
# ----------------------------------------------------------------------
x = 1
while x <= 5:
    print(x)
    x += 1 # 這一行漏掉以後，這個迴圈就會一直循環囉~
# 這邊是有限循環，程式會正常執行
# ----------------------------------------------------------------------
x = 1
while x <= 5:
    print(x)
# 「無限迴圈」這種事情要盡量避免，如果不小心發生了，可以按「ctrl + C」來退出













































































