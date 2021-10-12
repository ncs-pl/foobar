from math import sqrt


def norm(vec):
    """
    Return the norm of a vector
    """
    return sqrt(vec[0]**2 + vec[1]**2)


def solution(dimensions, your_position, trainer_position, distance):
    # shortest vector between you and the trainer
    shortest_vec = [trainer_position[0] - your_position[0],
                    trainer_position[1] - your_position[1]]
    shortest_vec_norm = norm(shortest_vec)

    # If the norm of the sortest vector between you and the trainer is greater than distance,
    # then there is no solution
    if shortest_vec_norm > distance:
        return 0
    # if the norm of the shortest vector is equal to the distance, then there is only this solution
    elif shortest_vec_norm == distance:
        return 1

    # Beginning of the algorithm...
    # The goal is to mirror the room given thanks to dimensions and then calculate all vectors between `your` in the original room
    # and the replicated trainer.
    # We make replicas using x, y, d and e where
    # x is the horizontal axis
    # y is the vertical axis
    # d is the line parallel to x which goes through (0; dimensions[1]) to (dimensions[0]; dimensions[1])
    # e is the line parallel to y which goes through (dimensions[0]; 0) to (dimensions[0]; dimensions[1])
    # After making our mirrors and getting our vectors, we calculate the norm of these and if the norm is lesser than distance
    # then it is a valid one

    num_valid_vec = 0

    return num_valid_vec
