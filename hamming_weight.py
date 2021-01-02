def hamming_weight(number):
    count = 0
    for i in bin(number)[2:]:
        if '1' in i:
            count += 1
    return count

