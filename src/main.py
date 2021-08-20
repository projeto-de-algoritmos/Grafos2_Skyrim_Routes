import pandas as pd
from flask import Flask, json, render_template,request

from graphclass import Graph
from dijkstra import shortest_path

app = Flask(__name__,template_folder='../front')

df = pd.read_csv('./static/NodesSkyrim.csv')
edges = []

for i, row in df.iterrows():
    edges.append((row.Origem, row.Destino, row.Peso))


grafo = Graph(edges=edges, directed=False)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        vertices = grafo.get_vertices()
        return render_template("index.html",vertices=vertices)
    else:
        pass
        # target = str(request.form.get('target')).replace("_"," ")
        # dependent = get_dependents(grafo, target)
        # # dependent[0] = [i for i in dependent[0] if i != '']
        #
        # if '' in dependent[0]:
        #     dependent[0] = ['Nenhuma matéria' for i in dependent[0] if i == '']
        #
        # if '' in dependent[1]:
        #     for i,value in enumerate(dependent[1]):
        #         if value == '':
        #             delete_element(dependent[1],i )
        #
        # dependencie = get_dependencies(grafo, target)
        # return render_template('list.html', target=target, dependent=dependent, dependencies=dependencie)

app.run(debug=True)
