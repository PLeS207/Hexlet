def diff(anl1, anl2):
    angle = (anl1, anl2)
    anl1 = max(angle)
    anl2 = min(angle)
    if anl2 < 180 < anl1 < 360:
        result = 360 - abs(anl2 - anl1)
    else:
        result = abs(anl1 - anl2)
    if result >= 360:
        while result >= 360:
            result -= 360
    return result
