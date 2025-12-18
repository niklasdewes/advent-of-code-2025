total_joltage = 0
max_len = 12

with open('input.txt') as f:
    for banks in f:
        stack = []
        banks = banks.strip()
        num = banks[0:]
        if len(num) <= max_len:
            continue
        elif len(num) > max_len:
            diff = len(num) - max_len
            for i in num:
                while stack and stack[-1] < i and diff > 0:
                    stack.pop()
                    diff -= 1
                stack.append(i)
        total_joltage += int("".join(stack[:max_len]))
                
print(total_joltage)