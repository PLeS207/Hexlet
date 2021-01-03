def is_degenerated(line):
    if line[0] == line[1]:
        return True
    return False


def is_vertical(line):
    if line[0][0] == line[1][0] and line[0][1] != line[1][1]:
        return True
    return False


def is_horizontal(line):
    if line[0][1] == line[1][1] and line[0][0] != line[1][0]:
        return True
    return False


def is_inclined(line):
    if line[0][1] != line[1][1] and line[0][0] != line[1][0]:
        return True
    return False


line1 = (0, 10), (100, 130)
print(is_degenerated(line1))
print(is_vertical(line1))
line2 = (42, 1), (42, 2)
print(is_vertical(line2))
line3 = (100, 50), (200, 50)
print(is_horizontal(line3))