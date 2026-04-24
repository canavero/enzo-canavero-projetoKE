# Projeto Knowledge Engine - F1 2023

Projeto da disciplina de Logica e Matematica Discreta.

Autor: Enzo Canavero

## Tema

Montei uma base de conhecimento em Prolog com os resultados da temporada
2023 da Formula 1. A partir dela da pra responder perguntas sobre pilotos,
equipes e corridas usando queries em Prolog.

## Dataset

Arquivo: `data/f1_2023.csv`

Foram 120 linhas (12 GPs x 10 pilotos pontuantes) com os campos:

- `gp` - nome do Grande Premio
- `piloto` - nome do piloto
- `equipe` - nome da equipe
- `grid` - posicao de largada
- `posicao` - posicao final
- `pontos` - pontos conquistados na corrida
- `volta_mais_rapida` - 1 se marcou a volta mais rapida, 0 caso contrario

Os dados foram coletados dos resultados oficiais da temporada 2023 da F1.

## Arquivos

- `data/f1_2023.csv` - dataset
- `etl.py` - script em Python que le o CSV e gera o base.pl
- `base.pl` - base de conhecimento em Prolog (gerada pelo etl.py)
- `perguntas.pl` - as queries para rodar no SWISH

## Como rodar

**1. Gerar o base.pl**

```
python3 etl.py
```

(so precisa de Python 3, nao usa nenhuma biblioteca externa)

**2. Rodar as queries**

1. Abrir https://swish.swi-prolog.org/
2. Copiar todo o conteudo do `base.pl` na aba **Program**
3. Copiar uma query do `perguntas.pl` na aba **Query**
4. Clicar em Run

## Predicado principal

```prolog
resultado(GP, Piloto, Equipe, Grid, Posicao, Pontos, VoltaMaisRapida).
```

Exemplo:

```prolog
resultado(bahrein, max_verstappen, red_bull, 1, 1, 25, 0).
```

## Perguntas

### 1) Classificacao do Mundial de Pilotos

Soma os pontos de cada piloto em todas as corridas e ordena do maior pro
menor. Usa `findall` + `sum_list` pra somar e `setof` + `reverse` pra
ordenar.

```prolog
?- classificacao_pilotos(Tabela).
```

Saida (top 5):

```
Tabela = [292-max_verstappen, 172-sergio_perez, 136-lewis_hamilton,
          134-fernando_alonso, 89-george_russell | ...]
```

### 2) Classificacao do Mundial de Construtores

Mesma ideia, mas somando os pontos por equipe.

```prolog
?- classificacao_construtores(Tabela).
```

### 3) Maior recuperacao da temporada

Em qual corrida um piloto ganhou mais posicoes entre o grid e a
chegada? Pra cada resultado, calcula `Grid - Posicao`, ordena e pega o
maior.

```prolog
?- maior_recuperacao(Piloto, GP, N).
```

Saida:

```
Piloto = sergio_perez,
GP = australia,
N = 15.
```

(Perez largou em 20o e terminou em 5o)

### 4) Ranking de vitorias

Todos os pilotos que venceram pelo menos uma corrida, ordenados por
numero de vitorias.

```prolog
?- setof(N-P, (piloto(P), total_vitorias(P, N), N > 0), L),
   reverse(L, Ranking).
```

### Perguntas simples extras

```prolog
% Quem venceu o GP da Espanha?
?- vitoria(Piloto, espanha).

% Todos os podios da Ferrari:
?- resultado(GP, Piloto, ferrari, _, Pos, _, _), Pos =< 3.
```
