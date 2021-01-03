def fizz_buzz(begin, end):
    string = ""
    if begin == end:
        return str(begin)
    for i in range(begin, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            i = 'FizzBuzz'
        elif i % 3 == 0 and i % 5 != 0:
            i = 'Fizz'
        elif i % 5 == 0 and i % 3 != 0:
            i = 'Buzz'
        string += str(i) + " "
    return string.rstrip()


print(fizz_buzz(1, 5))
