from vector_spaces import generate_code
import numpy as np


def get_cosets(q, n, code):
    code_over_field = generate_code(q, n)
    cosets = []

    for c in code_over_field:
        coset = []
        for codeword in code:
            coset.append(codeword+c)
        cosets.append(coset)

    cosets = np.mod(np.array(cosets), q)
    return cosets


def get_syndromes(coset_leaders, H, q):
    syndromes = []
    for c in coset_leaders:
        syndromes.append(np.dot(c, np.transpose(H)))
    syndromes = np.mod(np.array(syndromes), q)
    return syndromes


def decode_message(message, H, syndromes, q):
    syndrome = np.mod(np.dot(message, np.transpose(H)),q)
    return syndrome


if __name__=='__main__':
    #a = np.array([[0,0,0,0],[0,1,1,1],[0,2,2,2],[1,0,1,2],[1,1,2,0],[1,2,0,1],[2,0,2,1],[2,1,0,2],[2,2,1,0]])
    H = np.array([[2,2,1,0],[1,2,0,1]])
    #b = np.array([[0,0,0,0], [1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]])
    #print(get_syndromes(b, H, 3))
    encoded_msg = np.array([[2,1,0,2]])
    #print(decode_message(encoded_msg, H, 0, 3))
    G = np.array([[1,0,1,2],[0,1,1,1]])
    print(decode_message_2(encoded_msg, G, 3))
