with open('p022_names.txt') as f:
    text = f.read()

total = 0

for i, qname in enumerate(sorted(text.split(','))):
    name = qname.strip()[1:-1]
    score = 0
    for c in name:
        score += ord(c) - ord('A') + 1
    total += score * (i + 1)

print(total)
