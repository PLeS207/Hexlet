# BEGIN (write your solution here)
def rotate_left(triple):
    rotate = triple[1:] + triple[:1]
    return tuple(rotate)


def rotate_right(triple):
    rotate = triple[-1:] + triple[:-1]
    return tuple(rotate)


tpl = ('A', 'B', 'C')
print(rotate_left(tpl))
print(rotate_right(tpl))
