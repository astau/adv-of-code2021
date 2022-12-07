import re
def main():
    
    # Part 1 for horizontal or vertical lines
    lines = parse_file("data.txt")
    points_map = {}
    for ln in lines:
        x1, y1, x2, y2 = ln
        if x1 == x2 or y1 == y2: 
            pts = line_to_points(x1, y1, x2, y2) 
            for p in pts:
                if p in points_map:
                    points_map[p] += 1
                else:
                    points_map[p] = 1    
    points_overlap = [p for p in points_map if points_map[p] >= 2]
    print(f"Answer 1: {len(points_overlap)}") # 5306

    # Part 2 for horizontal, vertical and diagnol lines
    lines = parse_file("data.txt")
    points_map = {}
    for ln in lines:
        x1, y1, x2, y2 = ln
        if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2): 
            pts = line_to_points(x1, y1, x2, y2) 
            for p in pts:
                if p in points_map:
                    points_map[p] += 1
                else:
                    points_map[p] = 1    
    points_overlap = [p for p in points_map if points_map[p] >= 2]
    print(f"Answer 2: {len(points_overlap)}") # 17787

def line_to_points(x1, y1, x2, y2):
    x = int((x2-x1)/abs(x1-x2)) if abs(x1-x2) != 0 else 0 # -1, 0, or 1
    y = int((y2-y1)/abs(y1-y2)) if abs(y1-y2) != 0 else 0 # -1, 0, or 1
    result = []
    while not (x1 == x2 and y1 == y2):
        result.append((x1, y1))
        x1, y1 = x1 + x, y1 + y
    result.append((x1, y1)) # last pair
    return result
        

def parse_file(fname):
    result = []
    pattern = re.compile(r'(\d+)')
    with open(fname, "r") as file:
        data = file.read().split('\n')
        for line in data:
            result.append((int(i) for i in pattern.findall(line)))
    return result

if __name__ == "__main__":
    main()