def do_something(x):
    ''' This is a sample multiline comment
    '''
    if x == 0:
        return 0
    elif x + 4 == 1:
        if True:
            return 3
        else:
            return 2
    elif x == 32:
        return 4
    else:
        return "Doodoo"

''' Test case 1'''


def CekInteger(x):
    if x < 0:
        print("NEGATIF")
    elif x > 0:
        print("POSITIF")
    else:
        print("NOL")
    return


def Max(a, b, c, d):

    big = 0
    if a >= b and a >= c and a >= d:
        big = a
    elif b >= c and b >= d and b >= a:
        big = b
    elif c >= b and c >= d and c >= a:
        big = c
    elif d >= a and d >= b and d >= c:
        big = d
    return (big)


def Min(a, b, c, d):
    smol = 0
    if a <= b and a <= c and a <= d:
        smol = a
    elif b <= c and b <= d and b <= a:
        smol = b
    elif c <= b and c <= d and c <= a:
        smol = c
    elif d <= a and d <= b and d <= c:
        smol = d
    return (smol)


def IsAllPositif(a, b, c, d):
    if a > 0 and b > 0 and c > 0 and d > 0:
        return True
    return False


''' Test case 2'''
n = int(input())

for i in range(0, n):

    x = int(input())

mini = arr[0]
maksi = arr[0]

count = 0
for i in range(n):
    if x == arr[i]:
        count += 1
    if arr[i] >= maksi:
        maksi = arr[i]
    elif arr[i] <= mini:
        mini = arr[i]

if count == 0:
    print(x)
    print(" tidak ada")
else:
    if x == maksi:
        print("maksimum")
    if x == mini:
        print("minimum")
    if x != maksi:
        print("N#A")


''' Test case 3'''


class method(testingClass):
    """
    Testing comment multiline
    """
    def funcname(test, procedure):
        pass


cobainBool = True
if (not(cobainBool)):
    while(1):
        if True:
            pass
        elif False:
            break
        else:
            a = 3
            iniString = 'hello world'


def function(cobain, loop):
    if (len(cobain) > 5 and loop):
        pass
    else:
        x = len(cobain)
        for i in range(x + 10):
            print(i)
            if (i > 10 and (i % 10 == 3)):
                continue