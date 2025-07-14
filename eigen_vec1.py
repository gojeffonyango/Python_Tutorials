# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 20:42:41 2025

@author: gojef
"""
import numpy as np
A = np.array([[0.3,0.2,0],
              [0.6,0.2,0.2],
              [.1,0.6,0.8]])

eigvals, eigvecs = np.linalg.eig(A)

print(eigvals)

print(eigvecs)

zombie_A = np.array([[0.3,0.2,0],
              [0.6,0.2,0.2],
              [.1,0.6,0.8]])

def zombie_population(init_pop, n_years):
  return np.linalg.matrix_power(zombie_A,n_years)@init_pop

zombie_population([800,200,0],100)

init_pop = [1000,0,0]
num_healthy = [zombie_population(init_pop,n_years)[0] for n_years in range(0,20)]
num_sick = [zombie_population(init_pop,n_years)[1] for n_years in range(0,20)]
num_dead = [zombie_population(init_pop,n_years)[2] for n_years in range(0,20)]

import matplotlib.pyplot as plt
plt.plot(range(0,20),num_healthy,label='Healthy')
plt.plot(range(0,20),num_sick, label='Sick')
plt.plot(range(0,20),num_dead, label='Dead')
plt.legend()
plt.xlabel('Number of Years')
plt.ylabel('Number of Dead Population')