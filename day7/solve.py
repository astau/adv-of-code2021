def main():
    data = parse_file("data.txt")

    posi_map = {}
    for d in data:
        if d in posi_map: 
            posi_map[d] += 1
        else:
            posi_map[d] = 1

    # Part 1
    fuels = [(p, calc_fuel(posi_map, p, diff_steps)) for p in posi_map]
    _, min_fuel = find_min(fuels)
    print(f"Answer 1: {min_fuel}") # 347509

    # Part 1
    fuels = [(p, calc_fuel(posi_map, p, sigma_steps)) for p in posi_map]
    _, min_fuel = find_min(fuels)
    print(f"Answer 2: {min_fuel}") # 347509    
         
def find_min(fuels):
    min_fuel = fuels[0][1]
    min_posi = 0
    for i in fuels: 
        if i[1] < min_fuel:
            min_fuel = i[1]
            min_posi = i[0]
    return min_posi, min_fuel

def calc_fuel(posi_map, pos, fn):
    fuel = 0
    for p in posi_map:
        fuel += posi_map[p] * fn(pos, p)
    return fuel

diff_steps = lambda pos, p: abs(pos - p)
sigma_steps = lambda pos, p: int(diff_steps(pos, p) * (diff_steps(pos, p) + 1) / 2)

def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().strip().split(',')
        return [int(x) for x in data]

if __name__ == "__main__":
    main()