# 3-5======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
friends = ['振泓', '昂謙', '小偉']

print("因為" + friends[2] +"這學期的課太硬了，所以他沒空過來跟我們一起吃飯。")

# ---------------------------------------------------------------------------------------------------------------------
friends[2] = '川哥兒'
# ---------------------------------------------------------------------------------------------------------------------
print(friends[0] + "您好，要不要一起吃晚餐?")
print(friends[1] + "您好，要不要一起吃晚餐?")
print(friends[2] + "您好，要不要一起吃晚餐?")
# 3-6======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
print("哈囉~" + friends[0] + "," + friends[1] + "," + friends[2] + "," + "我找到更大的餐桌囉~我們去吃更好料的^^")
# ---------------------------------------------------------------------------------------------------------------------
friends.insert(0, '鉉宗')
friends.insert(2, '哲哲')
friends.append('晉豪')
# ---------------------------------------------------------------------------------------------------------------------
print("哈囉~" + friends[0] + ", " + friends[1] + ", " + friends[2] + ", " + friends[3] + ", " + friends[4] + ", " + friends[5] + ", 我們今晚一起吃晚餐喔^^")
# 3-7======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
print("哈囉~" + friends[0] + ", " + friends[1] + ", " + friends[2] + ", " + friends[3] + ", " + friends[4] + ", " + friends[5] + ", 這個餐桌雷我，所以我現在只能找2個人吃飯= =")
# ---------------------------------------------------------------------------------------------------------------------
removed_person = friends.pop(-1)
print(removed_person + " 真是抱歉！這次主要是跟消夜團一起吃飯，所以我們下次再約。")

removed_person = friends.pop()
print(removed_person + " 真是抱歉！這次主要是跟消夜團一起吃飯，所以我們下次再約。")

removed_person = friends.pop(0)
print(removed_person + " 真是抱歉！這次主要是跟消夜團一起吃飯，所以我們下次再約。")

vegetable = '哲哲'
friends.remove(vegetable)
print(vegetable + " 真是抱歉！這次主要是跟消夜團一起吃飯，而且吃肉，所以我們下次再約一起吃素。")
# ---------------------------------------------------------------------------------------------------------------------
print("嗨" + friends[0] + "~現在只剩下我們兩個跟" + friends[1] + "了，我們宵夜團一起在實驗室吃艋舺雞排^^")
print("嗨" + friends[1] + "~現在只剩下我們兩個跟" + friends[0] + "了，我們宵夜團一起在實驗室吃艋舺雞排^^")
# ---------------------------------------------------------------------------------------------------------------------
del friends[1]
del friends[0] #必須先砍1在砍0，或是兩個都砍0。因為砍了第一個以後，第二個會變成第一個。所以再砍第二個會因為沒有第二個元素而報錯
print(friends)