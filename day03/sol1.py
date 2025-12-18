total_joltage = 0

with open('input.txt') as f:
    for banks in f:
        first_dig = 0
        sec_dig = 0
        banks = banks.strip()
        num = banks[0:]
        for i in num[:-1]:
            if int(first_dig) < int(i):
                first_dig = i
                first_idx = num.find(first_dig)
        new_banks = [int(num_) for num_ in num[first_idx+1:]]
        for j in new_banks:
            if int(sec_dig) < int(j):
                sec_dig = j
        joltage = f'{first_dig}{sec_dig}'
        total_joltage += int(joltage)
                        
print(total_joltage)