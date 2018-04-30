import itertools
import random


def hamming_dist(x, y, d):
    """
    Parameters
    -----------
    x : string
        a codeword
    y : string
        a codeword the same length as x
    dist : int
        checked hamming distance
    Returns
    --------
    True if x and y have a hamming distance have d
    """
    if len(x) != len(y):
        print('x and y should be same length')
        return

    count = 0
    for i in range(len(x)):
        # check for differences
        if(x[i] != y[i]):
            count+=1
    return count>=d


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
    alphabet = ''
    for i in range(q):
        alphabet = alphabet+str(i)
    all_codewords = list(itertools.product(alphabet, repeat=n))
    code = [''.join(i) for i in all_codewords]
    return code


def create_n_d_code(q, n, d, randomize=False):
    """
    Creates a (n,d) code over finite field q.

    Parameters
    -----------
    q : prime int
        a field over q. This creates the code alphabet
    n : int
        length of codewords in code
    d : int
        minimum distance of code
    randomize : boolean
        generates code based off random codeword instead of starting with the
        0 vector

    Returns
    -------
    list : (n,d) code over finite field q
    """
    all_code = generate_code(q, n)

    if randomize:
        random.shuffle(all_code)

    # Start with first element
    new_code = [all_code[0]]

    # Brute force code generation method
    for potential_codeword in all_code[1:]: # skip first word
        is_min_distance = True
        for codeword in new_code:
            if not hamming_dist(potential_codeword, codeword, d):
                is_min_distance = False
                break
        if is_min_distance:
            new_code.append(potential_codeword)

    return new_code

if __name__=='__main__':
    #print(generate_code(2, 6))
    #print(create_n_d_code(3, 4, 3))
    print(create_n_d_code(2, 6, 3))
    
