# preliminaries
# maximum letter is Z (26)
import file
data = file.readCSV("p042_words.txt")
# print(max(len(x) for x in data))
# print(max(sum(ord(c) - ord('A') + 1 for c in x) for x in data))
# maximum word length is 14
# maximum word score is 192
tris = {1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190}
print(sum(1 for w in data if sum(ord(c) - ord('A') + 1 for c in w) in tris))
