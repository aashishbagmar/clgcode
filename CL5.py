import numpy as np
import random

# Fix randomness (important for same output)
random.seed(42)
np.random.seed(42)

# Distance matrix
distance_matrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

num_cities = len(distance_matrix)

# ACO Parameters
num_ants = 10
num_iterations = 50
alpha = 1        # pheromone importance
beta = 2         # visibility importance
evaporation_rate = 0.5
Q = 100          # pheromone constant

# Initialize pheromone matrix
pheromone = np.ones((num_cities, num_cities))

# Visibility matrix (avoid division by zero)
visibility = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            visibility[i][j] = 1 / distance_matrix[i][j]

best_route = None
best_distance = float('inf')

# ACO Algorithm
for iteration in range(num_iterations):
    all_routes = []
    all_distances = []

    for ant in range(num_ants):
        start_city = random.randint(0, num_cities - 1)
        route = [start_city]
        visited = set(route)

        # Build route
        while len(route) < num_cities:
            current_city = route[-1]
            probabilities = []

            for city in range(num_cities):
                if city not in visited:
                    tau = pheromone[current_city][city] ** alpha
                    eta = visibility[current_city][city] ** beta
                    probabilities.append((city, tau * eta))

            # Convert to probabilities
            cities, probs = zip(*probabilities)
            probs = np.array(probs)
            probs = probs / probs.sum()

            # Select next city
            next_city = np.random.choice(cities, p=probs)
            route.append(next_city)
            visited.add(next_city)

        # Return to start
        route.append(route[0])

        # Calculate distance
        distance = 0
        for i in range(len(route) - 1):
            distance += distance_matrix[route[i]][route[i + 1]]

        all_routes.append(route)
        all_distances.append(distance)

        # Update best solution
        if distance < best_distance:
            best_distance = distance
            best_route = route

    # Evaporation
    pheromone = (1 - evaporation_rate) * pheromone

    # Update pheromone
    for route, distance in zip(all_routes, all_distances):
        for i in range(len(route) - 1):
            a, b = route[i], route[i + 1]
            pheromone[a][b] += Q / distance
            pheromone[b][a] += Q / distance

# Final Output
print("Best Route:", best_route)
print("Shortest Distance:", best_distance)

