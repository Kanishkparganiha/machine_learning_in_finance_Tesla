# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:45:32 2018

BOOTSTRAP

@author: Yizhen Zhao
"""

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas_datareader import DataReader
from datetime import datetime


AAPL = DataReader('AAPL',  'yahoo', datetime(2020,1,1), datetime(2020,12,31))
X = AAPL['Adj Close'].values

sns.kdeplot(data=X)


"Bootstrap"
T= X.shape[0]
B = 5000
mu_boot = np.zeros(B)
se_boot = np.zeros(B)
t_stat_boot = np.zeros(B)
for i in range(0, B):
     x_boot = X[np.random.choice(T,T)]
     mu_boot[i] = np.mean(x_boot)
     se_boot[i] = np.std(x_boot)/np.sqrt(T)
     # t_stat_boot[i] = (mu_boot[i]-mu)/se_boot[i] 
     "Test whether mean from bootstrap sample = sample mean"
mu_boot = np.sort(mu_boot)
se_boot = np.sort(se_boot)
# t_stat_boot = np.sort(t_stat_boot)

print("confidence interval of mu_boot:", mu_boot[25], mu_boot[975])
# print("confidence interval of x estimated by Bootstrap", mu-t_stat_boot[975]*se, mu-t_stat_boot[25]*se)




