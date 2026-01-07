invalid_ids = 0

with open("input.txt") as f:
    for line in f:
        line = line.split(",")
        for ids in line:
            start, end = ids.split("-")
            for i in range(int(start), int(end) + 1):
                if len(str(start)) % 2 == 0 or len(str(end)) % 2 == 0:
                    s = str(i)
                    n = len(s)
                    for l in range(1, n // 2 + 1):
                        if n % l == 0:
                            m = s[:l]
                            count_rep = n // l
                            new_s = m * count_rep
                            if new_s == s:
                                s_split = len(s) // 2
                                l_s = s[:s_split]
                                r_s = s[s_split:]
                                if l_s == r_s:
                                    invalid_ids += int(s)   
                                    break
                else:
                    pass

print(invalid_ids)