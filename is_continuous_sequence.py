# BEGIN (write your solution here)
def is_continuous_sequence(items):
    if len(items) > 1:
        for i in range(len(items) - 1):
            if items[i] + 1 != items[i + 1]:
                return False
        return True
    return False
# END


print(is_continuous_sequence([0, 1, 2, 3]))