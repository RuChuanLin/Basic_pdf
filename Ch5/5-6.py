age = int(input())

if age < 2: # 小於2歲
    print("他是嬰兒")
elif age < 4: # 2(含)~4歲
    print("他正蹣跚學步")
elif age < 13: # 4(含)~13歲
    print("他是兒童")
elif age < 20: # 13(含)~20歲
    print("他是青少年")
elif age < 65: # 20(含)~65歲
    print("他是成年人")
else: # 65(含)歲以上
    print("他是老年人")