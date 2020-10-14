# 3.2======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
# 3.2.1======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #直接修改list裡面的第一個元素
print(motorcycles)
# 3.2.2======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') #把'ducati'插入在motorcycles中的第一個元素
print(motorcycles)
# 3.2.3======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] #把list裡面的第一個元素砍掉
print(motorcycles)
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1] #把list裡面的第二個元素刪掉
print(motorcycles)
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() #刪除list裡面的元素再把它指定到poped_motorcycle預設是砍最後一個抓出來
print(motorcycles)
print(popped_motorcycle)
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop() #刪除list裡面的最後一個元素再把它指定到last_owned
print("The last motorcycle I owned was a " + last_owned.title() + ".")
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0) #刪除list裡面的第一個元素再把它指定到first_owned
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') #砍掉'ducati'這個元素，這個函式可以讓我們不知道'ducati'是第幾個元素的狀況下把它砍掉
print(motorcycles)
# ---------------------------------------------------------------------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")