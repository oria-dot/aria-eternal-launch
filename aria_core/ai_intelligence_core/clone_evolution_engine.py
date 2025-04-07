import random
from loguru import logger

class Clone:
    def __init__(self, id, performance):
        self.id = id
        self.performance = performance

    def mutate(self):
        self.performance += random.uniform(-0.1, 0.2)
        return self

def evolve_clones(clones):
    sorted_clones = sorted(clones, key=lambda c: c.performance, reverse=True)
    top_half = sorted_clones[:len(clones)//2]
    logger.info(f"Top clones: {[c.id for c in top_half]}")

    new_generation = []
    for clone in top_half:
        new_clone = clone.mutate()
        new_clone.id = f"{clone.id}_m"
        new_generation.append(new_clone)
    return top_half + new_generation

if __name__ == "__main__":
    population = [Clone(f"clone_{i}", random.uniform(0.0, 1.0)) for i in range(10)]
    next_gen = evolve_clones(population)
    for c in next_gen:
        logger.info(f"{c.id}: {round(c.performance, 3)}")