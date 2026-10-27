### 📝 Análise do Cenário Base

**Comportamento do Fluxo Assimétrico:**
- Observe no gráfico o ponto exato (em minutos) em que a linha azul (Estação Origem) atinge a linha tracejada vermelha (Esgotamento). Isto indica que a taxa de chegada supera amplamente a taxa de retorno natural dessa estação.
- Paralelamente, verifique se a linha laranja (Estação Destino) toca a linha verde (Lotação Máxima). Quando isso ocorre, o sistema sofre de congestionamento estrutural.

**Métricas de Desistência:**
- O total de *Desistências na Origem* reflete a perda de demanda operacional. 
- O total de *Desistências no Destino* reflete uma falha crítica de serviço, pois o usuário concluiu o tempo de serviço (viagem), mas não conseguiu liberar o servidor (bicicleta), gerando retenção irreal.

**Proposta para o Cenário "Com Volume" e "Extremo":**
- Para a próxima etapa (Caso com Volume), o parâmetro `taxa_chegada` será reduzido para `1` (1 usuário por minuto) simulando o horário de pico.
- Para mitigar os gargalos observados neste caso base, introduziremos um novo processo SimPy (`env.process(caminhao_redistribuicao)`) que, a cada 120 minutos de relógio, remove bicicletas do Destino e devolve à Origem.