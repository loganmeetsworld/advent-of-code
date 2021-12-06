from collections import defaultdict

from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    days = 80 if level == 1 else 256

    # Create a new dictionary to act as a tracker with a default value of 0 (no fishies at that reproduction stage)
    # This tracker will have days until reproduction as keys, and number of fishies with that reproduction stage as values
    tracker = defaultdict(lambda: 0)

    # Add our input, which is a list of days until each fish will reproduce
    for days_until_reproduction in problem_input.split(','):
        tracker[days_until_reproduction] += 1

    reset_stage = '6'
    new_life_stage = '8'
    reproducing_stage = '0'
    while days > 0:
        new_day_tracker = {}
        # In each new day up to day 7 we move fishies up one to a new reproduction stage (those at day 8 will move back to 0)
        for i in range(8):
            new_day_tracker[str(i)] = tracker[str(i + 1)]
        
        # The number of fishies reproducing that day get added, and parent fishies reset
        new_day_tracker[reset_stage] += tracker[reproducing_stage]
        # Baby fishies start life at the beginning stage of reproduction, so any babies get moved to the start
        new_day_tracker[new_life_stage] = tracker[reproducing_stage]

        # Set the tracker to our new day and move forward a day
        tracker = new_day_tracker
        days -= 1

    # Add up all the fishies at various reproduction stages
    return sum(tracker.values())


aoc_utils.run(answer, cases)
