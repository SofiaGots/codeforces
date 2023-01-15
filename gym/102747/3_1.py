def s(i):
    s,z = i
    counter = 0
    j = 0
    while j < len(z):
        if z[j] == 1:
            j += s
            counter += 1
        else:
            j += 1
    return counter


if 0:
    data = [
        [ [3, [0,0,1,0,1,0,1,0]], [2] ],
    ]

    for i in data:
        answer = s(i[0].copy())
        print(f'{i[1]=} {answer=} ')

else:
    a = int(input())
    b = int(input())
    zabor = list()
    for i in range(b):
        zabor.append(
            int(input())
        )

    print(s([a,zabor]))