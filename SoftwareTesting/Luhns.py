def digits_of(number):
    return [int(i) for i in str(number)]

def luhn_checksum(card_number):
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(digits_of(2 * digit))
    return total % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def test(N):
    count = 0
    for i in range(N/10+1, N):
        if is_luhn_valid(i):
            print i
            
            count += 1
    print count, 'perc:', count*1.0/N

N = 1E2
test(int(N))
# 9%
