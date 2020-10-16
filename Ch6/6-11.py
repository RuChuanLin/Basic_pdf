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


for city, information in cities.items(): # 課本範例的寫法
    print("\nCity: " + city)
    country = information['country'] # 從字典賦值給變數
    population = information['population'] # 從字典賦值給變數
    fact = information['fact'] # 從字典賦值給變數
    print("\tCountry: " + country)
    print("\tPopulation" + population)
    print("\tParies" + fact)
    # 發現其實可以不用賦值直接print