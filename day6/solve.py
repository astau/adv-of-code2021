def main():
    data = parse_file("data.txt")

    count = 0
    fish_map = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for d in data:
        fish_map[d] += 1

    for day in range(256):
        newf = fish_map[0]
        for i in range(1, 9):
            fish_map[i-1] = fish_map[i]
        fish_map[6] += newf
        fish_map[8] = newf

        # Part 1 - 80 days    
        if day == 79:
            count = sum(list(fish_map.values()))
            print(f"Answer 1: {count}") # 391888
        
        # Part 2 - 256 days    
        if day == 255:
            count = sum(list(fish_map.values()))
            print(f"Answer 2: {count}")  # 1754597645339      

def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().strip().split(',')
        return [int(x) for x in data]

if __name__ == "__main__":
    main()