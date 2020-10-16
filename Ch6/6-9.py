favorite_places = {
    '我自己':['彰化', '台北', '台中'],
    '昂謙':['新竹', '台北', '台中以北'],
    '振泓':['桃園', '台北', '高雄'],
}

for name, places in favorite_places.items():
    print("\n" + name + "喜歡的地點: ") # ★可能要多打幾次來背熟
    for place in places:
        print("\t" + place)
