# 5.1===================================================================
# ----------------------------------------------------------------------
# 5.1.1=================================================================
# ----------------------------------------------------------------------
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw': # 把BMW用全部大寫輸出
        print(car.upper())
    else:print(car.title()) # 其餘的都是字首大寫
