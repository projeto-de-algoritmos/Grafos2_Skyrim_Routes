import pandas as pd
import os
import time
from flask import Flask, json, render_template,request
import cv2

from graphclass import Graph
from dijkstra import shortest_path

app = Flask(__name__, template_folder='front')

app.config['UPLOAD_FOLDER'] = "./static/"

df = pd.read_csv('./static/NodesSkyrim.csv')
edges = []

for i, row in df.iterrows():
    edges.append((row.Origem, row.Destino, row.Peso))

graph = Graph(edges=edges, directed=False)

def position_finder(paths):
    positions = pd.read_csv('./static/positions.csv')
    result = []

    for i,city in enumerate(paths[:-1]):
        if i < len(paths[:-1]) - 1:
            current = positions.query(f"city == '{city}'")
            the_next = positions.query(f"city == '{paths[i+1]}'")
            first = (int(current['width']), int(current['heigth']))
            second = (int(the_next['width']), int(the_next['heigth']))
            result.append((first, second))
    return result

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        vertices = graph.get_vertices()
        return render_template("index.html",vertices=vertices)
    else:
        start = str(request.form.get('start')).replace("_"," ")
        target = str(request.form.get('target')).replace("_"," ")

        path = shortest_path(graph, start,target)

        image = cv2.imread('./static/images/city.jpg')

        points = position_finder(path)

        for i in points:
            cv2.line(image, i[0], i[1], (0,0,255), 2)

        new_image_name = "path_" + str(time.time()) + ".png"

        for filename in os.listdir('./static/images/'):
            if filename.startswith('path_'):  
                os.remove('./static/images/' + filename)

        cv2.imwrite("./static/images/" + new_image_name, image)
        return render_template('result.html', path=path[:-1], start = start, \
                target = target, image = "./static/images/" + new_image_name)


app.run(debug=True)
