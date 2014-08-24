# find all python n-liners
# n hard-coded
n = 3

import glob

for fn in glob.iglob('*.py'):
    with open(fn) as f:
        if sum(1 for line in f if line.strip() and line.strip()[0:1] != '#') <= n:
            print(fn)
            f.seek(0)
            print(f.read())
            print('    - * -    ')
