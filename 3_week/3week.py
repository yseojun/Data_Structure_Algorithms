import random
from time import time

my_list = []
start_time = time()
for i in range(0, 1000):
    my_list.append(random.randint(0, 10000))
end_time = time()
run_time = end_time - start_time
print(run_time)