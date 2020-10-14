# ---------------------------------------------------------------------------------------------------------------------
message = "Hello Python world！" #把文字放在message這個變數裡面
print(message) #印出message的內容

message = "Hello Python Crash Course world！" #把「不太一樣」文字放在message這個變數裡面，把前面的資料覆蓋掉
print(message) #印出message的內容
# ---------------------------------------------------------------------------------------------------------------------
name = "ada lovelace" #把字串放在name這個變數裡面
print(name.title()) #印出name裡面的字串，而且印出來的樣子是每個單字的字首大寫
print(name.upper()) #印出name裡面的字串，而且印出來的樣子是每個字母都是大寫
print(name.lower()) #印出name裡面的字串，而且印出來的樣子是每個字母都是小寫
# ---------------------------------------------------------------------------------------------------------------------
first_name = "ada" #把字串「ada」放在「first_name」這個變數裡面
last_name = "lovelace" #把字串「lovelace」放在「last_name」這個變數裡面
full_name = first_name + " " + last_name #把「first_name」跟「last_name」還有空格字串進行合併變成一個句子，並且存在「full_name」這個變數裡面

print("Hello, " + full_name.title() + "!") #印出括號裡面的字串，重要的是full_name裡面的內容需要變成字首大寫才印出來
# ---------------------------------------------------------------------------------------------------------------------
print("Python") #印出python
print("\tPython") #  \t就是tab鍵按下去的意思(縮排)

print("Language:\nPython\nC\nJavaScript") #   \n就是換行的意思
# ★注意：路徑跟換行的斜線是一樣的！，都是「\」，在鍵盤的Enter鍵上面
print("Language:\n\tPython\n\tC\n\tJavaScript")# \n\t可以同時放在一起，同時進行換行跟縮排
# ---------------------------------------------------------------------------------------------------------------------
favorite_language = ' python '
favorite_language.rstrip() #砍右邊的空格
favorite_language.lstrip() #砍左邊的空格
favorite_language.strip() #砍左右兩邊的空格
favorite_language = favorite_language.strip() #把原本有空格的字串變數砍掉空格，再放回這個字串變數(把這個變數更新的意思)
# ---------------------------------------------------------------------------------------------------------------------
age = 23
message = "Happy " + str(age) + "rd birtgday!" #原本age是數字變數，把age行轉變成字串變數，再去跟前露兩個字串合併最後變成一個字串變數
print(message)
# ---------------------------------------------------------------------------------------------------------------------