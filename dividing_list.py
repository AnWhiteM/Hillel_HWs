# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

new_lst = [1, 2, 3, 4, 5, 6, 5, 7, 9, 10, 11]
l = len(new_lst)
if l % 2 == 0:
    hl = l // 2
    first_lst = new_lst[:hl]
    second_lst = new_lst[hl:]
    new_lst = []
    new_lst0 = [first_lst, second_lst]
    print(str(new_lst0))
elif l == 1:
    hl = int(l % 2)
    first_lst = new_lst[:hl]
    second_lst = new_lst[hl:]
    new_lst = []
    new_lst2 = [first_lst, second_lst]
    print(str(new_lst2))
elif l % 2 != 0:
    hl = int(l / -2)
    first_lst = new_lst[:hl]
    second_lst = new_lst[hl:]
    new_lst = []
    new_lst1 = [first_lst, second_lst]
    print(str(new_lst1))

# Только так получилось :'(
