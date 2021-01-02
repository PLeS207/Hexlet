def length_of_last_word(line):
    if line.replace("\n", '').replace("\t", '').strip():
        word = line.split()[-1]
        return len(word)
    return 0
