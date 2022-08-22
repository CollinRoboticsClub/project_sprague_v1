def clamp(value, min, max):
    return max(min(value, max), min)

def map(value, inMin, inMax, outMin, outMax):
    """Scales values linearly, like Arduino map()"""
    
    """
    >>> map(75, 50, 100, 0, 100)

    >>> inScale = 100 - 50 = 50
    >>> outScale = 100 - 0 = 100

    >>> from0to1 = (75 - 50) / 50 = 25/50 = 1/2

    >>> return 1/2 * 100 = 50 # YUH
    """

    inScale = inMax - inMin
    outScale = outMax - outMin
    
    from0to1 = (value - inMin) / inScale

    return from0to1 * outScale