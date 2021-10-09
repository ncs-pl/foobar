import math


def get_distance(vec):
    return math.sqrt(vec[0]**2 + vec[1]**2)


def solution(dimensions, your_position, trainer_position, distance):
    # Verify that we can reach the trainer
    dist_to_trainer = get_distance(
        (trainer_position[0] - your_position[0], trainer_position[1] - your_position[10]))
    if dist_to_trainer > distance:
        # Unreachable
        return 0
