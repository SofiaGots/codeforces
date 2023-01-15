A = int(input())
n = int(input())

answer = A + n

if A < 0 and answer >= 0:
        answer +=1 
elif A > 0 and answer <= 0:
    answer -= 1
print(answer)
