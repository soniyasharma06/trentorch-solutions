def is_subset(a, b):
    return a.issubset(b)

        


def argmax(values):
    """
    values: a non-empty list or tuple of numbers

    Returns:
        The INDEX of the largest value in values. If multiple values are
        tied for the maximum, return the first such index.
    """
    # TODO: Implement argmax from Theory: scan once, tracking the best
    # value and its index, updating only on a strictly larger value.
    best_index = 0
    best_value = values[0]
    for i, v in enumerate(values):
        if v > best_value:
            best_value = v
            best_index = i
    return best_index
