def sumZero(n):
    lst = []
    if n == 1:
        return [0]

    length = n // 2
    for i in range(1, length + 1):
        lst.extend([i, -i])

    if n % 2 == 0:
        lst.append(0)
    lst.append(n)
    return lst


print(sumZero(5))
