"""

usage:
    __main__.py [options]

options:
    -h, --help          print this help
    -v, --version       print version
    --log-level=LEVEL   log level used for terminal output   [default: warning]
    --render-png=BOOL   activate png files generation        [default: 1]


"""
import time
import docopt
from functools import partial

import neural_world.actions as action
from neural_world import commons
from neural_world.info import VERSION
from neural_world.config import Configuration
from neural_world.engine import Engine
from neural_world.prompt import Prompt
from neural_world.observer import (Archivist, TerminalWorldView, TreeBuilder)


LOGGER = commons.logger()


if __name__ == '__main__':
    # CLI arguments handling
    args = docopt.docopt(__doc__, version=VERSION)
    commons.log_level(args['--log-level'])
    render_png = bool(int(args['--render-png']))

    # Configuration
    config = Configuration()
    assert config.is_valid()

    # Observers
    v = TerminalWorldView
    a = partial(Archivist, archive_directory=config.dir_archive_simulation,
                render_graph=render_png)
    t = partial(TreeBuilder, archive_directory=config.dir_archive_simulation,
                render_graph=render_png)

    # Engine from rules
    e = Engine.generate_from(config, observers=(v, a, t))

    # Initialize the world
    e.world.populate()
    prompt = Prompt(config, e)

    # Main loop
    try:
        while not config.terminated:
            prompt.input()
            e.apply(config)

            if not e.world.have_life:
                # try again, life !
                for _ in range(config.init_indiv_count):
                    e.add(action.AddAction(config.incubator.spawn()))
                e.world.step_number = 0

    except (KeyboardInterrupt, EOFError):
        LOGGER.info('Treatment loop finished through keyboard interruption.')
    e.world.deinit()
    LOGGER.info('Deinitialization of World')
