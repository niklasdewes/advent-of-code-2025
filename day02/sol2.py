invalid_ids = 0

with open("input.txt") as f:
    for line in f:
        line = line.split(",")
        for ids in line:
            start, end = ids.split("-")
            for i in range(int(start), int(end) + 1):
                s = str(i)
                n = len(s)
                for l in range(1, n // 2 + 1):
                    if n % l == 0:
                        m = s[:l]
                        count_rep = n // l
                        new_s = m * count_rep
                        if new_s == s:
                            invalid_ids += int(s)   
                            break

print(invalid_ids)