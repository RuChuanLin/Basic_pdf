# 7.1===================================================================
# ----------------------------------------------------------------------
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# 7.1.1=================================================================
# ----------------------------------------------------------------------
name = input("Please enter your name: ")
print("Hello, " + name + "!")
# ----------------------------------------------------------------------
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? " # 提示太長，超過一行 -> 把提示儲存在變數裡面

name = input(prompt)
print("\nHello, " + name + "!")
# 7.1.2=================================================================
# ----------------------------------------------------------------------
age = input("How old are you? ") # input()輸入後會是字串，即使是數字也一樣
age # 會是'數字' -> 字串的內容是數字
# ----------------------------------------------------------------------
age = input("How old are you? ") # input()輸入後會是字串，即使是數字也一樣
age >= 18  # 拿字串跟數字比較的話會報錯，可以用int()強制型轉來解決這個問題
# ----------------------------------------------------------------------
age = input("How old are you? ") # input()輸入後會是字串，即使是數字也一樣
age = int(age)
age >= 18 # 印出True
# ----------------------------------------------------------------------
height = input("How tall are you, in inches? ")
height = int(height) # 在這裡強制型轉，為了後面進行判斷(跟整數int比較)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
# 7.1.3=================================================================
# ----------------------------------------------------------------------
4 % 3 # 餘數為1
5 % 3 # 餘數為2
6 % 3 # 餘數為0
7 % 3 # 餘數為1
# % 常被用來判斷某數值是否為偶數
# 某數字 % 2 == 0  -> 某數字 = 偶數
# 某數字 % 2 == 1  -> 某數字 = 奇數
# ----------------------------------------------------------------------
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number) # 本來是字串，強制型轉成int

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.") # 從int再強制型轉回字串
else:
    print("\nThe number " + str(number) + " is odd.") # 從int再強制型轉回字串
# 7.1.4=================================================================
# ----------------------------------------------------------------------
# Python2的就不管它囉^^








































































