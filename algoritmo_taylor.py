import math
import time
import sys 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Complexidade O(N)

def taylor_seno_x2(x, max_n=30, tol=1e-15):

    start_time = time.perf_counter()
    
    # Termo inicial n=0: x^2
    termo = x**2
    soma = termo
    n_executados = 0
    
    for n in range(1, max_n + 1):
        # Otimização: calcula o termo atual multiplicando o termo anterior por uma razão
        # Razão = (-x^4) / ( (2n) * (2n+1) )
        termo = termo * (-x**4) / ((2 * n) * (2 * n + 1))
        soma += termo
        
        # Critério de parada: limite de precisão da máquina (evita loop inútil)
        if abs(termo) < tol:
            n_executados = n
            break
    else:
        n_executados = max_n
        
    end_time = time.perf_counter()
    exec_time = end_time - start_time
    
    return soma, n_executados, exec_time