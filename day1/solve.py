def main():
    data = parse_file("data.txt")
    
    # Part 1
    inc_count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            inc_count += 1
    print(f"Answer 1 {inc_count}") # 1462

    # Part 2
    inc_count = 0
    for i in range(3, len(data)):
        if sum(data[i-2:i+1]) > sum(data[i-3:i]):
            inc_count += 1
    print(f"Answer 2 {inc_count}") #1497



def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().split('\n')
        result = []
        for d in data:
            result.append(int(d.strip()))
    return result


main()