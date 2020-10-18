dog = {
    'Type': '犬科',
    '主人': '冠翰',
}

wolf = {
    'Type': '犬科',
    '主人': '昂謙',
}

fox = {
    'Type': '犬科',
    '主人': '振泓',
}

cat = {
    'Type': '貓科',
    '主人': '鉉宗',
}

lion = {
    'Type': '貓科',
    '主人': '承哲',
}

tiger = {
    'Type': '貓科',
    '主人': '川哥兒',
}

pets = [dog, wolf, fox, cat, lion, tiger]

for pet in pets:
    print("\nType of animal is " + pet['Type'] + ".")
    print("It is " + pet['主人'] + "'s pet.")