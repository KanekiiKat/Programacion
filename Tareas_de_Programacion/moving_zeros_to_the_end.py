def move_zeros(lst):
    for num in lst:
        if num == 0:
            lst.remove(0)
            lst.append(0)
    return lst

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))