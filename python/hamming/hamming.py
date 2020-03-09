def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands length does not match.')

    distance_count = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            distance_count += 1

    return distance_count

