# Amazon future prediction 
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
year=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
# rev=[88.99,107.01,135.99,177.87,232.89,280.52,386.06,469.82,514.00,524.96]
profit=[-0.24,0.59,2.37,3.03,10.07,11.59,21.33,33.36,2.87,9.06]
# p-pentagon,o-circle,d=diamond,s=square in marker line
# plt.scatter(age,salary,marker='p') used to create graph
# plt.show() used to show graph
futuresales=np.poly1d(np.polyfit(year,profit,3))
print(futuresales(2024))
print(r2_score(profit,futuresales(year)))