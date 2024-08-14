# 1
names = ["Avi", "Bryan", "James"]
print(names[1])

# 2
sports = ["football", "basketball", "voleyball"]
sports[1] = "tennis"

# 3
numbers = [0,1,2,3,4,5]
del numbers[4]
print(numbers)

# 4
numbers2 = [6,7,8,9]
print(numbers+numbers2)

# 5
nums = [1,21,20,50,6,0.5]

print(len(nums) , max(nums) , min(nums))

# 6
students = {"Avi": 5, "Bryan": 4, "James": 6}

print(students.values())

# 7
students = {"Avi": 5, "Bryan": 4, "James": 6}

del students["Bryan"]
print(students)

# 8
students = {"Avi": 5, "Bryan": 4, "James": 6}
print(students.keys())
print(students.values())

# 9
films = ("TheGreenBook", "FightClub", "TheWolfOfWallStreet")

# 10
films = ("TheGreenBook", "FightClub", "TheWolfOfWallStreet")
print(films[0:2])