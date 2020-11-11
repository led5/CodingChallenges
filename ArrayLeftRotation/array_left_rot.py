def rotLeft(a, d):
    # Result of shifting elements of a by d-units to the left 
    return a[d:] + a[:d]

