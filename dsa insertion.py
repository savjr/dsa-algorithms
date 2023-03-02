def insertionsort(seq):
    indexing_length = range(1, len(seq))
    for i in indexing_length:
        value = seq[i]

        while seq[i-1] > value and i > 0:
            seq[i], seq[i-1] = seq[i-1], seq[1]
            i = i -1

    return seq


print(insertionsort([1, 2, 4, 36, 475, 75,
                     4, 776, 56, 776, 5, 36134, 5, 46653]))
