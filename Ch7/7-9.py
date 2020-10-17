# 7-8===================================================================
# ----------------------------------------------------------------------
# 原版本
sandwich_orders = ['tuna', 'pork', 'pastrami']
finished_sandwiches = []

while sandwich_orders: # ★list在空著的時候背強制型轉，會回傳False
    making_sandwich = sandwich_orders.pop()
    print("I made your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)

print("您點的全部三明治已經完成了^_^: ")
for finished_sandwich in finished_sandwiches: # ★即使在這裡用sorted()也不是user選擇的順序
    # 只是按照字首的ABCDE排列罷了
    print(finished_sandwich)

# 7-9===================================================================
# ----------------------------------------------------------------------
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'pork', 'pastrami']
finished_sandwiches = []

print("熟食店的五香煙燻牛肉(pastrami)賣完囉^_^")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print("I made your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)

print("除了五香煙燻牛肉(pastrami)以外，您點的全部三明治已經完成了^_^: ")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)



