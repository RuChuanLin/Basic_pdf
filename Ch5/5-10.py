# ----------------------------------------------------------------------
# 前三個動作要求
current_users = ['Admin', 'Eric', 'Steven', 'David', 'Keven']
new_users = ['Hank', 'John', 'Allon', 'Amy', 'Eric']
for new_user in new_users:
    if new_user not in current_users:
        print("這個使用者名稱沒有被使用，所以OK!")
    else:
        print("這個使用者名稱被用過了，所以需要你再輸入別的。")
# ----------------------------------------------------------------------
# 加入第4個，跟上面幾乎顛倒過來的思路了
current_users = ['Admin', 'Eric', 'Steven', 'David', 'Keven']
new_users = ['Hank', 'John', 'Allon', 'Amy', 'ERIC']
for new_user in new_users:
    if new_user in current_users:
        print("這個使用者名稱被用過了，所以需要你再輸入別的。")
    elif new_user.upper() in current_users:
        print("這個使用者名稱被用過了，所以需要你再輸入別的。")
    elif new_user.lower() in current_users:
        print("這個使用者名稱被用過了，所以需要你再輸入別的。")
    elif new_user.title() in current_users:
        print("這個使用者名稱被用過了，所以需要你再輸入別的。")
    else:
        print("這個使用者名稱沒有被使用，所以OK!")