import random
import time
from collections import defaultdict

# ──────────────────────────────────────────
# SERVER SETUP
# ──────────────────────────────────────────

servers = [
    {"id": "Server1", "weight": 1, "connections": 0, "response_time": 0.1},
    {"id": "Server2", "weight": 2, "connections": 0, "response_time": 0.2},
    {"id": "Server3", "weight": 3, "connections": 0, "response_time": 0.15},
]

# ──────────────────────────────────────────
# ALGORITHMS
# ──────────────────────────────────────────

# 1. Round Robin
rr_index = 0

def round_robin(request_id):
    global rr_index
    server = servers[rr_index % len(servers)]
    rr_index += 1
    return server["id"]

# 2. Weighted Round Robin
wrr_sequence = []

for s in servers:
    wrr_sequence.extend([s["id"]] * s["weight"])

wrr_index = 0

def weighted_round_robin(request_id):
    global wrr_index
    server = wrr_sequence[wrr_index % len(wrr_sequence)]
    wrr_index += 1
    return server

# 3. Least Connections
def least_connections(request_id):
    server = min(servers, key=lambda s: s["connections"])
    server["connections"] += 1
    return server["id"]

# 4. Least Response Time
def least_response_time(request_id):
    server = min(servers, key=lambda s: s["response_time"])
    return server["id"]

# 5. IP Hashing
def ip_hashing(client_ip):
    hash_val = sum(int(part) for part in client_ip.split("."))
    server = servers[hash_val % len(servers)]
    return server["id"]

# ──────────────────────────────────────────
# SIMULATE REQUESTS
# ──────────────────────────────────────────

def simulate(algorithm_name, algorithm_func, num_requests=10):

    print(f"\n{'='*45}")
    print(f" Algorithm: {algorithm_name}")
    print(f"{'='*45}")

    distribution = defaultdict(int)

    for i in range(1, num_requests + 1):

        client_ip = f"192.168.1.{random.randint(1, 20)}"

        if algorithm_name == "IP Hashing":
            assigned = algorithm_func(client_ip)
        else:
            assigned = algorithm_func(i)

        distribution[assigned] += 1

        print(f" Request {i:02d} | Client IP: {client_ip} → {assigned}")

    print(f"\n Distribution Summary:")

    for server, count in distribution.items():
        print(f" {server}: {count} requests")

# ──────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────

if __name__ == "__main__":

    print("\n*** Load Balancing Simulation ***")
    print(f"Servers: {[s['id'] for s in servers]}")
    print(f"Weights: {[s['weight'] for s in servers]}")

    simulate("Round Robin", round_robin)
    simulate("Weighted Round Robin", weighted_round_robin)
    simulate("Least Connections", least_connections)
    simulate("Least Response Time", least_response_time)
    simulate("IP Hashing", ip_hashing)

    print("\n*** Simulation Complete ***\n")