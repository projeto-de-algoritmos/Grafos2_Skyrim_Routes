import pandas as pd
from flask import Flask, json, render_template,request

from graphclass import Graph
from dijkstra import shortest_path

df = pd.read_csv('./static/NodesSkyrim.csv')
edges = []

for i, row in df.iterrows():
    edges.append((row.Origem, row.Destino, row.Peso))


grafo = Graph(edges=edges, directed=False)

path = shortest_path(grafo, 'Solitude', 'Dushnikh Yal')

print(path)
