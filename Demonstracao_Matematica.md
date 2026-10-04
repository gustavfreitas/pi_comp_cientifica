# Demonstração Matemática: Série de Taylor para $y = \sin(x^2)$

**Disciplina:** Projeto Integrador: Computação Científica  
**Integrantes:** Gustavo Souza Freitas, Miguel Hakira Mendes Kato, Gabriel Martins  

Este documento detalha as provas matemáticas que fundamentam o algoritmo desenvolvido para o EP1, justificando as escolhas de implementação e a otimização de complexidade.

---

## 1. Dedução da Função-Alvo (Evitando Derivadas Complexas)
O cálculo iterativo das derivadas sucessivas de $y = \sin(x^2)$ pela regra da cadeia gera polinômios extensos e de alto custo computacional (ex: $y'' = 2\cos(x^2) - 4x^2\sin(x^2)$$). Para viabilizar a simulação, utilizamos a expansão da Série de Maclaurin (Taylor em $a=0$) do seno fundamental e aplicamos uma substituição de variável.

Sabendo que a série do seno é:
$$\sin(u) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} u^{2n+1}$$

Substituímos o argumento $u = x^2$:
$$\sin(x^2) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} (x^2)^{2n+1}$$

Pela regra de potenciação, multiplicamos os expoentes, chegando à Fórmula do Termo Geral que embasa o nosso loop no Python:
$$\sin(x^2) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{4n+2}$$

---

## 2. Prova de Convergência (Teste da Razão)
Para garantir que o algoritmo não divirja para o infinito, precisamos provar o raio de convergência $R$. Aplicamos o Teste da Razão de d'Alembert no termo geral $a_n$:

$$L = \lim_{n \to \infty} \left\vert{} \frac{a_{n+1}}{a_n} \right\vert{} = \lim_{n \to \infty} \left\vert{} \frac{\frac{x^{4(n+1)+2}}{(2(n+1)+1)!}}{\frac{x^{4n+2}}{(2n+1)!}} \right\vert{}$$

$$L = \lim_{n \to \infty} \left\vert{} \frac{x^{4n+6}}{(2n+3)!} \cdot \frac{(2n+1)!}{x^{4n+2}} \right\vert{}$$

Simplificando os termos algébricos e expandindo o fatorial:
$$L = \lim_{n \to \infty} \left\vert{} x^4 \cdot \frac{(2n+1)!}{(2n+3)(2n+2)(2n+1)!} \right\vert{} = x^4 \cdot \lim_{n \to \infty} \frac{1}{(2n+3)(2n+2)}$$

Como o denominador cresce infinitamente e o numerador é constante para qualquer $x$ fixo:
$$L = x^4 \cdot 0 = 0$$

Como $0 < 1$ para todo $x \in \mathbb{R}$, **a série converge absolutamente para qualquer valor real**, justificando a estabilidade do algoritmo mesmo para valores de $x$ distantes da origem.

---

## 3. Prova da Otimização Algorítmica $O(N)$
No Python, calcular fatoriais como $(2n+1)!$ e potências elevadas a cada iteração causaria lentidão e *overflow* de memória. A lógica do nosso código se baseia em encontrar o próximo termo ($T_n$) multiplicando o termo atual ($T_{n-1}$) por uma razão matemática fixa.

Isolando a razão entre termos consecutivos:
$$\frac{T_n}{T_{n-1}} = \frac{ \frac{(-1)^n x^{4n+2}}{(2n+1)!} }{ \frac{(-1)^{n-1} x^{4n-2}}{(2n-1)!} }$$

Simplificando:
$$\frac{T_n}{T_{n-1}} = \frac{(-1)^n}{(-1)^{n-1}} \cdot \frac{x^{4n+2}}{x^{4n-2}} \cdot \frac{(2n-1)!}{(2n+1)!}$$
$$\frac{T_n}{T_{n-1}} = (-1) \cdot x^4 \cdot \frac{1}{(2n)(2n+1)}$$

Isolando $T_n$, temos a exata equação implementada no bloco `for` do nosso código, reduzindo o cálculo a operações aritméticas básicas e transformando o algoritmo para ordem linear $O(N)$:
$$T_n = T_{n-1} \cdot \left[ -\frac{x^4}{2n(2n+1)} \right]$$
