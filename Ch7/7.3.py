# 7.3===================================================================
# ----------------------------------------------------------------------
# 7.3.1=================================================================
# ----------------------------------------------------------------------
# 首先，創造一個待驗證使用者的list
# 和一個用來儲存已驗證使用者的空list
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 驗證每個使用者，直到沒有待驗證的使用者為止
# 把每個未驗證的使用者，從原本的list移到已驗證使用者的list中
while unconfirmed_users:
    current_user = unconfirmed_users.pop() # 刪除list之中的最後一個元素，並且將該元素賦值給current_user
    # unconfirmed_users這個list會一直循環到變成空的
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user) # 把抓出來的那個元素，儲存到被確認的那個list

# 顯示所有已驗證的使用者
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# 7.3.2=================================================================
# ----------------------------------------------------------------------
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# dog * 2; cat * 3; goldfish * 1; rabbit * 1
print(pets)

while 'cat' in pets: # 用迴圈
    pets.remove('cat') # 把'cat'由前往後全部刪除
# 每次的remove()都只能從list的「最前面」刪除「一個」指定的元素

print(pets)
# ----------------------------------------------------------------------
"""補充：
.pop()是從最後面
.remove()是從前面
.append()是從後面
.sort()是按照ABCDE順序排列，可指定參數：reverse = True
sorted()與.sort()相似功能，但是它是沒有副作用的函式
.XXX()幾乎都有副作用，XXX()幾乎沒有，比較是那種暫時性的"""
# ----------------------------------------------------------------------
responses = {} # 建立空字典，為了讓名字與回答相關聯 (使之成為key: value)
# 字典的中間是「:」，不是「;」喔！

# 設定一個標誌，指出是否繼續調查
polling_active = True

while polling_active:
    # 提示輸入被調查者的名字與回答
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday?")
    # 被賦值的變數是單數，上面list的變數名稱是單數

    # 把答案儲存在字典裡面
    responses[name] = response # ★格式要背一下
    # 字典加入 key: value的方式

    # 看看是否還有人要參與調查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    # 這裡就算不輸入'yes'也會繼續，算是bug
    if repeat == 'no':
        polling_active = False

# 調查結束，顯示結果
print("\n--- Poll Results ---")
for name, response in responses.items(): # for迴圈的暫存變數可以指定跟上面出現過的一模一樣
    # ★後面記得要加「.items()」
    print(name + " would like to climb " + response + ".")















































































