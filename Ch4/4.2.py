# 4.2======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
# 4.2.1======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician) # 因為該縮排的沒有縮所以會報錯
# 4.2.2======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n") #沒再迴圈裏面所以只會印出來一次，印最後一個人的名字
# 4.2.3======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
message = "Hello Python world!"
    print(message) #因為不該縮排的縮掉了，所以報錯

# 4.2.4======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you everyone, that was a great magic show!") #這東西不該縮排卻縮了，所以原本想要印出1次卻變成印出3次，多印了2次

# 4.2.5======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina']
for magician in magicians #冒號遺漏了，這樣會報錯
    print(magician)
    