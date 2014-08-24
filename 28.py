"""
Given an nxn square, where n is odd:
    .-----n-----.
   -1 . . . . . 2      2 = n^2, and the distance between 1, 2, 3, and 4 is n - 1
  | .           . thus 1 = n^2 - n  + 1
  | .           . thus 3 = n^2 - 2n + 2
  n .  SPIRALn  . thus 4 = n^2 - 3n + 3
  | .           . thus 1 + 2 + 3 + 4 = 4n^2 - 6n + 6
  | .           . -> wolfram|alpha, sum over odds from 1 to n
   -3 . . . . . 4 simplifies to (4*n^3 + 3*n^2 + 8*n - 15) / 6, then add one for center

resultant formula:
"""
n = 1001
print((4 * n ** 3 + 3 * n **2 + 8 * n - 9) // 6)
