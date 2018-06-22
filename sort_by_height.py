"""
Some people are standing in a row in a park. There are trees between them
which cannot be moved. Your task is to rearrange the people by their heights
in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is
the height of a person standing in the ith position.

Guaranteed constraints:
5 ≤ a.length ≤ 15,
-1 ≤ a[i] ≤ 200.

[output] array.integer

Sorted array a with all the trees untouched.
"""
seq = [-1, 150, 190, 170, -1, -1, 160, 180]
result_list = [num for num in sorted(seq) if num > 0]
for n, i in enumerate(seq):
    if i == -1:
        result_list.insert(n, -1)
print(result_list)