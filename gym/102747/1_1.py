

def s(i):
    A, n = i

    answer = A + n

    if A < 0 and answer >= 0:
            answer +=1 
    elif A > 0 and answer <= 0:
        answer -= 1

    return answer

if 0:
    data = [
        [ [5,-3], [2] ],
        [ [-3,1], [-2]],
        [ [-3,4], [2]],
        [ [-3,3], [1]],
        [ [3,-3], [-1]],
        
    ]

    for i in data:
        answer = s(i[0])
        print(f'{i[0]=} {i[1]=} {answer=} ')

else:
    a = int(input())
    b = int(input())
    print(s([a,b]))