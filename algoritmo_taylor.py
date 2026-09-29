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

print("GERANDO TABELA DE VALORES")
valores_x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5]
resultados = []

for x in valores_x:
    # Captura o valor exato para base de comparação
    real = math.sin(x**2)
    
    # Chama nossa função de Taylor
    aprox, n_iters, t_exec = taylor_seno_x2(x)
    
    erro_abs = abs(real - aprox)
    
    resultados.append({
        "Valor de x": x,
        "N (Iterações)": n_iters,
        "sen(x^2) Real": real,
        "Taylor Aprox": aprox,
        "Erro Absoluto": erro_abs,
        "Tempo Execução (s)": f"{t_exec:.2e}"
    })

# Renderiza a tabela usando Pandas com segurança (agora com sys importado)
df_resultados = pd.DataFrame(resultados)
if 'IPython' in sys.modules:
    from IPython.display import display
    display(df_resultados)
else:
    print(df_resultados.to_string(index=False))