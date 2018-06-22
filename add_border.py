"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string picture

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

[output] array.string

The same matrix of characters, framed with a border of asterisks of width 1.
"""
picture = ["abc",
           "ded"]
max_len = 0
for s in picture:
    if max_len < len(s):
        max_len = len(s)
    picture[picture.index(s)] = s.replace(s, f"*{s}*")
picture.insert(0, "*" * (max_len + 2))
picture.append("*" * 3)
print(picture)
