def duplicates(a):
    x = []
    for i in a:
        if i not in x:
            x.append(i)
    return x
b = [1,2,3,4,3,1]
print(b)
print(duplicates(b))
