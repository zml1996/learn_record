

def ss(piles):
    if len(piles) == 2:
        return max(piles)
    max_nums=max(ss(piles[1:]) + piles[0], ss(piles[:-1]) + piles[-1])
    print(max_nums,'----')
    return max_nums

piles=[5,3,4,5]
sums=sum(piles)
print(ss(piles))




