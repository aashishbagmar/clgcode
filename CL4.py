import random
from deap import base, creator, tools, algorithms

# Fix randomness for consistent output
random.seed(42)

# Evaluation function (minimize sum of squares)
def eval_func(individual):
    return (sum(x ** 2 for x in individual),)


# Avoid re-creation error (important in Jupyter)
if not hasattr(creator, "FitnessMin"):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
if not hasattr(creator, "Individual"):
    creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize toolbox
toolbox = base.Toolbox()

# Attribute: float values between -5 and 5
toolbox.register("attr_float", random.uniform, -5.0, 5.0)

# Individual: 3 variables
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=3)

# Population
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Operators
toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Create initial population
population = toolbox.population(n=50)

# Evaluate initial population
for ind in population:
    ind.fitness.values = toolbox.evaluate(ind)

# GA parameters
generations = 20

# Run Genetic Algorithm
for gen in range(generations):
    print(f"Generation {gen+1}")

    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    # Evaluate offspring
    for ind in offspring:
        ind.fitness.values = toolbox.evaluate(ind)

    # Select next generation
    population = toolbox.select(offspring, k=len(population))

# Best individual
best_ind = tools.selBest(population, k=1)[0]
best_fitness = best_ind.fitness.values[0]

print("\nBest individual:", best_ind)
print("Best fitness:", best_fitness)
