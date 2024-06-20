def bank(X, Y):
    total = X
    for i in range(Y):
        total += total * 0.1
    return total

X = 1000 # Например размер вклада
Y = 5 # Допустим срок вклада в годах
result = bank(X, Y)
print(result)
