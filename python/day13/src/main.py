import json


def compare(p1, p2, lenl, lenr):
    while True:
        try: l, r = next(p1), next(p2)
        except StopIteration:
            if lenl == lenr: return
            return True if lenl < lenr else False
        if isinstance(l, int) and isinstance(r, int):
            if l < r: return True
            if l > r: return False
        elif isinstance(l, list) and isinstance(r, list):
            res = compare(iter(l), iter(r), len(l), len(r))
            if res is not None: return res
        elif (isinstance(l, list) and isinstance(r, int)) or (isinstance(l, int) and isinstance(r, list)):
            if isinstance(l, int): res = compare(iter([l]), iter(r), 1, len(r))
            else: res = compare(iter(l), iter([r]), len(l), 1)
            if res is not None: return res

def main():
    pairs_silver = [x.strip().split('\n') for x in open("../input.txt").read().strip().split('\n\n')]
    pairs_gold = list(map(json.loads, filter(None, [x.strip() for x in open("../input.txt").readlines()])))
    
    print(f'Silver: {silver(pairs_silver)}')
    print(f'Gold: {gold(pairs_gold)}')

def silver(pairs):
    correct_order = list()
    for i, p in enumerate(pairs):
        p1, p2 = json.loads(p[0]), json.loads(p[1])
        correct_order.append(i+1 if compare(iter(p1), iter(p2), len(p1), len(p2)) else 0)
    return sum(correct_order)

def gold(pairs):
    div1, div2 = [[[2]], [[6]]]
    pairs.extend([div1, div2])        
    prev = list()
    while True:
        if pairs == prev: break
        prev = pairs.copy()
        for i in range(len(pairs)-1):
            l, r = pairs[i], pairs[i+1]
            res = compare(iter(pairs[i]), iter(pairs[i+1]), len(pairs[i]), len(pairs[i+1]))
            if not res:
                pairs[i] = r
                pairs[i+1] = l
    return (pairs.index(div1)+1) * (pairs.index(div2)+1)

if __name__ == "__main__":
    main()