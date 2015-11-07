"""
Basical implementation of a terminal view for World object.

"""
import neural_world.commons as commons
from neural_world.individual import Individual
from neural_world.nutrient import Nutrient


LOGGER = commons.logger()


class TerminalWorldView:
    def __init__(self, engine):
        self.engine = engine
        self.graphics = {
            Nutrient: '·',
            Individual: '#',
        }


    def update(self, world, *args, **kwargs):
        """Print World in the terminal"""
        x_prev, line = 0, ''
        for coords, objects in world.ordered_objects:
            x, y = coords
            if x_prev != x:
                x_prev = x
                print('|', line, '|')
                line = ''
            if len(objects) > 0:
                if any(isinstance(o, Individual) for o in objects):
                    line += self.graphics[Individual]
                else:
                    line += self.graphics[Nutrient]
            else:
                line += ' '

