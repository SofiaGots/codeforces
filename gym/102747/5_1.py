

def s1(i):
    a, b = i
    counter = 0
    for k in range(a, b+1):
        c = sum([int(j) for j in list(str(k))])
        if c % 2 == 1:
            counter += 1
        else:
            None
    return counter

def s(i):
    a, b = i
    if b % 2 == 1 and a % 2 == 1:
        return (b - a) // 2 + 1
    elif b % 2 == 0 and a % 2 == 0:
        return (b - a) // 2
    elif b % 2 == 1 and a % 2 == 0:
        return (b - a) //2 + 1
    else:
        return(b - a) // 2


if 0:
    data = [
        [[10, 20], [5]],
        [[20, 20], [0]],
        # [[-3,4], [2]],
        # [[-3,4], [2]],
    ]

    for i in data:
        answer = s(i[0])
        print(f'{i[0]=} {i[1]=} {answer=} ')

else:
    a = int(input())
    b = int(input())
    print(s([a,b]))