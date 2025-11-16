# run.py

from networks.flights import load_flights

if __name__ == "__main__":
    G = load_flights()
    print(G)
