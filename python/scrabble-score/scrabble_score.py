letter_vals = '''A, E, I, O, U, L, N, R, S, T---1
D, G---2
B, C, M, P---3
F, H, V, W, Y---4
K---5
J, X---8
Q, Z---10'''

clean_vals = [[c.split(', ') for c in r.split('---')] for r in letter_vals.split('\n')] 

LETTER_VALS = {}

for r in clean_vals:
    for l in r[0]:
        LETTER_VALS[l] = int(r[1][0])
        LETTER_VALS[l.lower()] = int(r[1][0])

def score(word):
    return sum([LETTER_VALS[w] for w in word])
