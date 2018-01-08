def min_dir(d_n, d_w, d_nw):
    direc = set()  # Empty set
    if d_n == min(d_n, d_w, d_nw):
        direc.add('N')
    if d_w == min(d_n, d_w, d_nw):
        direc.add('W')
    if d_nw == min(d_n, d_w, d_nw):
        direc.add('NW')
    return min(d_n, d_w, d_nw), direc


def lev(a, b):
    """
    Calculate the Levenshtein distance. Iterative implementation.
    :param a: Sequence a
    :param b: Sequence b
    :return: Returns the score and Levenshtein distance and the backtracking matrix
    """
    m = len(a)
    n = len(b)

    # let 'd' be the distance matrix of size i+1 x j+1
    # let 'd_b' be the backtracking matrix of size i+1 x j+1

    d = dict()
    d[(0, 0)] = 0

    d_b = dict()
    d_b[(0, 0)] = set()  # Empty set

    for i in range(1, m + 1):
        d[(i, 0)] = i
        d_b[(i, 0)] = {'N'}
    for j in range(1, n + 1):
        d[(0, j)] = j
        d_b[(0, j)] = {'W'}

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:  # Python count is different (starting at 0 instead of 1)
                s = 0
            else:
                s = 1
            d[(i, j)], d_b[(i, j)] = min_dir(d[(i - 1, j)] + 1,
                                             d[(i, j - 1)] + 1,
                                             d[(i - 1, j - 1)] + s)

    return d[(i, j)], d_b


# The following block of code checks for three examples if the results of the function levenshtein() are correct.

edit_distance, d_b = lev(a="cats", b="cats")
if edit_distance == 0:
    print ("'cats' vs 'cats'\t[Correct]")
else:
    print ("'cats' vs 'cats'\t[Wrong]")

edit_distance, d_b = lev(a="cats", b="kats")
if edit_distance == 1:
    print ("'cats' vs 'kats'\t[Correct]")
else:
    print ("'cats' vs 'kats'\t[Wrong]")

edit_distance, d_b = lev(a="cats", b="kittens")
if edit_distance == 5:
    print ("'cats' vs 'kittens'\t[Correct]")
else:
    print ("'cats' vs 'kittens'\t[Wrong]")

edit_distance, d_b = (lev(a="browncats", b="yellowkats"))
print ("'browncats' vs 'yellowkats': ", edit_distance)


