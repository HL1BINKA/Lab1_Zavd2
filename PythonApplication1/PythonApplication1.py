a, b = 0, 1
fibanachi = []
for i in range(1, 26):  
    if i >= 5 and i <= 25:
        fibanachi.append(a)
    a, b = b, a + b
print(fibanachi)
print("Count of elements ", len(fibanachi))