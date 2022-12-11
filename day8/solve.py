def main():
    data = parse_file("data.txt")    

    # Part 1
    # Count of 1, 4, 7, 8 i.e. output patterns of length 2, 4, 3, 7 respectively
    pat_count = 0
    for inp, oup in data:
        for el in oup:
            if len(el) in [2, 4, 3, 7]:
                pat_count += 1
    print(f"Answer 1: {pat_count}") # 369

    # Part 2
    pat_sum = 0
    for inp, oup in data:
        digits = deduce_digits(inp)
        pat_sum += int(''.join([digits[''.join(sorted(it))] for it in oup]))
    print(f"Answer 2: {pat_sum}") # 369

# for {0: 'char-seq', 1: 'char-seq' ...} first and swap key-values at the end.
def deduce_digits(inp):
    digits = {}
    it = sorted([''.join(sorted(x)) for x in inp], key=len)
    digits[1] = it.pop(0)
    digits[7] = it.pop(0)
    digits[4] = it.pop(0)
    digits[8] = it.pop()
    while it:
        d = it.pop(0)
        if len(d) == 5 and com_char_len(d, digits[1]) == 2:
            digits[3] = d
        elif len(d) == 5 and com_char_len(d, digits[4]) == 2:
            digits[2] = d            
        elif len(d) == 5 and com_char_len(d, digits[4]) == 3:
            digits[5] = d
        elif len(d) == 6 and com_char_len(d, digits[4]) == 3 and com_char_len(d, digits[7]) == 3:
            digits[0] = d
        elif len(d) == 6 and com_char_len(d, digits[4]) == 3 and com_char_len(d, digits[7]) == 2:
            digits[6] = d
        elif len(d) == 6 and com_char_len(d, digits[4]) == 4 and com_char_len(d, digits[7]) == 3:
            digits[9] = d

    return  {v: str(k) for k, v in digits.items()}

com_char_len = lambda s1, s2: len(''.join([c for c in s1 if c in s2]))

def parse_file(fname):
    result = []
    with open(fname, "r") as file:
        rows = file.read().split('\n')
        for row in rows:
            inp, oup = row.split("|")
            result.append((inp.strip().split(), oup.strip().split()))
    return result

if __name__ == "__main__":
    main()
