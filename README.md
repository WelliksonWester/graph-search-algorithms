<div align="center">

# Graph Search Algorithms

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-BFS%20|%20A*-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/status-concluído-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-purple?style=for-the-badge)

<p align="center">
  Implementação e análise comparativa de algoritmos clássicos de busca em grafos aplicados à resolução de rotas rodoviárias em Mato Grosso.
</p>

[Sobre](#-sobre) • [Modelagem](#-modelagem-do-grafo) • [Algoritmos](#-algoritmos) • [Comparativo](#-comparativo-de-execução) • [Como Usar](#-como-executar)

</div>

---

## 📌 Sobre

Este projeto explora o problema clássico de encontrar rotas ótimas entre cidades, demonstrando na prática as diferenças de desempenho e tomada de decisão entre uma busca não-informada (**BFS**) e uma busca heurística informada (**A\***).

O foco é analisar o custo de expansão de estados versus a otimalidade do caminho final em grafos ponderados.

---

## 🗺️ Modelagem do Grafo

O grafo representa a malha de conexão entre cidades de Mato Grosso, onde os pesos das arestas indicam a distância real em quilômetros:

[VG] ─── 10 km ─── [CBA] ─── 215 km ─── [ROND]
    │                   │
  60 km               130 km
    │                   │
  [JAN] ── 65 km ─── [ROS] ─── 60 km ─── [NOB] (Destino)

### Heurística $h(n)$
Para o algoritmo $A^*$, adota-se a estimativa de distância em linha reta até o objetivo (**NOB**):

| Cidade | Identificador | $h(n)$ até NOB (km) |
| :--- | :---: | :---: |
| **Nobres** | `NOB` | 0 |
| **Rosário Oeste** | `ROS` | 50 |
| **Jangada** | `JAN` | 100 |
| **Cuiabá** | `CBA` | 120 |
| **Várzea Grande** | `VG` | 125 |
| **Rondonópolis** | `ROND` | 265 |

> **Nota:** A função $h(n)$ é admissível ($h(n) \le h^*(n)$) e consistente, assegurando a otimalidade global do $A^*$.

---

## ⚙️ Algoritmos

### 1. Busca em Largura (BFS)
- **Estratégia:** Explora sistematicamente os vértices nível por nível utilizando uma fila FIFO (`deque`).
- **Objetivo:** Menor quantidade de arestas (saltos).
- **Limitação:** Ignora o custo acumulado em grafos ponderados.

### 2. Busca A\* ($A^*$)
- **Estratégia:** Fila de prioridade com min-heap (`heapq`), avaliada pela função:
  $$f(n) = g(n) + h(n)$$
  - $g(n)$: Custo real acumulado da origem até o nó $n$.
  - $h(n)$: Custo heurístico estimado de $n$ até o destino.
- **Vantagem:** Encontra o menor caminho em quilometragem podando caminhos desnecessários.

---

## 📊 Comparativo de Execução

Origem: **VG (Várzea Grande)** ➔ Destino: **NOB (Nobres)**

| Algoritmo | Trajeto Escolhido | Distância | Nós Expandidos | Eficiência |
| :--- | :--- | :---: | :---: | :---: |
| **BFS** | `VG` ➔ `CBA` ➔ `ROS` ➔ `NOB` | 200 km | 4 | Subótimo em custo |
| **A\*** | `VG` ➔ `JAN` ➔ `ROS` ➔ `NOB` | **185 km** | **3** | **Ótimo** |

### Saída do Terminal:
```bash
largura: ['VG', 'CBA', 'ROS', 'NOB'] 200 km, 4 expandidos
--------------------
A*: ['VG', 'JAN', 'ROS', 'NOB'] 185 km, 3 expandidos
```

## 💻 Como Executar
Pré-requisitos
Python 3.8+ instalado (sem bibliotecas externas necessárias).

### Passo a passo
```bash
# Clone o repositório
git clone https://github.com/WelliksonWester/graph-search-algorithms.git

# Acesse o diretório
cd graph-search-algorithms

# Execute o script
python busca.py
```