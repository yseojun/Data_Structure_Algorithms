from time import time
import random


def disjoint1(A, B, C):
	for a in A:
		for b in B:
			for c in C:
				if a == b == c:
					return False
	return True

def disjoint2(A, B, C):
	for a in A:
		for b in B:
			if a == b:
				for c in C:
					if a == c:
						return False
	return True

A = []
B = []
C = []

for val in range (0,100):
	A.append(random.randint(0,1000))
	B.append(random.randint(0,1000))
	C.append(random.randint(0,1000))

start_time = time()
print(disjoint1(A, B, C))
end_time = time()
run_time = end_time - start_time
print("disjoint1 : ", run_time)

start_time = time()
print(disjoint2(A, B, C))
end_time = time()
run_time = end_time - start_time
print("disjoint2 : ", run_time)