def s(i):
    l, r = i
    min = 0
    counter = 0
    for j in range(1, len(j)):
        
        # if r[j] > r[j-1] and r[j] < r[j+1]:
        #     j += 1
        # else:
        #     counter += 1
        #     if j != 0 and r[j] > r[j-1] and r[j-1] == min:
        #         counter 
        #     min == r[j]



if 1:
    data = [
        [ 7, [18, 10, 15, 20, 20, 10, 3], [3, 6] ]
    ]

    for i in data:
        answer = s(i[0])
        print(f'{i[0]=} {i[1]=} {answer=} ')

else:
    a = int(input())
    roller_coaster = list()
    for i in range(a):
        roller_coaster.append(
            int(input())
        )

    print(s([roller_coaster]))