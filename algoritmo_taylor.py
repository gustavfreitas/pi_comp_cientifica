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

# Tabela de Valores Utilizados

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

# Gráficos

print("\nGERANDO GRÁFICOS...")

plt.figure(figsize=(15, 5))

# Gráfico 1: Aproximação da Função

plt.subplot(1, 3, 1)
# Otimização visual: reduzido o domínio para -2.2 a 2.2 para o gráfico focar na região 
# de convergência onde as aproximações se moldam e evitar a distorção extrema das bordas
x_vals = np.linspace(-2.2, 2.2, 400)
y_real = np.sin(x_vals**2)

plt.plot(x_vals, y_real, label="Real: sen(x^2)", color="black", linewidth=2.5)

# Testando limites diferentes de N de maneira limpa
for n_teste in[2,4,8]:
    # Uma forma mais eficiente de gerar as aproximações do gráfico mantendo a lógica de somatório
    y_aprox = np.zeros_like(x_vals)
    for n in range(n_teste):
        y_aprox += ((-1)**n * x_vals**(4*n+2)) / math.factorial(2*n+1)
        
    plt.plot(x_vals, y_aprox, label=f"Taylor (N={n_teste})", linestyle="--")

plt.title("Aproximações da Série de Taylor")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-1.5, 1.5)
plt.legend()
plt.grid(True)

# --- Coletar dados de estresse progressivo de N para os próximos gráficos ---
x_alvo = 2.0  # Usamos x=2.0 pois requer mais processamento que x=0.5
ns_para_plot = range(1, 16)
erros_plot = []
tempos_plot = []

for n in ns_para_plot:
    soma, _, t = taylor_seno_x2(x_alvo, max_n=n, tol=0)  # Tol 0 para forçar até N
    erros_plot.append(abs(math.sin(x_alvo**2) - soma))
    tempos_plot.append(t)

# Gráfico 2: Erro vs N
plt.subplot(1, 3, 2)
plt.plot(ns_para_plot, erros_plot, marker='o', color='red')
plt.yscale('log')  # Escala logarítmica para ver a queda drástica do erro
plt.title(f"Erro Absoluto por Iteração (x={x_alvo})")
plt.xlabel("Número de Iterações (N)")
plt.ylabel("Erro Absoluto (escala log)")
plt.grid(True, which="both", ls="--")

# Gráfico 3: Tempo de Execução vs N 
plt.subplot(1, 3, 3)
plt.plot(ns_para_plot, tempos_plot, marker='s', color='green')
plt.title(f"Velocidade de Processamento (x={x_alvo})")
plt.xlabel("Número de Iterações (N)")
plt.ylabel("Tempo de Execução (segundos)")
plt.grid(True)

plt.tight_layout()
plt.show()