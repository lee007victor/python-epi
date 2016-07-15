# The knapsack problem.
def optimum_knapsack(items, cap):
    res = [[-1] * (cap + 1) for _ in range(len(items))]
    return solver(items, len(items) - 1, cap, res)

def solver(items, k, cap, res):
    if k < 0:
        return 0
    if res[k][cap] == -1:
        wo_cur = solver(items, k - 1, cap, res)
        w_cur = (0 if items[k][0] > cap else 
                 items[k][1] + solver(items, k - 1, cap - items[k][0], res))
        res[k][cap] = max(wo_cur, w_cur)
    print res
    return res[k][cap]

# Test.
case = [
    (5, 60),
    (3, 50),
    (4, 70),
    (2, 30),
    ]
print optimum_knapsack(case, 5)
