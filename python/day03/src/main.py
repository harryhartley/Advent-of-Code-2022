def matching_char_2(s1, s2):
    for x in s1:
        if x in s2:
            return x
    return 0

def matching_char_3(s1, s2, s3):
    for x in s1:
        if x in s2 and x in s3:
            return x
    return 0

def char_to_priority(c: str):
    if c == c.lower():
        return ord(c) - 96
    return ord(c) - 38

def group_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def main():
    input = [l.strip('\n') for l in open("../input.txt").readlines()]
    print(f"Silver: {silver(input)}")
    print(f"Gold: {gold(input)}")

def silver(input):
    p = map(lambda l : [l[0:len(l)//2], l[len(l)//2:]], input)
    return sum(char_to_priority(matching_char_2(bag[0], bag[1])) for bag in p)

def gold(input):
    p = list(group_list(input, 3))
    return sum(char_to_priority(matching_char_3(bag[0], bag[1], bag[2])) for bag in p)

main()