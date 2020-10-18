# 6-2===================================================================
# ----------------------------------------------------------------------
""""""
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

# 6-10=================================================================
# ----------------------------------------------------------------------
favorite_numbers = {
    'person 1': [1, 3, 5],
    'person 2': [2, 4, 6],
    'person 3': [3, 5, 7],
    'person 4': [4, 8, 32],
    'person 5': [5, 6, 8],
    }

for person, numbers in favorite_numbers.items():
    print("\n" + person.title() + " 喜歡的數字: ")
    for number in numbers:
        print("\t" + str(number))