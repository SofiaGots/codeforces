
def solution(suit):
    if suit == 2 or suit == 1:
        return 1
    else:
        return ((suit - 6)//4) + ((suit - 6)%4>0) + 1


if False:
    input = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    output =[1,1,1,1,1,1,2,2,2,2, 3, 3, 3]

    for (i, j) in zip(input, output):
        print(f'{i=} {j=} {solution(i)=}  - ', end='' )
        print(1 if j == solution(i) else 0)

else:
    print(
        solution(
            int(
                input()
            )
        )
    )
