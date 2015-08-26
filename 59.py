import operator, functools, itertools, string, file, enable1
text = tuple(map(int, file.read('p059_cipher.txt').split(',')))
s = max(map(''.join, itertools.product(string.ascii_lowercase, repeat=3)), key=lambda s: sum(1 for x in ''.join(itertools.starmap(lambda i, y: chr(int(y) ^ ord(s[i % 3])), enumerate(text))).split() if enable1.isword(x)))
print(sum(itertools.starmap(lambda i, y: int(y) ^ ord(s[i % 3]), enumerate(text))))
