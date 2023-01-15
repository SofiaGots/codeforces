

def s(i):
    pass


if 1:
    data = [
        [[5,-3], [2]],
        [[-3,1], [-2]],
        [[-3,4], [2]],
        [[-3,4], [2]],
    ]

    for i in data:
        answer = s(i[0])
        print(f'{i[0]=} {i[1]=} {answer=} ')

else:
    a = int(input())
    b = int(input())
    print(s([a,b]))