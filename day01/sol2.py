count_zero = 0
pos = 50

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        dir = line[0]
        val = int(line[1:])

        for v in range(val):
            if dir == "L":
                pos = (pos-1) % 100
            else: 
                pos = (pos+1) % 100

            if pos == 0:
                count_zero += 1

print(count_zero)