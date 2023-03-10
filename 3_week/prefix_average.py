from time import time
import random

def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return (A)

def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j + 1)
    return (A)

def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return (A)

A = []

for val in range (0,100):
	A.append(random.randint(0,1000))

start_time = time()
prefix_average1(A)
end_time = time()
run_time = end_time - start_time
print("prefix_average 1 : ", run_time)

start_time = time()
prefix_average2(A)
end_time = time()
run_time = end_time - start_time
print("prefix_average 2 : ", run_time)

start_time = time()
prefix_average3(A)
end_time = time()
run_time = end_time - start_time
print("prefix_average 3 : ", run_time)

