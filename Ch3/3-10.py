motorcycles = ['kimco', 'yahama', 'sym', 'aeon', 'gogoro', 'pgo', 'honda']
print(motorcycles[4])
print(motorcycles[4].title())
print(motorcycles[-1].title())

motorcycles[3] = 'ducati'
print(motorcycles)

motorcycles[3] = 'aeon'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'bmw')
print(motorcycles)

del motorcycles[-1]
print(motorcycles)
#目前剩下 ['bmw', 'kimco', 'yahama', 'sym', 'aeon', 'gogoro', 'pgo', 'honda'] ， 'ducati' 砍了

popped_motorcycle = motorcycles.pop(-4) #把倒數第4個元素 'aeon'砍掉抓出來存在變數裡面
print(popped_motorcycle)
print(motorcycles)

need_to_remove = 'honda'
motorcycles.remove(need_to_remove)
print(motorcycles)
print(need_to_remove.title() + " is to expensive, so it was removed.")

motorcycles = ['bmw', 'kimco', 'yahama', 'sym', 'aeon', 'gogoro', 'pgo', 'honda', 'ducati']
print(sorted(motorcycles))
print(sorted(motorcycles, reverse=True))

motorcycles.sort()
print(motorcycles)

motorcycles.sort(reverse=True)
print(motorcycles)

print(motorcycles)
motorcycles.reverse()
print(motorcycles)

len(motorcycles)
print(len(motorcycles))