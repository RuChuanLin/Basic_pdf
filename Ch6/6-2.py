favorite_numbers = {
    'number 1': 1,
    'number 2': 2,
    'number 3': 3,
    'number 4': 4,
    'number 5': 5,
    }

for number in range(1, 6):
    print("Number " +
          str(number) +
          " likes number " +
          str(favorite_numbers['number ' + str(number)])) # 指定幾號同學抓出他們的最愛數字
