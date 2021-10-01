import multiprocessing as mp
from multiprocessing import process
import concurrent.futures
import time

startTime = time.time()

""""
Multiprocessing without adding Arguements 

"""
def sleepOne():
    time.sleep(1)

processes = []

for _ in range(100):
    p = mp.Process(target=sleepOne)
    p.start()
    processes.append(p)

for p in processes:
    p.join()


endTime = time.time()

print("Total Execution Time = ",endTime-startTime)


""""
Multiprocessing with added Arguements 

"""

def sleep(duration):
    time.sleep(duration)
    return f"done {duration}"

startTime = time.time()
processes = []

for t in range(20):
    p = mp.Process(target=sleep,args=[t])
    p.start()
    processes.append(p)

for p in processes:
    p.join()


endTime = time.time()

print("Total Execution Time = ",endTime-startTime)



"""
Process Pool Execute 

"""



with concurrent.futures.ProcessPoolExecutor() as executor:
    s = time.time()
    results = [executor.submit(sleep,t) for t in range(20)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
    e = time.time()
    print(e-s)




"""
Process Pool Executor using map method
"""
with concurrent.futures.ProcessPoolExecutor() as executor:
    s = time.time()
    results = executor.map(sleep,range(0,20))
    for result in results:
        print(result)
    e = time.time()
    print(e-s)