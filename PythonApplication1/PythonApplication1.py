a, b = 0, 1
fib_sequence = []
for i in range(1, 26):  
    if i >= 4 and i <= 25:
        fib_sequence.append(a)
    a, b = b, a + b
print(fib_sequence)
print("Count of elements ", len(fib_sequence))