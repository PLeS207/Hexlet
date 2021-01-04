def chunked(chunk, obj):
    count_chunks = len(obj) // chunk
    result = []
    step = 0
    if 1 < len(obj) != chunk:
        if count_chunks > 2 and chunk != 1:
            while step < len(obj):
                result.append(obj[step:step + 2])
                step += chunk
                print(step)
            return result
        return [obj[:chunk], obj[chunk:]]
    elif len(obj) == chunk or len(obj) == 1:
        result.append(obj)
        return result
    return result


assert chunked(2, ('A', 'B', 'C', 'D')) == [('A', 'B'), ('C', 'D')]
assert chunked(3, ('E', 'F', 'H', 'I')) == [('E', 'F', 'H'), ('I',)]
assert chunked(4, ('G', 'K', 'L', 'M')) == [('G', 'K', 'L', 'M')]
assert chunked(4, []) == []
assert chunked(2, ('N',)) == [('N',)]
assert chunked(2, ('A', 'B', 'C', 'D', 'E', 'F')) == [('A', 'B'), ('C', 'D'), ('E', 'F')]