a = int(input())
b = int(input())
c = int(input())
counter = 0
while a != -1 and b != -1 and c != -1:
    if a != 0 and b != -1 and c != -1:
        a -= 1
        counter += 1
        if a != -1 and b != 0 and c != -1:
            b -= 1
            counter += 1
            if a != -1 and b != -1 and c != 0:
                c -= 1
                counter += 1
                if a != -1 and b != 0 and c != -1:
                    b -= 1
                    counter += 1
                else:
                    break
            else:
                break
        else:
            break
    else:
        break
print(counter)
# if b % 2 == 0:
#     answer = b*2
# else:
#     answer = b*2 + 1
# print(answer)