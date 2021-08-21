def shortest_path(graph, start, target):
    
    path = []
    visited = []
    temp_parents = {}
    to_visit = [start]
    distances = {key : float("inf") for key in graph.get_vertices()}
    distances[start] = 0
    final_distance = 0

    while to_visit:
        current = min([(distances[vertex], vertex) for vertex in to_visit])[1]
        if current == target:
            break
        visited.append(current)
        to_visit.remove(current)
        for neighbour, distance in graph.get_neighbors()[current].items():
            if neighbour in visited:
                continue
            vertex_distance = distances[current] + distance
            if vertex_distance < distances[neighbour]:
                distances[neighbour] = vertex_distance
                temp_parents[neighbour] = current
                to_visit.append(neighbour)

    final_distance = distances[target]
    if target not in temp_parents:
        return []
    while target:
        path.append(target)
        target = temp_parents.get(target)
    return path[::-1] + [final_distance]
