def is_power_of_three(number):
    if number % 3 == 0 or number == 1:
        while True:
            if number == 1:
                return True
            number /= 3
            if number < 1:
                return False
    return False

