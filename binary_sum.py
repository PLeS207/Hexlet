def binary_sum(number1, number2):
    num1 = int(number1, 2)
    num2 = int(number2, 2)
    bin_sum = bin(num1 + num2)
    return bin_sum[2:]
