import multiprocessing as mp
import time
import math

results_a = []
results_b = []
results_c = []

def make_calculatons_a():
  global results_a
  for i in range(1000000):
    results_a.append(math.sqrt(i))
  print("Calculations A done")


def make_calculatons_b():
  global results_b
  for i in range(1000000):
    results_b.append(i**2)
  print("Calculations B done")

def make_calculatons_c():
  global results_c
  for i in range(1000000):
    results_c.append(i**3)


if __name__ == '__main__':
  starttime = time.time()
  
  make_calculatons_a()
  make_calculatons_b()
  make_calculatons_c()
  
  
  # p1 = mp.Process(target=make_calculatons_a)
  # p2 = mp.Process(target=make_calculatons_b)
  # p3 = mp.Process(target=make_calculatons_c)
  
  # p1.start()
  # p2.start()
  # p3.start()
  
  # p1.join()
  # p2.join()
  # p3.join()
  
  print(results_a)
  print(results_b)
  print(results_c)
  
  endtime = time.time()
  print((endtime - starttime))

