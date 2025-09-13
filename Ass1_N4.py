# def max_operations(N, A):
#     operations = 0
    
#     # Keep dividing while all numbers are even
#     while all(a % 2 == 0 for a in A):
#         A = [a // 2 for a in A]
#         operations += 1
    
#     print(operations)

# # Input Parsing
# try:
#     # Read number of elements
#     N = int(input().strip())
    
#     # Read array elements
#     A = list(map(int, input().strip().split()))
    
#     # Validate that the array size matches N
#     if len(A) != N:
#         raise ValueError("Array size does not match N")
    
#     # Call the function
#     max_operations(N, A)

# except Exception as e:
#     # Handle errors and unexpected input
#     print("Invalid input:", str(e))


# def max_operations(N,A):
#     operations=0
#     while all(a%2==0 for a in A):
#         A=[a//2 for a in A]
#         operations +=1
#     print(operations)
# N=int(input())
# A=list(map(int,input().split()))
# max_operations(N,A)


def mx_optns(N,A):
    optns=0
    while all(a%2==0 for a in A):
        A=[a//2 for a in A]
        optns +=1
    print(optns)
N=int(input())
A=list(map(int,input().split())) 
mx_optns(N,A)

