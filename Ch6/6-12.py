# 之前有一個文法錯誤的拿來改
# 6.4.2=================================================================
# ----------------------------------------------------------------------
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    } # 在這裡每個value都是一個list

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    # 最後印出來，在sarah那邊文法會不對，因為她只喜歡一個語言
    for language in languages:
        print("\t" + language.title())
# ----------------------------------------------------------------------
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'He': [], #這邊再多一個完全不喜歡的
    } # 在這裡每個value都是一個list

for name, languages in favorite_languages.items():
    if len(languages) > 1: # 數量大於1才做
        print("\n" + name.title() + "'s favorite languages are:")
    elif len(languages) == 1: # 只喜歡一個才做
        print("\n" + name.title() + "'s favorite language is:")
    elif len(languages) == 0: # 一個都不喜歡
        print("\n" + name.title() + " doesn't like any language.")

    for language in languages:
        print("\t" + language.title())
# ----------------------------------------------------------------------
# 6-11把它拿來修，也相當於6.4.3變成平行
cities = {
    'Taipei': {'country': 'Taiwan',
         'population': '10000000',
         'fact': 'central of Taiwan',
         },
    'Wuhan': {'country': 'China',
         'population': '70000000',
         'fact': 'COVID-19',
         },
    'Paris': {'country': 'France',
         'population': '5000000',
         'fact': 'central of France',
         },
}

for city, information in cities.items():
    print("\nCity: " + city)
    for key, value in information.items(): # ★自己思考的
        print("\t" + key.title() + ": " + value)
        #直接抓key跟value印出來
        #這個蠻精簡的


# ======================================================================
#分成2邊的會失敗，再去用list其實很浪費變數且複雜

for city in cities.keys():
    print("\nCity: " + city.title())


for information in cities.values():
    print("\tCountry: " + information['country'])
    print("\tPopulation" + information['population'])
    print("\tfact" + information['fact'])
