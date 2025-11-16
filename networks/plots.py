# networks/plots.py

import random
import networkx as nx
import matplotlib.pyplot as plt


def compare_ws_er(N=100, K=6, seed=42):
    """
    Compare Watts-Strogatz WS (p=1) and Erdős–Rényi ER graphs.
    Draws both graphs side by side.
    """

    random.seed(seed)

    # WS graph with p=1 (every edge rewired)
    G_ws = nx.watts_strogatz_graph(N, K, 1.0)

    # ER graph with p = K/(N-1)
    p = K / (N - 1)
    G_er = nx.erdos_renyi_graph(N, p, seed=seed)

    # Draw both graphs
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    nx.draw_circular(G_ws, ax=axes[0], node_size=30)
    axes[0].set_title("WS Model (p=1)")

    nx.draw_spring(G_er, ax=axes[1], node_size=30)
    axes[1].set_title(f"ER Model (p={p:.3f})")

    plt.tight_layout()
    plt.show()
