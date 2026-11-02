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
