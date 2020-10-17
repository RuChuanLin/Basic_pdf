sandwich_orders = ['tuna', 'pork', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print("I made your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)

print("您點的全部三明治已經完成了^_^: ")
for finished_sandwich in finished_sandwiches: # ★即使在這裡用sorted()也不是user選擇的順序
    # 只是按照字首的ABCDE排列罷了
    print(finished_sandwich)