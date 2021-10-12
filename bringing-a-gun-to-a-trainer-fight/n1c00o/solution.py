from math import sqrt


def norm(vec):
    # norm of a vector AB = distance between A and B = sqrt((xb - xa)**2 + (yb - ya)**2)
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

    # get mirrors
    mirrors = []
    # todo

    # calculate vectors using our mirrors and inverting coordinates on a mirror
    vectors = []
    # todo

    # validate our vectors
    # Valid vectors norms are lesser or equal to distance (constraints of beam)
    # Valid vectors aren't colinear to shortest_vec (because if it is,
    # either the beam will go through trainer before reaching the mirrored trainer,
    # either the beam will bounce on the wall and touch yourself before reaching the trainer)
    num_valid_vec = 0

    for vec in vectors:
        # if the vector equals shortest_vec, we avoid any computation on it
        if vec == shortest_vec:
            num_valid_vec += 1
            continue

        # Check if the norm of the vector <= distance or not
        if norm(vec) > distance:
            continue

        # verify the vector is not colinear with shortest_vec
        # Two vectors (here u and v) are colinears if there is a real number k we can use to write u = kv
        # In other term, they are colinears if there is a relation of proportionality between vector's coordinates
        k = shortest_vec[0] / vec[0]
        if vec[1] * k == shortest_vec[1]:
            # if true, then vectors are colinear
            continue

        # if the vector passes our tests, then it is valid
        num_valid_vec += 1

    return num_valid_vec
