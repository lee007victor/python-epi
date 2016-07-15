# The towers of Hanoi problem

def compute_tower_hanoi(num_rings):
    pegs = [list(range(1, num_rings + 1)), [], []]
    helper(num_rings, pegs, 0, 1, 2)

def helper(num_rings, pegs, src, dst, mid):
    if num_rings > 0:
        helper(num_rings - 1, pegs, src, mid, dst)
        pegs[dst].append(pegs[src].pop())
        helper(num_rings - 1, pegs, mid, dst, src)
