from enum import Enum

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


class Zone(Enum):
  NOZONE=0
  Pedestrian=1
  Risk=2
  School=3
  Residential=4
  Shops=5
  Industrial=6

class State(Enum):
  Wait=0
  Forward=1
  TurnR=2
  TurnL=3
  RoundAbout=4
  Park=5

# temp class while waiting for long term decision
class Node:
  def __init__(self):
    pass

CURRENT_ZONE=Zone.NOZONE
CURRENT_STATE=State.Wait
NEXT_STATE=State.Wait
