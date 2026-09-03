from collections import deque
import heapq

grafo = {
    "VG": [("CBA", 10), ("JAN", 60)],
    "CBA": [("VG", 10), ("ROS", 130), ("ROND", 215)],
    "JAN": [("VG", 60), ("ROS", 65)],
    "ROS": [("CBA", 130), ("JAN", 65), ("NOB", 60)],
    "ROND": [("CBA", 215)],
    "NOB": [("ROS", 60)],
}

h = {"VG": 125, "CBA": 120, "JAN": 100, "ROS": 50, "ROND": 265, "NOB": 0}

def busca_largura(inicio, objetivo):
    fronteira = deque([[inicio]])
    descobertos = {inicio: True}
    expandidos = 0
    while fronteira:
        caminho = fronteira.popleft()
        atual = caminho[-1]
        if atual == objetivo:
            return caminho, expandidos

        expandidos += 1
        for vizinho, km in grafo[atual]:
            if vizinho not in descobertos:
                descobertos[vizinho] = True
                fronteira.append(caminho + [vizinho])

def custo(caminho):
    total = 0
    i = 0
    while i < len(caminho) -1:
        for vizinho, km in grafo[caminho[i]]:
            if vizinho == caminho[i + 1]:
                total += km

        i += 1

    return total

def a_estrela(inicio, objetivo):
    fila = [(h[inicio], 0, [inicio])] # (h, g, caminho]) = estimativa, gasto, custo
    expandidos = {}
    while fila:
        f, g, caminho = heapq.heappop(fila)
        atual = caminho[-1]
        if atual == objetivo:
            return caminho, g, len(expandidos)

        if atual in expandidos:
            continue

        expandidos[atual] = True

        for vizinho, km in grafo[atual]:
            novo_g = g + km
            heapq.heappush(fila, (novo_g + h[vizinho], novo_g, caminho + [vizinho]))

rota, gastos = busca_largura("VG", "NOB")

print("largura:", rota, custo(rota), "km,", gastos, "expandidos")

print("-" * 20)

rota2, km2, gastos2 = a_estrela("VG", "NOB")
print("A*:", rota2, km2, "km,", gastos2, "expandidos")