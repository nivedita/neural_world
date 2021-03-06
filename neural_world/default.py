"""
Particular default values of the simulation are put here.

"""
import os
import time

import neural_world.commons as commons
from neural_world.commons import Direction, NeuronType
from neural_world.neighbors import moore, vonneumann


# Stepping
STEP_NUMBER_PER_RUN = 100
WAITING_TIME = 0.1

# Per simulation values
DIR_SIMULATION_ARCHIVE = os.path.join(commons.DIR_ARCHIVES,
                                      'sim_' + str(int(time.time())))

# Neighbors access
NEIGHBOR_ACCESS = moore

# Individual constants
NEIGHBOR_COUNT = len(tuple(NEIGHBOR_ACCESS((0, 0))))
UNIT_TYPE_COUNT = len(('Individual', 'Nutrient'))
MEMORY_MIN_SIZE, MEMORY_MAX_SIZE = 1, 8
INPUT_NEURON_TYPE   = NeuronType.INPUT
OUTPUT_NEURON_TYPE  = NeuronType.OR
INDIVIDUAL_INITIAL_COUNT = 4
INDIVIDUAL_INITIAL_DENSITY = -1  # use count, not density
# Individual creation values
NEURON_INTER_MINCOUNT = 1
NEURON_INTER_MAXCOUNT = 20
NEURON_EDGES_MINCOUNT = 5
NEURON_EDGES_MAXCOUNT = 30

# Global Life
LIFE_DIVISION_MIN_ENERGY = 20

# Nutrient constants
NUTRIENT_ENERGY = 4
NUTRIENT_REGENERATION = 0.001
NUTRIENT_INITIAL_DENSITY = 0.6

# World space constants and refs
SPACE_WIDTH = 20
SPACE_HEIGHT = 20

# Evolution constants
MUTATION_RATE = 0.01
