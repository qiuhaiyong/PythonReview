print(False and 3 / 0)  # False
print(3 > 9 and 3 / 0)  # False

print(True or 3 / 0) # True
print(9 > 3 or 3 / 0) # True

print(not True)  # False
print(not False) # True
print(not 3 > 2) # False
print(not 3 < 2 and True) # True