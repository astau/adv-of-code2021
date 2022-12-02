def main():
    data = parse_file("data.txt")
    
    # Part 1 -- Ans 1524750
    x = y = 0
    for d in data:
        v = int(d[1])
        match d[0]:
            case "forward":
                x += v
            case "down":
                y += v
            case "up":
                y -= v

    print(f"Answer 1: {x * y}") # 1524750

    # Part 2
    x = y = aim = 0
    for d in data:
        v = int(d[1])
        match d[0]:
            case "forward":
                x += v
                y += (aim * v)
            case "down":
                aim += v
            case "up":
                aim -= v
    print(f"Answer 2: {x * y}") # 

def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().split('\n')
        result = []
        for d in data:
            result.append(tuple(d.split()))
    return result

main()