motorcycles = ['bmw', 'kimco', 'yahama', 'sym', 'aeon', 'gogoro', 'pgo', 'honda', 'ducati']

del motorcycles[9] #故意讓他報錯，本來是要砍掉最後一個(第9個)，但是索引應該是8才對

del motorcycles[-1] #正常，就是砍掉最後一個
print(motorcycles)