from pathlib import Path
import csv
import networkx as nx

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "flights.txt"

def load_flights():
    G = nx.Graph()

    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        # If your file is comma-separated, use delimiter=","
        reader = csv.reader(f)

        # If there is a header, read it and figure out columns
        header = next(reader)
        # Example: source in col 0, destination in col 1
        # Adjust these indices after you inspect the file!
        src_idx = 0
        dst_idx = 1

        for row in reader:
            # skip empty/bad rows
            if len(row) <= max(src_idx, dst_idx):
                continue

            src = row[src_idx].strip()
            dst = row[dst_idx].strip()
            if not src or not dst:
                continue

            G.add_edge(src, dst)

    print(f"Loaded {G.number_of_nodes()} airports")
    print(f"Loaded {G.number_of_edges()} routes")
    return G
