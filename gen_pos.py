import json
import random


output_filename = 'positions.json'
objects_count = 100
limit = 5


def random_position():
    return (
        random.randint(-limit, limit),
        random.randint(-limit, limit),
        random.randint(-limit, limit)
    )


if __name__ == '__main__':
    positions = []
    for i in range(objects_count):
        start = random_position()
        end = random_position()
        positions.append((start, end))


    with open(output_filename, 'w') as f:
        f.write(json.dumps(positions))

