def main():
    data = parse_file("data.txt")
    
    e_len = len(data[0])
    d_len = len(data)

    # Part 1
    gamma = [0] * e_len
    epsilon = []
    for i in range(e_len):
        gamma[i] = common_bit(data, i)
        epsilon.append(int(not gamma[i]))    
    gamma_int = int(''.join(str(i) for i in gamma), 2)
    epsilon_int = int(''.join(str(i) for i in epsilon), 2)
    print("Answer 1: ", gamma_int * epsilon_int, sep="") # 2261546

    # Part 2
    oxy_data = data.copy()
    i = 0    
    while len(oxy_data) > 1 and i < e_len:
        oxy_data = filterby_bitindex(oxy_data, i, str(common_bit(oxy_data, i)))
        i += 1
    oxy_int = int(''.join(str(i) for i in oxy_data), 2)

    co2_data = data.copy()
    i = 0    
    while len(co2_data) > 1 and i < e_len:
        co2_data = filterby_bitindex(co2_data, i, str(int(not common_bit(co2_data, i))))
        i += 1
    co2_int = int(''.join(str(i) for i in co2_data), 2)    
    
    print("Answer 2: ", oxy_int * co2_int, sep="") # 



def common_bit(data, index):
    ones = 0
    for d in data:
        if d[index] == '1':
            ones += 1
    return 1 if ones > len(data) - ones else 0

def filterby_bitindex(data, index, bit):
    return [x for x in data if x[index] == bit]    

def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().split('\n')
        result = []
        for d in data:
            result.append(d.strip())
    return result

main()