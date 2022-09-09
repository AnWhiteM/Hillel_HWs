new_lst = [1, 2, 3, 4, 5, 6]
l = int(len(new_lst) / -2)
print(l)

first_lst = new_lst[:l]
second_lst = new_lst[l:]

new_lst = []
new_lst = [first_lst, second_lst]
print(str(new_lst))
