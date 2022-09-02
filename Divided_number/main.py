user_number = int(input("Please enter 4-digit number: "))
res = user_number // 1000
user_number = user_number % 1000
print(str(res))
res1 = user_number // 100
user_number = user_number % 100
print(str(res1))
res2 = user_number // 10
user_number = user_number % 10
print(str(res2))
print(str(user_number))








