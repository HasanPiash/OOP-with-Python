# def split_balanced_strings(S):
#     balance = 0
#     balanced_count = 0
#     result = []
#     start = 0
#     for i, char in enumerate(S):
#         if char == 'L':
#             balance += 1
#         elif char == 'R':
#             balance -= 1
#         if balance == 0:
#             balanced_count += 1
#             result.append(S[start:i + 1])
#             start = i + 1
#     print(balanced_count)
#     for substring in result:
#         print(substring)
# S = input().strip()
# split_balanced_strings(S)


def splt_blc_strs(S):
    balance=0
    result=[]
    start=0

    for i in range(len(S)):
        if S[i]=='L':
            balance +=1
        else:
            balance -=1
        if balance==0:
            result.append(S[start:i+1])
            start=i+1

    print(len(result))
    print("\n".join(result))
S = input().strip()
splt_blc_strs(S)
