def s1(i):
    l,s,p = i

    counter = 0
    while (min(i) > 0 or counter == 0) and max(i) > 0:
        for j in [0,1,2,1]:
            if i[j] > 0:
                counter += 1
                i[j] -= 1
            else:
                break

    return counter

def s(i):    
    l,s,p = i

    if l == 0:
        return 0
    elif l < min(s//2+1,p):
        return l * 4
    elif s <= min(l,p) * 2:
        # нечетное
        if s%2 == 1:
            return 3 + (s//2) * 4
        else:
            return 1 + (s//2) * 4
    elif p < min(l,s) :
        return p*4 + 2
    else:
        return(i)


        

if 0:
    data = [
        [ [1234,2345,3456], [4691] ],
        [ [100,100,100], [201] ],
        [ [1000,1000,1000], [2001] ],
        [ [1,3,3], [4] ],
        [ [1,1,1], [3] ],
        [ [3,3,3], [7] ],
        [ [2,2,2], [5] ],
        [ [4,4,3], [9] ],
        [ [4,4,4], [9] ],
        [ [5,5,5], [11] ],
        [ [7,7,7], [15] ],
        [ [1,1,1], [3] ],
        [ [2,2,1], [5] ],
        [ [3,3,1], [6] ],
        [ [5,5,2], [10] ],
        [ [7,7,3], [14] ],
        [ [1,1,0], [2] ],
        [ [0,0,0], [0] ],
        [ [1,2,1], [4] ],
        [ [2,1,2], [3] ],
        [ [10_000_000,10_000_000,10_000_000], [4] ],
    ]

    for i in data:
        answer = s(i[0].copy())
        print(f'{i[0]=} {i[1]=} {answer=} ')

else:
    a = int(input())
    b = int(input())
    c = int(input())
    print(s([a,b,c]))