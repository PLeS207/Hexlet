def chunked(chunk, obj):
    result = []
    step = 0
    while step < len(obj):
        result.append(obj[step:step + chunk])
        step += chunk
    return result


assert chunked(2, ('A', 'B', 'C', 'D')) == [('A', 'B'), ('C', 'D')]
assert chunked(3, ('E', 'F', 'H', 'I')) == [('E', 'F', 'H'), ('I',)]
assert chunked(4, ('G', 'K', 'L', 'M')) == [('G', 'K', 'L', 'M')]
assert chunked(4, []) == []
assert chunked(2, ('N',)) == [('N',)]
assert chunked(2, ('A', 'B', 'C', 'D', 'E', 'F')) == [('A', 'B'), ('C', 'D'), ('E', 'F')]