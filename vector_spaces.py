import itertools
import numpy as np


def generate_code(q, n):
    """
    Parameters
    -----------
    q : prime int
        a field over q, the alphabet
    n : int
        length of codewords

    Returns
    --------
    list of codewords of length n over finite field q
    """
    code = list(itertools.product(list(range(q)), repeat=n))
    return np.array(code)


def get_spanning_set(set, q):
    span = []
    rows = set.shape[0]
    cols = set.shape[1]
    multipliers = list(itertools.product(list(range(q)), repeat=rows))
    multipliers = np.array(multipliers)
    for m in multipliers:
        m = m.reshape(1, rows)
        s = np.mod(np.dot(m, set),q)
        if s.tolist() not in span:
            span.append(s.tolist())
    return span


def get_orthogonal_set(set, q):
    orthog_set = []
    rows = set.shape[0]
    cols = set.shape[1]

    # Get list of all codewords in set
    full_set = np.array(generate_code(q, cols))
    for possible_orthog in full_set:
        is_orthogonal = True
        for s in set:
            x = np.mod(np.dot(possible_orthog, s),q)
            if x != 0:
                is_orthogonal = False
                break
        if is_orthogonal:
            orthog_set.append(possible_orthog.tolist())
    return orthog_set


if __name__=='__main__':
    set = np.array([[0,0,1,0,1],[1,1,0,0,1],[1,1,0,1,1]])
    span = get_spanning_set(set, 2)
    ortho = get_orthogonal_set(set, 2)
    print(span, '\n', ortho)
