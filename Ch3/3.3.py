# 3.3======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------

# 3.3.1======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #把裡面的元素按照ABCDE順序排列(會有副作用的函式)
print(cars)
# ---------------------------------------------------------------------------------------------------------------------
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #把裡面的元素按照ABCDE的相反順序排列(會有副作用的函式)
print(cars)
# 3.3.2======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) #這種方式就不會有副作用，是暫時性的

print("\nHere is the original list again:")
print(cars)
# 3.3.3======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(cars)

cars.reverse() #把list裡面的元素完全顛倒順序，有副作用
print(cars)
# 3.3.4======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------------
cars = ['bmw', 'audi', 'toyota', 'sabaru']
len(cars)