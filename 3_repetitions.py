dna = input()

max_count = 0
cur_count = 0
current_char = ''

for char in dna:
    if char == current_char:
        cur_count += 1
    else:
        max_count = max(cur_count, max_count)
        current_char = char
        cur_count = 1

if cur_count > max_count:
    max_count = cur_count

print(max_count)