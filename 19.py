cday = 1 # monday
def month(n, year):
    if n in (9, 4, 6, 11):
        return 30
    if n != 2:
        return 31
    if year % 4 != 0:
        return 28
    if year % 400 == 0 or year % 100 != 0:
        return 29
nsundays = 0
for monn in range(12, 100 * 12):
    if cday == 0:
        nsundays += 1
    cday = (cday + month(monn % 12 + 1, monn // 12 + 1900)) % 7
print(nsundays)
