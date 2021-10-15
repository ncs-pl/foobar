import math

# My biggest quality is being able to search on google :)


def get_mirror_coordinates(size, pos, rel_cg, layer_count):
    [w, h] = size
    (px, py) = pos

    dxR = (w-px)*2
    dxL = px*2
    x = [px-rel_cg[0]]*(layer_count*2+1)
    for i in range(layer_count+1, layer_count*2+1):
        x[i] = x[i-1]+dxR if (i-layer_count-1) % 2 == 0 else x[i-1]+dxL
    for i in range(layer_count-1, -1, -1):
        x[i] = x[i+1]-dxL if (layer_count-1-i) % 2 == 0 else x[i+1]-dxR

    dyU = (h-py)*2  # 275-100=175*2=350
    dyD = py*2
    y = [py-rel_cg[1]]*(layer_count*2+1)
    for i in range(layer_count+1, layer_count*2+1):
        y[i] = y[i-1]+dyU if (i-layer_count-1) % 2 == 0 else y[i-1]+dyD
    for i in range(layer_count-1, -1, -1):
        y[i] = y[i+1]-dyD if (layer_count-1-i) % 2 == 0 else y[i+1]-dyU

    return x, y


def solution(dimensions, your_position, trainer_position, distance):
    player_pos = (your_position[0], your_position[1])
    trainer_pos = (trainer_position[0], trainer_position[1])
    min_d = min(dimensions)
    layer_count = (distance//min_d)+1

    px, py = get_mirror_coordinates(
        dimensions, player_pos, player_pos, layer_count)
    tx, ty = get_mirror_coordinates(
        dimensions, trainer_pos, player_pos, layer_count)

    angle_dist = {}

    for _x in px:
        for _y in py:
            if (_x == 0 and _y == 0):
                continue
            d = math.hypot(_y, _x)
            if d <= distance:
                beam = math.atan2(_y, _x)
                if beam in angle_dist:
                    if d < angle_dist[beam]:
                        angle_dist[beam] = d
                else:
                    angle_dist[beam] = d

    res = set()
    for _x in tx:
        for _y in ty:
            d = math.hypot(_y, _x)
            if d <= distance:
                beam = math.atan2(_y, _x)
                if beam in angle_dist:
                    if d < angle_dist[beam]:
                        angle_dist[beam] = d
                        # res.add((_x,_y))
                        res.add(beam)
                        # print(f'({player_pos[0]+_x},{player_pos[1]+_y})')
                else:
                    angle_dist[beam] = d
                    res.add(beam)
                    # print(f'({player_pos[0]+_x},{player_pos[1]+_y})')
    # print(res)
    return len(res)
