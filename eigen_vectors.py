# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 20:37:12 2025

@author: gojef
"""

import numpy as np

A = np.array([[6,10,6],
              [0,8,12],
              [0,0,2]])

# Fill this in!
eigvals, eigvecs = np.linalg.eig(A)

# Notice that we can use variables in a print!
# f'something {var}' means sub in the var in the string
print(f'Eigenvalues = {eigvals}') 
print(f'Eigenvectors: \n{eigvecs}')