from pathlib import Path
import networkx as nx

def load_flights():
    """
    Loads flights.txt from the data/ folder and returns a graph.
    Assumes each line is: source destination
    Example:
        JFK LAX
        LAX SFO
    """

    # Path to project root
    ROOT = Path(__file__).resolve().parent.parent
    file = ROOT / "data" / "flights.txt"

    edges = []
    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                u, v = parts
                edges.append((u, v))

    G = nx.Graph()
    G.add_edges_from(edges)

    print("Loaded", len(G.nodes()), "airports")
    print("Loaded", len(G.edges()), "routes")

    return G
