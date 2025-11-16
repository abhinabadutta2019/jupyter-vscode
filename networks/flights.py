from pathlib import Path
import networkx as nx


def load_flights():
    # Find flights.txt relative to this file
    here = Path(__file__).resolve().parent
    data_path = here.parent / "data" / "flights.txt"

    G = nx.DiGraph()

    with open(data_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            # Safety: if line is too short, skip
            if len(parts) < 3:
                continue

            # columns in your file look like:
            # 0: !ROUTE_ID   1: SRC   2: DST   3: AIRCRAFT ...
            route_id = parts[0]
            src = parts[1]
            dst = parts[2]

            # Skip “dummy” rows with ZZZZ (your first header lines)
            if src == "ZZZZ" or dst == "ZZZZ":
                continue

            # Remove the leading "!" from codes if you want
            src = src.lstrip("!")
            dst = dst.lstrip("!")

            G.add_edge(src, dst, route=route_id.lstrip("!"))

    print(f"Loaded {G.number_of_nodes()} airports")
    print(f"Loaded {G.number_of_edges()} routes")
    return G
