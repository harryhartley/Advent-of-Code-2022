def main():
    with open('../input.txt', 'r') as f: input = f.read()
    parsed_input = [line.split("\n") for line in input.split("\n\n")]
    print(f"Silver: {silver(parsed_input)}")
    print(f"Gold: {gold(parsed_input)}")

def silver(input):
    def sum_strings(string_list):
        int_list = map(lambda x : int(x), string_list)
        return sum(int_list)
    sums = map(sum_strings, input)
    return sorted(sums)[-1]

def gold(input):
    def sum_strings(string_list):
        int_list = map(lambda x : int(x), string_list)
        return sum(int_list)
    sums = map(sum_strings, input)
    return sum(sorted(sums)[-3:])

main()