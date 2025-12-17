def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
a = [1, 2, 3, 4]
b = [5, 6, 9, 0]

print(overlapping(a, b))   
