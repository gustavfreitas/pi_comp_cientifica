<<<<<<< HEAD
# 🚲 EP2 - Simulação de Eventos Discretos: Bicicletas Compartilhadas

Entrega do Exercício-Programa 2 (EP2) de Computação Científica. Usa a biblioteca **SimPy** para simular um sistema de bicicletas compartilhadas (inspirado no Bike Itaú / Tembici, São Paulo) como um sistema de filas: o **usuário** espera por uma **bicicleta** (servidor) numa estação vazia, pedala (tempo de serviço) e depois espera por uma **vaga** numa estação cheia.

**Integrantes do Grupo:**
* Gustavo Souza Freitas
* Miguel Hakira Mendes Kato
* Gabriel Mendes

---

## 🧩 O que o modelo faz

- **6 estações** em duas zonas (3 de "bairro" e 3 de "centro"), cada uma com **docas limitadas** (capacidade) e fila de retirada e de devolução próprias (`FilterStore` do SimPy).
- **Chegadas variando no tempo** (processo de Poisson não homogêneo): picos de manhã (bairro → centro) e à tarde (centro → bairro), como descrito no estudo da USP/EESC sobre dados da Tembici.
- **Tempo de viagem** lognormal (70% utilitária, média 10 min; 30% recreativa, média 20 min; máximo de 60 min).
- **Desistência e desvio**: o usuário perde a paciência esperando bicicleta (desiste ou tenta outra estação) ou vaga (desvia para outra estação). As requisições expiradas são **canceladas** no SimPy.
- **Caminhão de redistribuição** que leva bicicletas da estação mais cheia para a mais vazia, com **falhas aleatórias** (tempo entre falhas e reparo aleatórios).
- **Manutenção**: bicicletas com defeito ficam paradas numa doca até serem recolhidas e reparadas.

## 📊 Cenários simulados (06h às 22h)

| Cenário | Demanda | Perturbações | Taxa de atendimento (média de 30 réplicas) |
|---|---|---|---|
| **Caso base** (dia normal) | 0,7 × perfil | caminhão sem falhas | 98,7% |
| **Caso com volume** (dia de pico) | 1,0 × perfil | caminhão sem falhas | 94,7% |
| **Caso extremo** (demanda alta + falhas) | 2,0 × perfil | caminhão quebra aleatoriamente; 3% de defeitos | 78,5% |

Para cada cenário o notebook gera os gráficos exigidos: tamanho das filas, usuários no sistema, tempo de cada usuário na fila e no sistema, tempo de trabalho de cada bicicleta (servidor) e desistências ao longo do tempo. Há ainda comparação entre cenários com intervalo de confiança de 95% e varreduras de parâmetros (frota × caminhões, docas, política do caminhão).

## 🎯 Principais conclusões

- O **caminhão** é o recurso mais valioso: no pico, sobe o atendimento de 85,7% para 94,7%.
- Um caminhão **mais frequente** (a cada 15 min) rende mais que um segundo caminhão: 97,3% contra 96,8% no caso com volume.
- Docas abaixo de ≈ 1,75× as bicicletas por estação geram espera por vaga; acima de ≈ 2,25× não há ganho.
- No **caso extremo**, frota e redistribuição sozinhas não chegam a 95% (melhor combinação testada: 87,7%).

Os parâmetros marcados como "estimativa" no notebook (seção 1.5) não vêm de dados reais; as comparações entre configurações são mais confiáveis do que os valores absolutos.

## 📚 Fontes

1. MobilityData. *General Bikeshare Feed Specification (GBFS)* v3.0 — https://gbfs.org/documentation/reference/ (usada como inspiração para o estado da estação: capacidade, bicicletas e vagas disponíveis; não fornece dados de demanda)
2. Bigatão, G. L.; Cunha, A. L. B. N. *Análise do padrão de viagens feitas por bicicletas elétricas e convencionais em um sistema de compartilhamento de bicicletas na cidade de São Paulo*. EESC/USP — https://repositorio.usp.br/directbitstream/e13e5dc3-9dea-4995-a591-a3884eae8f1f/4481-11592-1-PB.pdf (picos de horário, duração das viagens, volume anual)
3. Bike Itaú / Tembici. *Aluguel de bicicleta em São Paulo* — https://bikeitau.com.br/sao-paulo/ (241 estações, 2.700 bicicletas, limites de tempo das viagens)

---

## 🛠️ Como Executar o Projeto

**Google Colab (recomendado):** envie `bicicletas_compartilhadas.ipynb` para o Colab e use *Ambiente de execução → Executar tudo*. A primeira célula instala o SimPy se necessário. A execução completa leva cerca de 1 minuto.

**Localmente:**
```
pip install simpy numpy pandas matplotlib scipy
```
Abra `bicicletas_compartilhadas.ipynb` no Jupyter e execute as células em ordem. Os resultados são reprodutíveis (cada simulação usa sua própria semente).

---

## ▶️ Apresentação e Defesa do Código

[**Assista à apresentação no YouTube**](insira_seu_link_do_youtube_aqui_antes_de_enviar)
=======
# 🚲 EP2 - Simulação de Eventos Discretos: Bicicletas Compartilhadas

Este projeto é a entrega do Exercício-Programa 2 (EP2) da disciplina de Computação Científica. O objetivo é utilizar a biblioteca **SimPy** para modelar e analisar computacionalmente um sistema de filas baseado em eventos discretos, aplicado ao contexto de aluguel de bicicletas compartilhadas (como o Bike Itaú / Tembici).

**Integrantes do Grupo:**
* Gustavo Souza Freitas
* Miguel Hakira Mendes Kato
* Gabriel Martins

---

## 📊 Cenários Simulados
O projeto foi modelado com base em dados do protocolo GBFS e estatísticas reais de mobilidade urbana, estruturando três cenários progressivos no Jupyter Notebook:

1. **Caso Base:** Simulação do fluxo normal de usuários, validando a arquitetura do sistema com a capacidade limitada das estações (docas) e o trânsito padrão de bicicletas.
2. **Caso com Volume (Horário de Pico):** Modelagem de um fluxo altamente assimétrico (ex: deslocamento matutino Bairro $\to$ Centro), introduzindo a logística de um caminhão de redistribuição para evitar o esgotamento precoce das estações.
3. **Caso Extremo (Colapso Logístico):** Simulação de uma perturbação crítica (falha mecânica no caminhão de redistribuição durante o horário de pico), evidenciando a dependência do sistema em relação ao remanejamento ativo para conter a explosão de desistências.

---

## 🛠️ Como Executar o Projeto

**Pré-requisitos:**
Certifique-se de ter o Python instalado. O projeto utiliza o Jupyter Notebook para a execução e visualização dos dados.

**1. Instale as bibliotecas necessárias:**
Abra o seu terminal e execute o seguinte comando:
`pip install simpy numpy pandas matplotlib`

**2. Execução:**
* Abra o arquivo principal do projeto: `bicicletas_compartilhadas.ipynb`.
* Execute as células sequencialmente. O código gerará automaticamente as fotografias do relógio de simulação e plotará os gráficos de *step plot* (tamanho das filas), *boxplot* (tempo no sistema) e gráficos de barra para análise de desistências.

---

## ▶️ Apresentação e Defesa do Código
No vídeo abaixo, demonstramos a explicação teórica do problema, os blocos matemáticos construídos no SimPy e a nossa conclusão sobre qual seria o dimensionamento ideal de recursos para o sistema:

[**Assista à apresentação no YouTube**](insira_seu_link_do_youtube_aqui_antes_de_enviar)
>>>>>>> dc3dfb7a719c24dfa79a2e69188667009852e209
