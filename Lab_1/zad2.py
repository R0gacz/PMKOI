def gen(a, b):
    n = a
    for i in range(a, b):
        yield n
        n = n + 1


example = gen(1, 7)
print(example)
for i in example:
    print(i)