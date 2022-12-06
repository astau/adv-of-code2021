def main():
    data = parse_file("data.txt")

    e_len = len(data[0])
    d_len = len(data)

    # Part 1
    gamma = [0] * e_len
    epsilon = [0] * e_len
    for i in range(e_len):
        gamma[i], epsilon[i]  = common_bits(data, i)        
    gamma_int = int(''.join(str(i) for i in gamma), 2)
    epsilon_int = int(''.join(str(i) for i in epsilon), 2)
    print("Answer 1: ", gamma_int * epsilon_int, sep="") # 2261546

    # Part 2
    oxy_data = data.copy()
    co2_data = data.copy()
    for i in range(e_len):
        most, _ = common_bits(oxy_data, i)
        _, least = common_bits(co2_data, i)
        if len(oxy_data) > 1:
            oxy_data = filterby_bitindex(oxy_data, i, most)
        if len(co2_data) > 1:
            co2_data = filterby_bitindex(co2_data, i, least)

    oxy_int = int(''.join(str(i) for i in oxy_data), 2)
    co2_int = int(''.join(str(i) for i in co2_data), 2)

    print("Answer 2: ", oxy_int * co2_int, sep="") # 6775520

# return counts 1s, 0s
def count_bits(data, index): 
    ones = sum([int(d[index]) for d in data])             
    return ones, len(data) - ones

# return most, least common
def common_bits(data, index): 
    ones, zeroes = count_bits(data, index)
    if ones >= zeroes:
        return 1, 0  
    else: 
        return 0, 1 

def filterby_bitindex(data, index, bit):
    b = str(bit)
    return [x for x in data if x[index] == b]    

def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().split('\n')
        result = []
        for d in data:
            result.append(d.strip())
    return result

if __name__ == "__main__":
    main()