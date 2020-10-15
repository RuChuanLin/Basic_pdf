big_rivers = {
    'nile': 'egypt',
    'Danshui River': 'taiwan',
    'Yangtze River': 'china',
    }

for river, country in big_rivers.items():
    print("The " + river.title() + " runs through " + country.title())
# ----------------------------------------------------------------------
for river in big_rivers.keys():
    print(river.title())
# ----------------------------------------------------------------------
for country in big_rivers.values():
    print(country.title())











































