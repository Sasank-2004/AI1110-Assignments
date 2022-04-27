import numpy as np
import pandas as pd
from numpy import random as RN
from matplotlib import pyplot as plt
read = pd.read_excel("input.xlsx","Sheet1")
data = np.array(read)
x = [1,2,3,4,5,6] 
frequency = {data[0][1]:data[1][1],data[0][2]:data[1][2],data[0][3]:data[1][3],data[0][4]:data[1][4],data[0][5]:data[1][5],data[0][6]:data[1][6]}
N = frequency[1]+frequency[2]+frequency[3]+frequency[4]+frequency[5]+frequency[6]
theory_pr = [frequency[1]/N,frequency[2]/N,frequency[3]/N,frequency[4]/N,frequency[5]/N,frequency[6]/N]
print("Theoretical Probabilities : ")
print(f' P(1) = {theory_pr[0]}')
print(f' P(2) = {theory_pr[1]}')
print(f' P(3) = {theory_pr[2]}')
print(f' P(4) = {theory_pr[3]}')
print(f' P(5) = {theory_pr[4]}')
print(f' P(6) = {theory_pr[5]}')
X = RN.randint(1,high=7,size=N)
exp_pr = [(np.count_nonzero(X==1))/N,(np.count_nonzero(X==2))/N,(np.count_nonzero(X==3))/N,(np.count_nonzero(X==4))/N,(np.count_nonzero(X==5))/N,(np.count_nonzero(X==6))/N]
print("\nExperimental Probabilities : ")
print(f' P(1) = {exp_pr[0]}')
print(f' P(2) = {exp_pr[1]}')
print(f' P(3) = {exp_pr[2]}')
print(f' P(4) = {exp_pr[3]}')
print(f' P(5) = {exp_pr[4]}')
print(f' P(6) = {exp_pr[5]}')
width = 0.2
y1 = [theory_pr[0],theory_pr[1],theory_pr[2],theory_pr[3],theory_pr[4],theory_pr[5]] 
x2 = [1+width,2+width,3+width,4+width,5+width,6+width]
y2 = [exp_pr[0],exp_pr[1],exp_pr[2],exp_pr[3],exp_pr[4],exp_pr[5]] 
plt.stem(x, y1 ,linefmt='black' ,markerfmt = 'D',label = 'Theoretical')
plt.stem(x2, y2 ,linefmt= 'grey' , label = 'Experimental')
plt.xlabel('Outcomes')
plt.ylabel('Probability')
x3 = [1+width/2,2+width/2,3+width/2,4+width/2,5+width/2,6+width/2,]
plt.xticks(x3,x)
plt.legend(loc = 9)
plt.show()
