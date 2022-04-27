import numpy as np
import pandas as pd
from numpy import random as RN
from matplotlib import pyplot as plt
read = pd.read_excel("input.xlsx","Sheet1")
data = np.array(read)
x = [1,2,3,4,5,6] 
frequency = {data[0][i]:data[1][i]  for i in x}
N = sum(frequency[i] for i in x)
theory_pr = [frequency[i]/N for i in x]
print("Theoretical Probabilities : ")
for i in x:
    print(f' P({i}) = {theory_pr[i-1]}')
X = RN.randint(1,high=7,size=N)
exp_pr = [(np.count_nonzero(X==i))/N for i in x]
print("\nExperimental Probabilities : ")
for i in x:
    print(f' P({i}) = {exp_pr[i-1]}')
width = 0.2
y1 = [theory_pr[i-1] for i in x] 
x2 = [(i+width) for i in x ]
y2 = [exp_pr[i-1] for i in x] 
plt.stem(x, y1 ,linefmt='black' ,markerfmt = 'D',label = 'Theoretical')
plt.stem(x2, y2 ,linefmt= 'grey' , label = 'Experimental')
plt.xlabel('Outcomes')
plt.ylabel('Probability')
x3 = [i+width/2 for i in x]
plt.xticks(x3,x)
plt.legend(loc = 9)
plt.show()
