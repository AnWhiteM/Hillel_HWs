user_number = int(input("Please Input 5-digit number: "))
rev = 0

num = user_number % 10
user_number = user_number // 10
rev = rev * 10
rev = rev + num

num = user_number % 10
user_number = user_number // 10
rev = rev * 10
rev = rev + num

num = user_number % 10
user_number = user_number // 10
rev = rev * 10
rev = rev + num

num = user_number % 10
user_number = user_number // 10
rev = rev * 10
rev = rev + num

num = user_number % 10
user_number = user_number // 10
rev = rev * 10
rev = rev + num
print(str(rev))
