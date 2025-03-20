import math

# ----- 1) All Node & Road Data in a Single Array -----
NODES_DATA = [
    {
        "name": "PondsideAve.:QuackSt",
        "x": 28,
        "y": 329,
        "connections": [
            {"neighbor": "MigrationAve.:QuackSt.", "distance": 301},
            {"neighbor": "BreadcrumbAve.:WaddleWay", "distance": 404},
            {"neighbor": "PondsideAve.:WaddleWay", "distance": 223}
        ]
    },
    {
        "name": "MigrationAve.:QuackSt.",
        "x": 29,
        "y": 135,
        "connections": [
            {"neighbor": "PondsideAve.:QuackSt", "distance": 301},
            {"neighbor": "AquaticAve.:WaddleWay", "distance": 277},
            {"neighbor": "MigrationAve.:WaddleWay", "distance": 146}
        ]
    },
    {
        "name": "AquaticAve.:WaddleWay",
        "x": 129,
        "y": 29,
        "connections": [
            {"neighbor": "MigrationAve.:QuackSt.", "distance": 277},
            {"neighbor": "MigrationAve.:WaddleWay", "distance": 153},
            {"neighbor": "AquaticAve.:WaterfoulWay", "distance": 128}
        ]
    },
    {
        "name": "MigrationAve.:WaddleWay",
        "x": 129,
        "y": 135,
        "connections": [
            {"neighbor": "AquaticAve.:WaddleWay", "distance": 153},
            {"neighbor": "MigrationAve.:QuackSt.", "distance": 146},
            {"neighbor": "PondsideAve.:WaddleWay", "distance": 212},
            {"neighbor": "MigrationAve.:WaterfoulWay", "distance": 124}
        ]
    },
    {
        "name": "PondsideAve.:WaddleWay",
        "x": 157,
        "y": 266,
        "connections": [
            {"neighbor": "MigrationAve.:WaddleWay", "distance": 212},
            {"neighbor": "PondsideAve.:QuackSt", "distance": 223},
            {"neighbor": "BreadcrumbAve.:WaddleWay", "distance": 298},
            {"neighbor": "PondsideAve.:WaterfoulWay", "distance": 95}
        ]
    },
    {
        "name": "BreadcrumbAve.:WaddleWay",
        "x": 181,
        "y": 459,
        "connections": [
            {"neighbor": "PondsideAve.:WaddleWay", "distance": 298},
            {"neighbor": "PondsideAve.:QuackSt", "distance": 404},
            {"neighbor": "BreadcrumbAve.:TheCircle", "distance": 214}
        ]
    },
    {
        "name": "AquaticAve.:WaterfoulWay",
        "x": 213,
        "y": 29,
        "connections": [
            {"neighbor": "AquaticAve.:WaddleWay", "distance": 128},
            {"neighbor": "MigrationAve.:WaterfoulWay", "distance": 158},
            {"neighbor": "AquaticAve.:FeatherSt.", "distance": 133}
        ]
    },
    {
        "name": "MigrationAve.:WaterfoulWay",
        "x": 213,
        "y": 135,
        "connections": [
            {"neighbor": "AquaticAve.:WaterfoulWay", "distance": 158},
            {"neighbor": "MigrationAve.:WaddleWay", "distance": 124},
            {"neighbor": "PondsideAve.:WaterfoulWay", "distance": 160},
            {"neighbor": "MigrationAve.:FeatherSt.", "distance": 138}
        ]
    },
    {
        "name": "PondsideAve.:WaterfoulWay",
        "x": 214,
        "y": 241,
        "connections": [
            {"neighbor": "MigrationAve.:WaterfoulWay", "distance": 160},
            {"neighbor": "PondsideAve.:WaddleWay", "distance": 95},
            {"neighbor": "TheCircle:WaterfoulWay", "distance": 174},
            {"neighbor": "PondsideAve.:FeatherSt.", "distance": 136}
        ]
    },
    {
        "name": "TheCircle:WaterfoulWay",
        "x": 273,
        "y": 307,
        "connections": [
            {"neighbor": "PondsideAve.:WaterfoulWay", "distance": 174},
            {"neighbor": "TheCircle:FeatherSt.", "distance": 55},
            {"neighbor": "BreadcrumbAve.:TheCircle", "distance": 179}
        ]
    },
    {
        "name": "AquaticAve.:FeatherSt.",
        "x": 305,
        "y": 29,
        "connections": [
            {"neighbor": "AquaticAve.:WaterfoulWay", "distance": 133},
            {"neighbor": "MigrationAve.:FeatherSt.", "distance": 161},
            {"neighbor": "AquaticAve.:BeckSt.", "distance": 218}
        ]
    },
    {
        "name": "MigrationAve.:FeatherSt.",
        "x": 305,
        "y": 135,
        "connections": [
            {"neighbor": "AquaticAve.:FeatherSt.", "distance": 161},
            {"neighbor": "MigrationAve.:WaterfoulWay", "distance": 138},
            {"neighbor": "PondsideAve.:FeatherSt.", "distance": 148},
            {"neighbor": "MigrationAve.:BeckSt.", "distance": 218}
        ]
    },
    {
        "name": "PondsideAve.:FeatherSt.",
        "x": 305,
        "y": 233,
        "connections": [
            {"neighbor": "MigrationAve.:FeatherSt.", "distance": 148},
            {"neighbor": "PondsideAve.:WaterfoulWay", "distance": 136},
            {"neighbor": "TheCircle:FeatherSt.", "distance": 95},
            {"neighbor": "PondsideAve.:BeckSt.", "distance": 219}
        ]
    },
    {
        "name": "TheCircle:FeatherSt.",
        "x": 305,
        "y": 296,
        "connections": [
            {"neighbor": "PondsideAve.:FeatherSt.", "distance": 95},
            {"neighbor": "TheCircle:WaterfoulWay", "distance": 55},
            {"neighbor": "DabblerDr.:TheCircle", "distance": 96}
        ]
    },
    {
        "name": "AquaticAve.:BeckSt.",
        "x": 452,
        "y": 29,
        "connections": [
            {"neighbor": "AquaticAve.:FeatherSt.", "distance": 218},
            {"neighbor": "MigrationAve.:BeckSt.", "distance": 156},
            {"neighbor": "MigrationAve.:MallardSt.", "distance": 343}
        ]
    },
    {
        "name": "MigrationAve.:BeckSt.",
        "x": 452,
        "y": 135,
        "connections": [
            {"neighbor": "AquaticAve.:BeckSt.", "distance": 156},
            {"neighbor": "MigrationAve.:FeatherSt.", "distance": 218},
            {"neighbor": "PondsideAve.:BeckSt.", "distance": 149},
            {"neighbor": "MigrationAve.:MallardSt.", "distance": 194}
        ]
    },
    {
        "name": "PondsideAve.:BeckSt.",
        "x": 452,
        "y": 233,
        "connections": [
            {"neighbor": "MigrationAve.:BeckSt.", "distance": 149},
            {"neighbor": "PondsideAve.:FeatherSt.", "distance": 219},
            {"neighbor": "DabblerDr.:BeckSt.", "distance": 89},
            {"neighbor": "PondsideAve.:MallardSt.", "distance": 197}
        ]
    },
    {
        "name": "DabblerDr.:BeckSt.",
        "x": 452,
        "y": 293,
        "connections": [
            {"neighbor": "PondsideAve.:BeckSt.", "distance": 89},
            {"neighbor": "DabblerDr.:TheCircle", "distance": 173},
            {"neighbor": "DrakeDr.:BeckSt.", "distance": 160},
            {"neighbor": "DabblerDr.:MallardSt.", "distance": 192}
        ]
    },
    {
        "name": "DrakeDr.:BeckSt.",
        "x": 452,
        "y": 402,
        "connections": [
            {"neighbor": "DabblerDr.:BeckSt.", "distance": 160},
            {"neighbor": "DucklingDr.:BeckSt.", "distance": 92},
            {"neighbor": "DrakeDr.:MallardSt.", "distance": 250}
        ]
    },
    {
        "name": "DucklingDr.:BeckSt.",
        "x": 452,
        "y": 474,
        "connections": [
            {"neighbor": "DrakeDr.:BeckSt.", "distance": 92},
            {"neighbor": "TailAve.:BeckSt.", "distance": 15},
            {"neighbor": "DucklingDr.:MallardSt.", "distance": 371}
        ]
    },
    {
        "name": "TailAve.:BeckSt.",
        "x": 452,
        "y": 465,
        "connections": [
            {"neighbor": "DucklingDr.:BeckSt.", "distance": 15},
            {"neighbor": "TailAve.:TheCircle", "distance": 227}
        ]
    },
    {
        "name": "MigrationAve.:MallardSt.",
        "x": 585,
        "y": 135,
        "connections": [
            {"neighbor": "AquaticAve.:BeckSt.", "distance": 343},
            {"neighbor": "MigrationAve.:BeckSt.", "distance": 194},
            {"neighbor": "PondsideAve.:MallardSt.", "distance": 145}
        ]
    },
    {
        "name": "PondsideAve.:MallardSt.",
        "x": 585,
        "y": 233,
        "connections": [
            {"neighbor": "MigrationAve.:MallardSt.", "distance": 145},
            {"neighbor": "PondsideAve.:BeckSt.", "distance": 197},
            {"neighbor": "DabblerDr.:MallardSt.", "distance": 89}
        ]
    },
    {
        "name": "DabblerDr.:MallardSt.",
        "x": 585,
        "y": 293,
        "connections": [
            {"neighbor": "PondsideAve.:MallardSt.", "distance": 89},
            {"neighbor": "DabblerDr.:BeckSt.", "distance": 192},
            {"neighbor": "DrakeDr.:MallardSt.", "distance": 100},
            {"neighbor": "DucklingDr.:MallardSt.", "distance": 96}
        ]
    },
    {
        "name": "DrakeDr.:MallardSt.",
        "x": 576,
        "y": 354,
        "connections": [
            {"neighbor": "DabblerDr.:MallardSt.", "distance": 100},
            {"neighbor": "DrakeDr.:BeckSt.", "distance": 250}
        ]
    },
    {
        "name": "DucklingDr.:MallardSt.",
        "x": 593,
        "y": 354,
        "connections": [
            {"neighbor": "DabblerDr.:MallardSt.", "distance": 96},
            {"neighbor": "DucklingDr.:BeckSt.", "distance": 371}
        ]
    },
    {
        "name": "BreadcrumbAve.:TheCircle",
        "x": 284,
        "y": 393,
        "connections": [
            {"neighbor": "TheCircle:WaterfoulWay", "distance": 179},
            {"neighbor": "BreadcrumbAve.:WaddleWay", "distance": 214},
            {"neighbor": "TailAve.:TheCircle", "distance": 92}
        ]
    },
    {
        "name": "TailAve.:TheCircle",
        "x": 335,
        "y": 387,
        "connections": [
            {"neighbor": "DabblerDr.:TheCircle", "distance": 109},
            {"neighbor": "BreadcrumbAve.:TheCircle", "distance": 92},
            {"neighbor": "TailAve.:BeckSt.", "distance": 277}
        ]
    },
    {
        "name": "DabblerDr.:TheCircle",
        "x": 350,
        "y": 324,
        "connections": [
            {"neighbor": "TheCircle:FeatherSt.", "distance": 96},
            {"neighbor": "TailAve.:TheCircle", "distance": 109},
            {"neighbor": "DabblerDr.:BeckSt.", "distance": 173}
        ]
    },
]

NODE_COORDS = {}
MAP_GRAPH   = {}

for entry in NODES_DATA:
    node_name = entry["name"]
    x_coord   = entry["x"]
    y_coord   = entry["y"]
    NODE_COORDS[node_name] = (x_coord, y_coord)
    
    MAP_GRAPH[node_name] = []
    for conn in entry["connections"]:
        neighbor = conn["neighbor"]
        dist     = conn["distance"]
        MAP_GRAPH[node_name].append((neighbor, dist))

def heuristic(node_a, node_b):
    (x1, y1) = NODE_COORDS[node_a]
    (x2, y2) = NODE_COORDS[node_b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def a_star_search(start_node, goal_node):
    open_set = {start_node}
    came_from = {}
    
    g_score = {node: float('inf') for node in MAP_GRAPH}
    g_score[start_node] = 0.0
    
    f_score = {node: float('inf') for node in MAP_GRAPH}
    f_score[start_node] = heuristic(start_node, goal_node)
    
    while open_set:
        current = min(open_set, key=lambda n: f_score[n])
        if current == goal_node:
            return reconstruct_path(came_from, current)
        
        open_set.remove(current)
        for (neighbor, edge_cost) in MAP_GRAPH[current]:
            tentative_g = g_score[current] + edge_cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal_node)
                open_set.add(neighbor)
    
    return []

def find_nearest_node(x, y):
    min_dist = float('inf')
    nearest = None
    for node, (nx, ny) in NODE_COORDS.items():
        dist = math.hypot(nx - x, ny - y)
        if dist < min_dist:
            min_dist = dist
            nearest = node
    return nearest

if __name__ == "__main__":
    start = "PondsideAve.:QuackSt"
    goal_x, goal_y = 585, 135

    goal_node = find_nearest_node(goal_x, goal_y)
    print(f"Nearest node to ({goal_x}, {goal_y}) is: {goal_node}")

    path = a_star_search(start, goal_node)
    if path:
        print(f"Full path from '{start}' to '{goal_node}':")
        print(" -> ".join(path))
    else:
        print("No path found.")
