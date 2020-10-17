# ----------------------------------------------------------------------
# 標誌(Active)的版本
places = {}

active = True

while active:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    places[name] = place

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False


print("\n--- Poll Results ---")

for name, place in places.items():
    print(name.title() + " would like to visit " + place.title())

# ----------------------------------------------------------------------
# break的版本
places = {}

while True:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    places[name] = place

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        break

print("\n--- Poll Results ---")
for name, place in places.items():
    print(name.title() + " would like to visit " + place.title())

# ----------------------------------------------------------------------



c = {1:5, 1:6, } # 字典裏面不能有多個相同的key對到多個不同的value
# ★這樣亂宣告就只會輸出後面那一個
print(c)