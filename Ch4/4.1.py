# 4.1======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
# 4.1.1======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina']
for magician in magicians: #前面的臨時變數可以用任何名稱沒關係，把list裡面的元素一個一個指定去臨時變數
    print(magician)
# 4.1.2======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
# ---------------------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# 4.1.3======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")








