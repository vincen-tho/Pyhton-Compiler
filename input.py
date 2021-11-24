n = int(input())
while not(n == -999):
    if 30 <= n <= 200:
        count += 1
        sum += n
        if n <= 50:
            lt50 += 1
        elif n >= 100:
            gt100 += 1
    n = int(input())

if count != 0:
    print(count)
    print(lt50)
    print(gt100)
    print(round(sum/count))
else:
    print("Data kosong")