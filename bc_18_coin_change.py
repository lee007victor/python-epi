# Make changes resulting in the minimum number of coins
def change_making(cents):
    coins = (100, 50, 25, 10, 5, 1)
    ret = 0
    for n in coins:
        ret += cents / n
        cents %= n
    return ret
