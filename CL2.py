import random
from deap import base, creator, tools, algorithms

# Define evaluation function (replace with real NN training + validation)
def evaluate(individual):
    # Example: individual = [neurons, layers]
    neurons, layers = individual

    # Mock fitness (lower is better since FitnessMin)
    # Replace this with actual model error (e.g., MSE)
    fitness = (neurons * 0.01 + layers * 0.1) + random.random()

    return (fitness,)


# Genetic algorithm parameters
POPULATION_SIZE = 10
GENERATIONS = 5

# Avoid redefinition error (important in notebooks)
if not hasattr(creator, "FitnessMin"):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
if not hasattr(creator, "Individual"):
    creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize toolbox
toolbox = base.Toolbox()

# Define attributes (hyperparameters)
toolbox.register("attr_neurons", random.randint, 1, 100)  # neurons
toolbox.register("attr_layers", random.randint, 1, 5)     # layers

# Individual = [neurons, layers]
toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.attr_neurons, toolbox.attr_layers), n=1)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Genetic operators
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=[1, 1], up=[100, 5], indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Create initial population
population = toolbox.population(n=POPULATION_SIZE)

# Evaluate initial population
for ind in population:
    ind.fitness.values = toolbox.evaluate(ind)

# Run the genetic algorithm
for gen in range(GENERATIONS):
    print(f"\n--- Generation {gen+1} ---")

    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.2)

    # Evaluate offspring
    fitnesses = map(toolbox.evaluate, offspring)
    for ind, fit in zip(offspring, fitnesses):
        ind.fitness.values = fit

    # Select next generation
    population = toolbox.select(offspring, k=len(population))

# Get best individual
best_individual = tools.selBest(population, k=1)[0]

print("\nBest Parameters Found:")
print("Neurons:", best_individual[0])
print("Layers:", best_individual[1])
print("Fitness Value:", best_individual.fitness.values[0])
