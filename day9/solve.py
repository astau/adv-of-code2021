def main():
    data = parse_file("data.txt")
    dep = len(data)
    wid = len(data[0])
    # Part 1 Low points
    low_points = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_low(data[i][j], get_hv_points(data, i, j, dep, wid)):
                low_points.append((i, j))
    ans = 0
    for p in low_points:
        ans += (data[p[0]][p[1]] + 1)
    print(f"Answer 1: {ans}") # 600

    #Part 2 Low Basins
    basins = []
    for p in low_points:
        x, y = p[0], p[1]
        basins.append(form_basin(data, x, y, dep, wid))
    basins = sorted(basins, key=len, reverse=True)
    print(f"Answer 2: {len(basins[0]) * len(basins[1]) * len(basins[2])}") #987840
    
def form_basin(data, i, j, dep, wid):
    res = [(i, j)]
    pts = get_hv_points(data, i, j, dep, wid)
    for p in pts:
        if data[i][j] < p[0] < 9:
            res.append((p[1], p[2]))
            res.extend(form_basin(data, p[1], p[2], dep, wid))
    return set(res)


def is_low(p, pts):
    lc = [1 for x in pts if x[0] > p]
    return sum(lc) == len(pts)

def get_hv_points(data, i, j, dep, wid):
    res = [ (get_point(data, i+1, j, dep, wid), i+1, j), 
            (get_point(data, i-1, j, dep, wid) , i-1, j), 
            (get_point(data, i, j+1, dep, wid) , i, j+1), 
            (get_point(data, i, j-1, dep, wid), i, j-1)
        ]    
    return [x for x in res if x[0] != None]

def get_point(data, i, j, dep, wid):
    return data[i][j] if 0 <= i < dep and 0 <= j < wid else None
    
def parse_file(fname):
    result = []
    with open(fname, "r") as file:
        rows = file.read().split('\n')
        for row in rows:
            result.append([int(i) for i in row])
    return result

if __name__ == "__main__":
    main()