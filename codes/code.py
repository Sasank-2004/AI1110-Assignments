import numpy as np
import pandas as pd
from numpy import random as RN
read = pd.read_excel("input.xlsx","Sheet1")
data = np.array(read)
frequency = {data[0][i]:data[1][i]  for i in range(1,7,1)}
N = sum(frequency[i] for i in range(1,7,1))
theory_pr = [frequency[i]/N for i in range(1,7,1)]
print("Theoretical Probabilities : ")
for i in range(1,7,1):
    print(f' P({i}) = {theory_pr[i-1]}')
x = RN.randint(1,high=7,size=N)
exp_pr = [(np.count_nonzero(x==i))/N for i in range(1,7,1)]
print("\nExperimental Probabilities : ")
for i in range(1,7,1):
    print(f' P({i}) = {exp_pr[i-1]}')