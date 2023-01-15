A = int(input())
B = int(input())
C = int(input())
D = int(input())
aorb = 0
cord = 0
# def solution(A, B, C, D):
if A > B:
    aorb += B + 1
elif B > A:
    aorb += A + 1
elif A == B:
    aorb += A + 1
if C > D:
    cord += D + 1
elif D > C:
    cord += C + 1
elif C == D:
    cord += C + 1
print(aorb, cord)
# if False:
#     input = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#     output =[1,1,1,1,1,1,2,2,2,2, 3, 3, 3]

#     for (i, j) in zip(input, output):
#         print(f'{i=} {j=} {solution(i)=}  - ', end='' )
#         print(1 if j == solution(i) else 0)

# else:
#     print(
#         solution(
#             int(
#                 input()
#             )
#         )
#     )
