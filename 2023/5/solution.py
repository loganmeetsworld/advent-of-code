from aoc_utils import aoc_utils
from tests import cases

import re

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def answer(problem_input, level, test=False):
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light =  {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}

    seeds, s2s, s2f, f2w, w2l, l2t, t2h, h2l = [re.findall("\d+", i) for i in problem_input.split("\n\n")]

    for mapping in chunks(s2s, 3):
        x = list(range(int(mapping[0]), int(mapping[0]) + int(mapping[2])))
        y = list(range(int(mapping[1]), int(mapping[1]) + int(mapping[2])))
        for i in range(int(mapping[2])):
            seed_to_soil[y[i]] = x[i]

    for mapping in chunks(s2f, 3):
        x = list(range(int(mapping[0]), int(mapping[0]) + int(mapping[2])))
        y = list(range(int(mapping[1]), int(mapping[1]) + int(mapping[2])))
        for i in range(int(mapping[2])):
            soil_to_fertilizer[y[i]] = x[i]

    for mapping in chunks(f2w, 3):
        x = list(range(int(mapping[0]), int(mapping[0]) + int(mapping[2])))
        y = list(range(int(mapping[1]), int(mapping[1]) + int(mapping[2])))
        for i in range(int(mapping[2])):
            fertilizer_to_water[y[i]] = x[i]

    for mapping in chunks(w2l, 3):
        x = list(range(int(mapping[0]), int(mapping[0]) + int(mapping[2])))
        y = list(range(int(mapping[1]), int(mapping[1]) + int(mapping[2])))
        for i in range(int(mapping[2])):
            water_to_light[y[i]] = x[i]

    for mapping in chunks(l2t, 3):
        x = list(range(int(mapping[0]), int(mapping[0]) + int(mapping[2])))
        y = list(range(int(mapping[1]), int(mapping[1]) + int(mapping[2])))
        for i in range(int(mapping[2])):
            light_to_temperature[y[i]] = x[i]

    for mapping in chunks(t2h, 3):
        x = list(range(int(mapping[0]), int(mapping[0]) + int(mapping[2])))
        y = list(range(int(mapping[1]), int(mapping[1]) + int(mapping[2])))
        for i in range(int(mapping[2])):
            temperature_to_humidity[y[i]] = x[i]

    for mapping in chunks(h2l, 3):
        x = list(range(int(mapping[0]), int(mapping[0]) + int(mapping[2])))
        y = list(range(int(mapping[1]), int(mapping[1]) + int(mapping[2])))
        for i in range(int(mapping[2])):
            humidity_to_location[y[i]] = x[i]

    locations = []
    for seed in seeds:
        soil = seed_to_soil.get(int(seed), int(seed))
        fertilizer = soil_to_fertilizer.get(soil, soil)
        water = fertilizer_to_water.get(fertilizer, fertilizer)
        light = water_to_light.get(water, water)
        temperature = light_to_temperature.get(light, light)
        humidity = temperature_to_humidity.get(temperature, temperature)
        location = humidity_to_location.get(humidity, humidity)
        locations.append(location)

    return min(locations)


aoc_utils.run(answer, cases)
