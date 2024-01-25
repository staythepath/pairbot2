import shelve
from random import sample
from math import inf

MATCHING_HISTORY = shelve.open("matching_history.shelve")


def gen_rand_matching(members):
    perm = sample(members, len(members))
    matching = list(zip(perm[::2], pair[1::2]))
    return matching

def score_pair(pair):
    return 1 / MATCHING_HISTORY.get(pair, inf)

def score_matching(matching):
    return sum(score_pair(pair) ** 2 for pair in matching)

def gen_okay_matching(members, iters=1000):
    assert len(members) % 2 == 0
    return max((gen_rand_matching(members) for _ in range(iters)), key=score_matching)

def update_history(matching):
    for key in MATCHING_HISTORY:
        MATCHING_HISTORY[key] += 1
    for key in matching:
        MATCHING_HISTORY[key] = MATCHING_HISTORY[key[::-1]] = 1

def main():
    members = [...]
    matching = gen_okay_matching(members)
    update_history(matching)
    print("Matched Members:", matching)